<<<<<<< HEAD
class SavingsAccount:
    def __init__(self, savingsAccountBalance, interest):
=======
from BankAccount import BankAccount
class SavingsAccount:
    def __init__(self, name, savingsAccountBalance, interest):
        self.name = name
>>>>>>> 8dbc698baed033eaf940ad8ec46ce9b3687d23cb
        self.savingsAccountBalance = savingsAccountBalance
        self.interest = interest

    def applyInterest(self):
<<<<<<< HEAD
        savingsAccountBalance = self.savingsAccountBalance * self.interest
        print(f'Savings Account Balance: {savingsAccountBalance} Amount of Interest: {savingsAccountBalance * self.interest}')
        return savingsAccountBalance
=======
        self.savingsAccountBalance = self.savingsAccountBalance * (self.interest / 100)
        print(f'Savings Account Balance: {self.savingsAccountBalance} Amount of Interest: {self.savingsAccountBalance * self.interest}')
        return self.savingsAccountBalance
>>>>>>> 8dbc698baed033eaf940ad8ec46ce9b3687d23cb
