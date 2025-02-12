from BankAccount import BankAccount
class SavingsAccount:
    def __init__(self, name, savingsAccountBalance, interest):
        self.name = name
        self.savingsAccountBalance = savingsAccountBalance
        self.interest = interest

    def applyInterest(self):
        self.savingsAccountBalance = self.savingsAccountBalance * (self.interest / 100)
        print(f'Savings Account Balance: {self.savingsAccountBalance} Amount of Interest: {self.savingsAccountBalance * self.interest}')
        return self.savingsAccountBalance
