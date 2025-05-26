class Bank:

    def __init__(self, name):
        self.name = name
        self.balance = 0.0 
    
    def deposit(self, amount):
        if amount > 0 :
            self.balance += amount
            print(f"{amount} has been Deposited ! ")
        else :
            print("Please Enter a valid amount to deposit ! ")
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"{amount} has been withdrawn ! ")
        else :
            print("Insufficient balance or invalid amount ! ")
    
    def check_balance(self):
        print(f"{self.balance} is your current balance ! ")

bank1 = Bank("John Doe")

"""
bank1.deposit(1000)
bank1.withdraw(500)
bank1.check_balance()
"""

while True :
    print("Welcome to the Bank ! \n1. Deposit Money \n2. Withdraw Money \n3. Check Balance \n4. Exit")
    choice = input("Enter your choice: ")
    
    if choice == '1':
        amount = float(input("Enter the amount to deposit: "))
        bank1.deposit(amount)
    elif choice == '2':
        amount = float(input("Enter the amount to withdraw: "))
        bank1.withdraw(amount)
    elif choice == '3':
        bank1.check_balance()
    elif choice == '4':
        print("Thank you for using our services!")
        break
    else:
        print("Invalid choice, please try again.")