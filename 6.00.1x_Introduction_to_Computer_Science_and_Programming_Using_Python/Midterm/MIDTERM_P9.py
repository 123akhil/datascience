# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 00:26:45 2017

@author: Camilo Cruz
"""

def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
    flattenList = []
    for elem in aList:
        if type(elem) == list: 
            flattenList.extend(flatten(elem))
        else: 
            flattenList.append(elem)
    
    return flattenList


unflat = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
print(flatten(unflat))

#if a == list: print('List!!!!')
#print(a,type(a))
#flat = [1,'a','cat',2,3,'dog',4,5] (order matters).