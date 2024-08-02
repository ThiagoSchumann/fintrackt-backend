# src/application/use_cases/account/delete_account_use_case.py

from src.application.repositories.account_repo import AccountRepository

class DeleteAccountUseCase:
    def __init__(self, account_repository: AccountRepository):
        self.account_repository = account_repository

    def execute(self, account_id):
        return self.account_repository.delete_account(account_id)
