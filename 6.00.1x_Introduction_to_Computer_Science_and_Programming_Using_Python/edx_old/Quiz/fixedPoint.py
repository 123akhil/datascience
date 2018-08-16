# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 22:13:30 2017

@author: Camilo Cruz
"""

def fixedPoint(f, epsilon):
    """
    f: a function of one argument that returns a float
    epsilon: a small float
  
    returns the best guess when that guess is less than epsilon 
    away from f(guess) or after 100 trials, whichever comes first.
    """
    guess = 1.0
    for i in range(100):
        if abs(f(guess) - guess) < epsilon:
            print 'epsilon'
            return guess
        else:
            print 'loop'
            guess = f(guess)
    return guess

def square(n):
    return n*n
    
    
print fixedPoint(square, 8)