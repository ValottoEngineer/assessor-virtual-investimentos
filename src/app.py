from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/investimentos", methods=["GET"])
def lista_investimentos():
    return jsonify([
        {"id": 1, "nome": "Tesouro Selic", "risco": "baixo"},
        {"id": 2, "nome": "Ações XPTO", "risco": "alto"}
    ])

@app.route("/secure-data", methods=["GET"])
def secure_data():
    token = request.headers.get("Authorization")
    if token != "Bearer chave_valida":
        return jsonify({"error": "Access Denied"}), 403
    return jsonify({"message": "Acesso autorizado"})

# rota inicial
@app.route("/", methods=["GET"])
def index():
    return jsonify({"message": "API Assessor Virtual de Investimentos está rodando!"})
