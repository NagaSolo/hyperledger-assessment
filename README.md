### Hyperledger Fabric Developer Training - Level 2 Assessment

#### Question 1a
- You are given the following information, but you may prefer to do some research for yourself.

> 1 Jan 1900 was a Monday.
> Thirty days has September,
> April, June and November.
> All the rest have thirty-one,
> Saving February alone,
> Which has twenty-eight, rain or shine.
> And on leap years, twenty-nine.
> A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
> How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

#### Question 1b
Using NO BUILT IN LIBRARIES, write a program that satisfies the following problem:

> n! means n × (n − 1) × ... × 3 × 2 × 1

> For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800, and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 > + 8 + 0 + 0 = 27.

> Find the sum of the digits in the number 100!

#### Question 2
This section will evaluate your software practices, with a focus on object oriented programming. Do this question in a separete folder, in your preferred programming language.

#### Question 2a
We have provided you with a stub class called Account that represents a bank account. Please fill out the stub functions, then write a program that creates 3 unique instances of the class, and store them in a data structure of your choice. Explain your thought process behind choosing a data structure.

``` Python
class Account:
    def __init__(self, name, balance):
        self.id
        self.name
        self.balance

    def deposit(self, amount):

    def withdraw(self, amount):

    def __str__(self):
        return f"{self.name}'s account. Balance: {self.balance}"
```

#### Question 2b
We have recieved a request to create a new class DevAccount inheriting from the Account class for testing and development purposes. This new class contains the additional functions:

> Get Balance
> Set Balance
> Transfer to other account

Please implement the afformentioned class and their functions

#### Question 2c
Write a brief analysis about why you would use inheritance in this situation.

#### Question 3
You will be asked to demonstrate your code and thought process in a live interview. Prior to the demonstration, please ensure that all your code is working correctly.