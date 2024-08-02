# src/application/use_cases/account/update_account_use_case.py

from src.application.repositories.account_repo import AccountRepository

class UpdateAccountUseCase:
    def __init__(self, account_repository: AccountRepository):
        self.account_repository = account_repository

    def execute(self, account_id, name, account_type, balance, financial_institution_id):
        return self.account_repository.update_account(account_id, name, account_type, balance, financial_institution_id)
