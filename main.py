# main.py
from ui import T3
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt
import sys
from functools import partial
from PySide6.QtMultimedia import QSoundEffect
from PySide6.QtCore import QUrl
import os

class MainPage(T3.Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(MainPage, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.pushButton_close.clicked.connect(self.close)

        self.pushButton_close.setText("✖")
        self.pushButton_close.setStyleSheet("""
            QPushButton {
                font-size: 35px;
                color: red;
                background-color: transparent;
                border: none;
            }
        """)

        self.setStyleSheet("""
            QMainWindow {
                background: qlineargradient(
                    x1: 0, y1: 0,
                    x2: 1, y2: 1,
                    stop: 0 #ffe6f0,
                    stop: 1 #ffffff
                );
            }
        """)

        self.buttons = [
            self.pushButton_1, self.pushButton_2, self.pushButton_3,
            self.pushButton_4, self.pushButton_5, self.pushButton_6,
            self.pushButton_7, self.pushButton_8, self.pushButton_9
        ]

        for i, button in enumerate(self.buttons):
            button.clicked.connect(partial(self.markBox, i))
            button.setStyleSheet("""
                QPushButton {
                    background-color: transparent;
                    border: none;
                }
                QPushButton:disabled {
                    background-color: transparent;
                }
            """)

        self.disableAllButtons()
        self.flag = True

        self.pushButton_askPlayer.clicked.connect(self.showAskPlayer)
        self.pushButton_player1_X.clicked.connect(self.startPlayerX)
        self.pushButton_player2_O.clicked.connect(self.startPlayerO)
        self.pushButton_newMatch.clicked.connect(self.resetGame)

        self.initVisibility()
        self.label_info.show()

        # self.sounds = {
        #     "click": self.loadSound("sounds/click.wav"),
        #     "win": self.loadSound("sounds/win.wav"),
        #     "draw": self.loadSound("sounds/draw.wav"),
        # }

    # def loadSound(self, filename):
    #     effect = QSoundEffect()
    #     effect.setSource(QUrl.fromLocalFile(os.path.abspath(filename)))
    #     effect.setVolume(0.8)
    #     return effect
    
    def initVisibility(self):
        self.showGameBoard(True)
        self.setAskPlayerVisible(False)
        self.showWinner(False)

    def showGameBoard(self, visible):
        for btn in self.buttons:
            btn.setVisible(visible)
        self.VLine1.setVisible(visible)
        self.VLine2.setVisible(visible)
        self.HLine1.setVisible(visible)
        self.HLine2.setVisible(visible)

    def setAskPlayerVisible(self, visible):
        self.pushButton_player1_X.setVisible(visible)
        self.pushButton_player2_O.setVisible(visible)
        self.Cross.setVisible(visible)
        self.Zero.setVisible(visible)
        self.label.setVisible(visible)

    def showWinner(self, visible):
        self.label_edit.setVisible(visible)
        self.pushButton_newMatch.setVisible(visible)

    def showAskPlayer(self):
        self.label_info.show()
        self.pushButton_askPlayer.setDisabled(True)
        self.pushButton_askPlayer.hide()
        self.showGameBoard(False)
        self.showWinner(False)
        self.setAskPlayerVisible(True)

    def startPlayerX(self):
        self.flag = False
        self.resumeGameFromAsk()

    def startPlayerO(self):
        self.flag = True
        self.resumeGameFromAsk()

    def resumeGameFromAsk(self):
        self.setAskPlayerVisible(False)
        self.showGameBoard(True)
        self.label_info.hide()
        self.enableAllButtons()

    def markBox(self, index):
        # self.sounds["click"].play()
        icon = QIcon(":/crossAndZero/zero.png") if self.flag else QIcon(":/crossAndZero/cross.png")
        self.buttons[index].setIcon(icon)
        self.buttons[index].setDisabled(True)

        if self.winList():
            self.disableAllButtons()
            return

        if all(not button.isEnabled() for button in self.buttons):
            self.draw_match()
            return

        self.flag = not self.flag

    def winList(self):
        list_winner = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]

        for i in list_winner:
            if not self.buttons[i[0]].icon().isNull():
                icon1 = self.buttons[i[0]].icon()
                icon2 = self.buttons[i[1]].icon()
                icon3 = self.buttons[i[2]].icon()
                if icon1.pixmap(100, 100).toImage() == icon2.pixmap(100, 100).toImage() == icon3.pixmap(100, 100).toImage():
                    self.announceWinner()
                    return True
        return False

    def announceWinner(self):
        # self.sounds["win"].play()
        self.setStyleSheet("""
            QMainWindow {
                background: qlineargradient(
                    x1: 0, y1: 0,
                    x2: 1, y2: 1,
                    stop: 0 #ccffcc,
                    stop: 1 #006600
                );
            }
        """)
        winner_text = "🎉 Player X is the Winner 🎉" if not self.flag else "🎉 Player O is the Winner 🎉"
        self.label_edit.setText(winner_text)
        self.showGameBoard(False)
        self.setAskPlayerVisible(False)
        self.showWinner(True)

    def draw_match(self):
        # self.sounds["draw"].play()
        self.setStyleSheet("""
            QMainWindow {
                background: qlineargradient(
                    x1: 0, y1: 0,
                    x2: 1, y2: 1,
                    stop: 0 #fff7cc,
                    stop: 1 #ffd580
                );
            }
        """)
        self.label_edit.setText("It's a Draw ! Another Shot 😤 ?")
        self.label_edit.setStyleSheet("""
            QLabel {
                color: black;
                font: 25 11pt "URW Bookman";
                font-size: 40px;
            }
        """)
        self.showGameBoard(False)
        self.setAskPlayerVisible(False)
        self.showWinner(True)

    def disableAllButtons(self):
        for button in self.buttons:
            button.setDisabled(True)

    def enableAllButtons(self):
        for button in self.buttons:
            button.setEnabled(True)

    def resetGame(self):
        self.setStyleSheet("""
            QMainWindow {
                background: qlineargradient(
                    x1: 0, y1: 0,
                    x2: 1, y2: 1,
                    stop: 0 #ffe6f0,
                    stop: 1 #ffffff
                );
            }
        """)
        for button in self.buttons:
            button.setIcon(QIcon())
            button.setEnabled(True)
        self.showAskPlayer()

    def closeEvent(self, event):
        event.accept()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainPage()
    window.show()
    sys.exit(app.exec())