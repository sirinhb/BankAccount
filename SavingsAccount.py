class SavingsAccount:
    def __init__(self, savingsAccountBalance, interest):
        self.savingsAccountBalance = savingsAccountBalance
        self.interest = interest

    def applyInterest(self):
        savingsAccountBalance = self.savingsAccountBalance * self.interest
        print(f'Savings Account Balance: {savingsAccountBalance} Amount of Interest: {savingsAccountBalance * self.interest}')
        return savingsAccountBalance
