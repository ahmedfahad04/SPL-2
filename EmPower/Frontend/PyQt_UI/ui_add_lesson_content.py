# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_lesson_content.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(559, 679)
        self.formLayout = QFormLayout(Form)
        self.formLayout.setObjectName(u"formLayout")
        self.top_frame = QFrame(Form)
        self.top_frame.setObjectName(u"top_frame")
        self.top_frame.setMinimumSize(QSize(530, 90))
        self.top_frame.setMaximumSize(QSize(16777215, 90))
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


        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.top_frame)

        self.middle_frame = QFrame(Form)
        self.middle_frame.setObjectName(u"middle_frame")
        self.middle_frame.setMinimumSize(QSize(530, 560))
        self.middle_frame.setStyleSheet(u"background-color: rgb(32, 94, 115);\n"
"border-radius: 20px;")
        self.middle_frame.setFrameShape(QFrame.StyledPanel)
        self.middle_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.middle_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_3 = QFrame(self.middle_frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(493, 80))
        self.frame_3.setMaximumSize(QSize(493, 80))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lbl_category = QLabel(self.frame_3)
        self.lbl_category.setObjectName(u"lbl_category")
        self.lbl_category.setMinimumSize(QSize(120, 0))
        self.lbl_category.setMaximumSize(QSize(150, 16777215))
        font1 = QFont()
        font1.setFamilies([u"Hind Siliguri Medium"])
        font1.setPointSize(15)
        font1.setBold(False)
        self.lbl_category.setFont(font1)
        self.lbl_category.setStyleSheet(u"color: rgb(137, 218, 199);")

        self.horizontalLayout_5.addWidget(self.lbl_category)

        self.comboBox = QComboBox(self.frame_3)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(300, 50))
        self.comboBox.setStyleSheet(u"background-color: rgb(137, 218, 199);\n"
"padding-left: 15px;\n"
"border-radius: 10px;\n"
"color: rgb(43, 72, 101);")

        self.horizontalLayout_5.addWidget(self.comboBox)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.frame_2 = QFrame(self.middle_frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(491, 71))
        self.frame_2.setMaximumSize(QSize(491, 72))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.edit_lesson_tag = QLineEdit(self.frame_2)
        self.edit_lesson_tag.setObjectName(u"edit_lesson_tag")
        self.edit_lesson_tag.setMinimumSize(QSize(330, 50))
        font2 = QFont()
        font2.setFamilies([u"Hind Siliguri Medium"])
        font2.setPointSize(11)
        self.edit_lesson_tag.setFont(font2)
        self.edit_lesson_tag.setStyleSheet(u"background-color: rgb(137, 218, 199);\n"
"border: 2px solid rgb(101, 161, 146);\n"
"padding-left: 15px;\n"
"border-radius: 10px;\n"
"color: rgb(43, 72, 101);")

        self.horizontalLayout_3.addWidget(self.edit_lesson_tag)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame = QFrame(self.middle_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(491, 71))
        self.frame.setMaximumSize(QSize(491, 71))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_select_photo = QPushButton(self.frame)
        self.btn_select_photo.setObjectName(u"btn_select_photo")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_select_photo.sizePolicy().hasHeightForWidth())
        self.btn_select_photo.setSizePolicy(sizePolicy)
        self.btn_select_photo.setMinimumSize(QSize(171, 50))
        self.btn_select_photo.setMaximumSize(QSize(171, 51))
        font3 = QFont()
        font3.setFamilies([u"Hind Siliguri Medium"])
        font3.setPointSize(12)
        self.btn_select_photo.setFont(font3)
        self.btn_select_photo.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_select_photo.setStyleSheet(u"QPushButton {\n"
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
        self.btn_select_photo.setFlat(True)

        self.horizontalLayout_2.addWidget(self.btn_select_photo)

        self.lbl_photo_name = QLabel(self.frame)
        self.lbl_photo_name.setObjectName(u"lbl_photo_name")
        font4 = QFont()
        font4.setFamilies([u"Hind Siliguri Medium"])
        font4.setPointSize(13)
        font4.setBold(False)
        self.lbl_photo_name.setFont(font4)
        self.lbl_photo_name.setStyleSheet(u"color: rgb(137, 218, 199);\n"
"padding-left: 10px;\n"
"border: 3px solid rgb(43, 72, 101);")

        self.horizontalLayout_2.addWidget(self.lbl_photo_name)


        self.verticalLayout_2.addWidget(self.frame)

        self.frame_5 = QFrame(self.middle_frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(491, 142))
        self.frame_5.setMaximumSize(QSize(491, 142))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_4 = QLabel(self.frame_5)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"color: rgb(137, 218, 199)")

        self.verticalLayout_3.addWidget(self.label_4)

        self.frame_4 = QFrame(self.frame_5)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(469, 72))
        self.frame_4.setMaximumSize(QSize(469, 72))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btn_select_audio = QPushButton(self.frame_4)
        self.btn_select_audio.setObjectName(u"btn_select_audio")
        self.btn_select_audio.setMinimumSize(QSize(161, 50))
        self.btn_select_audio.setMaximumSize(QSize(161, 50))
        self.btn_select_audio.setFont(font2)
        self.btn_select_audio.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_select_audio.setStyleSheet(u"QPushButton {\n"
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
        self.btn_select_audio.setFlat(True)

        self.horizontalLayout_4.addWidget(self.btn_select_audio)

        self.label_5 = QLabel(self.frame_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(81, 45))
        self.label_5.setMaximumSize(QSize(81, 45))
        font5 = QFont()
        font5.setPointSize(16)
        self.label_5.setFont(font5)
        self.label_5.setStyleSheet(u"color: rgb(137, 218, 199);")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_5)

        self.btn_record_audio = QPushButton(self.frame_4)
        self.btn_record_audio.setObjectName(u"btn_record_audio")
        sizePolicy.setHeightForWidth(self.btn_record_audio.sizePolicy().hasHeightForWidth())
        self.btn_record_audio.setSizePolicy(sizePolicy)
        self.btn_record_audio.setMinimumSize(QSize(100, 50))
        self.btn_record_audio.setMaximumSize(QSize(161, 50))
        self.btn_record_audio.setFont(font2)
        self.btn_record_audio.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_record_audio.setStyleSheet(u"QPushButton {\n"
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
        self.btn_record_audio.setFlat(True)

        self.horizontalLayout_4.addWidget(self.btn_record_audio)


        self.verticalLayout_3.addWidget(self.frame_4)


        self.verticalLayout_2.addWidget(self.frame_5)

        self.btn_submit = QPushButton(self.middle_frame)
        self.btn_submit.setObjectName(u"btn_submit")
        self.btn_submit.setMinimumSize(QSize(100, 50))
        font6 = QFont()
        font6.setFamilies([u"Hind Siliguri Medium"])
        font6.setPointSize(13)
        self.btn_submit.setFont(font6)
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

        self.verticalLayout_2.addWidget(self.btn_submit)


        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.middle_frame)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lbl_heading.setText(QCoreApplication.translate("Form", u"\u09aa\u09be\u09a0\u09cd\u09af\u09c7\u09b0 \u0995\u09a8\u09cd\u099f\u09c7\u09a8\u09cd\u099f \u09af\u09c1\u0995\u09cd\u09a4 \u0995\u09b0\u09c1\u09a8", None))
        self.lbl_category.setText(QCoreApplication.translate("Form", u"\u0995\u09cd\u09af\u09be\u099f\u09c7\u0997\u09b0\u09bf", None))
        self.edit_lesson_tag.setPlaceholderText(QCoreApplication.translate("Form", u"\u09aa\u09be\u09a0\u09cd\u09af\u09c7\u09b0 \u09ac\u09bf\u09b7\u09df ", None))
        self.btn_select_photo.setText(QCoreApplication.translate("Form", u"\u099b\u09ac\u09bf \u09a8\u09bf\u09b0\u09cd\u09ac\u09be\u099a\u09a8 \u0995\u09b0\u09c1\u09a8", None))
#if QT_CONFIG(shortcut)
        self.btn_select_photo.setShortcut(QCoreApplication.translate("Form", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.lbl_photo_name.setText(QCoreApplication.translate("Form", u"\u099b\u09ac\u09bf\u09b0 \u09a8\u09be\u09ae", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u0985\u09a1\u09bf\u0993 \u09af\u09c1\u0995\u09cd\u09a4 \u0995\u09b0\u09c1\u09a8", None))
        self.btn_select_audio.setText(QCoreApplication.translate("Form", u"\u0985\u09a1\u09bf\u0993 \u09a8\u09bf\u09b0\u09cd\u09ac\u09be\u099a\u09a8 \u0995\u09b0\u09c1\u09a8", None))
#if QT_CONFIG(shortcut)
        self.btn_select_audio.setShortcut(QCoreApplication.translate("Form", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.label_5.setText(QCoreApplication.translate("Form", u"\u0985\u09a5\u09ac\u09be", None))
        self.btn_record_audio.setText(QCoreApplication.translate("Form", u"\u0985\u09a1\u09bf\u0993 \u09b0\u09c7\u0995\u09b0\u09cd\u09a1 \u0995\u09b0\u09c1\u09a8", None))
#if QT_CONFIG(shortcut)
        self.btn_record_audio.setShortcut(QCoreApplication.translate("Form", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.btn_submit.setText(QCoreApplication.translate("Form", u"\u09b2\u09c7\u09b8\u09a8 \u09a4\u09c8\u09b0\u09bf \u0995\u09b0\u09c1\u09a8 ", None))
#if QT_CONFIG(shortcut)
        self.btn_submit.setShortcut(QCoreApplication.translate("Form", u"Return", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

