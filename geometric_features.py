# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 14:44:18 2023

@author: Nicholas
"""

from numpy import array, sqrt, sin, cos, tan
from functools import partial

class drawing:
    def __init__(self,fileDir,name="New drawing"):
        self.fileDir=fileDir
        self.name=name
        self.features=[]
        self.dimensions=[]
        self.xAxis=line(self,array([0,0]),array([1,0]))
        self.yAxis=line(self,array([0,0]),array([0,1]))
    def __str__(self):
        return "{}".format(self.name)
    def add_feature(self,feature):
        self.features.append(feature)
    def add_dimension(self,dimension):
        self.dimensions.append(dimension)
        return dimension
    #def add_dimension(self,)
    def get_features():
        out=self.features
        for feature in self.features:
            out+=feature.children
    def rebuild():
        pass
        #Apply constraints
        #Apply Dimensions
        

#Planned dimensions:
    #Distance(Line/point, Line/point)
    #Angle(Line,Line)
    #Horizontal distance
    #Vertical distance
    
    
class dimension:
    def __init__(self,drawing,entity1,entity2):
        self.drawing=drawing
        self.entity1=entity1
        self.entity2=entity2
        
    def __str__(self):
        return "Dimension for \"{}\" involving {} and {}".format(self.drawing,self.entity1,self.entity2)
    
#Editors note: 10/16/2023    
#This dimension code is getting very convoluted. I'm going with a more centralized approach. All geometric features, constraints and 
#dimensions shall only be stored within the drawing object, and the numerical positions of features will be recalculated whenever
#a rebuild function is called within the drawing object. Each feature object will only contain numerical data, not partial functions, as
#I attempted to do. It is clear that relying on partial objects will make the program much more difficult to debug.

#I wonder if putting constraints and dimensions within a matrix and solving the matrix is a good way to build drawings?
#That would require defining each constraint as an algebraic equation. Quite a bit simpler than my old approach.
# A theoretical example:

#length constraint: l^2=x^2+y^2
#Angle constraint: 
#Already, with this approach, we've left the realm of linear equations

#Defining a right triangle:
#Three lines, Three points
#Required constraints: perpendicular, length, length, coincident, coincident, coincident
#perpendicul

    
"""
class vertical_distance(dimension): #Defines vertical distance between two points
    def __init__(self,drawing,entity1,entity2,distance):
        dimension.__init__(self,drawing,entity1,entity2)
        self.distance=distance
        self.baseLocation=entity1.location
        self.horizontal_distance2=entity2.location[0]
        self.distance=distance
        entity1.dimensions.append(self)
        entity2.dimensions.append(self)
        self.entity1.location=partial(self.location,self.entity1)
        self.entity2.location=partial(self.location,self.entity2)
        
        self.entity1.location_constraint=self
        self.entity2.location_constraint=self
        
    def __str__(self):
        return "Vertical Distance dimension ({}) between {} and {}".format(self.distance,self.entity1,self.entity2)
    def location(self,entity):
        if entity is self.entity1:
            return self.baseLocation
        if entity is self.entity2:
            return [self.horizontal_distance2,self.baseLocation[1]]+array([0,self.distance])
"""           
    
class vertical distance    
        
class angle(dimension):
    def __init__(self,drawing,entity1,entity2,angle):
        pass
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
    #Polygon
    #Rectangle
    
class geometric_feature:
    def __init__(self,drawing,construction=False):
        self.drawing=drawing
        self.construction=construction
        self.children=[]
        self.constraints=[]
        self.dimensions=[]
        self.underdefined=True
        self.degrees_of_freedom=0
    def get_children(self):
        out=self.children
        for child in self.children:
            out+=child.get_children()
        return out
    def get_intersection(self,otherFeature):
        return NotImplementedError
    def add_dimension(self,dimension):
        self.dimensions.append(dimension)
        
        return dimension
    def add_constraint(self,constraint):
        self.constraints.append(dimension)
        return constraint
    
    
    
class point(geometric_feature):
    def __init__(self,drawing,location=[0,0]):
        geometric_feature.__init__(self,drawing)
        
        self.location=array(location)
        self.location_constraint=None #Points to constraint/dimension defining the location if location is defined by one.
    def __str__(self):
        return "Point at [{},{}]".format(self.x(),self.y())
    def setX(self,newX): # X getter
        #if type(self.location) is partial:
        #    if self.location_constraint.entity1 is self:
        #        self.location_constraint
        #    elif self.location_constraint.entity2 is self:
        #        pass
        #else:
        #    self.location[0]=newX
        self.location[0]=newX
    def setY(self,newY): # Y setter
        #if type(self.location) is partial:
        #    pass
        #else:
        #    self.location[1]=newY
        self.location[1]=newY
    def x(self): #x getter
        if type(self.location) is partial:
            return self.location()[0]
        val=self.location[0]
        
        return val
    def y(self): # Y getter
        if type(self.location) is partial:
            return self.location()[1]
        val= self.location[1]
        return val
    
    def distance(self,otherPoint):
        return sqrt()
        
    
    
class line(geometric_feature):
    def __init__(self,drawing,point1,point2):
        geometric_feature.__init__(self,drawing)
        self.point=[point1,point2]
        self.children+=self.point
    def slope(self):
        return (self.dy())/self.dx()
    def dydx(self):
        return self.slope()
    def dx(self):
        return self.point[1].x()-self.point[1].x()
    def dy(self):
        return self.point[1].y()-self.point[0].y()
   
    def get_intersection(self,otherLine): #Returns point(s) of intersection between this line and other line
        if type(otherLine) is not line:
            return TypeError
        A1y=self.point[0].y()
        B1y=otherLine.point[0].y()
        A1x=otherLine.point[0].x()
        B1x=otherLine.point[0].x()
        dAdx=self.slope()
        dBdx=otherLine.slope()
        
        x_int=-(B1y-A1y+A1x*dAdx-B1x*dBdx)/(dBdx-dAdx)
        
        y_int=Axy+dAdx(x_int-A1x)
        
        return array([x_int,y_int])
        

        
class line_segment(line):       
    def length(self):
        return 


    
class polygon(geometric_feature): #polygon, with points entered manually
    def __init__(self,drawing,points):
        geometric_feature.__init(self,drawing)
        self.sides=len(points)
       
class corner_rectangle(geometric_feature): 
    def __init__(self,drawing,corner1,corner2):
        pass
    
    

canvas=drawing("")
point1=point(canvas,[0,0])
point2=point(canvas,[1,1.5])
    
print(point1)
print(point2)
print("Defining dimension")

#dim1=canvas.add_dimension(vertical_distance(canvas, point1, point2, 3))

print(point1)
print(point2)

#dim1.distance=5
point1.setY(3)

print(point1)
print(point2)
   
point1.setX(5)     


print(point1)
print(point2)