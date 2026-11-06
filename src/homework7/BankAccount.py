class BankAccount:
    def __init__(self, balance = 0):
        self.__balance = balance

    def get_balance(self) -> int:
        return self.__balance

    def deposit(self, amount: int) -> None:
        self.__balance += amount

    def withdraw(self, amount: int) -> None:
        if amount > self.__balance:
            raise ValueError("На счете недостаточно средств.")

        self.__balance -= amount

    def transfer(self, account: BankAccount, amount: int) -> None:
        if not isinstance(account, BankAccount):
            return NotImplemented        

        self.withdraw(amount)
        account.deposit(amount)
