from SavingsAccount import SavingsAccount
from CheckingAccount import CheckingAccount

# Savings Account Instances
averySavings = SavingsAccount("Avery Wood", 1500, 1.5)
sirinSavings= SavingsAccount("Sirin Blan", 5000, 2.0)

# Checking Account instances
averyChecking = CheckingAccount("Avery Wood", 1600, 1000, 500)
sirinChecking = CheckingAccount("Sirin Blan", 2000, 500,1234, 5678, 1000)

# Avery Instances
averySavings.applyInterest()
averyChecking.transfer(550)
averyChecking.transfer(300)
averySavings.applyInterest()

# Sirin Instances
sirinSavings.applyInterest()
sirinChecking.transfer(1000)
sirinChecking.transfer(500)
sirinSavings.applyInterest()

