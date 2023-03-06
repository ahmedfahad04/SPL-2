# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sound_recorder.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QWidget)

class Ui_audioRecorderWidget(object):
    def setupUi(self, audioRecorderWidget):
        if not audioRecorderWidget.objectName():
            audioRecorderWidget.setObjectName(u"audioRecorderWidget")
        audioRecorderWidget.resize(479, 566)
        self.gridLayout = QGridLayout(audioRecorderWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.audioRecorderFrame = QFrame(audioRecorderWidget)
        self.audioRecorderFrame.setObjectName(u"audioRecorderFrame")
        self.audioRecorderFrame.setStyleSheet(u"background-color: rgb(142, 226, 205)")
        self.audioRecorderFrame.setFrameShape(QFrame.StyledPanel)
        self.audioRecorderFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.audioRecorderFrame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 0, 4, 1, 1)

        self.horizontalSpacer = QSpacerItem(84, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 1, 0, 1, 2)

        self.startButton = QPushButton(self.audioRecorderFrame)
        self.startButton.setObjectName(u"startButton")
        self.startButton.setMinimumSize(QSize(100, 100))
        self.startButton.setMaximumSize(QSize(100, 100))
        self.startButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.startButton.setStyleSheet(u"QPushButton {\n"
"	border-radius: 50px;\n"
"	border: 3px solid rgb(206, 95, 95)\n"
"}\n"
"\n"
"QPushButton:hover:!pressed\n"
"{\n"
"	background-color:  rgb(255, 131, 139);\n"
"	border-radius: 50px;\n"
"}")
        icon = QIcon()
        icon.addFile(u"../Images/record_before_start_2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.startButton.setIcon(icon)
        self.startButton.setIconSize(QSize(200, 200))

        self.gridLayout_2.addWidget(self.startButton, 1, 4, 1, 1)

        self.stopButton = QPushButton(self.audioRecorderFrame)
        self.stopButton.setObjectName(u"stopButton")
        self.stopButton.setEnabled(False)
        self.stopButton.setMinimumSize(QSize(50, 40))
        self.stopButton.setMaximumSize(QSize(50, 40))
        self.stopButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.stopButton.setStyleSheet(u"border: none;")
        icon1 = QIcon()
        icon1.addFile(u"../Images/record_stop.png", QSize(), QIcon.Normal, QIcon.Off)
        self.stopButton.setIcon(icon1)
        self.stopButton.setIconSize(QSize(40, 100))

        self.gridLayout_2.addWidget(self.stopButton, 1, 5, 1, 2)

        self.horizontalSpacer_2 = QSpacerItem(75, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 1, 7, 1, 2)

        self.verticalSpacer_2 = QSpacerItem(20, 68, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 2, 4, 1, 1)

        self.recordingTime = QLabel(self.audioRecorderFrame)
        self.recordingTime.setObjectName(u"recordingTime")
        font = QFont()
        font.setPointSize(11)
        self.recordingTime.setFont(font)
        self.recordingTime.setStyleSheet(u"border: 2px solid rgb(0, 43, 91) ;\n"
"border-radius: 15px;\n"
"background-color: rgb(231, 231, 231);")
        self.recordingTime.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.recordingTime, 3, 2, 1, 5)

        self.verticalSpacer_3 = QSpacerItem(20, 68, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_3, 4, 4, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(46, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 5, 0, 1, 1)

        self.fileName = QLineEdit(self.audioRecorderFrame)
        self.fileName.setObjectName(u"fileName")
        self.fileName.setMinimumSize(QSize(330, 50))
        self.fileName.setMaximumSize(QSize(330, 50))
        font1 = QFont()
        font1.setPointSize(12)
        self.fileName.setFont(font1)
        self.fileName.setStyleSheet(u"border: 2px solid rgb(0, 43, 91) ;\n"
"border-radius: 15px;\n"
"background-color: rgb(231, 231, 231);")
        self.fileName.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.fileName, 5, 1, 1, 7)

        self.horizontalSpacer_4 = QSpacerItem(37, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_4, 5, 8, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 21, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_4, 6, 4, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(123, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_5, 7, 0, 1, 3)

        self.saveButton = QPushButton(self.audioRecorderFrame)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setMinimumSize(QSize(0, 40))
        self.saveButton.setMaximumSize(QSize(16777215, 40))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(False)
        self.saveButton.setFont(font2)
        self.saveButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.saveButton.setStyleSheet(u"QPushButton {\n"
"border: 2px solid rgb(0, 43, 91) ;\n"
"border-radius: 15px;\n"
"background-color: rgb(36, 105, 127);\n"
"color: rgb(137, 218, 199)\n"
"}\n"
"\n"
"QPushButton:hover:!pressed {\n"
"background-color: rgb(25, 76, 91);\n"
"}")

        self.gridLayout_2.addWidget(self.saveButton, 7, 3, 1, 3)

        self.horizontalSpacer_6 = QSpacerItem(114, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_6, 7, 6, 1, 3)

        self.verticalSpacer_5 = QSpacerItem(20, 28, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_5, 8, 4, 1, 1)

        self.soundingButton = QPushButton(self.audioRecorderFrame)
        self.soundingButton.setObjectName(u"soundingButton")
        self.soundingButton.setEnabled(False)
        self.soundingButton.setMinimumSize(QSize(50, 40))
        self.soundingButton.setMaximumSize(QSize(50, 40))
        self.soundingButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.soundingButton.setStyleSheet(u"QPushButton{\n"
"border: none;\n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u"../Images/record_listen.png", QSize(), QIcon.Normal, QIcon.Off)
        self.soundingButton.setIcon(icon2)
        self.soundingButton.setIconSize(QSize(40, 100))

        self.gridLayout_2.addWidget(self.soundingButton, 1, 2, 1, 2)


        self.gridLayout.addWidget(self.audioRecorderFrame, 1, 0, 1, 1)


        self.retranslateUi(audioRecorderWidget)

        QMetaObject.connectSlotsByName(audioRecorderWidget)
    # setupUi

    def retranslateUi(self, audioRecorderWidget):
        audioRecorderWidget.setWindowTitle(QCoreApplication.translate("audioRecorderWidget", u"Form", None))
        self.startButton.setText("")
        self.stopButton.setText("")
        self.recordingTime.setText(QCoreApplication.translate("audioRecorderWidget", u"\u09b8\u09ae\u09df...", None))
        self.fileName.setText("")
        self.fileName.setPlaceholderText(QCoreApplication.translate("audioRecorderWidget", u"\u0985\u09a1\u09bf\u0993 \u09ab\u09be\u0987\u09b2\u09c7\u09b0 \u09a8\u09be\u09ae \u09b2\u09bf\u0996\u09c1\u09a8", None))
        self.saveButton.setText(QCoreApplication.translate("audioRecorderWidget", u"\u09b8\u0982\u09b0\u0995\u09cd\u09b7\u09a3 \u0995\u09b0\u09c1\u09a8", None))
        self.soundingButton.setText("")
    # retranslateUi

