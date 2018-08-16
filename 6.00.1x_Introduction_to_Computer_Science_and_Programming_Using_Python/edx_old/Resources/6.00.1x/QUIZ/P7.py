def McNuggets(n):
    """
    n is an int

    Returns True if some integer combination of 6, 9 and 20 equals n
    Otherwise returns False.
    """
    

    # 6a+9b+20c=n
    
    if n == 6 or n == 9 or n == 20 or n==0:
        return True
    
    elif n >= 2*20:
        
        return McNuggets(n-20)
    
    elif n >= 2*9:
        
        return McNuggets(n-9)

    elif n >= 2*6:
        
        return McNuggets(n-6)
    
    else:
        
        return False
