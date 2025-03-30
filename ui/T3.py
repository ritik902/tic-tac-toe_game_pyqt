# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'T3.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QWidget)
import resource_rc
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1133, 813)
        MainWindow.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.VLine1 = QFrame(self.centralwidget)
        self.VLine1.setObjectName(u"VLine1")
        self.VLine1.setGeometry(QRect(500, 260, 5, 250))
        self.VLine1.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.VLine1.setFrameShape(QFrame.Shape.VLine)
        self.VLine1.setFrameShadow(QFrame.Shadow.Sunken)
        self.HLine1 = QFrame(self.centralwidget)
        self.HLine1.setObjectName(u"HLine1")
        self.HLine1.setGeometry(QRect(430, 330, 250, 5))
        self.HLine1.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.HLine1.setFrameShape(QFrame.Shape.HLine)
        self.HLine1.setFrameShadow(QFrame.Shadow.Sunken)
        self.VLine2 = QFrame(self.centralwidget)
        self.VLine2.setObjectName(u"VLine2")
        self.VLine2.setGeometry(QRect(600, 260, 5, 250))
        self.VLine2.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.VLine2.setFrameShape(QFrame.Shape.VLine)
        self.VLine2.setFrameShadow(QFrame.Shadow.Sunken)
        self.HLine2 = QFrame(self.centralwidget)
        self.HLine2.setObjectName(u"HLine2")
        self.HLine2.setGeometry(QRect(430, 410, 250, 5))
        self.HLine2.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.HLine2.setFrameShape(QFrame.Shape.HLine)
        self.HLine2.setFrameShadow(QFrame.Shadow.Sunken)
        self.pushButton_1 = QPushButton(self.centralwidget)
        self.pushButton_1.setObjectName(u"pushButton_1")
        self.pushButton_1.setGeometry(QRect(428, 257, 70, 70))
        self.pushButton_1.setStyleSheet(u"border:None;")
        self.pushButton_1.setIconSize(QSize(70, 70))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(520, 256, 70, 70))
        self.pushButton_2.setStyleSheet(u"border:None;")
        self.pushButton_2.setIconSize(QSize(70, 70))
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(611, 255, 70, 70))
        self.pushButton_3.setStyleSheet(u"border:None;")
        self.pushButton_3.setIconSize(QSize(70, 70))
        self.pushButton_6 = QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(610, 338, 70, 70))
        self.pushButton_6.setStyleSheet(u"border:None;")
        self.pushButton_6.setIconSize(QSize(70, 70))
        self.pushButton_9 = QPushButton(self.centralwidget)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(610, 425, 70, 70))
        self.pushButton_9.setStyleSheet(u"border:None;")
        self.pushButton_9.setIconSize(QSize(70, 70))
        self.pushButton_8 = QPushButton(self.centralwidget)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(516, 421, 70, 70))
        self.pushButton_8.setStyleSheet(u"border:None;")
        self.pushButton_8.setIconSize(QSize(70, 70))
        self.pushButton_7 = QPushButton(self.centralwidget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(423, 420, 70, 70))
        self.pushButton_7.setStyleSheet(u"border:None;")
        self.pushButton_7.setIconSize(QSize(70, 70))
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(425, 338, 70, 70))
        self.pushButton_4.setStyleSheet(u"border:None;")
        self.pushButton_4.setIconSize(QSize(70, 70))
        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(517, 338, 70, 70))
        self.pushButton_5.setStyleSheet(u"border:None;")
        self.pushButton_5.setIconSize(QSize(70, 70))
        self.pushButton_askPlayer = QPushButton(self.centralwidget)
        self.pushButton_askPlayer.setObjectName(u"pushButton_askPlayer")
        self.pushButton_askPlayer.setGeometry(QRect(480, 160, 150, 27))
        self.pushButton_askPlayer.setStyleSheet(u"QPushButton {\n"
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
        self.label_info = QLabel(self.centralwidget)
        self.label_info.setObjectName(u"label_info")
        self.label_info.setGeometry(QRect(432, 590, 280, 40))
        self.label_info.setStyleSheet(u"QLabel {\n"
"        font-size: 22px;\n"
"        font-weight: 600;\n"
"        color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #ff512f, stop:1 #dd2476);\n"
"    }")
        self.pushButton_close = QPushButton(self.centralwidget)
        self.pushButton_close.setObjectName(u"pushButton_close")
        self.pushButton_close.setGeometry(QRect(1080, 5, 50, 40))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_1.setText("")
        self.pushButton_2.setText("")
        self.pushButton_3.setText("")
        self.pushButton_6.setText("")
        self.pushButton_9.setText("")
        self.pushButton_8.setText("")
        self.pushButton_7.setText("")
        self.pushButton_4.setText("")
        self.pushButton_5.setText("")
        self.pushButton_askPlayer.setText(QCoreApplication.translate("MainWindow", u"select Player", None))
        self.label_info.setText(QCoreApplication.translate("MainWindow", u"Please Select Player First", None))
        self.pushButton_close.setText("")
    # retranslateUi

