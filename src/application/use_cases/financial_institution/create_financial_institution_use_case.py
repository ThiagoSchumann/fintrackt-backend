# src/application/use_cases/financial_institution/create_financial_institution_use_case.py

from src.application.repositories.financial_institution_repo import FinancialInstitutionRepository

class CreateFinancialInstitutionUseCase:
    def __init__(self, financial_institution_repository: FinancialInstitutionRepository):
        self.financial_institution_repository = financial_institution_repository

    def execute(self, name):
        return self.financial_institution_repository.create_financial_institution(name)
