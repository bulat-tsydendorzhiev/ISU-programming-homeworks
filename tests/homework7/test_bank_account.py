import pytest

from homework7.BankAccount import BankAccount


class TestInit:
    def test_default_balance_is_zero(self):
        assert BankAccount().get_balance() == 0

    def test_stores_initial_balance(self):
        assert BankAccount(150).get_balance() == 150


class TestDeposit:
    @pytest.mark.parametrize(
        ("initial", "amount", "expected"),
        [
            (100, 50, 150),
            (0, 250, 250),
            (100, 0, 100),
        ],
    )
    def test_deposit_increases_balance(self, initial, amount, expected):
        account = BankAccount(initial)

        account.deposit(amount)

        assert account.get_balance() == expected


class TestWithdraw:
    @pytest.mark.parametrize(
        ("amount", "expected"),
        [
            (30, 70),
            (100, 0),
            (0, 100),
        ],
    )
    def test_withdraw_decreases_balance(self, amount, expected):
        account = BankAccount(100)

        account.withdraw(amount)

        assert account.get_balance() == expected

    @pytest.mark.parametrize("amount", [101, 1000])
    def test_withdraw_more_than_balance_raises(self, amount):
        account = BankAccount(100)

        with pytest.raises(ValueError, match="недостаточно средств"):
            account.withdraw(amount)

        assert account.get_balance() == 100


class TestTransfer:
    def test_transfer_moves_money_between_accounts(self):
        sender = BankAccount(100)
        recipient = BankAccount(20)

        sender.transfer(recipient, 30)

        assert sender.get_balance() == 70
        assert recipient.get_balance() == 50

    def test_transfer_can_empty_source_account(self):
        sender = BankAccount(100)
        recipient = BankAccount(20)

        sender.transfer(recipient, 100)

        assert sender.get_balance() == 0
        assert recipient.get_balance() == 120

    def test_transfer_with_insufficient_funds_keeps_both_balances(self):
        sender = BankAccount(100)
        recipient = BankAccount(20)

        with pytest.raises(ValueError, match="недостаточно средств"):
            sender.transfer(recipient, 101)

        assert sender.get_balance() == 100
        assert recipient.get_balance() == 20

    def test_transfer_to_non_account_returns_not_implemented(self):
        sender = BankAccount(100)

        result = sender.transfer("recipient", 30)

        assert result is NotImplemented
        assert sender.get_balance() == 100
