class Bank_account:
    def __init__(self,name,balance=0):
        self.name = name
        self.balance = balance
    def deposit(self,amount):
        if amount <= 0:
            print("Invalid deposit amount.")
            return
        self.balance += amount
        print(f"{amount} deposited successfully.")

    def withdraw(self,amount):
        if amount > self.balance:
            print('Insufficient Balance')
        else:
            print('Withdraw succesfull of ' , amount , 'tk')
            self.balance -= amount
    def check_balance(self):
        print(self.balance)
account1 = Bank_account('ADNAN')

account1.deposit(50000)
account1.withdraw(5000)
account1.check_balance()


print(account1.name, account1.balance)


while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Choose: ")

    if choice == "1":
        amount = float(input("Enter amount: "))
        account1.deposit(amount)
    elif choice == "2":
        amount = float(input("Enter amount: "))
        account1.withdraw(amount)
    elif choice == "3":
        account1.check_balance()
    elif choice == "4":
        break
    else:
        print("Invalid choice.")