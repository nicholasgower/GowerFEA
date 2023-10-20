# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 10:52:03 2023

@author: Nicholas
"""
from numpy import array

def angle_constraint(P1,P2,theta,L1,L2):
    return -L1*array([P2[0],P1[1]])+array([[cos(theta),-sin(theta)],[sin(theta),cos(theta)]])