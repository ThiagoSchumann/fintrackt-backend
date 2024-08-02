# src/application/use_cases/financial_institution/delete_financial_institution_use_case.py

from src.application.repositories.financial_institution_repo import FinancialInstitutionRepository

class DeleteFinancialInstitutionUseCase:
    def __init__(self, financial_institution_repository: FinancialInstitutionRepository):
        self.financial_institution_repository = financial_institution_repository

    def execute(self, financial_institution_id):
        return self.financial_institution_repository.delete_financial_institution(financial_institution_id)
