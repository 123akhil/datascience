# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 01:10:40 2016

@author: Camilo Cruz
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 00:27:39 2016

@author: Camilo Cruz
"""

def gcdIter(a, b):
    gcd = min(a,b)
        
    while a%gcd != 0 or b%gcd != 0:
        gcd-=1
    
    return gcd 
print gcdIter(9,12)