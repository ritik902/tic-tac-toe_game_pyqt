from ui import askPlayer
from PySide6.QtWidgets import QDialog
from PySide6.QtCore import Qt

class askPlayerPage(askPlayer.Ui_Dialog,QDialog):
    def __init__(self,main=None):
        super(askPlayerPage,self).__init__(parent=main)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setupUi(self)

        self.main=main

        self.closeApp.hide()
        self.closeApp.setText("✖")
        self.closeApp.setStyleSheet("""
            QPushButton {
                font-size: 35px;
                color: red;
                background-color: transparent;
                border: none;
            }
        """)
        
        self.pushButton_player1_X.clicked.connect(self.startPlayerX)
        self.pushButton_player2_O.clicked.connect(self.startPlayerO)

        self.closeApp.clicked.connect(self.close)

    def startPlayerX(self):
        if self.main:
            self.main.flag=False
        self.accept()

    def startPlayerO(self):
        if self.main:
            self.main.flag=True
        self.accept()

    def closeEvent(self, event):
        event.accept()
        self.close()
