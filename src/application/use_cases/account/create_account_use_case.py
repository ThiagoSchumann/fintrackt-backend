# src/application/use_cases/account/create_account_use_case.py
from src.application.repositories.account_repo import AccountRepository

class CreateAccountUseCase:
    def __init__(self, account_repository: AccountRepository):
        self.account_repository = account_repository

    def execute(self, name, account_type, balance, financial_institution_id):
        return self.account_repository.create_account(name, account_type, balance, financial_institution_id)
