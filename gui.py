# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 10:38:57 2023

@author: Nicholas
"""
import sys
from PyQt6 import QtWidgets,uic


class gui:
    #Top bar buttons: New, file, save, add force, add stress, add constraint, generate mesh
    #Side bar settings: Object thickness, mesh size, elastic modulus, poisson's ratio
    
    #def __init__(self):
        #self.root=Tk("2D FEA")
        #self.frame=ttk.Frame(self.root)
        #self.root.mainloop()
        
    def __init__(self):
        app=QtWidgets.QApplication(sys.argv)
        window=uic.load_ui.loadUi("Qt Gui Design/mainwindow.ui")
        window.show()
        app.exec()
        
        
        
