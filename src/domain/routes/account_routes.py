# src/domain/routes/account_routes.py

from flask import Blueprint, request, jsonify, Response
from sqlalchemy.exc import SQLAlchemyError
from werkzeug.exceptions import BadRequest, NotFound
import json
from src.application.use_cases.account.create_account_use_case import CreateAccountUseCase
from src.application.use_cases.account.get_account_use_case import GetAccountUseCase
from src.application.use_cases.account.update_account_use_case import UpdateAccountUseCase
from src.application.use_cases.account.delete_account_use_case import DeleteAccountUseCase
from src.application.use_cases.account.list_accounts_use_case import ListAccountsUseCase
from src.application.repositories.account_repo import AccountRepository
from src.domain.entities.account import Account
from src.domain.dtos.account_dto import AccountDTO, FinancialInstitutionDTO, account_to_dto

account_bp = Blueprint('accounts', __name__)
account_repository = AccountRepository()
create_account_use_case = CreateAccountUseCase(account_repository)
get_account_use_case = GetAccountUseCase(account_repository)
update_account_use_case = UpdateAccountUseCase(account_repository)
delete_account_use_case = DeleteAccountUseCase(account_repository)
list_accounts_use_case = ListAccountsUseCase(account_repository)

def make_response(data, status_code):
    response = Response(
        response=json.dumps(data, indent=4),
        status=status_code,
        mimetype='application/json'
    )
    return response

# Create account
# POST /accounts
@account_bp.route('/', methods=['POST'])
def create_account():
    try:
        data = request.get_json()
        if not data:
            raise BadRequest("Invalid JSON data")
        
        required_fields = ['name', 'type', 'balance', 'financial_institution_id']
        for field in required_fields:
            if field not in data:
                raise BadRequest(f"Missing required field: {field}")
        
        new_account = create_account_use_case.execute(
            data['name'], data['type'], data['balance'], data['financial_institution_id']
        )
        
        response = account_to_dto(new_account).to_dict()
        return make_response(response, 201)
    
    except BadRequest as e:
        response = {"error": str(e)}
        return make_response(response, 400)
    
    except SQLAlchemyError as e:
        response = {"error": "Database error", "details": str(e)}
        return make_response(response, 500)
    
    except Exception as e:
        response = {"error": "Internal server error", "details": str(e)}
        return make_response(response, 500)

# Get account by ID
# GET /accounts/<int:account_id>
@account_bp.route('/<int:account_id>', methods=['GET'])
def get_account(account_id):
    try:
        account = get_account_use_case.execute(account_id)
        if account:
            response = account_to_dto(account).to_dict()
            return make_response(response, 200)
        else:
            raise NotFound("Account not found")
    
    except NotFound as e:
        response = {"error": str(e)}
        return make_response(response, 404)
    
    except SQLAlchemyError as e:
        response = {"error": "Database error", "details": str(e)}
        return make_response(response, 500)
    
    except Exception as e:
        response = {"error": "Internal server error", "details": str(e)}
        return make_response(response, 500)

# Update account
# PUT /accounts/<int:account_id>
@account_bp.route('/<int:account_id>', methods=['PUT'])
def update_account(account_id):
    try:
        data = request.get_json()
        if not data:
            raise BadRequest("Invalid JSON data")
        
        updated_account = update_account_use_case.execute(
            account_id, data['name'], data['type'], data['balance'], data['financial_institution_id']
        )
        
        if updated_account:
            response = account_to_dto(updated_account).to_dict()
            return make_response(response, 200)
        else:
            raise NotFound("Account not found")
    
    except BadRequest as e:
        response = {"error": str(e)}
        return make_response(response, 400)
    
    except NotFound as e:
        response = {"error": str(e)}
        return make_response(response, 404)
    
    except SQLAlchemyError as e:
        response = {"error": "Database error", "details": str(e)}
        return make_response(response, 500)
    
    except Exception as e:
        response = {"error": "Internal server error", "details": str(e)}
        return make_response(response, 500)

# Delete account
# DELETE /accounts/<int:account_id>
@account_bp.route('/<int:account_id>', methods=['DELETE'])
def delete_account(account_id):
    try:
        deleted_account = delete_account_use_case.execute(account_id)
        if deleted_account:
            return '', 204
        else:
            raise NotFound("Account not found")
    
    except NotFound as e:
        response = {"error": str(e)}
        return make_response(response, 404)
    
    except SQLAlchemyError as e:
        response = {"error": "Database error", "details": str(e)}
        return make_response(response, 500)
    
    except Exception as e:
        response = {"error": "Internal server error", "details": str(e)}
        return make_response(response, 500)

# List all accounts
# GET /accounts
@account_bp.route('/', methods=['GET'])
def list_accounts():
    try:
        accounts = list_accounts_use_case.execute()
        result = [account_to_dto(account).to_dict() for account in accounts]
        return make_response(result, 200)
    
    except SQLAlchemyError as e:
        response = {"error": "Database error", "details": str(e)}
        return make_response(response, 500)
    
    except Exception as e:
        response = {"error": "Internal server error", "details": str(e)}
        return make_response(response, 500)
