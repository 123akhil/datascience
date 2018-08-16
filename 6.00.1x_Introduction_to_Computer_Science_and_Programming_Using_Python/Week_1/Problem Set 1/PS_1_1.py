# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 05:38:46 2017

@author: Camilo Cruz
"""
s = 'ltqqrgagutkonoxvjr'

count = 0
for char in s:
    if char in 'aeiou':
        count += 1
print (count)