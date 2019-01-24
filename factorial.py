#!/usr/bin/env python
"""Module for estimation of factorial (Homework #1)

Note:  this is just a skeleton for you to work with.  But it already
       has some "bugs" you need to catch and fix.
"""


def factorial(n):

    if n == 0 or n < 0:

        outputCalc = 1

    else:

        outputCalc = 1

        for number in range(1, n+1):

            outputCalc = number * outputCalc

    return outputCalc


def test_factorial():
    assert factorial(1) == 1
    assert factorial(0) == 1
    assert factorial(-10) == 1


if __name__ == '__main__':
    # This is a way to determine either file was "executed", so if it was
    # imported (by e.g. pytest) as a library, we should not run code
    # below
    nconditions = int(input("Please enter number of conditions: "))
    norders = factorial(nconditions)
    print("Number of possible trial orders: " + str(norders))
