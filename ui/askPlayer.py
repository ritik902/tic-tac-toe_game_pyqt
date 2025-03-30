# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'askPlayer.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QWidget)
import resource_rc
import resource_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        Dialog.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.pushButton_player1_X = QPushButton(Dialog)
        self.pushButton_player1_X.setObjectName(u"pushButton_player1_X")
        self.pushButton_player1_X.setGeometry(QRect(53, 160, 120, 27))
        self.pushButton_player1_X.setStyleSheet(u"QPushButton {\n"
"        background-color: #2c3e50;\n"
"        color: white;\n"
"        border: none;\n"
"        border-radius: 10px;\n"
"        font-size: 20px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: red;\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: red;\n"
"    }\n"
"    QPushButton:disabled {\n"
"        background-color: #7f8c8d;\n"
"        color: #bdc3c7;\n"
"    }")
        self.pushButton_player2_O = QPushButton(Dialog)
        self.pushButton_player2_O.setObjectName(u"pushButton_player2_O")
        self.pushButton_player2_O.setGeometry(QRect(246, 160, 120, 27))
        self.pushButton_player2_O.setStyleSheet(u"QPushButton {\n"
"        background-color: #2c3e50;\n"
"        color: white;\n"
"        border: none;\n"
"        border-radius: 10px;\n"
"        font-size: 20px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: red;\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: red;\n"
"    }\n"
"    QPushButton:disabled {\n"
"        background-color: #7f8c8d;\n"
"        color: #bdc3c7;\n"
"    }\n"
"")
        self.Cross = QLabel(Dialog)
        self.Cross.setObjectName(u"Cross")
        self.Cross.setGeometry(QRect(90, 100, 50, 50))
        self.Cross.setPixmap(QPixmap(u":/crossAndZero/cross.png"))
        self.Cross.setScaledContents(True)
        self.Zero = QLabel(Dialog)
        self.Zero.setObjectName(u"Zero")
        self.Zero.setGeometry(QRect(280, 100, 50, 50))
        self.Zero.setPixmap(QPixmap(u":/crossAndZero/zero.png"))
        self.Zero.setScaledContents(True)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(100, 230, 221, 21))
        self.label.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 25 11pt \"URW Bookman\";\n"
"color: rgb(0, 0, 0);\n"
"font-size: 20px;")
        self.closeApp = QPushButton(Dialog)
        self.closeApp.setObjectName(u"closeApp")
        self.closeApp.setGeometry(QRect(354, 0, 50, 40))
        self.closeApp.setStyleSheet(u"border:None;\n"
"background-color: rgb(255, 255, 255);")
        self.closeApp.setIconSize(QSize(40, 40))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.pushButton_player1_X.setText(QCoreApplication.translate("Dialog", u"Player 1 (X)", None))
        self.pushButton_player2_O.setText(QCoreApplication.translate("Dialog", u"Player 2 (O)", None))
        self.Cross.setText("")
        self.Zero.setText("")
        self.label.setText(QCoreApplication.translate("Dialog", u"Default is Player 2 (O)", None))
        self.closeApp.setText("")
    # retranslateUi

