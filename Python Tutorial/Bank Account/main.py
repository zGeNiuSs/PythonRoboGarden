class BankAccount:
    def __init__(self, account_number, holder_name, account_type):
        self.account_number = account_number
        self.holder_name = holder_name
        self.account_type = account_type  #"Savings" or "Checking"
        self.balance = 0.0
        self.transaction_history = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited: ${amount:.2f}")
            print(f"${amount:.2f} has been deposited. New balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                self.transaction_history.append(f"Withdrew: ${amount:.2f}")
                print(f"${amount:.2f} has been withdrawn. New balance: ${self.balance:.2f}")
            else:
                print("Insufficient balance for this withdrawal.")
        else:
            print("Withdrawal amount must be positive.")

    def check_balance(self):
        print(f"Current balance: ${self.balance:.2f}")
        return self.balance

    def get_account_details(self):
        details = {
            "Account Number": self.account_number,
            "Holder Name": self.holder_name,
            "Account Type": self.account_type,
            "Balance": f"${self.balance:.2f}",
        }
        for key, value in details.items():
            print(f"{key}: {value}")
        return details

    def view_transaction_history(self):
        print("\nTransaction History:")
        if self.transaction_history:
            for transaction in self.transaction_history:
                print(transaction)
        else:
            print("No transactions yet.")


def main():
    my_account = BankAccount(account_number="1234567890", holder_name="John Doe", account_type="Savings")

    my_account.get_account_details()

    my_account.deposit(500)
    my_account.withdraw(150)
    my_account.withdraw(400)

    my_account.check_balance()

    my_account.view_transaction_history()

main()
