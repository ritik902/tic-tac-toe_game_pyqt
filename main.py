from ui import T3
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt
import sys
import winner_display,askPlayer
from functools import partial

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

        self.buttons=[
            self.pushButton_1, self.pushButton_2, self.pushButton_3,
            self.pushButton_4, self.pushButton_5, self.pushButton_6,
            self.pushButton_7, self.pushButton_8, self.pushButton_9
        ]

        self.disableAllButtons()

        self.flag=True  # False = Player 1 (X), True = Player 2 (O)

        self.pushButton_askPlayer.clicked.connect(self.showAskPlayer)


        # ======================================= from CHAT GPT =======================================
        # Connect buttons to the common function

        # for i, button in enumerate(self.buttons):
        #     button.clicked.connect(lambda _, idx=i: self.markBox(idx))

        # Connect buttons to markBox using partial
        
        for i, button in enumerate(self.buttons):
            button.clicked.connect(partial(self.markBox, i))
        # =============================================================================================

    def showAskPlayer(self):
        self.label_info.show()
        self.window_ask=askPlayer.askPlayerPage(main=self)
        r=self.window_ask.exec()
        self.enableAllButtons()
        self.label_info.hide()
        self.pushButton_askPlayer.setDisabled(True)

    def markBox(self, index):
        # if not self.buttons[index[0]].icon().isNull():
        #     return

        if self.flag:
            icon = QIcon(":/crossAndZero/zero.png")  # Player 2 (O)
        else:
            icon = QIcon(":/crossAndZero/cross.png")  # Player 1 (X)

        self.buttons[index].setIcon(icon)
        self.buttons[index].setDisabled(True)

        if self.winList():
            self.disableAllButtons()
            # print("winner announced")
            return
        
        '''
        # one liner but less readable from ChatGPT

        if all(button.isEnabled() == False for button in self.buttons):  
                self.announceDraw()
                return
        '''

        all_selected_buttons=True
        for button in self.buttons:
            if button.isEnabled():
                all_selected_buttons=False
                break
        if all_selected_buttons:
            self.draw_match()
            return

        self.flag = not self.flag

    def winList(self):
        # print("hello")
        list_winner=[
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]              # Diagonals
            ]

        for i in list_winner:
            # print(i)
            if not self.buttons[i[0]].icon().isNull():
                icon1 = self.buttons[i[0]].icon()
                # print(icon1)
                icon2 = self.buttons[i[1]].icon()
                icon3 = self.buttons[i[2]].icon()

                pixmap1 = icon1.pixmap(100, 100)
                # print(pixmap1)
                pixmap2 = icon2.pixmap(100, 100)
                pixmap3 = icon3.pixmap(100, 100)

                if pixmap1.toImage() == pixmap2.toImage() == pixmap3.toImage():
                    print(f"Winner detected at positions {i}!")
                    self.announceWinner(icon1)
                    return True                    

        # print("No winner found yet.")
        return False
    
    def announceWinner(self,winner_icon):
        # print(winner_icon)
        if not self.flag:
            self.winner = winner_display.WinnerPage(main=self)
            self.winner.show()
        else:
            self.winner = winner_display.WinnerPage(main=self)
            self.winner.label_edit.setText("Player O Wins")
            self.winner.show()

    def draw_match(self):
            self.draw = winner_display.WinnerPage(main=self)
            self.draw.label_edit.setText("Match Draw")
            self.draw.show()

    def disableAllButtons(self):
        for button in self.buttons:
            button.setDisabled(True)

    def enableAllButtons(self):
        for button in self.buttons:
            button.setEnabled(True)

    def resetGame(self):
        print("reset Game")
        for button in self.buttons:
            button.setIcon(QIcon())
        self.showAskPlayer()

    def closeEvent(self, event):
        event.accept()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainPage()
    window.show()
    sys.exit(app.exec())