# src/domain/routes/__init__.py

from .account_routes import account_bp

def register_routes(app):
    app.register_blueprint(account_bp, url_prefix='/accounts')
