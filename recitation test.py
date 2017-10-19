#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 15:32:21 2017

@author: Rita
"""

def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)

def main():
    number= int(input('Enter a nonnegative integer:'))
    fact = factorial(number)
    print('The factorial of',number,'is',fact)
main()