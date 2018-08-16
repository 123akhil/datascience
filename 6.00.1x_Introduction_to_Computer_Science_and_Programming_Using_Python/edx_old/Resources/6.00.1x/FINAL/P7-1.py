# -*- coding: utf-8 -*-
class Frob(object):
    def __init__(self, name):
        self.name = name
        self.before = None
        self.after = None
    def setBefore(self, before):
        self.before = before
    def setAfter(self, after):
        self.after = after
    def getBefore(self):
        return self.before
    def getAfter(self):
        return self.after
    def myName(self):
        return self.name

def insert(atMe, newFrob):
    """
    atMe: a Frob that is part of a doubly linked list
    newFrob:  a Frob with no links 
    This procedure appropriately inserts newFrob into the linked list that atMe is a part of.    
    """
   
    if newFrob.name < atMe.name:
        
        if atMe.before == None:
            
            atMe.before = newFrob
            newFrob.after = atMe
        
        elif newFrob.name >= atMe.before.name:

            atMe.before.after = newFrob
            newFrob.before = atMe.before
            atMe.before = newFrob
            newFrob.after = atMe
        else:
            insert(atMe.before,newFrob)        
    
    else:
        
        if atMe.after == None:
            
            atMe.after = newFrob
            newFrob.before = atMe
        elif newFrob.name < atMe.after.name:
            atMe.after.before = newFrob
            newFrob.after = atMe.after
            atMe.after = newFrob
            newFrob.before = atMe
        else:
            insert(atMe.after,newFrob)

eric = Frob('eric')
andrew = Frob('andrew')
ruth = Frob('ruth')
fred = Frob('fred')
martha = Frob('martha')
    
insert(eric, andrew)
insert(eric, ruth)
insert(eric, fred)
insert(ruth, martha) 
