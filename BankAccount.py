class BankAccount:
    bank="UNCC Bank"

    def __init__(self, customer_name, current_balance, minimum_balance):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance

    def deposit(self, moneyToAdd):
        self.current_balance += moneyToAdd

    def withdraw(self, moneyToWithdraw):
        if self.current_balance - moneyToWithdraw >= self.minimum_balance:
            self.current_balance -= moneyToWithdraw
        else:
            print("You cannot withdraw any money.\n")

    def __str__(self):
        return (f"Bank Name: {BankAccount.bank} \n"
                f"Name: {self.customer_name} \n"
                f"Current Balance: {self.current_balance} \n"
                f"Minimum Balance: {self.minimum_balance} \n")

c1= BankAccount("Sirin", 5000, 1000)
c1.deposit(5000)
c1.withdraw(1000)
print(c1)

c2= BankAccount("Omar", 1000, 3000)
c2.deposit(1000)
c2.withdraw(1000)
print(c2)