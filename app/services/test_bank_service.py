import pytest
from app.services.bank_service import BranchBankService, AtmBankService
from app.validator.amount_validator import AmountValidator

class MockAccountService:
    def __init__(self):
        self.deposits = []
        self.withdrawals = []
        self.transfers = []

    def deposit_money(self, account_id, amount):
        self.deposits.append((account_id, amount))

    def withdraw_money(self, account_id, amount):
        self.withdrawals.append((account_id, amount))

    def transfer_money(self, from_account_id, to_account_id, amount):
        self.transfers.append((from_account_id, to_account_id, amount))

# BranchBankService tests

def test_branchbankservice_deposit():
    mock = MockAccountService()
    service = BranchBankService(mock)
    service.deposit_money(1, 100)
    assert mock.deposits == [(1, 100)]

def test_branchbankservice_withdraw():
    mock = MockAccountService()
    service = BranchBankService(mock)
    service.withdraw_money(1, 50)
    assert mock.withdrawals == [(1, 50)]

def test_branchbankservice_transfer():
    mock = MockAccountService()
    service = BranchBankService(mock)
    service.transfer_money(1, 2, 200)
    assert mock.transfers == [(1, 2, 200)]

# AtmBankService tests

def test_atmbankservice_deposit_valid():
    mock = MockAccountService()
    validator = AmountValidator()
    service = AtmBankService(mock, validator)
    service.deposit_money(1, 100)
    assert mock.deposits == [(1, 100)]

def test_atmbankservice_deposit_too_large():
    mock = MockAccountService()
    validator = AmountValidator()
    service = AtmBankService(mock, validator)
    with pytest.raises(ValueError):
        service.deposit_money(1, 20000)

def test_atmbankservice_withdraw_valid():
    mock = MockAccountService()
    validator = AmountValidator()
    service = AtmBankService(mock, validator)
    service.withdraw_money(1, 100)
    assert mock.withdrawals == [(1, 100)]

def test_atmbankservice_withdraw_too_large():
    mock = MockAccountService()
    validator = AmountValidator()
    service = AtmBankService(mock, validator)
    with pytest.raises(ValueError):
        service.withdraw_money(1, 20000)
