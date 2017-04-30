#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import os
import random
import matplotlib
matplotlib.use('Qt5Agg')

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout, QApplication, QPushButton, 
    QHBoxLayout, QVBoxLayout)

from numpy import arange, sin, pi
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class MyMplCanvas(FigureCanvas):
    """Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.)."""

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        # We want the axes cleared every time plot() is called
        self.axes.hold(False)

        self.compute_initial_figure()

        #
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QtWidgets.QSizePolicy.Expanding,
                                   QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def compute_initial_figure(self):
        pass

"""Simple canvas with a sine plot."""
class MyStaticMplCanvas(MyMplCanvas):
    def compute_initial_figure(self):
        t = arange(0.0, 3.0, 0.01)
        s = sin(2*pi*t)
        self.axes.plot(t,s)     

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):
        

        expression = QLabel('f(x)=')
        expressionEdit = QLineEdit()
        expressionEdit.setMinimumWidth(200);
                
        startvalue = QLabel('from x=:')
        startvalueEdit = QLineEdit()
        startvalueEdit.setMinimumWidth(200);

        endvalue = QLabel('to x=:')
        endvalueEdit = QLineEdit()
        endvalueEdit.setMinimumWidth(200);
        
        self.main_widget = QtWidgets.QWidget(self)
        graph = MyStaticMplCanvas(self.main_widget)


        plotButton = QPushButton("plot")

        hbox = QHBoxLayout()
        grid_menu = QGridLayout()
        grid_menu.addWidget(expression, 0, 0)
        grid_menu.addWidget(expressionEdit, 0, 1)
        grid_menu.addWidget(startvalue, 1, 0)
        grid_menu.addWidget(startvalueEdit, 1, 1)
        grid_menu.addWidget(endvalue, 2, 0)
        grid_menu.addWidget(endvalueEdit, 2, 1)
        grid_menu.addWidget(plotButton, 3,1)
                
        hbox.addLayout(grid_menu)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addStretch(1)
        
        
        grid = QGridLayout()
        grid.setColumnStretch(0, 1)
        grid.setColumnStretch(1, 7)
        grid.setSpacing(5)
        
        grid.addLayout(vbox, 0, 0)
        
        grid.addWidget(graph, 0, 1)
        
        self.setLayout(grid) 
        
        self.showMaximized()
        self.setWindowTitle('Python Qt5 Plot')    
        self.show()
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
