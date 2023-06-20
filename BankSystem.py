


import sys

class Transaction:
    def __init__(self, date, type, amount):
        self.date = date
        self.type = type
        self.amount = amount


class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        self.transactions = []
        self.balance_alert = None
        self.transaction_alert = None

    def __str__(self):
        return f"Owner: {self.owner}, Balance: {self.balance} $"

    def add_to_account(self, amount):
        self.balance += amount
        self.transactions.append(Transaction("today", "add", amount))
        print(f"We just added {amount} $ to the account")
        if self.balance_alert and self.balance < self.balance_alert:
            print(f"Alert: Account balance is below {self.balance_alert} $")

    def withdraw_of_account(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transactions.append(Transaction("today", "withdraw", amount))
            print(f"{amount} $ was deducted from the account")
            if self.balance_alert and self.balance < self.balance_alert:
                print(f"Alert: Account balance is below {self.balance_alert} $")
            if self.transaction_alert and amount >= self.transaction_alert:
                print(f"Alert: A transaction of {amount} $ has been made")
        else:
            print("Withdraw failed. Insufficient funds.")

    def transfer_to_account(self, other_account, amount):
        if self.balance >= amount:
            self.withdraw_of_account(amount)
            other_account.add_to_account(amount)
            print(f"{amount} $ was transferred to {other_account.owner}'s account")
        else:
            print("Transfer failed. Insufficient funds.")

    def get_transaction_history(self):
        print("Transaction history:")
        for transaction in self.transactions:
            print(f"Date: {transaction.date}, Type: {transaction.type}, Amount: {transaction.amount} $")

    def set_balance_alert(self, amount):
        self.balance_alert = amount
        print(f"Balance alert set for {amount} $")

    def set_transaction_alert(self, amount):
        self.transaction_alert = amount
        print(f"Transaction alert set for {amount} $")


class Bank:
    def __init__(self):
        self.accounts = []

    def create_account(self, owner, balance):
        account = Account(owner, balance)
        self.accounts.append(account)
        print(f"Account for {owner} created with a balance of {balance} $")

    def close_account(self, account):
        self.accounts.remove(account)
        print(f"Account for {account.owner} has been closed.")

    def change_account_owner(self, account, new_owner):
        account.owner = new_owner
        print(f"The account owner has been changed to {new_owner}")

    def get_account_details(self):
        for account in self.accounts:
            print(account)

    def get_transaction_details(self):
        for account in self.accounts:
            account.get_transaction_history()


# Login system
username = ""
password = 0
while username != "ailin bahrami" or password != 1234:
    username = input("Enter your username: ")
    password = int(input("Enter your password: "))
    if username == "ailin bahrami" and password == 1234:
        print("ACCEPTED. Welcome to your account.")
        print("User information: \n ID card number: 121161850 \n Phone number: +49177181985 \n City: Cologne")
    else:
        print("Invalid username or password. Please enter valid credentials.")

# Account system
bank = Bank()
bank.create_account("ailin bahrami", 500)
bank.create_account("ailin bahrami", 1000)
print("Account details:")
bank.get_account_details()

# Menu system
while True:
    print("\nMenu:")
    print("1. Add money to account")
    print("2. Withdraw money from account")
    print("3. Check account balance")
    print("4. Transfer money to another account")
    print("5. View transaction history")
    print("6. Change account owner name")
    print("7. Delete account")
    print("8. View account details")
    print("9. View transaction details")
    print("10. Set balance alert")
    print("11. Set transaction alert")
    print("12. Exit program")
    choice = input("Enter your choice (1-12): ")

    if choice == "1":
        while True:
            try:
                amount = int(input("Enter the amount to add: "))
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        bank.accounts[0].add_to_account(amount)
        print(f"Your new balance is: {bank.accounts[0].balance} $")

    elif choice == "2":
        while True:
            try:
                amount = int(input("Enter the amount to withdraw: "))
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        bank.accounts[0].withdraw_of_account(amount)
        print(f"Your new balance is: {bank.accounts[0].balance} $")

    elif choice == "3":
        print(bank.accounts[0])

    elif choice == "4":
        while True:
            try:
                amount = int(input("Enter the amount to transfer: "))
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

        print("Which account do you want to transfer money from?")
        print("1. Account 1")
        print("2. Account 2")
        transfer_from_choice = input("Enter your choice (1-2): ")

        if transfer_from_choice == "1":
            transfer_from_account = bank.accounts[0]
        elif transfer_from_choice == "2":
            transfer_from_account = bank.accounts[0]
        else:
            print("Invalid choice. Please choose a valid option.")
            continue

        while True:
            try:
                account_number = int(input("Enter the account number of the recipient: "))
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

        transfer_to_account = Account(f"account {account_number}", 0)

        transfer_from_account.transfer_to_account(transfer_to_account, amount)

        print("Account details:")
        bank.get_account_details()

    elif choice == "5":
        history = bank.accounts[0].get_transaction_history()
        if not history:
            print("There are no more transactions for this account.")
        else:
                bank.accounts[0].get_transaction_history()
    

    elif choice == "6":
        new_owner = input("Enter the new owner name: ")
        bank.change_account_owner(bank.accounts[0], new_owner)

    elif choice == "7":
        bank.close_account(bank.accounts[0])

    elif choice == "8":
        print("Account details:")
        bank.get_account_details()

    elif choice == "9":
        print("Transaction details:")
        bank.get_transaction_details()

    elif choice == "10":
        while True:
            try:
                amount = int(input("Enter the balance threshold: "))
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        bank.accounts[0].set_balance_alert(amount)

    elif choice == "11":
        while True:
            try:
                amount = int(input("Enter the transaction threshold: "))
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        bank.accounts[0].set_transaction_alert(amount)

    elif choice == "12":
        print("Thank you for using our program.")
        sys.exit()

    else:
        print("Invalid choice. Please choose a valid option.")

    # Ask user if they want to perform another operation
    while True:
        another_operation = input("Do you want to perform another operation? (yes/no): ")
        if another_operation.lower() == "yes":
            break
        elif another_operation.lower() == "no":
            print("Thank you for using our program.")
            sys.exit()
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")