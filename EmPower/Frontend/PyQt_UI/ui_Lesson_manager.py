# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Lesson_manager.ui'
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
    QHBoxLayout, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1278, 871)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1200, 870))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.top_frame = QFrame(self.centralwidget)
        self.top_frame.setObjectName(u"top_frame")
        self.top_frame.setMinimumSize(QSize(1180, 80))
        self.top_frame.setMaximumSize(QSize(16777215, 80))
        self.top_frame.setStyleSheet(u"background-color: #2B4865;\n"
"border-top-left-radius: 20px;\n"
"border-top-right-radius: 20px;")
        self.top_frame.setFrameShape(QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.top_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_back_to_home = QPushButton(self.top_frame)
        self.btn_back_to_home.setObjectName(u"btn_back_to_home")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_back_to_home.sizePolicy().hasHeightForWidth())
        self.btn_back_to_home.setSizePolicy(sizePolicy2)
        self.btn_back_to_home.setMinimumSize(QSize(0, 60))
        self.btn_back_to_home.setMaximumSize(QSize(60, 60))
        self.btn_back_to_home.setBaseSize(QSize(0, 4))
        font = QFont()
        font.setPointSize(11)
        self.btn_back_to_home.setFont(font)
        self.btn_back_to_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_back_to_home.setMouseTracking(True)
        self.btn_back_to_home.setStyleSheet(u"QPushButton {\n"
"	background-color: #2B4865 #256D85;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover:!pressed\n"
"{\n"
"	background-color:  #256D85;\n"
"	border-radius: 30px;\n"
"}")
        icon = QIcon()
        icon.addFile(u"../Images/back_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_back_to_home.setIcon(icon)
        self.btn_back_to_home.setIconSize(QSize(200, 200))
        self.btn_back_to_home.setAutoDefault(False)
        self.btn_back_to_home.setFlat(False)

        self.horizontalLayout.addWidget(self.btn_back_to_home)

        self.lbl_headline = QLabel(self.top_frame)
        self.lbl_headline.setObjectName(u"lbl_headline")
        font1 = QFont()
        font1.setFamilies([u"Hind Siliguri Medium"])
        font1.setPointSize(27)
        self.lbl_headline.setFont(font1)
        self.lbl_headline.setStyleSheet(u"color: #8FE3CF")
        self.lbl_headline.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.lbl_headline)


        self.verticalLayout.addWidget(self.top_frame)

        self.mid_frame = QFrame(self.centralwidget)
        self.mid_frame.setObjectName(u"mid_frame")
        self.mid_frame.setMinimumSize(QSize(1180, 610))
        self.mid_frame.setStyleSheet(u"\n"
"background-color:rgb(36, 105, 127);")
        self.mid_frame.setFrameShape(QFrame.StyledPanel)
        self.mid_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.mid_frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.bottom_top_frame = QFrame(self.mid_frame)
        self.bottom_top_frame.setObjectName(u"bottom_top_frame")
        self.bottom_top_frame.setMinimumSize(QSize(0, 60))
        self.bottom_top_frame.setMaximumSize(QSize(16777215, 60))
        self.bottom_top_frame.setStyleSheet(u"background-color: rgb(29, 88, 105);\n"
"color: rgb(137, 218, 199);\n"
"border-radius: 20px;")
        self.bottom_top_frame.setFrameShape(QFrame.StyledPanel)
        self.bottom_top_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.bottom_top_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_3 = QSpacerItem(141, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.lbl_category = QLabel(self.bottom_top_frame)
        self.lbl_category.setObjectName(u"lbl_category")
        font2 = QFont()
        font2.setPointSize(16)
        self.lbl_category.setFont(font2)
        self.lbl_category.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.lbl_category)

        self.cmb_category = QComboBox(self.bottom_top_frame)
        self.cmb_category.addItem("")
        self.cmb_category.setObjectName(u"cmb_category")
        self.cmb_category.setMinimumSize(QSize(280, 30))
        self.cmb_category.setStyleSheet(u"background-color: rgb(137, 218, 199);\n"
"border-radius: 12px;\n"
"color: rgb(0, 43, 91);")

        self.horizontalLayout_2.addWidget(self.cmb_category)

        self.horizontalSpacer_6 = QSpacerItem(143, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_6)

        self.lbl_lessons = QLabel(self.bottom_top_frame)
        self.lbl_lessons.setObjectName(u"lbl_lessons")
        self.lbl_lessons.setFont(font2)
        self.lbl_lessons.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.lbl_lessons)

        self.cmb_lessons = QComboBox(self.bottom_top_frame)
        self.cmb_lessons.setObjectName(u"cmb_lessons")
        self.cmb_lessons.setMinimumSize(QSize(280, 30))
        self.cmb_lessons.setStyleSheet(u"background-color: rgb(137, 218, 199);\n"
"border-radius: 12px;\n"
"color: rgb(0, 43, 91);")

        self.horizontalLayout_2.addWidget(self.cmb_lessons)

        self.horizontalSpacer_5 = QSpacerItem(141, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_5)


        self.gridLayout.addWidget(self.bottom_top_frame, 0, 0, 1, 3)

        self.left_btn_frame = QFrame(self.mid_frame)
        self.left_btn_frame.setObjectName(u"left_btn_frame")
        self.left_btn_frame.setMinimumSize(QSize(60, 629))
        self.left_btn_frame.setMaximumSize(QSize(60, 16777215))
        self.left_btn_frame.setStyleSheet(u"")
        self.left_btn_frame.setFrameShape(QFrame.StyledPanel)
        self.left_btn_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.left_btn_frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btn_left = QPushButton(self.left_btn_frame)
        self.btn_left.setObjectName(u"btn_left")
        self.btn_left.setMinimumSize(QSize(60, 629))
        self.btn_left.setMaximumSize(QSize(60, 16777215))
        self.btn_left.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_left.setStyleSheet(u"QPushButton {background-color: rgb(30, 90, 108); border-radius: 20px;}\n"
"\n"
"QPushButton::hover  {\n"
"	background-color: rgb(20, 62, 74);\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"../Images/left.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_left.setIcon(icon1)
        self.btn_left.setIconSize(QSize(100, 100))

        self.verticalLayout_3.addWidget(self.btn_left)


        self.gridLayout.addWidget(self.left_btn_frame, 1, 0, 1, 1)

        self.middle_content_frame = QFrame(self.mid_frame)
        self.middle_content_frame.setObjectName(u"middle_content_frame")
        self.middle_content_frame.setStyleSheet(u"background-color: rgb(30, 90, 108);\n"
"border-radius: 20px;")
        self.middle_content_frame.setFrameShape(QFrame.StyledPanel)
        self.middle_content_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.middle_content_frame)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.lbl_image = QLabel(self.middle_content_frame)
        self.lbl_image.setObjectName(u"lbl_image")
        self.lbl_image.setMinimumSize(QSize(600, 571))
        font3 = QFont()
        font3.setPointSize(30)
        self.lbl_image.setFont(font3)
        self.lbl_image.setStyleSheet(u"border: 3px dotted  rgb(137, 218, 199);\n"
"color: rgb(137, 218, 199);")
        self.lbl_image.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.lbl_image)

        self.lbl_image_text = QLabel(self.middle_content_frame)
        self.lbl_image_text.setObjectName(u"lbl_image_text")
        self.lbl_image_text.setMinimumSize(QSize(390, 300))
        self.lbl_image_text.setMaximumSize(QSize(500, 16777215))
        self.lbl_image_text.setFont(font3)
        self.lbl_image_text.setStyleSheet(u"border: 3px dotted  rgb(137, 218, 199);\n"
"color: rgb(137, 218, 199);")
        self.lbl_image_text.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.lbl_image_text)


        self.gridLayout.addWidget(self.middle_content_frame, 1, 1, 1, 1)

        self.right_btn_frame = QFrame(self.mid_frame)
        self.right_btn_frame.setObjectName(u"right_btn_frame")
        self.right_btn_frame.setMinimumSize(QSize(60, 629))
        self.right_btn_frame.setMaximumSize(QSize(60, 16777215))
        self.right_btn_frame.setStyleSheet(u"")
        self.right_btn_frame.setFrameShape(QFrame.StyledPanel)
        self.right_btn_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.right_btn_frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btn_right = QPushButton(self.right_btn_frame)
        self.btn_right.setObjectName(u"btn_right")
        self.btn_right.setMinimumSize(QSize(60, 629))
        self.btn_right.setMaximumSize(QSize(60, 16777215))
        self.btn_right.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_right.setStyleSheet(u"QPushButton {background-color: rgb(30, 90, 108); border-radius: 20px;}\n"
"\n"
"QPushButton::hover  {\n"
"	background-color: rgb(20, 62, 74);\n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u"../Images/right.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_right.setIcon(icon2)
        self.btn_right.setIconSize(QSize(100, 100))

        self.verticalLayout_4.addWidget(self.btn_right)


        self.gridLayout.addWidget(self.right_btn_frame, 1, 2, 1, 1)


        self.verticalLayout.addWidget(self.mid_frame)

        self.bottom_frame = QFrame(self.centralwidget)
        self.bottom_frame.setObjectName(u"bottom_frame")
        self.bottom_frame.setMinimumSize(QSize(1180, 70))
        self.bottom_frame.setMaximumSize(QSize(16777215, 70))
        self.bottom_frame.setStyleSheet(u"background-color: rgb(42, 70, 98);\n"
"border-bottom-left-radius: 20px;\n"
"border-bottom-right-radius: 20px;")
        self.bottom_frame.setFrameShape(QFrame.StyledPanel)
        self.bottom_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.bottom_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_4 = QSpacerItem(38, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.btn_add_new_lessons = QPushButton(self.bottom_frame)
        self.btn_add_new_lessons.setObjectName(u"btn_add_new_lessons")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(230)
        sizePolicy3.setVerticalStretch(40)
        sizePolicy3.setHeightForWidth(self.btn_add_new_lessons.sizePolicy().hasHeightForWidth())
        self.btn_add_new_lessons.setSizePolicy(sizePolicy3)
        self.btn_add_new_lessons.setMinimumSize(QSize(250, 40))
        font4 = QFont()
        font4.setFamilies([u"Hind Siliguri Medium"])
        font4.setPointSize(12)
        font4.setBold(False)
        self.btn_add_new_lessons.setFont(font4)
        self.btn_add_new_lessons.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_add_new_lessons.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(160, 253, 230);\n"
"color:  #256D85 ;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	\n"
"	background-color: rgb(143, 227, 207);\n"
"	color: #2B4865;\n"
"\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"../Images/add_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_add_new_lessons.setIcon(icon3)

        self.horizontalLayout_3.addWidget(self.btn_add_new_lessons)

        self.horizontalSpacer = QSpacerItem(78, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.btn_update_lessons = QPushButton(self.bottom_frame)
        self.btn_update_lessons.setObjectName(u"btn_update_lessons")
        sizePolicy3.setHeightForWidth(self.btn_update_lessons.sizePolicy().hasHeightForWidth())
        self.btn_update_lessons.setSizePolicy(sizePolicy3)
        self.btn_update_lessons.setMinimumSize(QSize(250, 40))
        self.btn_update_lessons.setFont(font4)
        self.btn_update_lessons.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_update_lessons.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(160, 253, 230);\n"
"color:  #256D85 ;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	\n"
"	background-color: rgb(143, 227, 207);\n"
"	color: #2B4865;\n"
"\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u"../Images/edit_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_update_lessons.setIcon(icon4)

        self.horizontalLayout_3.addWidget(self.btn_update_lessons)

        self.horizontalSpacer_2 = QSpacerItem(38, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addWidget(self.bottom_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.btn_back_to_home.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_back_to_home.setText("")
        self.lbl_headline.setText(QCoreApplication.translate("MainWindow", u"\u09aa\u09be\u09a0\u09b8\u09c2\u099a\u09bf", None))
        self.lbl_category.setText(QCoreApplication.translate("MainWindow", u"\u0995\u09cd\u09af\u09be\u099f\u09be\u0997\u09b0\u09bf", None))
        self.cmb_category.setItemText(0, "")

        self.lbl_lessons.setText(QCoreApplication.translate("MainWindow", u"\u09aa\u09be\u09a0\u09b8\u09ae\u09c2\u09b9", None))
        self.btn_left.setText("")
        self.lbl_image.setText(QCoreApplication.translate("MainWindow", u"\u099b\u09ac\u09bf", None))
        self.lbl_image_text.setText(QCoreApplication.translate("MainWindow", u"\u09aa\u09b0\u09bf\u099a\u09df", None))
        self.btn_right.setText("")
        self.btn_add_new_lessons.setText(QCoreApplication.translate("MainWindow", u"\u09a8\u09a4\u09c1\u09a8 \u09aa\u09be\u09a0 \u09af\u09c1\u0995\u09cd\u09a4 \u0995\u09b0\u09c1\u09a8", None))
        self.btn_update_lessons.setText(QCoreApplication.translate("MainWindow", u"\u09aa\u09be\u09a0 \u0986\u09aa\u09a1\u09c7\u099f \u0995\u09b0\u09c1\u09a8", None))
    # retranslateUi

