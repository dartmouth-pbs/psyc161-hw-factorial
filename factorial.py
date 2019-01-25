#!/usr/bin/env python
"""Module for estimation of factorial (Homework #1)

Note:  this is just a skeleton for you to work with.  But it already
       has some "bugs" you need to catch and fix.
"""


def factorial(n):
    fac = 1
    for i in range(n):
        i += 1
        fac = i * fac 
        
    return fac


def test_factorial():
    assert factorial(1) == 1
    assert factorial(2) == 2
    assert factorial(3) == 6
    assert factorial(4) == 24


if __name__ == '__main__':
    # This is a way to determine either file was "executed", so if it was
    # imported (by e.g. pytest) as a library, we should not run code
    # below
    nconditions = int(input("Please enter number of conditions: "))
    norders = factorial(nconditions)
    print("Number of possible trial orders: " + str(norders))
