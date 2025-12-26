# ==================== Bank Management System ====================

class Account:
    acc_no = 100  # class variable for account number generation

    def __init__(self, holder_name, mob_no, pan_no, balance=1000):
        Account.acc_no += 1
        self.account_no = Account.acc_no
        self.holder_name = holder_name
        self.mob_no = mob_no
        self.pan_no = pan_no
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def display(self):
        print("\n===== Account Details =====")
        print(f"Account Holder Name : {self.holder_name}")
        print(f"Account Number      : {self.account_no}")
        print(f"Mobile Number       : {self.mob_no}")
        print(f"PAN Number          : {self.pan_no}")
        print(f"Balance             : {self.balance}")


class Bank:
    def __init__(self):
        self.accounts = {}  # key = account number, value = Account object

    def create_account(self, name, mob_no, pan_no):
        account = Account(name, mob_no, pan_no)
        self.accounts[account.account_no] = account
        print("\nAccount successfully created")
        print(f"Your Account Number is {account.account_no}")
        print("Initial Balance: 1000")

    def deposit(self, acc_no, amount):
        account = self.accounts.get(acc_no)
        if account:
            if account.deposit(amount):
                print(f"{amount}$ deposited successfully")
            else:
                print("Invalid deposit amount!")
        else:
            print("Account not found!")

    # 🔐 Withdrawal with PAN verification
    def withdraw(self, acc_no, pan_no, amount):
        account = self.accounts.get(acc_no)
        if not account:
            print("Account not found!")
            return

        if account.pan_no != pan_no:
            print("PAN verification failed!")
            return

        if account.withdraw(amount):
            print(f"{amount}$ withdrawn successfully")
        else:
            print("Insufficient balance or invalid amount!")

    def transfer(self, from_acc, to_acc, amount):
        acc1 = self.accounts.get(from_acc)
        acc2 = self.accounts.get(to_acc)

        if acc1 and acc2:
            if acc1.withdraw(amount):
                acc2.deposit(amount)
                print(f"{amount}$ transferred successfully")
            else:
                print("Insufficient balance!")
        else:
            print("One or both accounts not found!")

    def display(self, acc_no):
        account = self.accounts.get(acc_no)
        if account:
            account.display()
        else:
            print("Account not found!")


# ==================== User Interface ====================

bank = Bank()
print("========== Welcome to ABC Bank ==========")

while True:
    print("""
1. Create Account
2. Deposit
3. Withdraw (PAN Required)
4. Transfer
5. View Account Details
6. Exit
""")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid number!")
        continue

    if choice == 1:
        name = input("Enter Account Holder's Name: ")
        mob_no = input("Enter Mobile Number: ")
        pan_no = input("Enter PAN Card Number: ")
        bank.create_account(name, mob_no, pan_no)

    elif choice == 2:
        acc = int(input("Enter Account Number: "))
        amt = float(input("Enter amount to deposit: "))
        bank.deposit(acc, amt)

    elif choice == 3:
        acc = int(input("Enter Account Number: "))
        pan = input("Enter PAN Card Number for verification: ")
        amt = float(input("Enter amount to withdraw: "))
        bank.withdraw(acc, pan, amt)

    elif choice == 4:
        acc1 = int(input("Enter Sender Account Number: "))
        acc2 = int(input("Enter Receiver Account Number: "))
        amt = float(input("Enter amount to transfer: "))
        bank.transfer(acc1, acc2, amt)

    elif choice == 5:
        acc = int(input("Enter Account Number: "))
        bank.display(acc)

    elif choice == 6:
        print("Thanks for using ABC Bank. Come again!")
        break

    else:
        print("Invalid choice! Please try again.")
