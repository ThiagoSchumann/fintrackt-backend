# src/application/repositories/account_repo.py

from src.domain.entities.account import Account
from src.infra.http_server.http_server import db

class AccountRepository:
    def get_all_accounts(self):
        return db.session.query(Account).all()

    def get_account_by_id(self, account_id):
        return Account.query.get(account_id)

    def create_account(self, name, account_type, balance, financial_institution_id):
        new_account = Account(name=name, type=account_type, balance=balance, financial_institution_id=financial_institution_id)
        db.session.add(new_account)
        db.session.commit()
        return new_account

    def update_account(self, account_id, name, account_type, balance, financial_institution_id):
        account = Account.query.get(account_id)
        if account:
            account.name = name
            account.type = account_type
            account.balance = balance
            account.financial_institution_id = financial_institution_id
            db.session.commit()
        return account

    def delete_account(self, account_id):
        account = Account.query.get(account_id)
        if account:
            db.session.delete(account)
            db.session.commit()
        return account
