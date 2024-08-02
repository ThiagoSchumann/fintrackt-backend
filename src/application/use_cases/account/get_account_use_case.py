# src/application/use_cases/account/get_account_use_case.py

from src.application.repositories.account_repo import AccountRepository

class GetAccountUseCase:
    def __init__(self, account_repository: AccountRepository):
        self.account_repository = account_repository

    def execute(self, account_id):
        return self.account_repository.get_account_by_id(account_id)
