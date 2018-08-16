# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 19:08:53 2017

@author: Camilo Cruz
"""

#get keys
def f(a,b): 
#    return a+b #Test case 1
    return a>b #Test case 2
     
def getKeys(dict1, dict2):
    intersection    = sorted(set(dict1).intersection(dict2))
    diffDict1       = sorted(set(dict1).difference(dict2))
    diffDict2       = sorted(set(dict2).difference(dict1))
    
    return intersection, diffDict1 + diffDict2

def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    [match, diff] = getKeys(d1, d2)
#    print(match, diff)
    answerTuple = ()
    matchDict = {}
    diffDict = {}
    
    for key in match:
        matchDict[key] = f(d1[key],d2[key])
    
    for key in diff:
        try:
            diffDict[key] = d1[key]
                        
        except KeyError:
            diffDict[key] = d2[key]
            continue
    
    answerTuple = (matchDict,) + (diffDict,)
    return answerTuple            
    
        
'''Test case 1
#d1 = {1:30, 2:20, 3:30, 5:80}
#d2 = {1:40, 2:50, 3:60, 4:70, 6:90}
'''

#Test case 2
d1 = {1:30, 2:20, 3:30}
d2 = {1:40, 2:50, 3:60}
#

print(dict_interdiff(d1, d2))
    