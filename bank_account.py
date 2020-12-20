class BankAccount:
    def __init__(self, int_rate = 0, balance = 0):
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            self.balance -= 5
            print('Insufficient Funds: Charging a $5 fee')
        return self
    def display_account_info(self):
        print(f'Balance: ${self.balance}')
        return self
    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance + self.balance * self.int_rate
        return self

account1 = BankAccount(balance=100)
account2 = BankAccount(.01, 500)

account1.deposit(100).deposit(250).deposit(50).withdraw(150).yield_interest().display_account_info()
account2.deposit(125).deposit(175).withdraw(100).withdraw(50).withdraw(175).withdraw(500).yield_interest().display_account_info()

