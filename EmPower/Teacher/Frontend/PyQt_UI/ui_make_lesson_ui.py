# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_make_lesson.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QListView,
    QPlainTextEdit, QSizePolicy, QTextEdit, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1239, 581)
        Form.setMinimumSize(QSize(1180, 520))
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.middle_content_frame = QFrame(Form)
        self.middle_content_frame.setObjectName(u"middle_content_frame")
        self.middle_content_frame.setMinimumSize(QSize(1180, 500))
        self.middle_content_frame.setStyleSheet(u"background-color: rgb(36, 105, 127)")
        self.middle_content_frame.setFrameShape(QFrame.StyledPanel)
        self.middle_content_frame.setFrameShadow(QFrame.Raised)
        self.listView = QListView(self.middle_content_frame)
        self.listView.setObjectName(u"listView")
        self.listView.setGeometry(QRect(90, 90, 256, 192))
        self.plainTextEdit = QPlainTextEdit(self.middle_content_frame)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(140, 120, 104, 41))
        self.textEdit = QTextEdit(self.middle_content_frame)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(130, 180, 91, 51))

        self.horizontalLayout.addWidget(self.middle_content_frame)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.plainTextEdit.setPlainText(QCoreApplication.translate("Form", u"kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkafjfalfjkajajf\n"
"", None))
        self.textEdit.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">afafjklfja;lfkjfkjfdsf;ksdjfkjfksdjfkajf;sjfksjfkasjf;kafkjf;la</p></body></html>", None))
    # retranslateUi

