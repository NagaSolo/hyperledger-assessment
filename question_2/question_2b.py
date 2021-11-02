
""" Question 2b

    - Class Account from question 2a
    - Create child class DevAccount inheriting from parent class Account
    - Set balance properties to 0 upon instantiation
    - Add method set_balance() and get_balance() to child class
    - Manual testing DevAccount class

"""

import uuid

# class Account from question 2a
class Account:
    def __init__(self, name, balance):
        self.id = uuid.uuid4()
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f'Current balance is: {self.balance}'

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
        else:
            return 'Insufficient balance to withdraw'

    def __str__(self):
        return f"{self.name}'s account. Balance: {self.balance}"


# DevAccount class inherit properties and methods from Account
class DevAccount(Account):
    def __init__(self, name):
        super().__init__(name, balance=0)

    def set_balance(self, amount):
        self.balance = amount

    def get_balance(self):
        return f"Current balance is: {self.balance}"

if __name__ == '__main__':
    
    # instantiate a dev account
    account_dev = DevAccount('Bojan')
    print(account_dev)

    # manual testing setting balance
    account_dev.set_balance(50)
    print(account_dev)

    # manual testing getting balance
    print(account_dev.get_balance())