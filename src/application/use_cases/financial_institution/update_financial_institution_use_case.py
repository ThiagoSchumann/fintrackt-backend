# src/application/use_cases/financial_institution/update_financial_institution_use_case.py
 
from src.application.repositories.financial_institution_repo import FinancialInstitutionRepository

class UpdateFinancialInstitutionUseCase:
    def __init__(self, financial_institution_repository: FinancialInstitutionRepository):
        self.financial_institution_repository = financial_institution_repository

    def execute(self, financial_institution_id, name):
        return self.financial_institution_repository.update_financial_institution(financial_institution_id, name)
