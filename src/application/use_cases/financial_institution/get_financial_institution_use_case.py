# src/application/use_cases/financial_institution/get_financial_institution_use_case.py

from src.application.repositories.financial_institution_repo import FinancialInstitutionRepository

class GetFinancialInstitutionUseCase:
    def __init__(self, financial_institution_repository: FinancialInstitutionRepository):
        self.financial_institution_repository = financial_institution_repository

    def execute(self, financial_institution_id):
        return self.financial_institution_repository.get_financial_institution_by_id(financial_institution_id)
