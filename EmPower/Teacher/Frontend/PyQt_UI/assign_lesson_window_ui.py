# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'assign_lesson_window.ui'
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
        Form.resize(521, 481)
        self.gridLayout_2 = QGridLayout(Form)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.top_frame = QFrame(Form)
        self.top_frame.setObjectName(u"top_frame")
        self.top_frame.setMinimumSize(QSize(521, 90))
        self.top_frame.setMaximumSize(QSize(16777215, 16777215))
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
        self.middle_frame.setMinimumSize(QSize(521, 391))
        self.middle_frame.setStyleSheet(u"background-color: rgb(32, 94, 115);\n"
"color: rgb(137, 218, 199);")
        self.middle_frame.setFrameShape(QFrame.StyledPanel)
        self.middle_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.middle_frame)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.middle_frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(300, 80))
        self.frame_3.setMaximumSize(QSize(16777215, 16777215))
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

        self.lsn_cmb_lesson_list = QComboBox(self.frame_3)
        self.lsn_cmb_lesson_list.addItem("")
        self.lsn_cmb_lesson_list.setObjectName(u"lsn_cmb_lesson_list")
        self.lsn_cmb_lesson_list.setMinimumSize(QSize(308, 50))
        font2 = QFont()
        font2.setFamilies([u"Hind Siliguri Medium"])
        font2.setPointSize(12)
        self.lsn_cmb_lesson_list.setFont(font2)
        self.lsn_cmb_lesson_list.setStyleSheet(u"background-color: rgb(137, 218, 199);\n"
"padding-left: 15px;\n"
"border-radius: 10px;\n"
"color: rgb(43, 72, 101);")

        self.horizontalLayout_5.addWidget(self.lsn_cmb_lesson_list)


        self.gridLayout.addWidget(self.frame_3, 0, 0, 1, 1)

        self.frame_6 = QFrame(self.middle_frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(497, 72))
        self.frame_6.setMaximumSize(QSize(16777215, 16777215))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lbl_lesson_id = QLabel(self.frame_6)
        self.lbl_lesson_id.setObjectName(u"lbl_lesson_id")
        self.lbl_lesson_id.setMinimumSize(QSize(151, 48))
        self.lbl_lesson_id.setMaximumSize(QSize(211, 16777215))
        font3 = QFont()
        font3.setFamilies([u"Hind Siliguri Medium"])
        font3.setPointSize(12)
        font3.setBold(False)
        self.lbl_lesson_id.setFont(font3)
        self.lbl_lesson_id.setStyleSheet(u"color: rgb(137, 218, 199);")

        self.horizontalLayout_2.addWidget(self.lbl_lesson_id)

        self.lsn_edit_student_id = QLineEdit(self.frame_6)
        self.lsn_edit_student_id.setObjectName(u"lsn_edit_student_id")
        self.lsn_edit_student_id.setEnabled(False)
        self.lsn_edit_student_id.setMinimumSize(QSize(300, 50))
        font4 = QFont()
        font4.setFamilies([u"Hind Siliguri"])
        font4.setPointSize(12)
        font4.setBold(False)
        self.lsn_edit_student_id.setFont(font4)
        self.lsn_edit_student_id.setStyleSheet(u"background-color: rgb(137, 218, 199);\n"
"border: 2px solid rgb(101, 161, 146);\n"
"padding-left: 15px;\n"
"border-radius: 10px;\n"
"color: rgb(43, 72, 101);")
        self.lsn_edit_student_id.setCursorPosition(0)

        self.horizontalLayout_2.addWidget(self.lsn_edit_student_id)


        self.gridLayout.addWidget(self.frame_6, 1, 0, 1, 1)

        self.frame_2 = QFrame(self.middle_frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(501, 74))
        self.frame_2.setMaximumSize(QSize(16777215, 16777215))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.lbl_lesson_topic = QLabel(self.frame_2)
        self.lbl_lesson_topic.setObjectName(u"lbl_lesson_topic")
        self.lbl_lesson_topic.setMinimumSize(QSize(151, 0))
        self.lbl_lesson_topic.setMaximumSize(QSize(150, 16777215))
        font5 = QFont()
        font5.setFamilies([u"Hind Siliguri Medium"])
        font5.setPointSize(13)
        font5.setBold(False)
        self.lbl_lesson_topic.setFont(font5)
        self.lbl_lesson_topic.setStyleSheet(u"color: rgb(137, 218, 199);")

        self.horizontalLayout_6.addWidget(self.lbl_lesson_topic)

        self.lsn_edit_student_name = QLineEdit(self.frame_2)
        self.lsn_edit_student_name.setObjectName(u"lsn_edit_student_name")
        self.lsn_edit_student_name.setEnabled(False)
        self.lsn_edit_student_name.setMinimumSize(QSize(300, 50))
        font6 = QFont()
        font6.setFamilies([u"Hind Siliguri Medium"])
        font6.setPointSize(11)
        self.lsn_edit_student_name.setFont(font6)
        self.lsn_edit_student_name.setStyleSheet(u"background-color: rgb(137, 218, 199);\n"
"border: 2px solid rgb(101, 161, 146);\n"
"padding-left: 15px;\n"
"border-radius: 10px;\n"
"color: rgb(43, 72, 101);")

        self.horizontalLayout_6.addWidget(self.lsn_edit_student_name)


        self.gridLayout.addWidget(self.frame_2, 2, 0, 1, 1)

        self.lsn_btn_assign_lsn_to_std = QPushButton(self.middle_frame)
        self.lsn_btn_assign_lsn_to_std.setObjectName(u"lsn_btn_assign_lsn_to_std")
        self.lsn_btn_assign_lsn_to_std.setMinimumSize(QSize(200, 50))
        font7 = QFont()
        font7.setFamilies([u"Hind Siliguri Medium"])
        font7.setPointSize(13)
        self.lsn_btn_assign_lsn_to_std.setFont(font7)
        self.lsn_btn_assign_lsn_to_std.setCursor(QCursor(Qt.PointingHandCursor))
        self.lsn_btn_assign_lsn_to_std.setStyleSheet(u"QPushButton {\n"
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
        self.lsn_btn_assign_lsn_to_std.setFlat(True)

        self.gridLayout.addWidget(self.lsn_btn_assign_lsn_to_std, 4, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 52, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 5, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 53, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 3, 0, 1, 1)


        self.gridLayout_2.addWidget(self.middle_frame, 1, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lbl_heading.setText(QCoreApplication.translate("Form", u"\u09aa\u09be\u09a0 \u09ac\u09b0\u09be\u09a6\u09cd\u09a6\u0995\u09b0\u09a3 \u0989\u0987\u09a8\u09cd\u09a1\u09cb", None))
        self.lbl_category.setText(QCoreApplication.translate("Form", u"\u09aa\u09be\u09a0\u09b8\u09ae\u09c2\u09b9", None))
        self.lsn_cmb_lesson_list.setItemText(0, QCoreApplication.translate("Form", u"\u09aa\u09be\u09a0 \u09a8\u09bf\u09b0\u09cd\u09ac\u09be\u099a\u09a8 \u0995\u09b0\u09c1\u09a8", None))

        self.lbl_lesson_id.setText(QCoreApplication.translate("Form", u"\u09b6\u09bf\u0995\u09cd\u09b7\u09be\u09b0\u09cd\u09a5\u09c0\u09b0 \u0986\u0987\u09a1\u09bf", None))
        self.lsn_edit_student_id.setPlaceholderText("")
        self.lbl_lesson_topic.setText(QCoreApplication.translate("Form", u"\u09b6\u09bf\u0995\u09cd\u09b7\u09be\u09b0\u09cd\u09a5\u09c0\u09b0 \u09a8\u09be\u09ae", None))
        self.lsn_edit_student_name.setPlaceholderText("")
        self.lsn_btn_assign_lsn_to_std.setText(QCoreApplication.translate("Form", u"\u09aa\u09be\u09a0 \u09ac\u09b0\u09be\u09a6\u09cd\u09a6 \u0995\u09b0\u09c1\u09a8", None))
#if QT_CONFIG(shortcut)
        self.lsn_btn_assign_lsn_to_std.setShortcut(QCoreApplication.translate("Form", u"Return", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

