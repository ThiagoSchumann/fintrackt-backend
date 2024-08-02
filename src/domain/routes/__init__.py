# src/domain/routes/__init__.py
from .account_routes import account_bp
from .financial_institution_routes import financial_institution_bp

def register_routes(app):
    app.register_blueprint(account_bp, url_prefix='/api/v1/accounts')
    app.register_blueprint(financial_institution_bp, url_prefix='/api/v1/financial_institutions')
