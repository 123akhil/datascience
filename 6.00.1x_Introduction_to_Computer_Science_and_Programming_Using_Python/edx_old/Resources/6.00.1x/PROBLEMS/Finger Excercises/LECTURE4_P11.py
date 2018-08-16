def isVowel2(char):
    '''
    char: a single letter of any case

    returns: True if char is a vowel and False otherwise.
    '''
    for x in ['a','e','i','o','u','A','E','I','O','U']:
        if char == x:
            result = True
            break
        else:
            result = False
     
    return result