# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 22:45:07 2017

@author: Camilo Cruz
"""

class Coordinate(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'

    def __eq__(self, other):
        # make sure other is the same type object
        assert type(other) == type(self)
        # returns True if coordinates refer to same point in the plane
        return (self.getX() == other.getX()) and (self.getY() == other.getY())
    
    def __repr__(self):
        return 'Coordinate(' + str(self.getX()) + ',' + str(self.getY()) + ')'