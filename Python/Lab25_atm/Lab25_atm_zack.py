class ATM:
    def __init__(self, amount):
        self.balance = amount

    def deposit(self, amount):
        self.balance += amount

    def check_withdraw(self, amount):
        return amount <= self.balance

    def withdraw(self, amount):
        self.balance -= amount

account = ATM(100)
account.deposit(50)
print(account.check_withdraw(200))
print(account.check_withdraw(100))
account.withdraw(100)
print(account.balance)