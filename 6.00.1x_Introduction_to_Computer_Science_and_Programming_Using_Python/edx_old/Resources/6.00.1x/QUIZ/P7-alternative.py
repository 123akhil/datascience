def McNuggets(n):
    """
    n is an int

    Returns True if some integer combination of 6, 9 and 20 equals n
    Otherwise returns False.
    """
    
    # 6a+9b+20c=n
    
    def f(a,b,c):
        
        return 6*a+9*b+20*c
    
    c = 1
    b = 1
    a = 1
    
    while f(a,b,c) <= n:
        
        if f(a,b,c)== n:
            
            return True
        else:
            c = c - 1
            
            b = b + 1
        
        

    
    
    
    