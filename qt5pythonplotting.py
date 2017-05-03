#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import os
import random
import matplotlib
matplotlib.use('Qt5Agg')

from PyQt5.QtCore import Qt

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import (QMainWindow, QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout, QApplication, QPushButton, 
	QHBoxLayout, QVBoxLayout, QApplication)

from numpy import arange, sin, pi
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure


class MyMplCanvas(FigureCanvasQTAgg):
	"""Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.)."""
	def __init__(self, parent=None):
		fig = Figure()
		self.axes = fig.add_subplot(111)
		self.axes.hold(False) # Clear the Axis everytime plot() is called
		self.compute_initial_figure()
		FigureCanvasQTAgg.__init__(self, fig)
		self.setParent(parent)
		FigureCanvasQTAgg.setSizePolicy(self, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
		FigureCanvasQTAgg.updateGeometry(self)
	def compute_initial_figure(self):
		pass

"""Simple canvas with a sine plot."""	
class MyStaticMplCanvas(MyMplCanvas):
	def compute_initial_figure(self):
		t = arange(0.0, 3.0, 0.01)
		s = sin(2*pi*t)
		self.axes.plot(t,s)   
		self.axes.grid()
	def update_figure(self, expression, beginning, end):
		x = arange(beginning,end,(end-beginning)/1000.0)
		exec('y = ' +str(expression),locals(),globals())
		self.axes.plot(x,y,'r')
		self.axes.grid()  
		self.draw()  

class Example(QWidget):
	
	def __init__(self):
		super().__init__()
		
		self.initUI()
		
		
	def initUI(self):
		

		expression = QLabel('f(x)=')
		self.expressionEdit = QLineEdit()
		self.expressionEdit.setMinimumWidth(200);
				
		startvalue = QLabel('from x=:')
		self.startvalueEdit = QLineEdit()
		self.startvalueEdit.setMinimumWidth(200);

		endvalue = QLabel('to x=:')
		self.endvalueEdit = QLineEdit()
		self.endvalueEdit.setMinimumWidth(200);
		
		self.main_widget = QWidget(self)
		self.graph = MyStaticMplCanvas(self.main_widget)


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
		#self.statusBar()
        
		
		self.setLayout(grid) 
		
		self.showMaximized()
		self.setWindowTitle('Python Qt5 Plot')	
		self.show()
		
	def plotButtonClicked(self):
		self.graph.update_figure(str(self.expressionEdit.text()),float(self.startvalueEdit.text()),float(self.endvalueEdit.text()))	
	#Key Events
	def keyPressEvent(self, e):
		if e.key() == Qt.Key_Space:
			self.plotButtonClicked()
		elif e.key() == Qt.Key_Escape:
			self.close()
if __name__ == '__main__':
	
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())
