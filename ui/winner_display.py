# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'winner_display.ui'
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        Dialog.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_edit = QLabel(Dialog)
        self.label_edit.setObjectName(u"label_edit")
        self.label_edit.setGeometry(QRect(140, 100, 150, 19))
        self.label_edit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 25 11pt \"URW Bookman\";\n"
"font-size: 20px;\n"
"color: rgb(38, 162, 105);")
        self.pushButton_newMatch = QPushButton(Dialog)
        self.pushButton_newMatch.setObjectName(u"pushButton_newMatch")
        self.pushButton_newMatch.setGeometry(QRect(144, 150, 130, 27))
        self.pushButton_newMatch.setStyleSheet(u"QPushButton {\n"
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
        self.closeApp = QPushButton(Dialog)
        self.closeApp.setObjectName(u"closeApp")
        self.closeApp.setGeometry(QRect(362, 3, 40, 30))
        self.closeApp.setStyleSheet(u"border:None;\n"
"background-color: rgb(255, 255, 255);")
        self.closeApp.setIconSize(QSize(40, 40))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_edit.setText(QCoreApplication.translate("Dialog", u"Player X Wins", None))
        self.pushButton_newMatch.setText(QCoreApplication.translate("Dialog", u"New Match?", None))
        self.closeApp.setText("")
    # retranslateUi

