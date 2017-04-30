#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial 

In this example, we create a simple
window in PyQt5.

author: Jan Bodnar
website: zetcode.com 
last edited: January 2015
"""
import sys
from PyQt5.QtWidgets import (QWidget, QToolTip, QPushButton, QApplication, QMessageBox, QDesktopWidget)
from PyQt5.QtGui import QIcon # For the icon
from PyQt5.QtGui import QFont # For the tooltip font
from PyQt5.QtCore import QCoreApplication # For quit button

class Example(QWidget): #The Example class inherits from the QWidget class.
    
    def __init__(self):
        super().__init__()  #The __init__() method is a constructor method in Python language.
        
        self.initUI()
        
        
    def initUI(self):
        #Create a tooltip
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidget</b> widget')
        
        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)       
        
        qbtn = QPushButton('Quit', self) #The first parameter of the constructor is the label of the button. The second parameter is the parent widget.
        qbtn.clicked.connect(QCoreApplication.instance().quit) #The event processing system in PyQt5 is built with the signal & slot mechanism. If we click on the button, the signal clicked is emitted. The slot can be a Qt slot or any Python callable. The QCoreApplication contains the main event loop; it processes and dispatches all events. The instance() method gives us its current instance. Note that QCoreApplication is created with the QApplication. The clicked signal is connected to the quit() method which terminates the application. The communication is done between two objects: the sender and the receiver. The sender is the push button, the receiver is the application object.
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(200, 50)  
        
        self.resize(500, 500)
        self.center()

        self.setWindowTitle('Tooltips')    
        self.show()
        
    def center(self):
        
        qr = self.frameGeometry()       # We get a rectangle specifying the geometry of the main window.
        cp = QDesktopWidget().availableGeometry().center() #We figure out the screen resolution of our monitor. And from this resolution, we get the center point.
        qr.moveCenter(cp) #Our rectangle has already its width and height. Now we set the center of the rectangle to the center of the screen. The rectangle's size is unchanged.
        self.move(qr.topLeft())    #We move the top-left point of the application window to the top-left point of the qr rectangle, thus centering the window on our screen.
        
        # Change the closeEvent Function to implement a QMessageBox
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QMessageBox.Yes | QMessageBox.No , QMessageBox.Yes)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()             
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example() 
    sys.exit(app.exec_()) #The exec_() method has an underscore. It is because the exec is a Python keyword. And thus, exec_() was used instead.