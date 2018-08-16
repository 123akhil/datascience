def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    exp = 0
    
    while (base**exp < num):
            exp += 1
            
    if abs(base**exp - num) >= abs(base**(exp-1) - num):
        return exp-1
    
    return exp
    

print(closest_power(2, 384)) # 8
print(closest_power(10, 550)) #4
print(closest_power(3, 12))  # 2
print(closest_power(4, 12))  # 2
print(closest_power(4, 1))  # 0