# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 20:11:26 2017

@author: Camilo Cruz
"""

def laceStrings(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    lacedString = ''
    dif = len(s1) - len(s2)
    
    if dif == 0:
         for i in range(len(s2)):
            lacedString = lacedString + s1[i]
            lacedString = lacedString + s2[i]
        
    if dif < 0:
        for i in range(len(s1)):
            lacedString = lacedString + s1[i]
            lacedString = lacedString + s2[i]
        
        for i in range(dif, 0):
            lacedString = lacedString + s2[i] 
    
    if dif > 0:
        for i in range(len(s2)):
            lacedString = lacedString + s1[i]
            lacedString = lacedString + s2[i]
        
        for i in range(-dif,0):
            lacedString = lacedString + s1[i]
        
            
    return lacedString

print(laceStrings('HOLA', '1234'))
print(laceStrings('HOLA', '1234567'))
print(laceStrings('ALEMANIA', '1234'))