# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'player.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QPushButton,
    QSizePolicy, QSlider, QSpacerItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(807, 561)
        Form.setMinimumSize(QSize(690, 560))
        Form.setStyleSheet(u"background-color: rgb(208, 208, 208);")
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.video_label = QLabel(Form)
        self.video_label.setObjectName(u"video_label")
        self.video_label.setStyleSheet(u"border: 2px solid blue;")

        self.gridLayout.addWidget(self.video_label, 0, 0, 1, 5)

        self.openfile = QPushButton(Form)
        self.openfile.setObjectName(u"openfile")

        self.gridLayout.addWidget(self.openfile, 1, 0, 1, 1)

        self.playBtn = QPushButton(Form)
        self.playBtn.setObjectName(u"playBtn")
        self.playBtn.setEnabled(False)
        self.playBtn.setFlat(False)

        self.gridLayout.addWidget(self.playBtn, 1, 1, 1, 1)

        self.volume_Slider = QSlider(Form)
        self.volume_Slider.setObjectName(u"volume_Slider")
        self.volume_Slider.setMinimumSize(QSize(109, 25))
        self.volume_Slider.setMaximumSize(QSize(109, 25))
        self.volume_Slider.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.volume_Slider, 1, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(60, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 3, 1, 1)

        self.horizontalSlider = QSlider(Form)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setMinimumSize(QSize(350, 0))
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.horizontalSlider, 1, 4, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.video_label.setText("")
        self.openfile.setText(QCoreApplication.translate("Form", u"Open File", None))
        self.playBtn.setText(QCoreApplication.translate("Form", u"Play", None))
    # retranslateUi

