# src/security_headers.py
def apply_security_headers(app):
    """
    Aplica CSP, X-Frame-Options e X-Content-Type-Options em todas as respostas.
    """
    @app.after_request
    def _set_headers(resp):
        resp.headers["Content-Security-Policy"] = (
            "default-src 'self'; frame-ancestors 'none'; object-src 'none'; base-uri 'self'"
        )
        resp.headers["X-Frame-Options"] = "DENY"
        resp.headers["X-Content-Type-Options"] = "nosniff"
        return resp
