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


class MyStaticMplCanvas(MyMplCanvas):
    """Simple canvas with a sine plot."""

    def compute_initial_figure(self):
        t = arange(0.0, 3.0, 0.01)
        s = sin(2*pi*t)
        self.axes.plot(t, s)


class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):
        

        
        self.main_widget = QtWidgets.QWidget(self)
        graph = MyStaticMplCanvas(self.main_widget)


        hbox0 = QHBoxLayout()
        vbox_menu = QVBoxLayout()
        vbox_graph = QVBoxLayout()
        
        hbox0.addLayout(vbox_menu)
        hbox0.addLayout(vbox_graph)

        
        #The menu
        
        expression = QLabel('Expression: f(x)=')
        expressionEdit = QLineEdit()
        expressionEdit.setMaximumWidth(200);
                
        startvalue = QLabel('Start value:')
        startvalueEdit = QLineEdit()
        startvalueEdit.setMaximumWidth(200);

        endvalue = QLabel('End value:')
        endvalueEdit = QLineEdit()
        endvalueEdit.setMaximumWidth(200);
        
        hbox_menu_1 = QHBoxLayout()
        vbox_menu.addLayout(hbox_menu_1)
        hbox_menu_1.addWidget(expression)
        hbox_menu_1.addWidget(expressionEdit)
        hbox_menu_1.addStretch(0)
        vbox_menu.addStretch(1)
        

        
        
        # Where the graph is located
        vbox_graph.addWidget(graph)

        
        self.setLayout(hbox0)    
        
        
        self.showMaximized()
        self.setWindowTitle('Python Qt5 Plot')    
        self.show()
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
