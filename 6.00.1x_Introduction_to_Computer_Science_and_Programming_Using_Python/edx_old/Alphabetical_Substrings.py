# -*- coding: utf-8 -*-
"""
Count the number of times a substring is found on a larger string
Created on Wed Nov 02 23:39:59 2016
@author: Camilo
Note: Erase the '#' to visualize the execution
"""

word = 'cam'
string = 'pppppppaeiouppppppaeioupzaaaaaaeiosxyz' #modify for raw_input
count = 0
for_count = 0
substr = string[0]
max_str = string[0]

#range_max = len(string) - len(word) + 1

for i in range(1, len(string)):
    for_count += 1
    #print for_count, 'Substr:' + substr, 'Max:' + max_str
    
        
    if string[i] >= string[i-1]:
        substr += string[i]
        #max_str += string[i] 
        if len(substr) > len(max_str):
            max_str = substr
    
    elif string[i] < string[i-1] :
        #substr += string[i]
        #max_str = substr
        substr = string[i]
    
    

print ('Longest substring in alphabetical order is: ') + max_str
#print for_count                   
