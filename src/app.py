import logging
from flask import Flask, jsonify, request

from schemas import LoginSchema, InvestimentoSchema
from rbac import generate_token, require_role
from security_headers import apply_security_headers
from consent import consent_bp

# -----------------------------------------------------------------------------
# Logs básicos
# -----------------------------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# -----------------------------------------------------------------------------
# App
# -----------------------------------------------------------------------------
app = Flask(__name__)

# Segurança de cabeçalhos (CSP, XFO, X-CTO)
apply_security_headers(app)

# Endpoints de consentimento (LGPD)
app.register_blueprint(consent_bp)

# -----------------------------------------------------------------------------
# Tratamento simples de erros (opcional, útil p/ prints)
# -----------------------------------------------------------------------------
@app.errorhandler(400)
@app.errorhandler(404)
@app.errorhandler(500)
def handle_err(e):
    code = getattr(e, "code", 500)
    return jsonify({"error": e.__class__.__name__}), code

# -----------------------------------------------------------------------------
# Rotas existentes
# -----------------------------------------------------------------------------
@app.route("/investimentos", methods=["GET"])
def lista_investimentos():
    return jsonify([
        {"id": 1, "nome": "Tesouro Selic", "risco": "baixo"},
        {"id": 2, "nome": "Ações XPTO", "risco": "alto"},
    ])

# -----------------------------------------------------------------------------
# NOVO: Login (gera JWT) + RBAC
# -----------------------------------------------------------------------------
@app.post("/login")
def login():
    data = request.get_json() or {}
    errors = LoginSchema().validate(data)
    if errors:
        return jsonify({"errors": errors}), 400

    # regra didática: emails que terminam com @adm.com são "admin"
    role = "admin" if data["email"].endswith("@adm.com") else "user"
    token = generate_token(user_id=data["email"], role=role, exp_minutes=10)
    return jsonify({"token": token, "role": role}), 200

# Antes: checava "Bearer chave_valida"
# Agora: exige token válido com role admin OU user
@app.route("/secure-data", methods=["GET"])
@require_role("admin", "user")
def secure_data():
    return jsonify({"message": "Acesso autorizado"}), 200

# Admin-only: cria investimento (validação/sanitização)
@app.post("/investimentos")
@require_role("admin")
def novo_investimento():
    data = request.get_json() or {}
    errors = InvestimentoSchema().validate(data)
    if errors:
        return jsonify({"errors": errors}), 400
    return jsonify({"status": "criado", "item": data}), 201

# LGPD: direito de exclusão (admin-only)
@app.delete("/users/<user_id>/erase")
@require_role("admin")
def erase_user(user_id):
    # aqui você conectaria sua rotina real de anonimização/remoção
    return jsonify({"status": "erased", "user": user_id}), 200

# Rota inicial
@app.route("/", methods=["GET"])
def index():
    return jsonify({"message": "API Assessor Virtual de Investimentos está rodando!"})

# -----------------------------------------------------------------------------
if __name__ == "__main__":
    # debug=True apenas para laboratório (não usar em produção)
    app.run(host="0.0.0.0", port=5000, debug=True)
