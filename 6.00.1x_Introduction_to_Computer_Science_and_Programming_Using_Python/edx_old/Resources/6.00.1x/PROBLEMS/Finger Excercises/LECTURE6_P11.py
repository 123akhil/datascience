animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')


def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    largest = 0
    
    if len (aDict) > 0:

        for x in aDict:
            
            if largest <= len (aDict[x]):
    
                largest = len (aDict[x])
                result = x
    
        return result
            
        
        
