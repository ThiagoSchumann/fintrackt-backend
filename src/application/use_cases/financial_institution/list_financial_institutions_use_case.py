# src/application/use_cases/financial_institution/list_financial_institutions_use_case.py

from src.application.repositories.financial_institution_repo import FinancialInstitutionRepository

class ListFinancialInstitutionsUseCase:
    def __init__(self, financial_institution_repository: FinancialInstitutionRepository):
        self.financial_institution_repository = financial_institution_repository

    def execute(self):
        return self.financial_institution_repository.get_all_financial_institutions()
