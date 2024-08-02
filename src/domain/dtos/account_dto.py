# src/domain/dtos/account_dto.py

from typing import Optional
from src.domain.entities.account import Account

class FinancialInstitutionDTO:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }

class AccountDTO:
    def __init__(self, id: int, name: str, type: str, balance: float, financial_institution: Optional[FinancialInstitutionDTO] = None):
        self.id = id
        self.name = name
        self.type = type
        self.balance = balance
        self.financial_institution = financial_institution

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "type": self.type,
            "balance": self.balance,
            "financial_institution": self.financial_institution.to_dict() if self.financial_institution else None
        }

def account_to_dto(account) -> AccountDTO:
    if isinstance(account, dict):
        financial_institution_dto = FinancialInstitutionDTO(
            id=account['financial_institution']['id'],
            name=account['financial_institution']['name']
        ) if account.get('financial_institution') else None

        return AccountDTO(
            id=account['id'],
            name=account['name'],
            type=account['type'],
            balance=account['balance'],
            financial_institution=financial_institution_dto
        )
    elif isinstance(account, Account):
        financial_institution_dto = FinancialInstitutionDTO(
            id=account.financial_institution.id,
            name=account.financial_institution.name
        ) if account.financial_institution else None

        return AccountDTO(
            id=account.id,
            name=account.name,
            type=account.type,
            balance=account.balance,
            financial_institution=financial_institution_dto
        )
    else:
        raise TypeError(f"Unsupported type for account: {type(account)}")
