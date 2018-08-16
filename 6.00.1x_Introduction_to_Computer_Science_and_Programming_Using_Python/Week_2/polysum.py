import math #importing math library to use mathematical function tan and pi constant.

def polysum(n, s):
    '''
    Assumes a regular polygon with:
        
    n: polygon's number of sides
    s: regular polygon side's size
    
    This function returns the sum of the area and square of the perimeter of a regular polygon.
    '''
    
    area = (0.25 * n * (s**2)) / (math.tan(math.pi / n))
    per = n * s
    
    polysum = area + per**2
    
    return round(polysum,4) #round to 4 decimal places

#print (polysum(33,13)) #test case: uncomment to perform the test // answer: 198642.2466