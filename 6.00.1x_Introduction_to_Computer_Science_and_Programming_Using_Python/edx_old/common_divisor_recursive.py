# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 00:27:39 2016

@author: Camilo Cruz
"""

def gcdIter(a, b):
    if a < b:
        gcd = a
    else:
        gcd = b
        
    while a%gcd != 0 or b%gcd != 0:
        gcd-=1
    
    return gcd        
    
    