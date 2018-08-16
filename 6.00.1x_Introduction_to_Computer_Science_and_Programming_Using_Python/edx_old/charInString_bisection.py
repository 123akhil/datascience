def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # base case: 
    pos = len(aStr)/2
    
    if len(aStr) == 0:
        return False
    
    elif char == aStr[pos]:
        return True
    
    elif len(aStr) == 1:
        if char == aStr[0]:
            return True
        else:
            return False
    
    elif char < aStr[pos]:
        return isIn(char, aStr[:pos])

    elif char > aStr[pos]:
        return isIn(char, aStr[pos:])

print isIn('d','abcdefghi')