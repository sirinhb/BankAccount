from SavingsAccount import SavingsAccount
from CheckingAccount import CheckingAccount

averySavings = SavingsAccount("Avery Wood", 1500, 1.5)
sirinSavings= SavingsAccount("Sirin Blan", 5000, 2.0)
sirinSavings.applyInterest()

averyChecking = CheckingAccount("Avery Wood", 1600, 1000, 500)
sirinChecking = CheckingAccount("Sirin Blan", 2000, 500, 1000)
sirinChecking.transfer()