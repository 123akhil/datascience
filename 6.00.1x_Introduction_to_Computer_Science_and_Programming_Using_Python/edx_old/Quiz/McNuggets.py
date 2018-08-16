# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 21:39:18 2017

@author: Camilo Cruz
"""
def McNuggets(n):
    """
    n is an int

    Returns True if some integer combination of 6, 9 and 20 equals n
    Otherwise returns False.
    """
    if n == 0:
        return True
    
    for i in (6, 9, 20):
        if n >= i and McNuggets(n - i):
            return True
        
    return False