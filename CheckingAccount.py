from BankAccount import BankAccount

class CheckingAccount(BankAccount):
    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number, transfer_limit):
        super().__init__(customer_name, current_balance, minimum_balance, account_number, routing_number)
        self.transfer_limit = transfer_limit

    def transfer(self, amount):
        if amount <= self.transfer_limit and self.current_balance - amount >= self.minimum_balance:
            self.current_balance -= amount
            print(f"Transfer successful! New balance: {self.current_balance}")
        else:
            print("Transfer amount exceeds the limit or insufficient funds.")
