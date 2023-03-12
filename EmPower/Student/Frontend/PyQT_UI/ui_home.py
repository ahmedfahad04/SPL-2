# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'home.ui'
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
    QSpacerItem, QStackedWidget, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1322, 923)
        MainWindow.setMinimumSize(QSize(1322, 923))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(1300, 900))
        self.stackedWidget.setStyleSheet(u"background-color: #F4F1DE;")
        self.upload_lesson_page = QWidget()
        self.upload_lesson_page.setObjectName(u"upload_lesson_page")
        self.gridLayout_2 = QGridLayout(self.upload_lesson_page)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.top_frame = QFrame(self.upload_lesson_page)
        self.top_frame.setObjectName(u"top_frame")
        self.top_frame.setMinimumSize(QSize(1280, 95))
        self.top_frame.setMaximumSize(QSize(16777215, 80))
        self.top_frame.setStyleSheet(u"background-color: #E07A5F;\n"
"color: #3D405B; ")
        self.top_frame.setFrameShape(QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.top_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btn_back_to_home = QPushButton(self.top_frame)
        self.btn_back_to_home.setObjectName(u"btn_back_to_home")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_back_to_home.sizePolicy().hasHeightForWidth())
        self.btn_back_to_home.setSizePolicy(sizePolicy)
        self.btn_back_to_home.setMinimumSize(QSize(0, 60))
        self.btn_back_to_home.setMaximumSize(QSize(60, 60))
        self.btn_back_to_home.setBaseSize(QSize(0, 4))
        font = QFont()
        font.setPointSize(11)
        self.btn_back_to_home.setFont(font)
        self.btn_back_to_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_back_to_home.setMouseTracking(True)
        self.btn_back_to_home.setStyleSheet(u"QPushButton {\n"
"	background-color: ;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover:!pressed\n"
"{\n"
"	background-color: #F4F1DE;\n"
"	border-radius: 30px;\n"
"}")
        icon = QIcon()
        icon.addFile(u"../Images/back.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_back_to_home.setIcon(icon)
        self.btn_back_to_home.setIconSize(QSize(200, 200))
        self.btn_back_to_home.setAutoDefault(False)
        self.btn_back_to_home.setFlat(False)

        self.horizontalLayout_3.addWidget(self.btn_back_to_home)

        self.lbl_headline = QLabel(self.top_frame)
        self.lbl_headline.setObjectName(u"lbl_headline")
        font1 = QFont()
        font1.setFamilies([u"Kalpurush"])
        font1.setPointSize(30)
        self.lbl_headline.setFont(font1)
        self.lbl_headline.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"padding-left: 5px;")
        self.lbl_headline.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.lbl_headline)


        self.gridLayout_2.addWidget(self.top_frame, 0, 0, 1, 1)

        self.bottom_frame = QFrame(self.upload_lesson_page)
        self.bottom_frame.setObjectName(u"bottom_frame")
        self.bottom_frame.setMinimumSize(QSize(1280, 700))
        self.bottom_frame.setStyleSheet(u"border: 2px solid rgb(224, 122, 95);")
        self.bottom_frame.setFrameShape(QFrame.StyledPanel)
        self.bottom_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.bottom_frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer = QSpacerItem(20, 138, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer, 0, 3, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(407, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 1, 0, 1, 2)

        self.btn_select_folder = QPushButton(self.bottom_frame)
        self.btn_select_folder.setObjectName(u"btn_select_folder")
        self.btn_select_folder.setMinimumSize(QSize(450, 80))
        self.btn_select_folder.setMaximumSize(QSize(350, 350))
        font2 = QFont()
        font2.setFamilies([u"Kalpurush"])
        font2.setPointSize(20)
        self.btn_select_folder.setFont(font2)
        self.btn_select_folder.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_select_folder.setMouseTracking(False)
        self.btn_select_folder.setStyleSheet(u"QPushButton {\n"
"border: 5px solid #E07A5F;\n"
"border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover:!pressed {\n"
"background-color: #3D405B;\n"
"color: #F4F1DE;\n"
"}")
        self.btn_select_folder.setIconSize(QSize(400, 400))

        self.gridLayout.addWidget(self.btn_select_folder, 1, 2, 1, 3)

        self.horizontalSpacer_4 = QSpacerItem(378, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 1, 5, 1, 2)

        self.verticalSpacer_3 = QSpacerItem(20, 25, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 2, 3, 1, 1)

        self.horizontalSpacer = QSpacerItem(297, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 3, 0, 1, 1)

        self.edit_lesson_list = QTextEdit(self.bottom_frame)
        self.edit_lesson_list.setObjectName(u"edit_lesson_list")
        self.edit_lesson_list.setMinimumSize(QSize(650, 220))
        font3 = QFont()
        font3.setFamilies([u"Kalpurush"])
        font3.setPointSize(18)
        font3.setBold(False)
        font3.setItalic(False)
        self.edit_lesson_list.setFont(font3)
        self.edit_lesson_list.setStyleSheet(u"border: 2px solid rgb(224, 122, 95);\n"
"padding-left: 10px;")

        self.gridLayout.addWidget(self.edit_lesson_list, 3, 1, 1, 5)

        self.horizontalSpacer_2 = QSpacerItem(297, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 3, 6, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 138, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_4, 4, 3, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(507, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_6, 5, 0, 1, 3)

        self.bnt_start_lesson = QPushButton(self.bottom_frame)
        self.bnt_start_lesson.setObjectName(u"bnt_start_lesson")
        self.bnt_start_lesson.setEnabled(False)
        self.bnt_start_lesson.setMinimumSize(QSize(250, 60))
        self.bnt_start_lesson.setMaximumSize(QSize(250, 350))
        self.bnt_start_lesson.setFont(font2)
        self.bnt_start_lesson.setCursor(QCursor(Qt.PointingHandCursor))
        self.bnt_start_lesson.setMouseTracking(False)
        self.bnt_start_lesson.setStyleSheet(u"QPushButton {\n"
"border: 3px solid rgb(61, 64, 91);\n"
"border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover:!pressed {\n"
"background-color: rgb(224, 122, 95);\n"
"color: #F4F1DE;\n"
"}")
        self.bnt_start_lesson.setIconSize(QSize(400, 400))

        self.gridLayout.addWidget(self.bnt_start_lesson, 5, 3, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(497, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_5, 5, 4, 1, 3)

        self.verticalSpacer_2 = QSpacerItem(20, 58, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_2, 6, 3, 1, 1)


        self.gridLayout_2.addWidget(self.bottom_frame, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.upload_lesson_page)
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.verticalLayout_3 = QVBoxLayout(self.home_page)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.top_frame_3 = QFrame(self.home_page)
        self.top_frame_3.setObjectName(u"top_frame_3")
        self.top_frame_3.setMinimumSize(QSize(1300, 650))
        self.top_frame_3.setStyleSheet(u"")
        self.top_frame_3.setFrameShape(QFrame.StyledPanel)
        self.top_frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.top_frame_3)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, 0, 0)
        self.btn_lesson = QPushButton(self.top_frame_3)
        self.btn_lesson.setObjectName(u"btn_lesson")
        self.btn_lesson.setMaximumSize(QSize(350, 350))
        self.btn_lesson.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_lesson.setStyleSheet(u"QPushButton {\n"
"border: 5px solid #E07A5F;\n"
"border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover:!pressed {\n"
"background-color: #3D405B;\n"
"color: #F4F1DE;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: #F4F1DE;\n"
"color: #E07A5F;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"../Images/lessons_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_lesson.setIcon(icon1)
        self.btn_lesson.setIconSize(QSize(400, 400))

        self.horizontalLayout.addWidget(self.btn_lesson)

        self.btn_evaluation = QPushButton(self.top_frame_3)
        self.btn_evaluation.setObjectName(u"btn_evaluation")
        self.btn_evaluation.setMaximumSize(QSize(350, 350))
        self.btn_evaluation.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_evaluation.setMouseTracking(False)
        self.btn_evaluation.setStyleSheet(u"QPushButton {\n"
"border: 5px solid #E07A5F;\n"
"border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover:!pressed {\n"
"background-color: #3D405B;\n"
"color: #F4F1DE;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"../Images/evaluation_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_evaluation.setIcon(icon2)
        self.btn_evaluation.setIconSize(QSize(400, 400))

        self.horizontalLayout.addWidget(self.btn_evaluation)


        self.verticalLayout_3.addWidget(self.top_frame_3)

        self.bottom_frame_3 = QFrame(self.home_page)
        self.bottom_frame_3.setObjectName(u"bottom_frame_3")
        self.bottom_frame_3.setMinimumSize(QSize(1301, 151))
        self.bottom_frame_3.setFrameShape(QFrame.StyledPanel)
        self.bottom_frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.bottom_frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.bottom_frame_3)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(1300, 150))
        self.label.setPixmap(QPixmap(u"../Images/banner_icon.png"))
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout_3.addWidget(self.bottom_frame_3)

        self.stackedWidget.addWidget(self.home_page)
        self.lesson_page = QWidget()
        self.lesson_page.setObjectName(u"lesson_page")
        self.verticalLayout = QVBoxLayout(self.lesson_page)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.top_frame_2 = QFrame(self.lesson_page)
        self.top_frame_2.setObjectName(u"top_frame_2")
        self.top_frame_2.setMinimumSize(QSize(1280, 95))
        self.top_frame_2.setMaximumSize(QSize(16777215, 80))
        self.top_frame_2.setStyleSheet(u"background-color: #E07A5F;\n"
"color: #3D405B; ")
        self.top_frame_2.setFrameShape(QFrame.StyledPanel)
        self.top_frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.top_frame_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.btn_back_to_home_2 = QPushButton(self.top_frame_2)
        self.btn_back_to_home_2.setObjectName(u"btn_back_to_home_2")
        sizePolicy.setHeightForWidth(self.btn_back_to_home_2.sizePolicy().hasHeightForWidth())
        self.btn_back_to_home_2.setSizePolicy(sizePolicy)
        self.btn_back_to_home_2.setMinimumSize(QSize(0, 60))
        self.btn_back_to_home_2.setMaximumSize(QSize(60, 60))
        self.btn_back_to_home_2.setBaseSize(QSize(0, 4))
        self.btn_back_to_home_2.setFont(font)
        self.btn_back_to_home_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_back_to_home_2.setMouseTracking(True)
        self.btn_back_to_home_2.setStyleSheet(u"QPushButton {\n"
"	background-color: ;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover:!pressed\n"
"{\n"
"	background-color: #F4F1DE;\n"
"	border-radius: 30px;\n"
"}")
        self.btn_back_to_home_2.setIcon(icon)
        self.btn_back_to_home_2.setIconSize(QSize(250, 250))
        self.btn_back_to_home_2.setAutoDefault(False)
        self.btn_back_to_home_2.setFlat(False)

        self.horizontalLayout_4.addWidget(self.btn_back_to_home_2)

        self.lbl_lesson_headline = QLabel(self.top_frame_2)
        self.lbl_lesson_headline.setObjectName(u"lbl_lesson_headline")
        font4 = QFont()
        font4.setFamilies([u"Kalpurush"])
        font4.setPointSize(30)
        font4.setBold(False)
        font4.setItalic(False)
        self.lbl_lesson_headline.setFont(font4)
        self.lbl_lesson_headline.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"padding-left: 5px;\n"
"font: 30pt \"Kalpurush\";")
        self.lbl_lesson_headline.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.lbl_lesson_headline)


        self.verticalLayout.addWidget(self.top_frame_2)

        self.bottom_frame_2 = QFrame(self.lesson_page)
        self.bottom_frame_2.setObjectName(u"bottom_frame_2")
        self.bottom_frame_2.setStyleSheet(u"background-color: rgb(244, 241, 222);\n"
"border: none;")
        self.bottom_frame_2.setFrameShape(QFrame.StyledPanel)
        self.bottom_frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.bottom_frame_2)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.btn_prev_lesson = QPushButton(self.bottom_frame_2)
        self.btn_prev_lesson.setObjectName(u"btn_prev_lesson")
        self.btn_prev_lesson.setMinimumSize(QSize(70, 777))
        self.btn_prev_lesson.setMaximumSize(QSize(60, 16777215))
        self.btn_prev_lesson.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_prev_lesson.setStyleSheet(u"QPushButton {\n"
"border: 3px solid #E07A5F;\n"
"border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover:!pressed {\n"
"background-color: #3D405B;\n"
"color: #F4F1DE;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"../Images/backward.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_prev_lesson.setIcon(icon3)
        self.btn_prev_lesson.setIconSize(QSize(150, 150))

        self.horizontalLayout_7.addWidget(self.btn_prev_lesson)

        self.lbl_image = QLabel(self.bottom_frame_2)
        self.lbl_image.setObjectName(u"lbl_image")
        self.lbl_image.setMinimumSize(QSize(800, 777))
        self.lbl_image.setMaximumSize(QSize(16777215, 16777215))
        font5 = QFont()
        font5.setPointSize(30)
        self.lbl_image.setFont(font5)
        self.lbl_image.setStyleSheet(u"border: 3px dashed rgb(222, 219, 202);\n"
"color:  rgb(61, 64, 91);")
        self.lbl_image.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.lbl_image)

        self.lbl_image_text = QLabel(self.bottom_frame_2)
        self.lbl_image_text.setObjectName(u"lbl_image_text")
        self.lbl_image_text.setMinimumSize(QSize(300, 777))
        self.lbl_image_text.setMaximumSize(QSize(700, 16777215))
        font6 = QFont()
        font6.setPointSize(25)
        self.lbl_image_text.setFont(font6)
        self.lbl_image_text.setStyleSheet(u"border: 3px dashed rgb(222, 219, 202);\n"
"color:  rgb(61, 64, 91);")
        self.lbl_image_text.setAlignment(Qt.AlignCenter)
        self.lbl_image_text.setWordWrap(True)

        self.horizontalLayout_7.addWidget(self.lbl_image_text)

        self.btn_next_lesson = QPushButton(self.bottom_frame_2)
        self.btn_next_lesson.setObjectName(u"btn_next_lesson")
        self.btn_next_lesson.setMinimumSize(QSize(70, 777))
        self.btn_next_lesson.setMaximumSize(QSize(60, 16777215))
        self.btn_next_lesson.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_next_lesson.setStyleSheet(u"QPushButton {\n"
"border: 3px solid #E07A5F;\n"
"border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover:!pressed {\n"
"background-color: #3D405B;\n"
"color: #F4F1DE;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u"../Images/forward.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_next_lesson.setIcon(icon4)
        self.btn_next_lesson.setIconSize(QSize(100, 100))

        self.horizontalLayout_7.addWidget(self.btn_next_lesson)


        self.verticalLayout.addWidget(self.bottom_frame_2)

        self.stackedWidget.addWidget(self.lesson_page)

        self.verticalLayout_2.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)
        self.btn_back_to_home.setDefault(False)
        self.btn_back_to_home_2.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_back_to_home.setText("")
        self.lbl_headline.setText(QCoreApplication.translate("MainWindow", u"\u09aa\u09be\u09a0\u09b8\u09ae\u09c2\u09b9 ", None))
        self.btn_select_folder.setText(QCoreApplication.translate("MainWindow", u"\u09ab\u09cb\u09b2\u09cd\u09a1\u09be\u09b0 \u09a8\u09bf\u09b0\u09cd\u09ac\u09be\u099a\u09a8 \u0995\u09b0\u09c1\u09a8", None))
        self.edit_lesson_list.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u09aa\u09be\u09a0\u09b8\u09ae\u09c2\u09b9  ", None))
        self.bnt_start_lesson.setText(QCoreApplication.translate("MainWindow", u"\u09b6\u09c1\u09b0\u09c1 \u0995\u09b0\u09c1\u09a8", None))
        self.btn_lesson.setText("")
        self.btn_evaluation.setText("")
        self.label.setText("")
        self.btn_back_to_home_2.setText("")
        self.lbl_lesson_headline.setText(QCoreApplication.translate("MainWindow", u"\u09a8\u09be\u09ae \u09b6\u09bf\u0996\u09a8 - \u09aa\u09be\u09a0 \u09e7", None))
        self.btn_prev_lesson.setText("")
        self.lbl_image.setText(QCoreApplication.translate("MainWindow", u"\u099b\u09ac\u09bf", None))
        self.lbl_image_text.setText(QCoreApplication.translate("MainWindow", u"\u09aa\u09b0\u09bf\u099a\u09df", None))
        self.btn_next_lesson.setText("")
    # retranslateUi

