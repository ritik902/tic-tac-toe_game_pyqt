from ui import winner_display
from PySide6.QtWidgets import QDialog
from PySide6.QtCore import Qt

class WinnerPage(winner_display.Ui_Dialog,QDialog):
    def __init__(self,main=None):
        super(WinnerPage,self).__init__(parent=main)
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

        self.pushButton_newMatch.clicked.connect(self.clearPreviousMatch)
        self.closeApp.clicked.connect(self.close)


    def clearPreviousMatch(self):
        self.close()
        if self.main:
            self.main.resetGame()
    
    def closeEvent(self, event):
        event.accept()
        self.close()