# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 20:16:05 2023

@author: Nicholas
"""
from tkinter import *
from tkinter import ttk
import ezdxf

class drawing:
    class __init__(self,fileDir):
        
        pass

class mesh:
    class __init__(self,drawing):
        self.drawing=drawing
        
class mesh_node:
    class __init__(self,corners=[[0,0],[1,0],[0,1],[1,1]],parent_mesh):
        self.parent=parent_mesh
        
        
class gui:
    #Top bar buttons: New, file, save, add force, add stress, add constraint, generate mesh
    #Side bar settings: Object thickness, mesh size, elastic modulus, poisson's ratio
    def __init__(self):
        self.root=Tk("2D FEA")
        self.frame=ttk.Frame(self.root)
        self.root.mainloop()
        
        
class simulation:
    def __init__(self):
        self.drawing
        self.mesh
        
window=gui()