#!/usr/bin/env python
"""Module for estimation of factorial (Homework #1)
Mohsen Rakhshan
Note:  I am playing with this homework to learn git and ...
"""


def factorial(n):

    outputCalc = 1
    for number in range(1, n+1):
        outputCalc = number * outputCalc
    return outputCalc


def test_factorial():
    assert factorial(2) == 1
    assert factorial(0) == 1
    assert factorial(-10) == 1


if __name__ == '__main__':
    nconditions = int(input("Please enter number of conditions: "))
    norders = factorial(nconditions)
    print("Number of possible trial orders: " + str(norders))
