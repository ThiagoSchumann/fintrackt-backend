# src/application/repositories/account_repo.py
from src.domain.entities.account import Account
from src.infra.http_server.http_server import db

class AccountRepository:
    def get_all_accounts(self):
        return Account.query.all()

    def create_account(self, name, account_type, balance, financial_institution_id):
        new_account = Account(name=name, type=account_type, balance=balance, financial_institution_id=financial_institution_id)
        db.session.add(new_account)
        db.session.commit()
        return new_account
