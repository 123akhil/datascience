# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 23:16:40 2016

@author: Camilo Cruz
"""
import numpy

def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)

#print f(5)

def radiationExposure(start, stop, step):
    assert stop > start, 'Stop time must be greater than start time!'
    assert step < (stop - start), 'Step size is too big!'
    
    #time = stop - start
    totalRadiation = 0
    for i in numpy.arange(start,stop,step):
        stepRadiation = f(i)*step
        totalRadiation += stepRadiation
    return totalRadiation

print radiationExposure(0, 5, 1)
print radiationExposure(5, 11, 1)
print radiationExposure(0, 11, 1)
print radiationExposure(40, 100, 1.5)
