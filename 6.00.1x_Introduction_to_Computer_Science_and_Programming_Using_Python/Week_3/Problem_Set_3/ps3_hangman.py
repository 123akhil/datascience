# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print ("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print ("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    noExist = None
    for i in secretWord:
        if (i in lettersGuessed) == False:
            noExist = True

    return not noExist



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


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    chars = string.ascii_lowercase

    for i in lettersGuessed:
        if (i in chars) == True:
            chars = chars.replace(i,'')
           
    return chars
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print('Welcome to the game, Hangman!')
    print ('I am thinking of a word that is %d letters long.' % len(secretWord))
#    secretWord_s = secretWord
    lettersGuessed = []
    mistakesMade = 0
    numGuessLeft = 8
    availableLetters = getAvailableLetters('')
    

    while True:
        print('-------------')
        print('You have %d guesses left.' % numGuessLeft)
        print('Available letters: %s' % availableLetters)
        
        guess = input('Please guess a letter: ')
        guessLower = guess.lower()

        
        if len(guessLower) > 1: #Prints error when char is not a single letter
            print ('Error. You must select a SINGLE letter.', getGuessedWord(secretWord, lettersGuessed))
            continue
        
        if (guessLower in getAvailableLetters('')) == False: #Prints error when typed char is not a letter
            print ('Error. You must select a letter.', getGuessedWord(secretWord, lettersGuessed))
            continue
        
        if (guessLower in lettersGuessed) == True: #skip the loop if the guessed letter is repeated
            print('Oops! You\'ve already guessed that letter: ', getGuessedWord(secretWord, lettersGuessed)) 
            continue
        
        lettersGuessed.append(guessLower)

        
        if (guessLower in availableLetters) == True: #Letter is guessed 1st time
            availableLetters =  getAvailableLetters(lettersGuessed)
        
        if (guessLower in secretWord) == True: #Good guess
            print('Good guess: ', getGuessedWord(secretWord, lettersGuessed))
        
        if (guessLower in secretWord) == False: #Incorrect guess
            mistakesMade += 1
            numGuessLeft -= 1
            print('Oops! That letter is not in my word: ', getGuessedWord(secretWord, lettersGuessed))
 
            
        if (isWordGuessed(secretWord, lettersGuessed)) == True: #Game won
            print('-----------\nCongratulations, you won!')
            break
        
        if mistakesMade == 8: #Game lost
            print('-----------\nSorry, you ran out of guesses. The word was %s.' % secretWord)
            break
        



# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
