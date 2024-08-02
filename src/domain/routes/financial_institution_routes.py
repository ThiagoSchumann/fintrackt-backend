# src/domain/routes/financial_institution_routes.py

from flask import Blueprint, request, jsonify
from src.application.use_cases.financial_institution.create_financial_institution_use_case import CreateFinancialInstitutionUseCase
from src.application.use_cases.financial_institution.get_financial_institution_use_case import GetFinancialInstitutionUseCase
from src.application.use_cases.financial_institution.update_financial_institution_use_case import UpdateFinancialInstitutionUseCase
from src.application.use_cases.financial_institution.delete_financial_institution_use_case import DeleteFinancialInstitutionUseCase
from src.application.use_cases.financial_institution.list_financial_institutions_use_case import ListFinancialInstitutionsUseCase
from src.application.repositories.financial_institution_repo import FinancialInstitutionRepository

financial_institution_bp = Blueprint('financial_institutions', __name__)
financial_institution_repository = FinancialInstitutionRepository()
create_financial_institution_use_case = CreateFinancialInstitutionUseCase(financial_institution_repository)
get_financial_institution_use_case = GetFinancialInstitutionUseCase(financial_institution_repository)
update_financial_institution_use_case = UpdateFinancialInstitutionUseCase(financial_institution_repository)
delete_financial_institution_use_case = DeleteFinancialInstitutionUseCase(financial_institution_repository)
list_financial_institutions_use_case = ListFinancialInstitutionsUseCase(financial_institution_repository)

# Create financial institution
# POST /financial_institutions
@financial_institution_bp.route('/', methods=['POST'])
def create_financial_institution():
    data = request.get_json()
    new_institution = create_financial_institution_use_case.execute(data['name'])
    return jsonify(id=new_institution.id, name=new_institution.name), 201

# Get financial institution by ID
# GET /financial_institutions/<int:financial_institution_id>
@financial_institution_bp.route('/<int:financial_institution_id>', methods=['GET'])
def get_financial_institution(financial_institution_id):
    institution = get_financial_institution_use_case.execute(financial_institution_id)
    if institution:
        return jsonify(id=institution.id, name=institution.name)
    else:
        return jsonify({'error': 'Financial Institution not found'}), 404

# Update financial institution
# PUT /financial_institutions/<int:financial_institution_id>
@financial_institution_bp.route('/<int:financial_institution_id>', methods=['PUT'])
def update_financial_institution(financial_institution_id):
    data = request.get_json()
    updated_institution = update_financial_institution_use_case.execute(financial_institution_id, data['name'])
    if updated_institution:
        return jsonify(id=updated_institution.id, name=updated_institution.name)
    else:
        return jsonify({'error': 'Financial Institution not found'}), 404

# Delete financial institution
# DELETE /financial_institutions/<int:financial_institution_id>
@financial_institution_bp.route('/<int:financial_institution_id>', methods=['DELETE'])
def delete_financial_institution(financial_institution_id):
    deleted_institution = delete_financial_institution_use_case.execute(financial_institution_id)
    if deleted_institution:
        return jsonify({}), 204
    else:
        return jsonify({'error': 'Financial Institution not found'}), 404

# List all financial institutions
# GET /financial_institutions
@financial_institution_bp.route('/', methods=['GET'])
def list_financial_institutions():
    institutions = list_financial_institutions_use_case.execute()
    institutions_json = [{'id': institution.id, 'name': institution.name} for institution in institutions]
    return jsonify(institutions_json)
