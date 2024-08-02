# src/application/use_cases/account/list_accounts_use_case.py

from src.application.repositories.account_repo import AccountRepository

class ListAccountsUseCase:
    def __init__(self, account_repository: AccountRepository):
        self.account_repository = account_repository

    def execute(self):
        accounts = self.account_repository.get_all_accounts()
        result = []
        for account in accounts:
            account_data = {
                "id": account.id,
                "name": account.name,
                "type": account.type,
                "balance": account.balance,
                "financial_institution": {
                    "id": account.financial_institution.id,
                    "name": account.financial_institution.name
                } if account.financial_institution else None
            }
            result.append(account_data)
        return result
