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
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.mainframe = QFrame(self.centralwidget)
        self.mainframe.setObjectName(u"mainframe")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainframe.sizePolicy().hasHeightForWidth())
        self.mainframe.setSizePolicy(sizePolicy)
        self.mainframe.setMaximumSize(QSize(16777215, 16777215))
        self.mainframe.setStyleSheet(u"background-color: rgb(0, 43, 91)")
        self.mainframe.setFrameShape(QFrame.StyledPanel)
        self.mainframe.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.mainframe)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frm_banner_pic = QFrame(self.mainframe)
        self.frm_banner_pic.setObjectName(u"frm_banner_pic")
        self.frm_banner_pic.setMaximumSize(QSize(1200, 300))
        self.frm_banner_pic.setStyleSheet(u"border: none;")
        self.frm_banner_pic.setFrameShape(QFrame.StyledPanel)
        self.frm_banner_pic.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frm_banner_pic)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.b_picture = QLabel(self.frm_banner_pic)
        self.b_picture.setObjectName(u"b_picture")
        self.b_picture.setLayoutDirection(Qt.LeftToRight)
        self.b_picture.setStyleSheet(u"border: none;")
        self.b_picture.setFrameShape(QFrame.StyledPanel)
        self.b_picture.setPixmap(QPixmap(u"../Images/banner_logo.png"))
        self.b_picture.setScaledContents(False)
        self.b_picture.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.b_picture)


        self.gridLayout.addWidget(self.frm_banner_pic, 1, 0, 1, 1)

        self.space_frame = QFrame(self.mainframe)
        self.space_frame.setObjectName(u"space_frame")
        self.space_frame.setMaximumSize(QSize(16777215, 100))
        self.space_frame.setFrameShape(QFrame.StyledPanel)
        self.space_frame.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.space_frame, 3, 0, 1, 1)

        self.frm_btn_lbl = QFrame(self.mainframe)
        self.frm_btn_lbl.setObjectName(u"frm_btn_lbl")
        self.frm_btn_lbl.setMinimumSize(QSize(0, 50))
        self.frm_btn_lbl.setMaximumSize(QSize(16777215, 80))
        self.frm_btn_lbl.setFrameShape(QFrame.StyledPanel)
        self.frm_btn_lbl.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frm_btn_lbl)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lbl_student = QLabel(self.frm_btn_lbl)
        self.lbl_student.setObjectName(u"lbl_student")
        self.lbl_student.setMaximumSize(QSize(16777215, 60))
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(False)
        self.lbl_student.setFont(font1)
        self.lbl_student.setStyleSheet(u"color: rgb(26, 181, 219);")
        self.lbl_student.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.lbl_student)

        self.lbl_lesson = QLabel(self.frm_btn_lbl)
        self.lbl_lesson.setObjectName(u"lbl_lesson")
        self.lbl_lesson.setMaximumSize(QSize(16777215, 50))
        font2 = QFont()
        font2.setPointSize(14)
        self.lbl_lesson.setFont(font2)
        self.lbl_lesson.setStyleSheet(u"color: rgb(26, 181, 219);")
        self.lbl_lesson.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.lbl_lesson)

        self.lbl_quiz = QLabel(self.frm_btn_lbl)
        self.lbl_quiz.setObjectName(u"lbl_quiz")
        self.lbl_quiz.setMaximumSize(QSize(16777215, 50))
        self.lbl_quiz.setFont(font2)
        self.lbl_quiz.setStyleSheet(u"color: rgb(26, 181, 219);")
        self.lbl_quiz.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.lbl_quiz)

        self.lbl_progress = QLabel(self.frm_btn_lbl)
        self.lbl_progress.setObjectName(u"lbl_progress")
        self.lbl_progress.setMaximumSize(QSize(16777215, 50))
        self.lbl_progress.setFont(font2)
        self.lbl_progress.setStyleSheet(u"color: rgb(26, 181, 219);")
        self.lbl_progress.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.lbl_progress)

        self.lbl_settings = QLabel(self.frm_btn_lbl)
        self.lbl_settings.setObjectName(u"lbl_settings")
        self.lbl_settings.setMaximumSize(QSize(16777215, 50))
        self.lbl_settings.setFont(font2)
        self.lbl_settings.setStyleSheet(u"color: rgb(26, 181, 219);")
        self.lbl_settings.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.lbl_settings)


        self.gridLayout.addWidget(self.frm_btn_lbl, 5, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(10, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_2, 2, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer, 0, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 80, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_3, 6, 0, 1, 1)

        self.frm_button = QFrame(self.mainframe)
        self.frm_button.setObjectName(u"frm_button")
        self.frm_button.setMinimumSize(QSize(1100, 190))
        self.frm_button.setMaximumSize(QSize(1270, 190))
        self.frm_button.setStyleSheet(u"")
        self.frm_button.setFrameShape(QFrame.StyledPanel)
        self.frm_button.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frm_button)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, -1, 0)
        self.btn_student = QPushButton(self.frm_button)
        self.btn_student.setObjectName(u"btn_student")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_student.sizePolicy().hasHeightForWidth())
        self.btn_student.setSizePolicy(sizePolicy1)
        self.btn_student.setMinimumSize(QSize(150, 150))
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
"	background-color: qlineargradient(spread:pad, x1:0.383, y1:0.727, x2:1, y2:0, stop:0 rgba(49, 181, 148, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	border: 4px solid qlineargradient(spread:pad, x1:0.716905, y1:0.347, x2:0, y2:1, stop:0 rgba(26, 181, 219, 255), stop:1 rgba(255, 255, 255, 255)) ;\n"
"	border-radius: 15px;\n"
"	margin: 10px;\n"
"}\n"
"\n"
"QPushButton:hover:!pressed\n"
"{\n"
" 	border: 4px solid qlineargradient(spread:pad, x1:0.338, y1:0.602273, x2:1, y2:0, stop:0 rgba(26, 181, 219, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	background-color: qlineargradient(spread:pad, x1:0.606965, y1:0.409, x2:0, y2:1, stop:0 rgba(81, 181, 159, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u"../Images/student_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_student.setIcon(icon)
        self.btn_student.setIconSize(QSize(80, 70))
        self.btn_student.setFlat(False)

        self.horizontalLayout_2.addWidget(self.btn_student)

        self.btn_lesson = QPushButton(self.frm_button)
        self.btn_lesson.setObjectName(u"btn_lesson")
        sizePolicy1.setHeightForWidth(self.btn_lesson.sizePolicy().hasHeightForWidth())
        self.btn_lesson.setSizePolicy(sizePolicy1)
        self.btn_lesson.setMinimumSize(QSize(150, 150))
        self.btn_lesson.setMaximumSize(QSize(200, 200))
        self.btn_lesson.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_lesson.setStyleSheet(u"QPushButton {\n"
"	background-color: qlineargradient(spread:pad, x1:0.383, y1:0.727, x2:1, y2:0, stop:0 rgba(49, 181, 148, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	border: 4px solid qlineargradient(spread:pad, x1:0.716905, y1:0.347, x2:0, y2:1, stop:0 rgba(26, 181, 219, 255), stop:1 rgba(255, 255, 255, 255)) ;\n"
"	border-radius: 15px;\n"
"	margin: 10px;\n"
"}\n"
"\n"
"QPushButton:hover:!pressed\n"
"{\n"
" 	border: 4px solid qlineargradient(spread:pad, x1:0.338, y1:0.602273, x2:1, y2:0, stop:0 rgba(26, 181, 219, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	background-color: qlineargradient(spread:pad, x1:0.606965, y1:0.409, x2:0, y2:1, stop:0 rgba(81, 181, 159, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"../Images/lesson_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_lesson.setIcon(icon1)
        self.btn_lesson.setIconSize(QSize(70, 90))

        self.horizontalLayout_2.addWidget(self.btn_lesson)

        self.btn_quiz = QPushButton(self.frm_button)
        self.btn_quiz.setObjectName(u"btn_quiz")
        sizePolicy1.setHeightForWidth(self.btn_quiz.sizePolicy().hasHeightForWidth())
        self.btn_quiz.setSizePolicy(sizePolicy1)
        self.btn_quiz.setMinimumSize(QSize(150, 150))
        self.btn_quiz.setMaximumSize(QSize(200, 200))
        self.btn_quiz.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_quiz.setStyleSheet(u"QPushButton {\n"
"	background-color: qlineargradient(spread:pad, x1:0.383, y1:0.727, x2:1, y2:0, stop:0 rgba(49, 181, 148, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	border: 4px solid qlineargradient(spread:pad, x1:0.716905, y1:0.347, x2:0, y2:1, stop:0 rgba(26, 181, 219, 255), stop:1 rgba(255, 255, 255, 255)) ;\n"
"	border-radius: 15px;\n"
"	margin: 10px;\n"
"}\n"
"\n"
"QPushButton:hover:!pressed\n"
"{\n"
" 	border: 4px solid qlineargradient(spread:pad, x1:0.338, y1:0.602273, x2:1, y2:0, stop:0 rgba(26, 181, 219, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	background-color: qlineargradient(spread:pad, x1:0.606965, y1:0.409, x2:0, y2:1, stop:0 rgba(81, 181, 159, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u"../Images/assessment_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_quiz.setIcon(icon2)
        self.btn_quiz.setIconSize(QSize(70, 90))

        self.horizontalLayout_2.addWidget(self.btn_quiz)

        self.btn_progress = QPushButton(self.frm_button)
        self.btn_progress.setObjectName(u"btn_progress")
        sizePolicy1.setHeightForWidth(self.btn_progress.sizePolicy().hasHeightForWidth())
        self.btn_progress.setSizePolicy(sizePolicy1)
        self.btn_progress.setMinimumSize(QSize(150, 150))
        self.btn_progress.setMaximumSize(QSize(200, 200))
        self.btn_progress.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_progress.setStyleSheet(u"QPushButton {\n"
"	background-color: qlineargradient(spread:pad, x1:0.383, y1:0.727, x2:1, y2:0, stop:0 rgba(49, 181, 148, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	border: 4px solid qlineargradient(spread:pad, x1:0.716905, y1:0.347, x2:0, y2:1, stop:0 rgba(26, 181, 219, 255), stop:1 rgba(255, 255, 255, 255)) ;\n"
"	border-radius: 15px;\n"
"	margin: 10px;\n"
"}\n"
"\n"
"QPushButton:hover:!pressed\n"
"{\n"
" 	border: 4px solid qlineargradient(spread:pad, x1:0.338, y1:0.602273, x2:1, y2:0, stop:0 rgba(26, 181, 219, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	background-color: qlineargradient(spread:pad, x1:0.606965, y1:0.409, x2:0, y2:1, stop:0 rgba(81, 181, 159, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"")
        icon3 = QIcon()
        icon3.addFile(u"../Images/performance_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_progress.setIcon(icon3)
        self.btn_progress.setIconSize(QSize(150, 150))

        self.horizontalLayout_2.addWidget(self.btn_progress)

        self.btn_settings = QPushButton(self.frm_button)
        self.btn_settings.setObjectName(u"btn_settings")
        sizePolicy1.setHeightForWidth(self.btn_settings.sizePolicy().hasHeightForWidth())
        self.btn_settings.setSizePolicy(sizePolicy1)
        self.btn_settings.setMinimumSize(QSize(150, 150))
        self.btn_settings.setMaximumSize(QSize(200, 200))
        self.btn_settings.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_settings.setStyleSheet(u"QPushButton {\n"
"	background-color: qlineargradient(spread:pad, x1:0.383, y1:0.727, x2:1, y2:0, stop:0 rgba(49, 181, 148, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	border: 4px solid qlineargradient(spread:pad, x1:0.716905, y1:0.347, x2:0, y2:1, stop:0 rgba(26, 181, 219, 255), stop:1 rgba(255, 255, 255, 255)) ;\n"
"	border-radius: 15px;\n"
"	margin: 10px;\n"
"}\n"
"\n"
"QPushButton:hover:!pressed\n"
"{\n"
" 	border: 4px solid qlineargradient(spread:pad, x1:0.338, y1:0.602273, x2:1, y2:0, stop:0 rgba(26, 181, 219, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	background-color: qlineargradient(spread:pad, x1:0.606965, y1:0.409, x2:0, y2:1, stop:0 rgba(81, 181, 159, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"")
        icon4 = QIcon()
        icon4.addFile(u"../Images/settings_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_settings.setIcon(icon4)
        self.btn_settings.setIconSize(QSize(70, 70))

        self.horizontalLayout_2.addWidget(self.btn_settings)


        self.gridLayout.addWidget(self.frm_button, 4, 0, 1, 1)


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

