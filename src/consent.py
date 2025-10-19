# src/consent.py
from datetime import datetime
from flask import Blueprint, jsonify, request

consent_bp = Blueprint("consent", __name__, url_prefix="/")

# "Banco" em memória (didático)
CONSENT_DB = {}

@consent_bp.post("/consent")
def give_consent():
    """
    Registra consentimento de um usuário.
    body: { "user_id": "u123", "scope": "marketing" }
    """
    data = request.get_json() or {}
    user = data.get("user_id")
    scope = data.get("scope", "default")
    if not user:
        return jsonify({"error": "user_id é obrigatório"}), 400

    CONSENT_DB[user] = {"granted": True, "scope": scope, "ts": datetime.utcnow().isoformat()}
    return jsonify({"status": "ok", "consent": CONSENT_DB[user]}), 200

@consent_bp.delete("/consent/<user_id>")
def revoke_consent(user_id):
    """
    Revoga consentimento do usuário.
    """
    CONSENT_DB[user_id] = {"granted": False, "ts": datetime.utcnow().isoformat()}
    return jsonify({"status": "revoked", "consent": CONSENT_DB[user_id]}), 200
