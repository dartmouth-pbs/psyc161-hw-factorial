#!/usr/bin/env python
"""Module for estimation of factorial (Homework #1)

Note:  this is just a skeleton for you to work with.  But it already
       has some "bugs" you need to catch and fix.
"""


def factorial(n):
    # Define your logic for factorial here
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n-1)


def test_factorial():
    # Tests the function with value 1
    assert factorial(1) == 1
    assert factorial(0) == 1


if __name__ == '__main__':
    # This is a way to determine either file was "executed", so if it was
    # imported as a library, we should not run code below
    conditions = int(input("Please enter number of conditions: "))
    orders = factorial(conditions)
    print("Number of possible trial orders: " + str(orders))
