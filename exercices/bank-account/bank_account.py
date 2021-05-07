class BankAccount:
    def __init__(self):
        self.is_open: bool = False
        self.balance: int = 0

    def get_balance(self):
        if not self.is_open: raise ValueError('account not open')
        return self.balance

    def open(self):
        if self.is_open: raise ValueError('account already open')
        self.is_open = True

    def deposit(self, amount):
        if amount < 0:
            raise ValueError('invalid deposit amount')
        elif not self.is_open:
            raise ValueError('account not open')
        self.balance += amount

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError('invalid withdrawal amount')
        elif not self.is_open: raise ValueError('account not open')
        elif amount > self.balance:
            raise ValueError('amount to withdraw superior to account balance')
        self.balance -= amount

    def close(self):
        if not self.is_open: raise ValueError('account already closed')
        self.is_open = False
        self.balance = 0
