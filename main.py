# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 20:16:05 2023

@author: Nicholas
"""
from tkinter import *
from tkinter import ttk
from gui import *
import ezdxf





class mesh:
    def __init__(self,drawing):
        self.drawing=drawing
        
class mesh_node:
    def __init__(self,parent_mesh,corners=[[0,0],[1,0],[0,1],[1,1]],):
        self.parent=parent_mesh
        self.neighbors=[]
        #self.
        

        
        
class simulation:
    def __init__(self):
        self.drawing
        self.mesh
        
window=gui()