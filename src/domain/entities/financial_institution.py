# src/domain/entities/financial_institution.py

from src.infra.http_server.http_server import db

class FinancialInstitution(db.Model):
    __tablename__ = 'financial_institution'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
