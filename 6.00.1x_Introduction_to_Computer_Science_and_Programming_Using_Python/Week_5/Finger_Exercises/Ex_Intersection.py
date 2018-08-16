# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 23:00:33 2017

@author: Camilo Cruz
"""

class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self""" 
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'
    
    def intersect(self, other):
        """Returns the intersection set between two intSet"""
        assert type(self) == type(other) #check if objects are same class
        intersectionSet = []
        
        #Go through both sets
        for e1 in self.vals:
            for e2 in other.vals:
                if e1 == e2:  # Check if value is on both sets
                    intersectionSet.append(e1)
        return '{' + ','.join([str(e) for e in intersectionSet]) + '}'

        '''Alternative
                # Initialize a new intSet    
                commonValueSet = intSet()
                # Go through the values in this set
                for val in self.vals:
                    # Check if each value is a member of the other set    
                    if other.member(val):
                        commonValueSet.insert(val)
                return commonValueSet
        '''


    def __len__(self):
        return len(self.vals)