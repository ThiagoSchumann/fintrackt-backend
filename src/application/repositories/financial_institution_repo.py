# src/application/repositories/financial_institution_repo.py

from src.domain.entities.financial_institution import FinancialInstitution
from src.infra.http_server.http_server import db

class FinancialInstitutionRepository:
    def get_all_financial_institutions(self):
        return FinancialInstitution.query.all()

    def get_financial_institution_by_id(self, financial_institution_id):
        return FinancialInstitution.query.get(financial_institution_id)

    def create_financial_institution(self, name):
        new_institution = FinancialInstitution(name=name)
        db.session.add(new_institution)
        db.session.commit()
        return new_institution

    def update_financial_institution(self, financial_institution_id, name):
        institution = FinancialInstitution.query.get(financial_institution_id)
        if institution:
            institution.name = name
            db.session.commit()
        return institution

    def delete_financial_institution(self, financial_institution_id):
        institution = FinancialInstitution.query.get(financial_institution_id)
        if institution:
            db.session.delete(institution)
            db.session.commit()
        return institution
