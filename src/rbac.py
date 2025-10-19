# src/rbac.py
import os
import jwt
import datetime
from functools import wraps
from flask import request, jsonify

# Chave do JWT (use GitHub Secret/ .env em prod)
SECRET = os.getenv("SECRET_KEY", "dev-secret")
ALGO = "HS256"

def generate_token(user_id: str, role: str, exp_minutes: int = 15) -> str:
    """Gera um JWT simples com sub (usuário) e role (papel)."""
    payload = {
        "sub": user_id,
        "role": role,
        "iat": datetime.datetime.utcnow(),
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=exp_minutes),
    }
    return jwt.encode(payload, SECRET, algorithm=ALGO)

def require_role(*roles):
    """
    Decorator de RBAC.
    Ex.: @require_role("admin")  ou  @require_role("admin","user")
    """
    def deco(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            auth = request.headers.get("Authorization", "")
            if not auth.startswith("Bearer "):
                # sem token → negado
                return jsonify({"error": "Access Denied"}), 403

            token = auth.split(" ", 1)[1]
            try:
                payload = jwt.decode(token, SECRET, algorithms=[ALGO])
                if roles and payload.get("role") not in roles:
                    return jsonify({"error": "Forbidden"}), 403
            except jwt.ExpiredSignatureError:
                return jsonify({"error": "Token expired"}), 401
            except Exception:
                return jsonify({"error": "Invalid token"}), 401

            return fn(*args, **kwargs)
        return wrapper
    return deco
