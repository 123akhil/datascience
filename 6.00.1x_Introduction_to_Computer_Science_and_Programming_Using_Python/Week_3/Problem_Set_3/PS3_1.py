# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 01:04:52 2016

@author: Camilo Cruz
"""

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
   
    noExist = None
    for i in secretWord:
        #if (i in lettersGuessed) == True:
            #print i +' in '+ str(lettersGuessed),'-> True'
        if (i in lettersGuessed) == False:
            noExist = True
            #print i +' in '+ str(lettersGuessed),'-> False'
    return not noExist



secretWord = 'apple' 
lettersGuessed = ['e', 'i', 'k', 'p', 'a', 'l']


print isWordGuessed(secretWord, lettersGuessed)