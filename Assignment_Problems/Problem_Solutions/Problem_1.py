'''
Problem: Create a class called "BankAccount" that represents a bank account. The class should
have the following features:
● A constructor method that takes the account holder's name and initial balance as
parameters and initializes them.
● A method called "deposit" that takes an amount as a parameter and adds it to the
account balance.
● A method called "withdraw" that takes an amount as a parameter and subtracts it from
the account balance, if the account has sufficient funds.
● A method called "get_balance" that returns the current balance of the account.
● A method called "display_account_info" that prints the account holder's name and
current balance.
Write the BankAccount class and demonstrate its usage by creating multiple instances of the
class, performing various transactions, and displaying the account information.
'''
class BankAccount:
    def __init__(self,account_holder,initial_balance):
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self,amount):
        self.balance += amount

    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Due to Insufficient Fund, Withdrawal is Cancelled!")

    def get_balance(self):
        return self.balance

    def display_account_info(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: {self.balance}")

account1 = BankAccount("Aniket Ugale",5000)
account1.display_account_info()

account1.deposit(1000)
account1.display_account_info()

account1.withdraw(2000)
account1.display_account_info()

account1.withdraw(4200)
account1.display_account_info()


