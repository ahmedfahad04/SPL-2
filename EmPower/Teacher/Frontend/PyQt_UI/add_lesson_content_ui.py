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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(656, 809)
        Form.setMinimumSize(QSize(656, 809))
        Form.setMaximumSize(QSize(670, 809))
        self.gridLayout_2 = QGridLayout(Form)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.top_frame = QFrame(Form)
        self.top_frame.setObjectName(u"top_frame")
        self.top_frame.setMinimumSize(QSize(641, 90))
        self.top_frame.setMaximumSize(QSize(16777215, 90))
        self.top_frame.setStyleSheet(u"background-color: rgb(43, 72, 101);")
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


        self.gridLayout_2.addWidget(self.top_frame, 0, 0, 1, 1)

        self.middle_frame = QFrame(Form)
        self.middle_frame.setObjectName(u"middle_frame")
        self.middle_frame.setMinimumSize(QSize(641, 710))
        self.middle_frame.setStyleSheet(u"background-color: rgb(32, 94, 115);\n"
"color: rgb(137, 218, 199);")
        self.middle_frame.setFrameShape(QFrame.StyledPanel)
        self.middle_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.middle_frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.frame_3 = QFrame(self.middle_frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(630, 80))
        self.frame_3.setMaximumSize(QSize(493, 80))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, -1, 15, -1)
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

        self.cmb_category = QComboBox(self.frame_3)
        self.cmb_category.addItem("")
        self.cmb_category.addItem("")
        self.cmb_category.addItem("")
        self.cmb_category.addItem("")
        self.cmb_category.addItem("")
        self.cmb_category.setObjectName(u"cmb_category")
        self.cmb_category.setMinimumSize(QSize(300, 50))
        font2 = QFont()
        font2.setFamilies([u"Hind Siliguri Medium"])
        font2.setPointSize(12)
        self.cmb_category.setFont(font2)
        self.cmb_category.setStyleSheet(u"background-color: rgb(137, 218, 199);\n"
"padding-left: 15px;\n"
"border-radius: 10px;\n"
"color: rgb(43, 72, 101);")

        self.horizontalLayout_5.addWidget(self.cmb_category)


        self.gridLayout_3.addWidget(self.frame_3, 0, 0, 1, 3)

        self.frame_6 = QFrame(self.middle_frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(630, 71))
        self.frame_6.setMaximumSize(QSize(600, 72))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lbl_lesson_id = QLabel(self.frame_6)
        self.lbl_lesson_id.setObjectName(u"lbl_lesson_id")
        self.lbl_lesson_id.setMinimumSize(QSize(151, 0))
        self.lbl_lesson_id.setMaximumSize(QSize(200, 16777215))
        self.lbl_lesson_id.setFont(font1)
        self.lbl_lesson_id.setStyleSheet(u"color: rgb(137, 218, 199);")

        self.horizontalLayout_3.addWidget(self.lbl_lesson_id)

        self.edit_lesson_id = QLineEdit(self.frame_6)
        self.edit_lesson_id.setObjectName(u"edit_lesson_id")
        self.edit_lesson_id.setMinimumSize(QSize(325, 50))
        font3 = QFont()
        font3.setFamilies([u"Hind Siliguri"])
        font3.setPointSize(12)
        font3.setBold(False)
        self.edit_lesson_id.setFont(font3)
        self.edit_lesson_id.setStyleSheet(u"background-color: rgb(137, 218, 199);\n"
"border: 2px solid rgb(101, 161, 146);\n"
"padding-left: 15px;\n"
"border-radius: 10px;\n"
"color: rgb(43, 72, 101);")
        self.edit_lesson_id.setCursorPosition(0)

        self.horizontalLayout_3.addWidget(self.edit_lesson_id)


        self.gridLayout_3.addWidget(self.frame_6, 1, 0, 1, 3)

        self.frame_2 = QFrame(self.middle_frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(630, 71))
        self.frame_2.setMaximumSize(QSize(600, 72))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.lbl_lesson_topic = QLabel(self.frame_2)
        self.lbl_lesson_topic.setObjectName(u"lbl_lesson_topic")
        self.lbl_lesson_topic.setMinimumSize(QSize(151, 0))
        self.lbl_lesson_topic.setMaximumSize(QSize(150, 16777215))
        font4 = QFont()
        font4.setFamilies([u"Hind Siliguri Medium"])
        font4.setPointSize(13)
        font4.setBold(False)
        self.lbl_lesson_topic.setFont(font4)
        self.lbl_lesson_topic.setStyleSheet(u"color: rgb(137, 218, 199);")

        self.horizontalLayout_6.addWidget(self.lbl_lesson_topic)

        self.edit_lesson_topic = QLineEdit(self.frame_2)
        self.edit_lesson_topic.setObjectName(u"edit_lesson_topic")
        self.edit_lesson_topic.setMinimumSize(QSize(448, 50))
        font5 = QFont()
        font5.setFamilies([u"Hind Siliguri Medium"])
        font5.setPointSize(11)
        self.edit_lesson_topic.setFont(font5)
        self.edit_lesson_topic.setStyleSheet(u"background-color: rgb(137, 218, 199);\n"
"border: 2px solid rgb(101, 161, 146);\n"
"padding-left: 15px;\n"
"border-radius: 10px;\n"
"color: rgb(43, 72, 101);")

        self.horizontalLayout_6.addWidget(self.edit_lesson_topic)


        self.gridLayout_3.addWidget(self.frame_2, 2, 0, 1, 3)

        self.frame = QFrame(self.middle_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(630, 71))
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
        self.btn_select_photo.setMinimumSize(QSize(200, 50))
        self.btn_select_photo.setMaximumSize(QSize(150, 51))
        self.btn_select_photo.setFont(font5)
        self.btn_select_photo.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_select_photo.setStyleSheet(u"QPushButton {\n"
"border: 3px solid rgb(43, 72, 101);\n"
"border-radius: 10px;\n"
"background-color:  rgb(43, 72, 101);\n"
"color: rgb(137, 218, 199)\n"
"}\n"
"\n"
"QPushButton::hover:!pressed {\n"
"background-color: rgb(0, 43, 91);\n"
"border: 3px solid rgb(0, 43, 91); \n"
"}")
        self.btn_select_photo.setFlat(True)

        self.horizontalLayout_2.addWidget(self.btn_select_photo)

        self.lbl_photo_name = QLabel(self.frame)
        self.lbl_photo_name.setObjectName(u"lbl_photo_name")
        self.lbl_photo_name.setFont(font4)
        self.lbl_photo_name.setStyleSheet(u"color: rgb(137, 218, 199);\n"
"padding-left: 10px;\n"
"border: 3px solid rgb(43, 72, 101);\n"
"border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"border-bottom-right-radius: 10px;")
        self.lbl_photo_name.setWordWrap(True)

        self.horizontalLayout_2.addWidget(self.lbl_photo_name)


        self.gridLayout_3.addWidget(self.frame, 3, 0, 1, 3)

        self.frame_5 = QFrame(self.middle_frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(630, 179))
        self.frame_5.setMaximumSize(QSize(491, 142))
        self.frame_5.setStyleSheet(u"")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lbl_audio = QLabel(self.frame_5)
        self.lbl_audio.setObjectName(u"lbl_audio")
        self.lbl_audio.setMinimumSize(QSize(371, 47))
        self.lbl_audio.setFont(font4)
        self.lbl_audio.setStyleSheet(u"color: rgb(137, 218, 199);\n"
"padding-left: 10px;\n"
"border: 3px solid rgb(43, 72, 101);\n"
"border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"border-bottom-right-radius: 10px;")
        self.lbl_audio.setWordWrap(True)

        self.gridLayout.addWidget(self.lbl_audio, 0, 1, 1, 1)

        self.btn_select_audio = QPushButton(self.frame_5)
        self.btn_select_audio.setObjectName(u"btn_select_audio")
        self.btn_select_audio.setMinimumSize(QSize(200, 50))
        self.btn_select_audio.setMaximumSize(QSize(200, 50))
        self.btn_select_audio.setFont(font5)
        self.btn_select_audio.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_select_audio.setStyleSheet(u"QPushButton {\n"
"border: 3px solid rgb(43, 72, 101);\n"
"border-radius: 10px;\n"
"background-color:  rgb(43, 72, 101);\n"
"color: rgb(137, 218, 199)\n"
"}\n"
"\n"
"QPushButton::hover:!pressed {\n"
"background-color: rgb(0, 43, 91);\n"
"border: 3px solid rgb(0, 43, 91); \n"
"}")
        self.btn_select_audio.setFlat(True)

        self.gridLayout.addWidget(self.btn_select_audio, 0, 0, 1, 1)

        self.frame_4 = QFrame(self.frame_5)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(610, 17))
        self.frame_4.setMaximumSize(QSize(465, 72))
        self.frame_4.setStyleSheet(u"border: none;")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.lbl_or = QLabel(self.frame_4)
        self.lbl_or.setObjectName(u"lbl_or")
        self.lbl_or.setMinimumSize(QSize(81, 45))
        self.lbl_or.setMaximumSize(QSize(81, 45))
        font6 = QFont()
        font6.setPointSize(16)
        self.lbl_or.setFont(font6)
        self.lbl_or.setStyleSheet(u"color: rgb(137, 218, 199);")
        self.lbl_or.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.lbl_or)


        self.gridLayout.addWidget(self.frame_4, 1, 0, 1, 2)

        self.btn_record_audio = QPushButton(self.frame_5)
        self.btn_record_audio.setObjectName(u"btn_record_audio")
        sizePolicy.setHeightForWidth(self.btn_record_audio.sizePolicy().hasHeightForWidth())
        self.btn_record_audio.setSizePolicy(sizePolicy)
        self.btn_record_audio.setMinimumSize(QSize(610, 50))
        self.btn_record_audio.setMaximumSize(QSize(200, 50))
        self.btn_record_audio.setFont(font5)
        self.btn_record_audio.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_record_audio.setStyleSheet(u"QPushButton {\n"
"border: 3px solid rgb(43, 72, 101);\n"
"border-radius: 10px;\n"
"background-color:  rgb(43, 72, 101);\n"
"color: rgb(137, 218, 199)\n"
"}\n"
"\n"
"QPushButton::hover:!pressed {\n"
"background-color: rgb(0, 43, 91);\n"
"border: 3px solid rgb(0, 43, 91); \n"
"}")
        self.btn_record_audio.setFlat(True)

        self.gridLayout.addWidget(self.btn_record_audio, 2, 0, 1, 2)


        self.gridLayout_3.addWidget(self.frame_5, 4, 0, 1, 3)

        self.horizontalSpacer = QSpacerItem(212, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 5, 0, 2, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 31, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 5, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(212, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 5, 2, 2, 1)

        self.btn_submit = QPushButton(self.middle_frame)
        self.btn_submit.setObjectName(u"btn_submit")
        self.btn_submit.setMinimumSize(QSize(200, 50))
        font7 = QFont()
        font7.setFamilies([u"Hind Siliguri Medium"])
        font7.setPointSize(13)
        self.btn_submit.setFont(font7)
        self.btn_submit.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_submit.setStyleSheet(u"QPushButton {\n"
"border: 3px solid rgb(43, 72, 101);\n"
"border-radius: 10px;\n"
"background-color:  #002B5B;\n"
"color: rgb(137, 218, 199)\n"
"}\n"
"\n"
"QPushButton::hover:!pressed {\n"
"background-color: rgb(43, 72, 101);\n"
"border: 3px solid rgb(0, 43, 91); \n"
"}")
        self.btn_submit.setFlat(True)

        self.gridLayout_3.addWidget(self.btn_submit, 6, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 7, 1, 1, 1)

        self.lbl_lsn_cat_status = QLabel(self.middle_frame)
        self.lbl_lsn_cat_status.setObjectName(u"lbl_lsn_cat_status")
        self.lbl_lsn_cat_status.setMinimumSize(QSize(481, 41))
        self.lbl_lsn_cat_status.setFont(font2)
        self.lbl_lsn_cat_status.setStyleSheet(u"border: 2px solid  rgb(0, 43, 91);\n"
"color: rgb(255, 0, 0);\n"
"background-color: rgb(137, 218, 199);")
        self.lbl_lsn_cat_status.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.lbl_lsn_cat_status, 8, 0, 1, 3)


        self.gridLayout_2.addWidget(self.middle_frame, 1, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lbl_heading.setText(QCoreApplication.translate("Form", u"\u09ae\u09a1\u09bf\u0989\u09b2\u09c7\u09b0 \u0995\u09a8\u09cd\u099f\u09c7\u09a8\u09cd\u099f \u09af\u09c1\u0995\u09cd\u09a4 \u0995\u09b0\u09c1\u09a8", None))
        self.lbl_category.setText(QCoreApplication.translate("Form", u"\u0995\u09cd\u09af\u09be\u099f\u09c7\u0997\u09b0\u09bf", None))
        self.cmb_category.setItemText(0, QCoreApplication.translate("Form", u"\u0995\u09cd\u09af\u09be\u099f\u09be\u0997\u09b0\u09bf \u09a8\u09bf\u09b0\u09cd\u09ac\u09be\u099a\u09a8 \u0995\u09b0\u09c1\u09a8", None))
        self.cmb_category.setItemText(1, QCoreApplication.translate("Form", u"\u09a8\u09be\u09ae \u09b6\u09bf\u0996\u09a8 (Noun)", None))
        self.cmb_category.setItemText(2, QCoreApplication.translate("Form", u"\u0995\u09cd\u09b0\u09bf\u09df\u09be \u09b6\u09bf\u0996\u09a8 (Verb)", None))
        self.cmb_category.setItemText(3, QCoreApplication.translate("Form", u"\u09b8\u09ae\u09cd\u09aa\u09b0\u09cd\u0995 \u09b6\u09bf\u0996\u09a8 (Association)", None))
        self.cmb_category.setItemText(4, QCoreApplication.translate("Form", u"\u0995\u09b0\u09cd\u09ae\u09a7\u09be\u09b0\u09be \u09b6\u09bf\u0996\u09a8 (Activity)", None))

        self.lbl_lesson_id.setText(QCoreApplication.translate("Form", u"\u09aa\u09be\u09a0\u09cd\u09af\u0995\u09cd\u09b0\u09ae", None))
        self.edit_lesson_id.setPlaceholderText(QCoreApplication.translate("Form", u"\u09af\u09c7\u09ae\u09a8\u0983 \u09e7", None))
        self.lbl_lesson_topic.setText(QCoreApplication.translate("Form", u"\u09aa\u09be\u09a0\u09cd\u09af\u09c7\u09b0 \u09ac\u09bf\u09b7\u09df", None))
        self.edit_lesson_topic.setPlaceholderText(QCoreApplication.translate("Form", u"\u09af\u09c7\u09ae\u09a8\u0983 \u0986\u09ae ", None))
        self.btn_select_photo.setText(QCoreApplication.translate("Form", u"\u099b\u09ac\u09bf/\u09ad\u09bf\u09a1\u09bf\u0993 \u09a8\u09bf\u09b0\u09cd\u09ac\u09be\u099a\u09a8 \u0995\u09b0\u09c1\u09a8", None))
#if QT_CONFIG(shortcut)
        self.btn_select_photo.setShortcut(QCoreApplication.translate("Form", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.lbl_photo_name.setText("")
        self.lbl_audio.setText("")
        self.btn_select_audio.setText(QCoreApplication.translate("Form", u"\u0985\u09a1\u09bf\u0993 \u09a8\u09bf\u09b0\u09cd\u09ac\u09be\u099a\u09a8 \u0995\u09b0\u09c1\u09a8", None))
#if QT_CONFIG(shortcut)
        self.btn_select_audio.setShortcut(QCoreApplication.translate("Form", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.lbl_or.setText(QCoreApplication.translate("Form", u"\u0985\u09a5\u09ac\u09be", None))
        self.btn_record_audio.setText(QCoreApplication.translate("Form", u"\u0985\u09a1\u09bf\u0993 \u09b0\u09c7\u0995\u09b0\u09cd\u09a1 \u0995\u09b0\u09c1\u09a8", None))
#if QT_CONFIG(shortcut)
        self.btn_record_audio.setShortcut(QCoreApplication.translate("Form", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.btn_submit.setText(QCoreApplication.translate("Form", u"\u09ae\u09a1\u09bf\u0989\u09b2 \u09a4\u09c8\u09b0\u09bf \u0995\u09b0\u09c1\u09a8 ", None))
#if QT_CONFIG(shortcut)
        self.btn_submit.setShortcut(QCoreApplication.translate("Form", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.lbl_lsn_cat_status.setText("")
    # retranslateUi

