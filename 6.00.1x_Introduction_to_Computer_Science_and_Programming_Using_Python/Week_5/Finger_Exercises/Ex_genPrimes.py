# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 20:28:44 2017

@author: Camilo Cruz
"""

def getPrimes():
    primes = [2]
    x = 2
    yield 2
    
    while True:
        x += 1
        for n in primes:
            if (x % n) == 0:
                break
            if primes[-1] == n:
                primes.append(x)
                yield primes[-1]
                
        
        
            
            
