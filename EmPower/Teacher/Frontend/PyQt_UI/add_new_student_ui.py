# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_new_student.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(552, 720)
        Form.setMinimumSize(QSize(550, 720))
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.top_frame = QFrame(Form)
        self.top_frame.setObjectName(u"top_frame")
        self.top_frame.setMinimumSize(QSize(530, 70))
        self.top_frame.setStyleSheet(u"background-color: rgb(43, 72, 101);\n"
"border-radius: 20px;")
        self.top_frame.setFrameShape(QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.top_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lbl_heading = QLabel(self.top_frame)
        self.lbl_heading.setObjectName(u"lbl_heading")
        font = QFont()
        font.setFamilies([u"Hind Siliguri Medium"])
        font.setPointSize(19)
        font.setBold(False)
        self.lbl_heading.setFont(font)
        self.lbl_heading.setStyleSheet(u"color: rgb(143, 227, 207);")
        self.lbl_heading.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.lbl_heading)


        self.verticalLayout.addWidget(self.top_frame)

        self.middle_frame = QFrame(Form)
        self.middle_frame.setObjectName(u"middle_frame")
        self.middle_frame.setMinimumSize(QSize(530, 560))
        self.middle_frame.setStyleSheet(u"background-color: rgb(32, 94, 115);\n"
"border-radius: 20px;")
        self.middle_frame.setFrameShape(QFrame.StyledPanel)
        self.middle_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.middle_frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.middle_frame)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(151, 51))
        font1 = QFont()
        font1.setPointSize(10)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"border: 3px solid rgb(43, 72, 101);\n"
"border-radius: 10px;\n"
"background-color:  rgb(43, 72, 101);\n"
"color: rgb(137, 218, 199)")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.input_id = QLineEdit(self.middle_frame)
        self.input_id.setObjectName(u"input_id")
        self.input_id.setMinimumSize(QSize(330, 55))
        font2 = QFont()
        font2.setFamilies([u"Kalpurush"])
        font2.setPointSize(11)
        font2.setBold(False)
        self.input_id.setFont(font2)
        self.input_id.setStyleSheet(u"background-color: rgb(137, 218, 199);\n"
"border: 2px solid rgb(101, 161, 146);\n"
"padding-left: 15px;\n"
"border-radius: 10px;\n"
"color: black;")

        self.gridLayout.addWidget(self.input_id, 0, 1, 1, 1)

        self.label_2 = QLabel(self.middle_frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(151, 41))
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"border: 3px solid rgb(43, 72, 101);\n"
"border-radius: 10px;\n"
"background-color:  rgb(43, 72, 101);\n"
"color: rgb(137, 218, 199)")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.input_name = QLineEdit(self.middle_frame)
        self.input_name.setObjectName(u"input_name")
        self.input_name.setMinimumSize(QSize(330, 50))
        self.input_name.setFont(font2)
        self.input_name.setStyleSheet(u"background-color: rgb(137, 218, 199);\n"
"border: 2px solid rgb(101, 161, 146);\n"
"padding-left: 15px;\n"
"border-radius: 10px;\n"
"color: black;")

        self.gridLayout.addWidget(self.input_name, 1, 1, 1, 1)

        self.label_3 = QLabel(self.middle_frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(151, 41))
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"border: 3px solid rgb(43, 72, 101);\n"
"border-radius: 10px;\n"
"background-color:  rgb(43, 72, 101);\n"
"color: rgb(137, 218, 199)")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.input_age = QLineEdit(self.middle_frame)
        self.input_age.setObjectName(u"input_age")
        self.input_age.setMinimumSize(QSize(330, 50))
        self.input_age.setFont(font2)
        self.input_age.setStyleSheet(u"background-color: rgb(137, 218, 199);\n"
"border: 2px solid rgb(101, 161, 146);\n"
"padding-left: 15px;\n"
"border-radius: 10px;\n"
"color: black;")

        self.gridLayout.addWidget(self.input_age, 2, 1, 1, 1)

        self.label_4 = QLabel(self.middle_frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(151, 41))
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"border: 3px solid rgb(43, 72, 101);\n"
"border-radius: 10px;\n"
"background-color:  rgb(43, 72, 101);\n"
"color: rgb(137, 218, 199)")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.input_address = QLineEdit(self.middle_frame)
        self.input_address.setObjectName(u"input_address")
        self.input_address.setMinimumSize(QSize(330, 50))
        font3 = QFont()
        font3.setFamilies([u"Kalpurush"])
        font3.setPointSize(11)
        self.input_address.setFont(font3)
        self.input_address.setStyleSheet(u"background-color: rgb(137, 218, 199);\n"
"border: 2px solid rgb(101, 161, 146);\n"
"padding-left: 15px;\n"
"border-radius: 10px;\n"
"color: black;")

        self.gridLayout.addWidget(self.input_address, 3, 1, 1, 1)

        self.label_5 = QLabel(self.middle_frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(151, 41))
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"border: 3px solid rgb(43, 72, 101);\n"
"border-radius: 10px;\n"
"background-color:  rgb(43, 72, 101);\n"
"color: rgb(137, 218, 199)")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)

        self.input_guardian = QLineEdit(self.middle_frame)
        self.input_guardian.setObjectName(u"input_guardian")
        self.input_guardian.setMinimumSize(QSize(330, 50))
        self.input_guardian.setFont(font3)
        self.input_guardian.setStyleSheet(u"background-color: rgb(137, 218, 199);\n"
"border: 2px solid rgb(101, 161, 146);\n"
"padding-left: 15px;\n"
"border-radius: 10px;\n"
"color: black;")

        self.gridLayout.addWidget(self.input_guardian, 4, 1, 1, 1)

        self.label_6 = QLabel(self.middle_frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(151, 41))
        font4 = QFont()
        font4.setPointSize(8)
        self.label_6.setFont(font4)
        self.label_6.setStyleSheet(u"border: 3px solid rgb(43, 72, 101);\n"
"border-radius: 10px;\n"
"background-color:  rgb(43, 72, 101);\n"
"color: rgb(137, 218, 199)")
        self.label_6.setAlignment(Qt.AlignCenter)
        self.label_6.setWordWrap(False)

        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)

        self.input_phone = QLineEdit(self.middle_frame)
        self.input_phone.setObjectName(u"input_phone")
        self.input_phone.setMinimumSize(QSize(330, 50))
        self.input_phone.setFont(font3)
        self.input_phone.setStyleSheet(u"background-color: rgb(137, 218, 199);\n"
"border: 2px solid rgb(101, 161, 146);\n"
"padding-left: 15px;\n"
"border-radius: 10px;\n"
"color: black;")

        self.gridLayout.addWidget(self.input_phone, 5, 1, 1, 1)

        self.btn_submit = QPushButton(self.middle_frame)
        self.btn_submit.setObjectName(u"btn_submit")
        self.btn_submit.setMinimumSize(QSize(100, 50))
        font5 = QFont()
        font5.setFamilies([u"Hind Siliguri Medium"])
        font5.setPointSize(13)
        self.btn_submit.setFont(font5)
        self.btn_submit.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_submit.setStyleSheet(u"QPushButton {\n"
"border: 3px solid rgb(43, 72, 101);\n"
"border-radius: 10px;\n"
"background-color:  #002B5B;\n"
"color: rgb(137, 218, 199)\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"background-color: rgb(43, 72, 101);\n"
"border: 3px solid rgb(0, 43, 91); \n"
"}")
        self.btn_submit.setFlat(True)

        self.gridLayout.addWidget(self.btn_submit, 6, 0, 1, 2)


        self.verticalLayout.addWidget(self.middle_frame)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lbl_heading.setText(QCoreApplication.translate("Form", u"\u09b6\u09bf\u0995\u09cd\u09b7\u09be\u09b0\u09cd\u09a5\u09c0\u09b0 \u09a4\u09a5\u09cd\u09af \u09aa\u09cd\u09b0\u09a6\u09be\u09a8 \u0995\u09b0\u09c1\u09a8", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u09b6\u09bf\u0995\u09cd\u09b7\u09be\u09b0\u09cd\u09a5\u09c0 \u0986\u0987\u09a1\u09bf", None))
        self.input_id.setText("")
        self.input_id.setPlaceholderText("")
        self.label_2.setText(QCoreApplication.translate("Form", u"\u09b6\u09bf\u0995\u09cd\u09b7\u09be\u09b0\u09cd\u09a5\u09c0\u09b0 \u09a8\u09be\u09ae ", None))
        self.input_name.setPlaceholderText("")
        self.label_3.setText(QCoreApplication.translate("Form", u"\u09b6\u09bf\u0995\u09cd\u09b7\u09be\u09b0\u09cd\u09a5\u09c0\u09b0 \u09ac\u09df\u09b8", None))
        self.input_age.setPlaceholderText("")
        self.label_4.setText(QCoreApplication.translate("Form", u"\u09a0\u09bf\u0995\u09be\u09a8\u09be", None))
        self.input_address.setPlaceholderText("")
        self.label_5.setText(QCoreApplication.translate("Form", u"\u0985\u09ad\u09bf\u09ad\u09be\u09ac\u0995\u09c7\u09b0 \u09a8\u09be\u09ae", None))
        self.input_guardian.setPlaceholderText("")
        self.label_6.setText(QCoreApplication.translate("Form", u"\u0985\u09ad\u09bf\u09ad\u09be\u09ac\u0995\u09c7\u09b0 \u09ae\u09cb\u09ac\u09be\u0987\u09b2 \u09a8\u09ae\u09cd\u09ac\u09b0", None))
        self.input_phone.setPlaceholderText("")
        self.btn_submit.setText(QCoreApplication.translate("Form", u"\u09a4\u09a5\u09cd\u09af \u09af\u09c1\u0995\u09cd\u09a4 \u0995\u09b0\u09c1\u09a8 ", None))
#if QT_CONFIG(shortcut)
        self.btn_submit.setShortcut(QCoreApplication.translate("Form", u"Return", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

