def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    
    limit = (len (aStr))/2
    
    
    if len(aStr) == 1:
        
        if char == aStr:
            
            return True
    
        else:
        
            return False
    elif len(aStr) == 0:
        
        return False
    
    if char < aStr[limit]:
        
        return isIn(char, aStr [:limit])
        
    else:

        return isIn(char, aStr [limit:])
        
