# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 05:45:57 2017

@author: Camilo Cruz
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

print(count)