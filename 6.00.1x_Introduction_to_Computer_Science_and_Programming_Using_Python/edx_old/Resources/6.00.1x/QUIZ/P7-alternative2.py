def McNuggets(n):
    """
    n is an int

    Returns True if some integer combination of 6, 9 and 20 equals n
    Otherwise returns False.
    """
    
    def f1(a,b,c):
        
        return 6*a+9*b+20*c
     
    c = 0
    while f1(0,0,c) <= n:
        b = 0
        while f1(0,b,c) <= n:
            a = 0
            while f1(a,b,c) <= n:
                if f1(a,b,c) == n:
                    print 'a = ' + str(a)
                    print 'b = ' + str(b)
                    print 'c = ' + str(c)
                    return True
                a = a+1
            b = b+1
        c = c+1
    return f1(a,b,c) == n