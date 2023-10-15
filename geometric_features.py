# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 14:44:18 2023

@author: Nicholas
"""

from numpy import array

class drawing:
    def __init__(self,fileDir):
        self.fileDir=fileDir
        self.features=[]
        self.xAxis=line(self,array([0,0]),array([1,0]))
        self.yAxis=line(self,array([0,0]),array([0,1]))
    def add_feature(self,)

    def 

#Planned dimensions:
    #Distance(Line/point, Line/point)
    #Angle(Line,Line)
    #Horizontal distance
    #Vertical distance
    
    
class dimension:
    def __init__(self,drawing,entity1,entity2):
        
#Planned constraints:
    #Coincident (distance=0)
    #parallel (angle=0)
        #horizontal (parallel to x axis)
        #vertical   (parallel to y axis) 
    #perpendicular (angle=90)
    
    #concentric (Two circles/arcs have the same center)
        #coradial (Two circles/arcs)
    #Equal(Two lines have the same length, or two circles have the same radius)



#Planned geometric features:
    #Point
    #Line (Two points)
    #Line Segment (Two points)
    #Circle #Center, radius
    #Arc # Two points, radius
    #     
    
class geometric_feature:
    def __init__(self,drawing,construction=False):
        self.drawing=drawing
        self.construction=construction
        self.children=[]:
    def get_children:
        return [self.children]
        
class point(geometric_feature):
    def __init__(self,drawing,location=[0,0]):
        geometric_feature.__init__(self,drawing)
        self.location=location
        
class line(geometric_feature):
    def __init__(self,drawing,point1,point2):
        geometric_feature.__init__(self,drawing)
        self.points=[point1,point2]
class line_segment(line):       
    def
    
class rectangle:
        
class corner_rectangle(geometric_feature):
    def __init__(self,drawing,corner1,corner2):
        
        
        