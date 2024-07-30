# src/domain/entities/account.py

from src.infra.http_server.http_server import db
from src.domain.entities.financial_institution import FinancialInstitution

class Account(db.Model):
    __tablename__ = 'account'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    type = db.Column(db.String(20), nullable=False)
    balance = db.Column(db.Float, nullable=False)
    financial_institution_id = db.Column(db.Integer, db.ForeignKey('financial_institution.id'))

    financial_institution = db.relationship('FinancialInstitution', backref=db.backref('accounts', lazy=True))
