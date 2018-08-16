# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 01:36:47 2016

@author: Camilo Cruz
"""

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    guess = ''
    for i in secretWord:
        if (i in lettersGuessed) == True:
            guess = guess + i + ' '
            
        if (i in lettersGuessed) == False:
            guess = guess + '_ '
            
    return guess
    
secretWord = 'applewerkauf' 
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print getGuessedWord(secretWord, lettersGuessed)
#'_ pp_ e'