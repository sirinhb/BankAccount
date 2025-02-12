from SavingsAccount import SavingsAccount
from CheckingAccount import CheckingAccount

<<<<<<< HEAD
averySavings = SavingsAccount("Avery Wood", 1500, 1.5)
sirinSavings= SavingsAccount("Sirin Blan", 5000, 2.0)
sirinSavings.applyInterest()

averyChecking = CheckingAccount("Avery Wood", 1600, 1000, 500)
sirinChecking = CheckingAccount("Sirin Blan", 2000, 500, 1000)
sirinChecking.transfer()
=======
# Savings Account Instances
averySavings = SavingsAccount("Avery Wood", 1500, 1.5)

# Checking Account instances
averyChecking = CheckingAccount("Avery Wood", 1600, 1000, 500)


# Avery Instances
averySavings.applyInterest()
averyChecking.transfer(550)
averyChecking.transfer(300)
averySavings.applyInterest()
>>>>>>> 8dbc698baed033eaf940ad8ec46ce9b3687d23cb
