# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'lesson_page.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1281, 804)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(0, 43, 91);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.left_menu_frame = QFrame(self.frame)
        self.left_menu_frame.setObjectName(u"left_menu_frame")
        self.left_menu_frame.setMinimumSize(QSize(275, 780))
        self.left_menu_frame.setMaximumSize(QSize(275, 16777215))
        self.left_menu_frame.setStyleSheet(u"background-color: rgb(36, 105, 127)")
        self.left_menu_frame.setFrameShape(QFrame.StyledPanel)
        self.left_menu_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.left_menu_frame)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.left_menu_frame)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setMinimumSize(QSize(275, 70))
        self.frame_4.setMaximumSize(QSize(275, 70))
        self.frame_4.setStyleSheet(u"background-color: rgb(137, 218, 199);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.left_menu_frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(275, 530))
        self.frame_5.setMaximumSize(QSize(275, 16777215))
        self.frame_5.setStyleSheet(u"background-color: rgb(137, 218, 199);")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.left_menu_frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(275, 100))
        self.frame_6.setMaximumSize(QSize(275, 100))
        self.frame_6.setStyleSheet(u"background-color: rgb(143, 227, 207)")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_2 = QSpacerItem(53, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.label = QLabel(self.frame_6)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(127, 90))
        self.label.setMaximumSize(QSize(140, 90))
        self.label.setStyleSheet(u"")
        self.label.setPixmap(QPixmap(u"../Images/bottom_banner.png"))

        self.horizontalLayout_3.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(51, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.verticalLayout.addWidget(self.frame_6)


        self.horizontalLayout_2.addWidget(self.left_menu_frame)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(950, 780))
        self.frame_3.setStyleSheet(u"background-color: rgb(36, 105, 127);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_7 = QFrame(self.frame_3)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(950, 95))
        self.frame_7.setMaximumSize(QSize(16777215, 95))
        self.frame_7.setStyleSheet(u"")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton = QPushButton(self.frame_7)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(90, 80))
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"	background-color: #2B4865 #256D85;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover:!pressed\n"
"{\n"
"	background-color:  #256D85;\n"
"	border-top-left-radius: 15px;\n"
"	border-bottom-left-radius: 15px;\n"
"}")
        icon = QIcon()
        icon.addFile(u"../Images/backward.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(150, 150))

        self.horizontalLayout_4.addWidget(self.pushButton)

        self.label_2 = QLabel(self.frame_7)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(660, 0))
        self.label_2.setMaximumSize(QSize(16777215, 70))
        self.label_2.setStyleSheet(u"background-color: rgb(137, 218, 199);\n"
"border-radius: 15px;")

        self.horizontalLayout_4.addWidget(self.label_2)

        self.pushButton_2 = QPushButton(self.frame_7)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMaximumSize(QSize(90, 80))
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"	background-color: #2B4865 #256D85;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover:!pressed\n"
"{\n"
"	background-color:  #256D85;\n"
"	border-top-right-radius: 15px;\n"
"	border-bottom-right-radius: 15px;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"../Images/forward.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QSize(150, 150))

        self.horizontalLayout_4.addWidget(self.pushButton_2)


        self.verticalLayout_2.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.frame_3)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(950, 660))
        self.frame_8.setStyleSheet(u"border: 2px solid rgb(0, 43, 91);")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.frame_8)


        self.horizontalLayout_2.addWidget(self.frame_3)


        self.horizontalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.pushButton.setText("")
        self.label_2.setText("")
        self.pushButton_2.setText("")
    # retranslateUi

