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
    QStackedWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 719)
        MainWindow.setMinimumSize(QSize(1280, 700))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(1280, 700))
        self.gridLayout_6 = QGridLayout(self.centralwidget)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(1280, 700))
        self.stackedWidget.setStyleSheet(u"background-color: #F4F1DE;")
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.home_page.setMinimumSize(QSize(1280, 600))
        self.verticalLayout_3 = QVBoxLayout(self.home_page)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.top_frame_3 = QFrame(self.home_page)
        self.top_frame_3.setObjectName(u"top_frame_3")
        self.top_frame_3.setMinimumSize(QSize(1300, 344))
        self.top_frame_3.setStyleSheet(u"")
        self.top_frame_3.setFrameShape(QFrame.StyledPanel)
        self.top_frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.top_frame_3)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, 0, 0)
        self.btn_lesson = QPushButton(self.top_frame_3)
        self.btn_lesson.setObjectName(u"btn_lesson")
        self.btn_lesson.setMaximumSize(QSize(350, 280))
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
        icon = QIcon()
        icon.addFile(u"../Images/lessons_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_lesson.setIcon(icon)
        self.btn_lesson.setIconSize(QSize(400, 400))

        self.horizontalLayout.addWidget(self.btn_lesson)


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
        self.label.setMinimumSize(QSize(1280, 120))
        self.label.setPixmap(QPixmap(u"../Images/banner_icon.png"))
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout_3.addWidget(self.bottom_frame_3)

        self.stackedWidget.addWidget(self.home_page)
        self.lesson_page = QWidget()
        self.lesson_page.setObjectName(u"lesson_page")
        self.lesson_page.setMinimumSize(QSize(1280, 700))
        self.gridLayout_3 = QGridLayout(self.lesson_page)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.top_frame_2 = QFrame(self.lesson_page)
        self.top_frame_2.setObjectName(u"top_frame_2")
        self.top_frame_2.setMinimumSize(QSize(1280, 100))
        self.top_frame_2.setMaximumSize(QSize(16777215, 100))
        self.top_frame_2.setStyleSheet(u"background-color: #E07A5F;\n"
"color: #3D405B; ")
        self.top_frame_2.setFrameShape(QFrame.StyledPanel)
        self.top_frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.top_frame_2)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(11, 11, 0, 4)
        self.lbl_lesson_headline = QLabel(self.top_frame_2)
        self.lbl_lesson_headline.setObjectName(u"lbl_lesson_headline")
        self.lbl_lesson_headline.setMinimumSize(QSize(1189, 58))
        font = QFont()
        font.setFamilies([u"Kalpurush"])
        font.setPointSize(26)
        font.setBold(False)
        font.setItalic(False)
        self.lbl_lesson_headline.setFont(font)
        self.lbl_lesson_headline.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 26pt \"Kalpurush\";")
        self.lbl_lesson_headline.setAlignment(Qt.AlignCenter)
        self.lbl_lesson_headline.setMargin(-10)

        self.gridLayout_4.addWidget(self.lbl_lesson_headline, 0, 0, 1, 1)

        self.lbl_lesson_sub_heading = QLabel(self.top_frame_2)
        self.lbl_lesson_sub_heading.setObjectName(u"lbl_lesson_sub_heading")
        self.lbl_lesson_sub_heading.setMinimumSize(QSize(1189, 30))
        font1 = QFont()
        font1.setFamilies([u"Kalpurush"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.lbl_lesson_sub_heading.setFont(font1)
        self.lbl_lesson_sub_heading.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"padding-left: 5px;\n"
"font: 12pt \"Kalpurush\";")
        self.lbl_lesson_sub_heading.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.lbl_lesson_sub_heading, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.top_frame_2, 0, 0, 1, 1)

        self.frame = QFrame(self.lesson_page)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(1280, 550))
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(11, 0, -1, -1)
        self.btn_prev_lesson = QPushButton(self.frame)
        self.btn_prev_lesson.setObjectName(u"btn_prev_lesson")
        self.btn_prev_lesson.setMinimumSize(QSize(70, 500))
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
        icon1 = QIcon()
        icon1.addFile(u"../Images/backward.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_prev_lesson.setIcon(icon1)
        self.btn_prev_lesson.setIconSize(QSize(150, 150))

        self.gridLayout.addWidget(self.btn_prev_lesson, 0, 0, 1, 1)

        self.middle_content_frame = QFrame(self.frame)
        self.middle_content_frame.setObjectName(u"middle_content_frame")
        self.middle_content_frame.setMinimumSize(QSize(1100, 585))
        self.middle_content_frame.setStyleSheet(u"background-color: rgb(244, 241, 222);\n"
"color: rgb(61, 64, 91);\n"
"border: none;")
        self.middle_content_frame.setFrameShape(QFrame.StyledPanel)
        self.middle_content_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.middle_content_frame)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(5, 10, 5, 10)
        self.mediaStackWidget = QStackedWidget(self.middle_content_frame)
        self.mediaStackWidget.setObjectName(u"mediaStackWidget")
        self.mediaStackWidget.setMinimumSize(QSize(651, 565))
        self.image_page = QWidget()
        self.image_page.setObjectName(u"image_page")
        self.horizontalLayout_9 = QHBoxLayout(self.image_page)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.lsn_lbl_image = QLabel(self.image_page)
        self.lsn_lbl_image.setObjectName(u"lsn_lbl_image")
        self.lsn_lbl_image.setMinimumSize(QSize(690, 380))
        font2 = QFont()
        font2.setFamilies([u"Kalpurush"])
        font2.setPointSize(30)
        self.lsn_lbl_image.setFont(font2)
        self.lsn_lbl_image.setStyleSheet(u"border: 3px dotted rgb(227, 224, 207) ;\n"
"color: rgb(61, 64, 91);")
        self.lsn_lbl_image.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.lsn_lbl_image)

        self.mediaStackWidget.addWidget(self.image_page)
        self.video_page = QWidget()
        self.video_page.setObjectName(u"video_page")
        self.verticalLayout_5 = QVBoxLayout(self.video_page)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 5, 5)
        self.video_player_widget = QHBoxLayout()
        self.video_player_widget.setObjectName(u"video_player_widget")

        self.verticalLayout_5.addLayout(self.video_player_widget)

        self.mediaStackWidget.addWidget(self.video_page)

        self.horizontalLayout_12.addWidget(self.mediaStackWidget)

        self.lsn_lbl_lesson_topic = QLabel(self.middle_content_frame)
        self.lsn_lbl_lesson_topic.setObjectName(u"lsn_lbl_lesson_topic")
        self.lsn_lbl_lesson_topic.setMinimumSize(QSize(434, 565))
        self.lsn_lbl_lesson_topic.setMaximumSize(QSize(800, 16777215))
        font3 = QFont()
        font3.setFamilies([u"Kalpurush"])
        font3.setPointSize(40)
        self.lsn_lbl_lesson_topic.setFont(font3)
        self.lsn_lbl_lesson_topic.setStyleSheet(u"border: 3px dotted rgb(227, 224, 207) ;\n"
"color: rgb(61, 64, 91);")
        self.lsn_lbl_lesson_topic.setAlignment(Qt.AlignCenter)
        self.lsn_lbl_lesson_topic.setWordWrap(True)

        self.horizontalLayout_12.addWidget(self.lsn_lbl_lesson_topic)


        self.gridLayout.addWidget(self.middle_content_frame, 0, 1, 1, 1)

        self.btn_next_lesson = QPushButton(self.frame)
        self.btn_next_lesson.setObjectName(u"btn_next_lesson")
        self.btn_next_lesson.setMinimumSize(QSize(70, 500))
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
        icon2 = QIcon()
        icon2.addFile(u"../Images/forward.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_next_lesson.setIcon(icon2)
        self.btn_next_lesson.setIconSize(QSize(150, 150))

        self.gridLayout.addWidget(self.btn_next_lesson, 0, 2, 1, 1)


        self.gridLayout_3.addWidget(self.frame, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.lesson_page)
        self.evaluation_page = QWidget()
        self.evaluation_page.setObjectName(u"evaluation_page")
        self.gridLayout_7 = QGridLayout(self.evaluation_page)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.top_frame_4 = QFrame(self.evaluation_page)
        self.top_frame_4.setObjectName(u"top_frame_4")
        self.top_frame_4.setMinimumSize(QSize(1280, 100))
        self.top_frame_4.setMaximumSize(QSize(16777215, 100))
        self.top_frame_4.setStyleSheet(u"background-color: #E07A5F;\n"
"color: #3D405B; ")
        self.top_frame_4.setFrameShape(QFrame.StyledPanel)
        self.top_frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.top_frame_4)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(11, 11, 0, 4)
        self.lbl_lesson_headline_2 = QLabel(self.top_frame_4)
        self.lbl_lesson_headline_2.setObjectName(u"lbl_lesson_headline_2")
        self.lbl_lesson_headline_2.setMinimumSize(QSize(1189, 58))
        self.lbl_lesson_headline_2.setFont(font)
        self.lbl_lesson_headline_2.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 26pt \"Kalpurush\";")
        self.lbl_lesson_headline_2.setAlignment(Qt.AlignCenter)
        self.lbl_lesson_headline_2.setMargin(-10)

        self.gridLayout_5.addWidget(self.lbl_lesson_headline_2, 0, 0, 1, 1)

        self.lbl_lesson_sub_heading_2 = QLabel(self.top_frame_4)
        self.lbl_lesson_sub_heading_2.setObjectName(u"lbl_lesson_sub_heading_2")
        self.lbl_lesson_sub_heading_2.setMinimumSize(QSize(1189, 30))
        self.lbl_lesson_sub_heading_2.setFont(font1)
        self.lbl_lesson_sub_heading_2.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"padding-left: 5px;\n"
"font: 12pt \"Kalpurush\";")
        self.lbl_lesson_sub_heading_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.lbl_lesson_sub_heading_2, 1, 0, 1, 1)


        self.gridLayout_7.addWidget(self.top_frame_4, 0, 0, 1, 1)

        self.frame_2 = QFrame(self.evaluation_page)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(1280, 550))
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_2)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(11, 11, -1, -1)
        self.puzzle_frame = QFrame(self.frame_2)
        self.puzzle_frame.setObjectName(u"puzzle_frame")
        self.puzzle_frame.setMinimumSize(QSize(1100, 585))
        self.puzzle_frame.setStyleSheet(u"background-color: rgb(244, 241, 222);\n"
"color: rgb(61, 64, 91);\n"
"border: none;")
        self.puzzle_frame.setFrameShape(QFrame.StyledPanel)
        self.puzzle_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.puzzle_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.puzzle_piece_frame = QFrame(self.puzzle_frame)
        self.puzzle_piece_frame.setObjectName(u"puzzle_piece_frame")
        self.puzzle_piece_frame.setMinimumSize(QSize(370, 571))
        self.puzzle_piece_frame.setMaximumSize(QSize(291, 16777215))
        self.puzzle_piece_frame.setStyleSheet(u"")
        self.puzzle_piece_frame.setFrameShape(QFrame.StyledPanel)
        self.puzzle_piece_frame.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3.addWidget(self.puzzle_piece_frame)

        self.puzzle_widget_frame = QFrame(self.puzzle_frame)
        self.puzzle_widget_frame.setObjectName(u"puzzle_widget_frame")
        self.puzzle_widget_frame.setMinimumSize(QSize(865, 561))
        self.puzzle_widget_frame.setStyleSheet(u"")
        self.puzzle_widget_frame.setFrameShape(QFrame.StyledPanel)
        self.puzzle_widget_frame.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3.addWidget(self.puzzle_widget_frame)


        self.gridLayout_2.addWidget(self.puzzle_frame, 0, 0, 1, 1)


        self.gridLayout_7.addWidget(self.frame_2, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.evaluation_page)

        self.gridLayout_6.addWidget(self.stackedWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)
        self.mediaStackWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_lesson.setText("")
        self.label.setText("")
        self.lbl_lesson_headline.setText(QCoreApplication.translate("MainWindow", u"\u09aa\u09be\u09a0 \u09e7", None))
        self.lbl_lesson_sub_heading.setText(QCoreApplication.translate("MainWindow", u"\u09a8\u09be\u09ae \u09b6\u09bf\u0996\u09a8 - \u09ae\u09a1\u09bf\u0989\u09b2 \u09e7", None))
        self.btn_prev_lesson.setText("")
        self.lsn_lbl_image.setText(QCoreApplication.translate("MainWindow", u"\u099b\u09ac\u09bf", None))
        self.lsn_lbl_lesson_topic.setText(QCoreApplication.translate("MainWindow", u"\u09aa\u09b0\u09bf\u099a\u09df", None))
        self.btn_next_lesson.setText("")
        self.lbl_lesson_headline_2.setText(QCoreApplication.translate("MainWindow", u"\u09a7\u09be\u0981\u09a7\u09be", None))
        self.lbl_lesson_sub_heading_2.setText(QCoreApplication.translate("MainWindow", u"\u09aa\u09be\u09a0 \u09ae\u09c2\u09b2\u09cd\u09af\u09be\u09df\u09a8", None))
    # retranslateUi

