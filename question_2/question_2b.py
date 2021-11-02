
""" Question 2b

    - Class Account from question 2a
    - Create child class DevAccount inheriting from parent class Account
    - Set balance properties to 0 upon instantiation
    - Add method set_balance() and get_balance() and transfer_fund() to child class
    - Manual testing DevAccount class

"""

from collections import namedtuple
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

    def transfer_fund(self, amount, recipient):
        if not isinstance(recipient, DevAccount):
            return "Recipient does not exists !"
        elif amount > self.balance:
            return f"Balance is less than transfer funds"
        else:
            self.balance -= amount
            recipient.balance += amount
            return f"Current balance is: {self.balance}"

if __name__ == '__main__':
    
    print('\ninstantiate a dev account:')
    account_bojan = DevAccount('Bojan')
    print(account_bojan)

    print('\nmanual testing setting balance:')
    account_bojan.set_balance(50)
    print(account_bojan)

    print('\nmanual testing getting balance:')
    print(account_bojan.get_balance())

    print('\ninstantiate another dev account:')
    account_boyski = DevAccount('Boyski')
    print(account_boyski)

    print('\nmanual testing transfer from one account to another:')
    print(account_bojan.transfer_fund(10, account_boyski))
    print(account_boyski)