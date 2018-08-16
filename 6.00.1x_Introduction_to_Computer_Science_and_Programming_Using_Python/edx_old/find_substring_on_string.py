# -*- coding: utf-8 -*-
"""
Count the number of times a substring is found on a larger string
Created on Wed Nov 02 23:39:59 2016
@author: Camilo
Note: Erase the '#' to visualize the execution
"""

word = 'cam'
string = 'camilo casa costal camaron callado'
count = 0
for_count = 0

range_max = len(string) - len(word) + 1

for i in range(0, range_max):
    for_count += 1
    sub_string = string[i:i+len(word)]
    print for_count, sub_string
    if sub_string == word:
        count +=1

print count                    
