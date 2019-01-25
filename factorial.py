#!/usr/bin/env python
"""Module for estimation of factorial (Homework #1)

Note:  this is just a skeleton for you to work with.  But it already
       has some "bugs" you need to catch and fix.
"""


def factorial(n):
    answer = 1
    for x in range(1, n + 1):
        answer = answer * x
    return answer


def test_factorial():
    assert factorial(1) == 1
    # TODO: add more


if __name__ == '__main__':

    # This is a way to determine either file was "executed", so if it was
    # imported (by e.g. pytest) as a library, we should not run code
    # below

    nconditions = int(input("Please enter number of conditions: "))
    norders = factorial(nconditions)
    print("Number of possible trial orders: " + str(norders))
