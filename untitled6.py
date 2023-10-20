# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 17:53:32 2023

@author: Nicholas
"""

from scipy.optimize import fsolve
from numpy import pi, arctan2, sqrt

angle = pi/2
h = 10
w = 10

def equations(p):
    x = p[0]
    y = p[1]
    return [
        x[0] - x[1],
        y[0] - y[1],
        x[3] - x[4],
        y[3] - y[4],
        x[1] - x[5],
        y[1] - y[5],
        -angle + arctan2(y[5] - y[4], x[5] - x[4]) - arctan2(y[2] - y[3], x[2] - x[3]),
        -h + sqrt((x[5] - x[4])**2 + (y[5] - y[4])**2),
        -w + sqrt((x[4] - x[3])**2 + (y[4] - y[3])**2),
        x[0],
        y[0],
        arctan2(y[5] - y[4], x[5] - x[4])
    ]

x, y = fsolve(equations, ([1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]))