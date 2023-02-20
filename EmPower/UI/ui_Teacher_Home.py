# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Teacher_Home.ui'
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
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 800)
        font = QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.mainframe = QFrame(self.centralwidget)
        self.mainframe.setObjectName(u"mainframe")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainframe.sizePolicy().hasHeightForWidth())
        self.mainframe.setSizePolicy(sizePolicy)
        self.mainframe.setMaximumSize(QSize(16777215, 16777215))
        self.mainframe.setStyleSheet(u"background-color: #FEE8E9;")
        self.mainframe.setFrameShape(QFrame.StyledPanel)
        self.mainframe.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.mainframe)
        self.gridLayout.setObjectName(u"gridLayout")
        self.banner_pic_frame = QFrame(self.mainframe)
        self.banner_pic_frame.setObjectName(u"banner_pic_frame")
        self.banner_pic_frame.setMaximumSize(QSize(1200, 300))
        self.banner_pic_frame.setStyleSheet(u"border: none;")
        self.banner_pic_frame.setFrameShape(QFrame.StyledPanel)
        self.banner_pic_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.banner_pic_frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.b_picture = QLabel(self.banner_pic_frame)
        self.b_picture.setObjectName(u"b_picture")
        self.b_picture.setLayoutDirection(Qt.LeftToRight)
        self.b_picture.setStyleSheet(u"border: none;")
        self.b_picture.setFrameShape(QFrame.StyledPanel)
        self.b_picture.setPixmap(QPixmap(u"final_logo.png"))
        self.b_picture.setScaledContents(False)
        self.b_picture.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.b_picture)


        self.gridLayout.addWidget(self.banner_pic_frame, 1, 0, 1, 1)

        self.space_frame = QFrame(self.mainframe)
        self.space_frame.setObjectName(u"space_frame")
        self.space_frame.setMaximumSize(QSize(16777215, 100))
        self.space_frame.setFrameShape(QFrame.StyledPanel)
        self.space_frame.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.space_frame, 3, 0, 1, 1)

        self.bnt_lbl_frame = QFrame(self.mainframe)
        self.bnt_lbl_frame.setObjectName(u"bnt_lbl_frame")
        self.bnt_lbl_frame.setMinimumSize(QSize(0, 50))
        self.bnt_lbl_frame.setMaximumSize(QSize(16777215, 80))
        self.bnt_lbl_frame.setFrameShape(QFrame.StyledPanel)
        self.bnt_lbl_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.bnt_lbl_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lbl_student = QLabel(self.bnt_lbl_frame)
        self.lbl_student.setObjectName(u"lbl_student")
        self.lbl_student.setMaximumSize(QSize(16777215, 60))
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(False)
        self.lbl_student.setFont(font1)
        self.lbl_student.setStyleSheet(u"color: rgb(129, 102, 106);")
        self.lbl_student.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.lbl_student)

        self.lbl_lesson = QLabel(self.bnt_lbl_frame)
        self.lbl_lesson.setObjectName(u"lbl_lesson")
        self.lbl_lesson.setMaximumSize(QSize(16777215, 50))
        font2 = QFont()
        font2.setPointSize(16)
        self.lbl_lesson.setFont(font2)
        self.lbl_lesson.setStyleSheet(u"color: rgb(129, 102, 106);")
        self.lbl_lesson.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.lbl_lesson)

        self.lbl_quiz = QLabel(self.bnt_lbl_frame)
        self.lbl_quiz.setObjectName(u"lbl_quiz")
        self.lbl_quiz.setMaximumSize(QSize(16777215, 50))
        self.lbl_quiz.setFont(font2)
        self.lbl_quiz.setStyleSheet(u"color: rgb(129, 102, 106);")
        self.lbl_quiz.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.lbl_quiz)

        self.lbl_progress = QLabel(self.bnt_lbl_frame)
        self.lbl_progress.setObjectName(u"lbl_progress")
        self.lbl_progress.setMaximumSize(QSize(16777215, 50))
        self.lbl_progress.setFont(font2)
        self.lbl_progress.setStyleSheet(u"color: rgb(129, 102, 106);")
        self.lbl_progress.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.lbl_progress)

        self.lbl_settings = QLabel(self.bnt_lbl_frame)
        self.lbl_settings.setObjectName(u"lbl_settings")
        self.lbl_settings.setMaximumSize(QSize(16777215, 50))
        self.lbl_settings.setFont(font2)
        self.lbl_settings.setStyleSheet(u"color: rgb(129, 102, 106);")
        self.lbl_settings.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.lbl_settings)


        self.gridLayout.addWidget(self.bnt_lbl_frame, 5, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(10, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_2, 2, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer, 0, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 80, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_3, 6, 0, 1, 1)

        self.btn_frame = QFrame(self.mainframe)
        self.btn_frame.setObjectName(u"btn_frame")
        self.btn_frame.setMinimumSize(QSize(0, 190))
        self.btn_frame.setMaximumSize(QSize(1270, 190))
        self.btn_frame.setStyleSheet(u"")
        self.btn_frame.setFrameShape(QFrame.StyledPanel)
        self.btn_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.btn_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, -1, 0)
        self.btn_student = QPushButton(self.btn_frame)
        self.btn_student.setObjectName(u"btn_student")
        self.btn_student.setMaximumSize(QSize(200, 200))
        font3 = QFont()
        font3.setPointSize(9)
        font3.setBold(False)
        font3.setStyleStrategy(QFont.PreferDefault)
        self.btn_student.setFont(font3)
        self.btn_student.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_student.setMouseTracking(True)
        self.btn_student.setAcceptDrops(True)
        self.btn_student.setStyleSheet(u"QPushButton {\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(227, 208, 209, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	border: 5px solid rgb(238, 218, 219);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover:!pressed\n"
"{\n"
" 	border: 5px solid  rgb(148, 122, 125);\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:0.318, x2:0, y2:1, stop:0.313433 rgba(222, 204, 205, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u"icons8_student_male_32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_student.setIcon(icon)
        self.btn_student.setIconSize(QSize(500, 500))
        self.btn_student.setFlat(False)

        self.horizontalLayout_2.addWidget(self.btn_student)

        self.btn_lesson = QPushButton(self.btn_frame)
        self.btn_lesson.setObjectName(u"btn_lesson")
        self.btn_lesson.setMaximumSize(QSize(200, 200))
        self.btn_lesson.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_lesson.setStyleSheet(u"QPushButton {\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(227, 208, 209, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	border: 5px solid rgb(238, 218, 219);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover:!pressed\n"
"{\n"
" 	border: 5px solid  rgb(148, 122, 125);\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:0.318, x2:0, y2:1, stop:0.313433 rgba(222, 204, 205, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"lesson_64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_lesson.setIcon(icon1)
        self.btn_lesson.setIconSize(QSize(150, 150))

        self.horizontalLayout_2.addWidget(self.btn_lesson)

        self.btn_quiz = QPushButton(self.btn_frame)
        self.btn_quiz.setObjectName(u"btn_quiz")
        self.btn_quiz.setMaximumSize(QSize(200, 200))
        self.btn_quiz.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_quiz.setStyleSheet(u"QPushButton {\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(227, 208, 209, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	border: 5px solid rgb(238, 218, 219);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover:!pressed\n"
"{\n"
" 	border: 5px solid  rgb(148, 122, 125);\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:0.318, x2:0, y2:1, stop:0.313433 rgba(222, 204, 205, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"list_64px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_quiz.setIcon(icon2)
        self.btn_quiz.setIconSize(QSize(150, 150))

        self.horizontalLayout_2.addWidget(self.btn_quiz)

        self.btn_progress = QPushButton(self.btn_frame)
        self.btn_progress.setObjectName(u"btn_progress")
        self.btn_progress.setMaximumSize(QSize(200, 200))
        self.btn_progress.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_progress.setStyleSheet(u"QPushButton {\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(227, 208, 209, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	border: 5px solid rgb(238, 218, 219);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover:!pressed\n"
"{\n"
" 	border: 5px solid  rgb(148, 122, 125);\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:0.318, x2:0, y2:1, stop:0.313433 rgba(222, 204, 205, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"presentation_64px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_progress.setIcon(icon3)
        self.btn_progress.setIconSize(QSize(150, 150))

        self.horizontalLayout_2.addWidget(self.btn_progress)

        self.btn_settings = QPushButton(self.btn_frame)
        self.btn_settings.setObjectName(u"btn_settings")
        self.btn_settings.setMaximumSize(QSize(200, 200))
        self.btn_settings.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_settings.setStyleSheet(u"QPushButton {\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(227, 208, 209, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	border: 5px solid rgb(238, 218, 219);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover:!pressed\n"
"{\n"
" 	border: 5px solid  rgb(148, 122, 125);\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:0.318, x2:0, y2:1, stop:0.313433 rgba(222, 204, 205, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u"settings_64px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_settings.setIcon(icon4)
        self.btn_settings.setIconSize(QSize(150, 150))

        self.horizontalLayout_2.addWidget(self.btn_settings)


        self.gridLayout.addWidget(self.btn_frame, 4, 0, 1, 1)


        self.gridLayout_2.addWidget(self.mainframe, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.b_picture.setText("")
        self.lbl_student.setText(QCoreApplication.translate("MainWindow", u"\u09b6\u09bf\u0995\u09cd\u09b7\u09be\u09b0\u09cd\u09a5\u09c0 \u09a8\u09bf\u09ac\u09a8\u09cd\u09a7\u09a8", None))
        self.lbl_lesson.setText(QCoreApplication.translate("MainWindow", u"\u09aa\u09be\u09a0\u09cd\u09af\u09b8\u09c2\u099a\u09c0", None))
        self.lbl_quiz.setText(QCoreApplication.translate("MainWindow", u"\u09aa\u09be\u09a0 \u09ae\u09c2\u09b2\u09cd\u09af\u09be\u09df\u09a8", None))
        self.lbl_progress.setText(QCoreApplication.translate("MainWindow", u"\u09b6\u09bf\u0995\u09cd\u09b7\u09be\u09b0\u09cd\u09a5\u09c0\u09b0 \u09aa\u09be\u09b0\u09ab\u09b0\u09ae\u09cd\u09af\u09be\u09a8\u09cd\u09b8", None))
        self.lbl_settings.setText(QCoreApplication.translate("MainWindow", u"\u09b8\u09c7\u099f\u09bf\u0982\u09b8", None))
        self.btn_student.setText("")
        self.btn_lesson.setText("")
        self.btn_quiz.setText("")
        self.btn_progress.setText("")
        self.btn_settings.setText("")
    # retranslateUi

