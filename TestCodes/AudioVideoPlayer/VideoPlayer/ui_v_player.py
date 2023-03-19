# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'v_player.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QPushButton,
    QSizePolicy, QSlider, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(690, 561)
        Form.setMinimumSize(QSize(690, 560))
        Form.setStyleSheet(u"background-color: bisque;")
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.video_window = QFrame(Form)
        self.video_window.setObjectName(u"video_window")
        self.video_window.setMinimumSize(QSize(600, 500))
        self.video_window.setStyleSheet(u"border: 2px solid blue;")
        self.video_window.setFrameShape(QFrame.StyledPanel)
        self.video_window.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.video_window)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.openfile = QPushButton(Form)
        self.openfile.setObjectName(u"openfile")

        self.horizontalLayout.addWidget(self.openfile)

        self.playBtn = QPushButton(Form)
        self.playBtn.setObjectName(u"playBtn")
        self.playBtn.setEnabled(False)
        self.playBtn.setFlat(False)

        self.horizontalLayout.addWidget(self.playBtn)

        self.volume_Slider = QSlider(Form)
        self.volume_Slider.setObjectName(u"volume_Slider")
        self.volume_Slider.setOrientation(Qt.Horizontal)

        self.horizontalLayout.addWidget(self.volume_Slider)

        self.horizontalSpacer = QSpacerItem(58, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.horizontalSlider = QSlider(Form)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setMinimumSize(QSize(350, 0))
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.horizontalLayout.addWidget(self.horizontalSlider)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.openfile.setText(QCoreApplication.translate("Form", u"Open File", None))
        self.playBtn.setText(QCoreApplication.translate("Form", u"Play", None))
    # retranslateUi

