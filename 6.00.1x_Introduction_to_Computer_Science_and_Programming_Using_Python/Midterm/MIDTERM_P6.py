# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 18:21:51 2017

@author: Camilo Cruz
"""

def deep_reverse(L):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also 
    reverses the order of the int elements in every element of L. 
    It does not return anything.
    """
    for i in range(len(L)):
        L[i].reverse()
    
    return L.reverse()
         
            
L = [[1, 2], [3, 4], [5, 6, 7]]
deep_reverse(L) 
print(L)


i = ([[0, 1, 2], [1, 2, 3]])
deep_reverse(i)
print(i)
    