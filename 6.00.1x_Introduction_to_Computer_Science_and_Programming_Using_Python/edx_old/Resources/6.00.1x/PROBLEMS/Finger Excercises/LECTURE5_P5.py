def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    
    minimum = min (a,b)
    
    maximum = max (a,b)
    
    if minimum == 0:
        
        return maximum
    
    elif minimum > 0:
        
        return gcdRecur(minimum, maximum % minimum)