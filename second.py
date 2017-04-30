
import sys
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QApplication, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtMultimedia import QSound

class Example(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
    def playSound(self):
        QSound.play('alert.wav')
    
    def initUI(self):               
        
        textEdit = QTextEdit()
        self.setCentralWidget(textEdit)

        exitAction = QAction(QIcon('icon.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)
        
        soundAction = QAction(QIcon('sound.png'),'Play Sound', self)
        soundAction.triggered.connect(self.playSound)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)

        
        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exitAction)
        toolbar.addAction(soundAction)
        
        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Main window')    
        self.show()
    
    def closeEvent(self, event):
        self.playSound()
        reply = QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QMessageBox.Yes | QMessageBox.No , QMessageBox.Yes)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()      
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())