
""" Question 2a

    - Added unique id using uuid4
    - Added logic to method deposit() and withdraw()
    - Instantiate 3 instances
    - Store instances with namedtuple
    - Store instances with hash maps

"""

import uuid

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

if __name__ == '__main__':

    account1 = Account('Boris', 20)
    account2 = Account('Borhan', 30)
    account3 = Account('Borat', 20)

    # store instance as hashmap
    accounts = {acc.id:acc for acc in [account1, account2, account3]}
    print(accounts.keys())
    print(accounts.values())

    # store instance using data structure namedtuple
    # from collections import namedtuple
    # account = namedtuple('Account', ('ID Name Balance'))

    # boris_account = account(str(account1.id), account1.name, account1.balance)
    # borhan_account = account(str(account2.id), account2.name, account2.balance)
    # borat_account = account(str(account3.id), account3.name, account3.balance)