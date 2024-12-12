# Task 4 

class BankAccount:
    def __init__(self):
        self.balance = 0  

    def deposit(self, amount):
        if amount > 0:  
            self.balance += amount
            print(f"Balance after Deposit : {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0: 
            if self.balance >= amount:  
                self.balance -= amount
                print(f"Balance After Withdrawal : {self.balance}")
            else:
                print("Insufficient balance.")
        else:
            print("Withdrawal amount must be positive.")

    def get_balance(self):
        return self.balance


account = BankAccount()

while True:
    print("\nChoose an operation:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")  
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        amount = float(input("Enter amount to deposit: "))
        account.deposit(amount)
    elif choice == '2':
        amount = float(input("Enter amount to withdraw: "))
        account.withdraw(amount)
    elif choice == '3':
        print(f"Current Balance: {account.get_balance()}")
    elif choice == '4':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
