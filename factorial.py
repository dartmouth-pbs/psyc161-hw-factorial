#!/usr/bin/env python
"""Module for estimation of factorial (Homework #1)

Note:  this is just a skeleton for you to work with.  But it already
       has some "bugs" you need to catch and fix.
"""


def factorial(n):
    # TODO Define your logic for factorial here
    if n - 1 != 0:
    	multiplier = factorial(n-1)
    	return n*multiplier # TODO!
    else:
    	return n

def test_factorial():
    assert factorial(1) == 1
    # TODO: add more

if __name__ == '__main__':
    # This is a way to determine either file was "executed", so if it was
    # imported (by e.g. pytest) as a library, we should not run code
    # below
    nconditions = int(raw_input("Please enter number of conditions: "))
    norders = factorial(nconditions)
    print("Number of possible trial orders: " + str(norders))
