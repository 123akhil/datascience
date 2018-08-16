# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 18:17:14 2017

@author: Camilo Cruz
"""

def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    sum = 0
    
    for i in range(len(listA)):
        sum += listA[i] * listB[i]

    return sum

print(dotProduct([1, 2, 3] , [4, 5, 6]))