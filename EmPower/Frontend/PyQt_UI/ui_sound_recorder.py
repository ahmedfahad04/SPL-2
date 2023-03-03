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

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(479, 566)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(142, 226, 205)")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 0, 4, 1, 1)

        self.horizontalSpacer = QSpacerItem(84, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 1, 0, 1, 2)

        self.pushButton_4 = QPushButton(self.frame)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(50, 40))
        self.pushButton_4.setMaximumSize(QSize(50, 40))
        self.pushButton_4.setStyleSheet(u"QPushButton{\n"
"border: none;\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u"../Images/record_listen.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon)
        self.pushButton_4.setIconSize(QSize(40, 100))

        self.gridLayout_2.addWidget(self.pushButton_4, 1, 2, 1, 2)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(100, 100))
        self.pushButton.setMaximumSize(QSize(100, 100))
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"	border-radius: 50px;\n"
"	border: 3px solid rgb(206, 95, 95)\n"
"}\n"
"\n"
"QPushButton:hover:!pressed\n"
"{\n"
"	background-color:  rgb(255, 131, 139);\n"
"	border-radius: 50px;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"../Images/record_before_start_2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QSize(200, 200))

        self.gridLayout_2.addWidget(self.pushButton, 1, 4, 1, 1)

        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(50, 40))
        self.pushButton_2.setMaximumSize(QSize(50, 40))
        self.pushButton_2.setStyleSheet(u"border: none;")
        icon2 = QIcon()
        icon2.addFile(u"../Images/record_stop.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setIconSize(QSize(40, 100))

        self.gridLayout_2.addWidget(self.pushButton_2, 1, 5, 1, 2)

        self.horizontalSpacer_2 = QSpacerItem(75, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 1, 7, 1, 2)

        self.verticalSpacer_2 = QSpacerItem(20, 68, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 2, 4, 1, 1)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setStyleSheet(u"border: 2px solid rgb(0, 43, 91) ;\n"
"border-radius: 15px;\n"
"background-color: rgb(231, 231, 231);")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label, 3, 2, 1, 5)

        self.verticalSpacer_3 = QSpacerItem(20, 68, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_3, 4, 4, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(46, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 5, 0, 1, 1)

        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(330, 50))
        self.lineEdit.setMaximumSize(QSize(330, 50))
        font1 = QFont()
        font1.setPointSize(12)
        self.lineEdit.setFont(font1)
        self.lineEdit.setStyleSheet(u"border: 2px solid rgb(0, 43, 91) ;\n"
"border-radius: 15px;\n"
"background-color: rgb(231, 231, 231);")
        self.lineEdit.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lineEdit, 5, 1, 1, 7)

        self.horizontalSpacer_4 = QSpacerItem(37, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_4, 5, 8, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 21, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_4, 6, 4, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(123, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_5, 7, 0, 1, 3)

        self.pushButton_3 = QPushButton(self.frame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(0, 40))
        self.pushButton_3.setMaximumSize(QSize(16777215, 40))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(False)
        self.pushButton_3.setFont(font2)
        self.pushButton_3.setStyleSheet(u"border: 2px solid rgb(0, 43, 91) ;\n"
"border-radius: 15px;\n"
"background-color: rgb(36, 105, 127);\n"
"color: rgb(137, 218, 199)")

        self.gridLayout_2.addWidget(self.pushButton_3, 7, 3, 1, 3)

        self.horizontalSpacer_6 = QSpacerItem(114, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_6, 7, 6, 1, 3)

        self.verticalSpacer_5 = QSpacerItem(20, 28, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_5, 8, 4, 1, 1)


        self.gridLayout.addWidget(self.frame, 1, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton_4.setText("")
        self.pushButton.setText("")
        self.pushButton_2.setText("")
        self.label.setText(QCoreApplication.translate("Form", u"\u09b8\u09ae\u09df...", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"\u0985\u09a1\u09bf\u0993 \u09ab\u09be\u0987\u09b2\u09c7\u09b0 \u09a8\u09be\u09ae \u09b2\u09bf\u0996\u09c1\u09a8", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"\u09b8\u0982\u09b0\u0995\u09cd\u09b7\u09a3 \u0995\u09b0\u09c1\u09a8", None))
    # retranslateUi

