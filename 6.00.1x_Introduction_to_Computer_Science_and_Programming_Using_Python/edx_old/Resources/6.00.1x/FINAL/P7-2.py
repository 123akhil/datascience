def findFront(start):
    """
    start: a Frob that is part of a doubly linked list
    returns: the Frob at the beginning of the linked list 
    """
    if start.before == None:
        return start
    else:
        return findFront(start.before)
