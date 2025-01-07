import os

class BankAccount:
    account_counter = 1  # variable to assign unique IDs to accounts.

    def __init__(self, name, account_type, balance=0):
        self.name = name
        self.account_type = account_type
        self.balance = balance
        self.account_id = BankAccount.account_counter
        BankAccount.account_counter += 1

        self.filename = f"{self.account_id}_{self.account_type}_{self.name}.txt"

        with open(self.filename, "w") as file:
            file.write(f"Account Created: {self.name}, Type: {self.account_type}, ID: {self.account_id}\n")
            file.write(f"Initial Balance: ${self.balance:.2f}\n")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            with open(self.filename, "a") as file:
                file.write(f"Deposited: ${amount:.2f}, New Balance: ${self.balance:.2f}\n")
            print(f"${amount:.2f} deposited successfully.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                with open(self.filename, "a") as file:
                    file.write(f"Withdrew: ${amount:.2f}, New Balance: ${self.balance:.2f}\n")
                print(f"${amount:.2f} withdrawn successfully.")
            else:
                print("Insufficient balance for this withdrawal.")
        else:
            print("Withdrawal amount must be positive.")

    def get_balance(self):
        print(f"Current Balance: ${self.balance:.2f}")
        return self.balance

    def get_user_id(self):
        print(f"User ID: {self.account_id}")
        return self.account_id

    def get_user_name(self):
        print(f"Account Holder: {self.name}")
        return self.name

    def get_account_type(self):
        print(f"Account Type: {self.account_type}")
        return self.account_type

    def get_transaction_history(self):
        print(f"\nTransaction History for {self.name}:")
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                print(file.read())
        else:
            print("Transaction history not found.")

def main():
    account1 = BankAccount("Alice", "Savings", 100)
    account2 = BankAccount("Bob", "Chequing", 50)

    account1.deposit(200)
    account1.withdraw(50)
    account1.get_balance()
    account1.get_transaction_history()

    account2.deposit(100)
    account2.withdraw(20)
    account2.withdraw(150)  # Insufficient balance
    account2.get_balance()
    account2.get_transaction_history()

main()
