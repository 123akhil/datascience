# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 01:47:07 2016

@author: Camilo Cruz
"""

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string
    chars = string.ascii_lowercase
    #print(chars)
    for i in lettersGuessed:
        if (i in chars) == True:
            chars = chars.replace(i,'')
            #print(chars)
           
    return chars
    
lettersGuessed = ['a', 'b', 'c']
print getAvailableLetters(lettersGuessed)
print getAvailableLetters('')
