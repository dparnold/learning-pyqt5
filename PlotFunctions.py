#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial 

This program creates a statusbar.

author: Jan Bodnar
website: zetcode.com 
last edited: January 2015
"""

import sys, os
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import (QMainWindow, QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout, QApplication, QPushButton, 
    QHBoxLayout, QVBoxLayout, QApplication, qApp, QAction, QToolTip)

from numpy import arange, sin, pi
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure


class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
        
    def initUI(self):  
        plotFunctionAction = QAction(QIcon('plotIcon.png'), 'Plot f(x)', self)
        plotFunctionAction.setShortcut('Ctrl+P')
        plotFunctionAction.setStatusTip('Plot a function f(x)')
        plotFunctionAction.triggered.connect(self.plotFunctionButtonClicked)     
        
        PlotDataAction = QAction(QIcon('sound.png'), '&Exit', self)        
        PlotDataAction.setShortcut('Ctrl+Q')
        PlotDataAction.setStatusTip('Exit application')
        PlotDataAction.triggered.connect(self.plotDataButtonClicked)  
             
        """"Set the Toolbar """
        self.toolbar = self.addToolBar('Main toolbar')
        self.toolbar.addAction(plotFunctionAction)
        self.toolbar.addAction(PlotDataAction)
        self.toolbar.setIconSize(QSize(60, 40))
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')
        fileMenu.addAction(plotFunctionAction)
        settingsMenu = menubar.addMenu('Settings')
        
        self.statusBar().showMessage('Ready')
        
        """"Set the central Widget """
        self.plotFunctionWidget = PlotFunctionWidget()
        self.setCentralWidget(self.plotFunctionWidget)
        
        self.showMaximized()
        self.setWindowTitle('Python Qt5 Plot')    
        self.show()
    #Key Events
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()   
    def plotFunctionButtonClicked(self):
        self.plotFunctionWidget = PlotFunctionWidget()
        self.setCentralWidget(self.plotFunctionWidget)
    def plotDataButtonClicked(self):
        self.plotDataWidget = PlotDataWidget()
        self.setCentralWidget(self.plotDataWidget)
      
class PlotFunctionWidget(QWidget):
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):
        self.graphWidget = QWidget(self)
        self.graph = PlotFunctionCanvas(self.graphWidget)
        
        self.textEdit = QTextEdit()

        expression = QLabel('f(x)=')
        self.expressionEdit = QLineEdit()
        self.expressionEdit.setMinimumWidth(200);
                
        startvalue = QLabel('from x=:')
        self.startvalueEdit = QLineEdit()
        self.startvalueEdit.setMinimumWidth(200);

        endvalue = QLabel('to x=:')
        self.endvalueEdit = QLineEdit()
        self.endvalueEdit.setMinimumWidth(200);


        plotButton = QPushButton("plot")
        plotButton.clicked.connect(self.plotButtonClicked) 


        hbox = QHBoxLayout()
        grid_menu = QGridLayout()
        grid_menu.addWidget(expression, 0, 0)
        grid_menu.addWidget(self.expressionEdit, 0, 1)
        grid_menu.addWidget(startvalue, 1, 0)
        grid_menu.addWidget(self.startvalueEdit, 1, 1)
        grid_menu.addWidget(endvalue, 2, 0)
        grid_menu.addWidget(self.endvalueEdit, 2, 1)
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
        
        grid.addWidget(self.graph, 0, 1)
        
        
        self.setLayout(grid) 
        
        self.showMaximized()
        self.setWindowTitle('Python Qt5 Plot')    
        self.show()
        
    def plotButtonClicked(self):
        self.graph.update_figure(str(self.expressionEdit.text()),float(self.startvalueEdit.text()),float(self.endvalueEdit.text()))    

class PlotDataWidget(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
    def initUI(self):  
        
        QToolTip.setFont(QFont('SansSerif', 10))
        
        self.setToolTip('This is a <b>QWidget</b> widget')
        
        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)     
        self.showMaximized()
        self.setWindowTitle('Python Qt5 Plot')    
        self.show()
class MplCanvas(FigureCanvasQTAgg):
    """Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.)."""
    def __init__(self, parent=None):
        fig = Figure()
        self.axes = fig.add_subplot(111)
        self.compute_initial_figure()
        FigureCanvasQTAgg.__init__(self, fig)
        self.setParent(parent)
        FigureCanvasQTAgg.setSizePolicy(self, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        FigureCanvasQTAgg.updateGeometry(self)
    def compute_initial_figure(self):
        pass
class PlotFunctionCanvas(MplCanvas):
    def compute_initial_figure(self):
        t = arange(0.0, 3.0, 0.01)
        s = sin(2*pi*t)
        self.axes.plot(t,s)   
        self.axes.grid()
    def update_figure(self, expression, beginning, end):
        x = arange(beginning,end,(end-beginning)/1000.0)
        exec('y = ' +str(expression),locals(),globals())
        self.axes.clear()
        self.axes.plot(x,y,'r')
        self.axes.grid()  
        self.draw()          
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())