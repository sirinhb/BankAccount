from SavingsAccount import SavingsAccount
from CheckingAccount import CheckingAccount

# Savings Account Instances
averySavings = SavingsAccount("Avery Wood", 1500, 1.5)

# Checking Account instances
averyChecking = CheckingAccount("Avery Wood", 1600, 1000, 500)


# Avery Instances
averySavings.applyInterest()
averyChecking.transfer(550)
averyChecking.transfer(300)
averySavings.applyInterest()