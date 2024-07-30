# src/domain/routes/account_routes.py

from flask import Blueprint, request, jsonify
from src.application.use_cases.account.create_account_use_case import CreateAccountUseCase
from src.application.repositories.account_repo import AccountRepository

account_bp = Blueprint('accounts', __name__)
account_repository = AccountRepository()
create_account_use_case = CreateAccountUseCase(account_repository)

@account_bp.route('/', methods=['POST'])
def create_account():
    data = request.get_json()
    new_account = create_account_use_case.execute(data['name'], data['type'], data['balance'], data['financial_institution_id'])
    return jsonify(id=new_account.id, name=new_account.name, type=new_account.type, balance=new_account.balance), 201
