#!/usr/bin/env python
"""Module for estimation of factorial (Homework #1)

Note:  this is just a skeleton for you to work with.  But it already
       has some "bugs" you need to catch and fix.
"""


def factorial(n):
    final_answer = 1
    for i in range(n):
        product = n - i
        final_answer *= product
    return final_answer

def test_factorial():
    assert factorial(1) == 1
    assert factorial(3) == 6
    assert factorial(6) == 720

if __name__ == '__main__':
    # This is a way to determine either file was "executed", so if it was
    # imported (by e.g. pytest) as a library, we should not run code
    # below
    nconditions = int(raw_input("Please enter number of conditions: "))
    norders = factorial(nconditions)
    print("Number of possible trial orders: " + str(norders))
