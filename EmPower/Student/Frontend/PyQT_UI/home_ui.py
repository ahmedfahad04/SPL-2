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
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 710)
        MainWindow.setMinimumSize(QSize(1280, 710))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(1280, 700))
        self.horizontalLayout_15 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
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
        self.puzzle_page = QWidget()
        self.puzzle_page.setObjectName(u"puzzle_page")
        self.gridLayout_7 = QGridLayout(self.puzzle_page)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.top_frame_4 = QFrame(self.puzzle_page)
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

        self.puzzle_main = QFrame(self.puzzle_page)
        self.puzzle_main.setObjectName(u"puzzle_main")
        self.puzzle_main.setMinimumSize(QSize(1280, 550))
        self.puzzle_main.setStyleSheet(u"")
        self.puzzle_main.setFrameShape(QFrame.StyledPanel)
        self.puzzle_main.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.puzzle_main)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(11, 11, -1, -1)
        self.puzzle_frame = QFrame(self.puzzle_main)
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


        self.gridLayout_7.addWidget(self.puzzle_main, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.puzzle_page)
        self.celebration_page = QWidget()
        self.celebration_page.setObjectName(u"celebration_page")
        self.gridLayout_9 = QGridLayout(self.celebration_page)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.celebration_frame = QFrame(self.celebration_page)
        self.celebration_frame.setObjectName(u"celebration_frame")
        self.celebration_frame.setMinimumSize(QSize(1280, 550))
        self.celebration_frame.setStyleSheet(u"border: 3px dot-dash rgb(61, 64, 91);\n"
"")
        self.celebration_frame.setFrameShape(QFrame.StyledPanel)
        self.celebration_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.celebration_frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.c_middle_frame = QFrame(self.celebration_frame)
        self.c_middle_frame.setObjectName(u"c_middle_frame")
        self.c_middle_frame.setMinimumSize(QSize(465, 691))
        self.c_middle_frame.setStyleSheet(u"border: none;\n"
"")
        self.c_middle_frame.setFrameShape(QFrame.StyledPanel)
        self.c_middle_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.c_middle_frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.c_lable = QLabel(self.c_middle_frame)
        self.c_lable.setObjectName(u"c_lable")
        self.c_lable.setMinimumSize(QSize(434, 194))
        self.c_lable.setMaximumSize(QSize(16777215, 300))
        font4 = QFont()
        font4.setFamilies([u"Kalpurush"])
        font4.setPointSize(61)
        self.c_lable.setFont(font4)
        self.c_lable.setStyleSheet(u"background-color: none;")
        self.c_lable.setAlignment(Qt.AlignCenter)
        self.c_lable.setWordWrap(True)

        self.verticalLayout.addWidget(self.c_lable)

        self.c_gif = QLabel(self.c_middle_frame)
        self.c_gif.setObjectName(u"c_gif")
        self.c_gif.setMinimumSize(QSize(390, 475))
        self.c_gif.setStyleSheet(u"background-color: none;")

        self.verticalLayout.addWidget(self.c_gif)


        self.horizontalLayout_4.addWidget(self.c_middle_frame)

        self.c_right_frame = QFrame(self.celebration_frame)
        self.c_right_frame.setObjectName(u"c_right_frame")
        self.c_right_frame.setMinimumSize(QSize(366, 691))
        self.c_right_frame.setMaximumSize(QSize(378, 691))
        self.c_right_frame.setStyleSheet(u"border: none;\n"
"")
        self.c_right_frame.setFrameShape(QFrame.StyledPanel)
        self.c_right_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.c_right_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer = QSpacerItem(20, 306, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.c_next_quiz_lbl = QLabel(self.c_right_frame)
        self.c_next_quiz_lbl.setObjectName(u"c_next_quiz_lbl")
        self.c_next_quiz_lbl.setMinimumSize(QSize(369, 350))
        self.c_next_quiz_lbl.setMaximumSize(QSize(369, 16777215))
        font5 = QFont()
        font5.setPointSize(30)
        self.c_next_quiz_lbl.setFont(font5)
        self.c_next_quiz_lbl.setStyleSheet(u"")
        self.c_next_quiz_lbl.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.verticalLayout_2.addWidget(self.c_next_quiz_lbl)

        self.c_next_quiz = QPushButton(self.c_right_frame)
        self.c_next_quiz.setObjectName(u"c_next_quiz")
        self.c_next_quiz.setMaximumSize(QSize(353, 16777215))
        self.c_next_quiz.setCursor(QCursor(Qt.PointingHandCursor))
        self.c_next_quiz.setStyleSheet(u"QPushButton {\n"
"border: 3px solid #E07A5F;\n"
"border-radius: 20px;\n"
"background-color:  #3D405B;\n"
"}\n"
"\n"
"QPushButton:hover:!pressed {\n"
"background-color: #3D405B;\n"
"background-color:  rgb(42, 44, 63);\n"
"}")
        self.c_next_quiz.setIcon(icon2)
        self.c_next_quiz.setIconSize(QSize(90, 80))

        self.verticalLayout_2.addWidget(self.c_next_quiz)


        self.horizontalLayout_4.addWidget(self.c_right_frame)


        self.gridLayout_9.addWidget(self.celebration_frame, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.celebration_page)
        self.navigation_page = QWidget()
        self.navigation_page.setObjectName(u"navigation_page")
        self.horizontalLayout_7 = QHBoxLayout(self.navigation_page)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.navigation_frame = QFrame(self.navigation_page)
        self.navigation_frame.setObjectName(u"navigation_frame")
        self.navigation_frame.setMinimumSize(QSize(1280, 491))
        self.navigation_frame.setStyleSheet(u"border: 3px dot-dash rgb(61, 64, 91);\n"
"")
        self.navigation_frame.setFrameShape(QFrame.StyledPanel)
        self.navigation_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.navigation_frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.n_middle_frame = QFrame(self.navigation_frame)
        self.n_middle_frame.setObjectName(u"n_middle_frame")
        self.n_middle_frame.setMinimumSize(QSize(623, 650))
        self.n_middle_frame.setMaximumSize(QSize(623, 691))
        self.n_middle_frame.setStyleSheet(u"border: none;")
        self.n_middle_frame.setFrameShape(QFrame.StyledPanel)
        self.n_middle_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.n_middle_frame)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.n_message = QLabel(self.n_middle_frame)
        self.n_message.setObjectName(u"n_message")
        self.n_message.setMinimumSize(QSize(434, 194))
        self.n_message.setMaximumSize(QSize(16777215, 300))
        font6 = QFont()
        font6.setFamilies([u"Kalpurush"])
        font6.setPointSize(39)
        font6.setBold(False)
        self.n_message.setFont(font6)
        self.n_message.setStyleSheet(u"background-color: none;")
        self.n_message.setAlignment(Qt.AlignCenter)
        self.n_message.setWordWrap(True)

        self.verticalLayout_7.addWidget(self.n_message)

        self.n_icon = QLabel(self.n_middle_frame)
        self.n_icon.setObjectName(u"n_icon")
        self.n_icon.setMinimumSize(QSize(390, 442))
        self.n_icon.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.n_icon.setPixmap(QPixmap(u"../Images/evaluation_icon.png"))
        self.n_icon.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.n_icon)


        self.horizontalLayout_5.addWidget(self.n_middle_frame)

        self.n_right_frame = QFrame(self.navigation_frame)
        self.n_right_frame.setObjectName(u"n_right_frame")
        self.n_right_frame.setMinimumSize(QSize(622, 650))
        self.n_right_frame.setMaximumSize(QSize(630, 691))
        self.n_right_frame.setStyleSheet(u"border: none;\n"
"")
        self.n_right_frame.setFrameShape(QFrame.StyledPanel)
        self.n_right_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.n_right_frame)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.n_type_lbl = QLabel(self.n_right_frame)
        self.n_type_lbl.setObjectName(u"n_type_lbl")
        self.n_type_lbl.setMinimumSize(QSize(520, 520))
        self.n_type_lbl.setMaximumSize(QSize(520, 520))
        font7 = QFont()
        font7.setPointSize(55)
        self.n_type_lbl.setFont(font7)
        self.n_type_lbl.setStyleSheet(u"border: 3px solid rgb(61, 64, 91);")
        self.n_type_lbl.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.n_type_lbl, 0, 0, 1, 1)

        self.n_proceed_btn = QPushButton(self.n_right_frame)
        self.n_proceed_btn.setObjectName(u"n_proceed_btn")
        self.n_proceed_btn.setMinimumSize(QSize(271, 101))
        self.n_proceed_btn.setMaximumSize(QSize(353, 16777215))
        self.n_proceed_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.n_proceed_btn.setStyleSheet(u"QPushButton {\n"
"border: 3px solid #E07A5F;\n"
"border-radius: 20px;\n"
"background-color:  rgb(61, 64, 91);\n"
"}\n"
"\n"
"QPushButton:hover:!pressed {\n"
"background-color: #3D405B;\n"
"background-color:  rgb(35, 37, 53);\n"
"}")
        self.n_proceed_btn.setIcon(icon2)
        self.n_proceed_btn.setIconSize(QSize(90, 80))

        self.gridLayout_6.addWidget(self.n_proceed_btn, 1, 0, 1, 1)


        self.horizontalLayout_5.addWidget(self.n_right_frame)


        self.horizontalLayout_7.addWidget(self.navigation_frame)

        self.stackedWidget.addWidget(self.navigation_page)
        self.matching_page = QWidget()
        self.matching_page.setObjectName(u"matching_page")
        self.verticalLayout_6 = QVBoxLayout(self.matching_page)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.top_frame_5 = QFrame(self.matching_page)
        self.top_frame_5.setObjectName(u"top_frame_5")
        self.top_frame_5.setMinimumSize(QSize(1280, 100))
        self.top_frame_5.setMaximumSize(QSize(16777215, 100))
        self.top_frame_5.setStyleSheet(u"background-color: #E07A5F;\n"
"color: #3D405B; ")
        self.top_frame_5.setFrameShape(QFrame.StyledPanel)
        self.top_frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.top_frame_5)
        self.gridLayout_8.setSpacing(0)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(11, 11, 0, 4)
        self.lbl_lesson_sub_heading_3 = QLabel(self.top_frame_5)
        self.lbl_lesson_sub_heading_3.setObjectName(u"lbl_lesson_sub_heading_3")
        self.lbl_lesson_sub_heading_3.setMinimumSize(QSize(1189, 30))
        self.lbl_lesson_sub_heading_3.setFont(font1)
        self.lbl_lesson_sub_heading_3.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"padding-left: 5px;\n"
"font: 12pt \"Kalpurush\";")
        self.lbl_lesson_sub_heading_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.lbl_lesson_sub_heading_3, 1, 0, 1, 1)

        self.lbl_lesson_headline_3 = QLabel(self.top_frame_5)
        self.lbl_lesson_headline_3.setObjectName(u"lbl_lesson_headline_3")
        self.lbl_lesson_headline_3.setMinimumSize(QSize(1189, 58))
        self.lbl_lesson_headline_3.setFont(font)
        self.lbl_lesson_headline_3.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 26pt \"Kalpurush\";")
        self.lbl_lesson_headline_3.setAlignment(Qt.AlignCenter)
        self.lbl_lesson_headline_3.setMargin(-10)

        self.gridLayout_8.addWidget(self.lbl_lesson_headline_3, 0, 0, 1, 1)


        self.verticalLayout_6.addWidget(self.top_frame_5)

        self.puzzle_widget_frame_2 = QFrame(self.matching_page)
        self.puzzle_widget_frame_2.setObjectName(u"puzzle_widget_frame_2")
        self.puzzle_widget_frame_2.setMinimumSize(QSize(865, 561))
        self.puzzle_widget_frame_2.setStyleSheet(u"background-color: none;\n"
"border: 2px solid rgb(0, 43, 91);")
        self.puzzle_widget_frame_2.setFrameShape(QFrame.StyledPanel)
        self.puzzle_widget_frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.puzzle_widget_frame_2)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.frame_4 = QFrame(self.puzzle_widget_frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(624, 193))
        self.frame_4.setStyleSheet(u"border: none;")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.mat_img_lbl_3 = QLabel(self.frame_4)
        self.mat_img_lbl_3.setObjectName(u"mat_img_lbl_3")
        self.mat_img_lbl_3.setMinimumSize(QSize(239, 171))
        self.mat_img_lbl_3.setStyleSheet(u"border: 2px solid rgb(0, 43, 91);")

        self.horizontalLayout_11.addWidget(self.mat_img_lbl_3)

        self.label_9 = QLabel(self.frame_4)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(111, 41))
        self.label_9.setMaximumSize(QSize(105, 171))
        font8 = QFont()
        font8.setPointSize(8)
        self.label_9.setFont(font8)
        self.label_9.setStyleSheet(u"border: none;")
        self.label_9.setPixmap(QPixmap(u"../Images/connect_1.png"))
        self.label_9.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.label_9)

        self.mat_txt_lbl_3_frame = QFrame(self.frame_4)
        self.mat_txt_lbl_3_frame.setObjectName(u"mat_txt_lbl_3_frame")
        self.mat_txt_lbl_3_frame.setMinimumSize(QSize(238, 171))
        self.mat_txt_lbl_3_frame.setStyleSheet(u"border: 3px dashed rgb(0, 43, 91);\n"
"background-color: rgb(200, 198, 182);")
        self.mat_txt_lbl_3_frame.setFrameShape(QFrame.StyledPanel)
        self.mat_txt_lbl_3_frame.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_11.addWidget(self.mat_txt_lbl_3_frame)


        self.gridLayout_10.addWidget(self.frame_4, 1, 0, 1, 1)

        self.frame_6 = QFrame(self.puzzle_widget_frame_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(1254, 139))
        self.frame_6.setMaximumSize(QSize(16777215, 139))
        self.frame_6.setStyleSheet(u"border: 2px dashed rgb(0, 43, 91);")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_12 = QGridLayout(self.frame_6)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.label_18 = QLabel(self.frame_6)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(131, 111))
        self.label_18.setStyleSheet(u"border: none;\n"
"background-color: rgb(255, 252, 232);")
        self.label_18.setPixmap(QPixmap(u"../Images/drag_2-100x100.png"))
        self.label_18.setAlignment(Qt.AlignCenter)

        self.gridLayout_12.addWidget(self.label_18, 0, 0, 3, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_12.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 18, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_12.addItem(self.verticalSpacer_3, 0, 2, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 18, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_12.addItem(self.verticalSpacer_7, 0, 4, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 18, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_12.addItem(self.verticalSpacer_8, 0, 7, 1, 1)

        self.verticalSpacer_10 = QSpacerItem(20, 18, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_12.addItem(self.verticalSpacer_10, 0, 9, 1, 1)

        self.mat_option_1_frame = QFrame(self.frame_6)
        self.mat_option_1_frame.setObjectName(u"mat_option_1_frame")
        self.mat_option_1_frame.setMinimumSize(QSize(201, 61))
        self.mat_option_1_frame.setCursor(QCursor(Qt.PointingHandCursor))
        self.mat_option_1_frame.setStyleSheet(u"border: 2px dotted rgb(0, 43, 91);\n"
"background-color: rgb(236, 233, 215);\n"
"border-radius: 25px;")
        self.mat_option_1_frame.setFrameShape(QFrame.StyledPanel)
        self.mat_option_1_frame.setFrameShadow(QFrame.Raised)

        self.gridLayout_12.addWidget(self.mat_option_1_frame, 1, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(78, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_12.addItem(self.horizontalSpacer_2, 1, 3, 1, 1)

        self.mat_option_2_frame = QFrame(self.frame_6)
        self.mat_option_2_frame.setObjectName(u"mat_option_2_frame")
        self.mat_option_2_frame.setMinimumSize(QSize(201, 61))
        self.mat_option_2_frame.setCursor(QCursor(Qt.PointingHandCursor))
        self.mat_option_2_frame.setStyleSheet(u"border: 2px dotted rgb(0, 43, 91);\n"
"background-color: rgb(236, 233, 215);\n"
"border-radius: 25px;")
        self.mat_option_2_frame.setFrameShape(QFrame.StyledPanel)
        self.mat_option_2_frame.setFrameShadow(QFrame.Raised)

        self.gridLayout_12.addWidget(self.mat_option_2_frame, 1, 4, 1, 2)

        self.horizontalSpacer_3 = QSpacerItem(79, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_12.addItem(self.horizontalSpacer_3, 1, 6, 1, 1)

        self.mat_option_3_frame = QFrame(self.frame_6)
        self.mat_option_3_frame.setObjectName(u"mat_option_3_frame")
        self.mat_option_3_frame.setMinimumSize(QSize(201, 61))
        self.mat_option_3_frame.setCursor(QCursor(Qt.PointingHandCursor))
        self.mat_option_3_frame.setStyleSheet(u"border: 2px dotted rgb(0, 43, 91);\n"
"background-color: rgb(236, 233, 215);\n"
"border-radius: 25px;")
        self.mat_option_3_frame.setFrameShape(QFrame.StyledPanel)
        self.mat_option_3_frame.setFrameShadow(QFrame.Raised)

        self.gridLayout_12.addWidget(self.mat_option_3_frame, 1, 7, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(78, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_12.addItem(self.horizontalSpacer_4, 1, 8, 1, 1)

        self.mat_option_4_frame = QFrame(self.frame_6)
        self.mat_option_4_frame.setObjectName(u"mat_option_4_frame")
        self.mat_option_4_frame.setMinimumSize(QSize(201, 61))
        self.mat_option_4_frame.setCursor(QCursor(Qt.PointingHandCursor))
        self.mat_option_4_frame.setStyleSheet(u"border: 2px dotted rgb(0, 43, 91);\n"
"background-color: rgb(236, 233, 215);\n"
"border-radius: 25px;")
        self.mat_option_4_frame.setFrameShape(QFrame.StyledPanel)
        self.mat_option_4_frame.setFrameShadow(QFrame.Raised)

        self.gridLayout_12.addWidget(self.mat_option_4_frame, 1, 9, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 18, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_12.addItem(self.verticalSpacer_5, 2, 2, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 18, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_12.addItem(self.verticalSpacer_6, 2, 5, 1, 1)

        self.verticalSpacer_9 = QSpacerItem(20, 18, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_12.addItem(self.verticalSpacer_9, 2, 7, 1, 1)

        self.verticalSpacer_11 = QSpacerItem(20, 18, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_12.addItem(self.verticalSpacer_11, 2, 9, 1, 1)


        self.gridLayout_10.addWidget(self.frame_6, 2, 0, 1, 2)

        self.frame_5 = QFrame(self.puzzle_widget_frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(624, 193))
        self.frame_5.setStyleSheet(u"border: none;")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.mat_img_lbl_4 = QLabel(self.frame_5)
        self.mat_img_lbl_4.setObjectName(u"mat_img_lbl_4")
        self.mat_img_lbl_4.setMinimumSize(QSize(239, 171))
        self.mat_img_lbl_4.setStyleSheet(u"border: 2px solid rgb(0, 43, 91);")

        self.horizontalLayout_13.addWidget(self.mat_img_lbl_4)

        self.label_12 = QLabel(self.frame_5)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(111, 41))
        self.label_12.setMaximumSize(QSize(105, 171))
        self.label_12.setFont(font8)
        self.label_12.setStyleSheet(u"border: none;")
        self.label_12.setPixmap(QPixmap(u"../Images/connect_1.png"))
        self.label_12.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.label_12)

        self.mat_txt_lbl_4_frame = QFrame(self.frame_5)
        self.mat_txt_lbl_4_frame.setObjectName(u"mat_txt_lbl_4_frame")
        self.mat_txt_lbl_4_frame.setMinimumSize(QSize(238, 171))
        self.mat_txt_lbl_4_frame.setStyleSheet(u"border: 3px dashed rgb(0, 43, 91);\n"
"background-color: rgb(200, 198, 182);")
        self.mat_txt_lbl_4_frame.setFrameShape(QFrame.StyledPanel)
        self.mat_txt_lbl_4_frame.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_13.addWidget(self.mat_txt_lbl_4_frame)


        self.gridLayout_10.addWidget(self.frame_5, 1, 1, 1, 1)

        self.frame_2 = QFrame(self.puzzle_widget_frame_2)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(624, 193))
        self.frame_2.setStyleSheet(u"border: none;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.mat_img_lbl_1 = QLabel(self.frame_2)
        self.mat_img_lbl_1.setObjectName(u"mat_img_lbl_1")
        self.mat_img_lbl_1.setMinimumSize(QSize(239, 171))
        self.mat_img_lbl_1.setStyleSheet(u"border: 2px solid rgb(0, 43, 91);")

        self.horizontalLayout_8.addWidget(self.mat_img_lbl_1)

        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(111, 41))
        self.label_4.setMaximumSize(QSize(105, 171))
        self.label_4.setFont(font8)
        self.label_4.setStyleSheet(u"border: none;")
        self.label_4.setPixmap(QPixmap(u"../Images/connect_1.png"))
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_4)

        self.mat_txt_lbl_1_frame = QFrame(self.frame_2)
        self.mat_txt_lbl_1_frame.setObjectName(u"mat_txt_lbl_1_frame")
        self.mat_txt_lbl_1_frame.setMinimumSize(QSize(238, 171))
        self.mat_txt_lbl_1_frame.setStyleSheet(u"border: 3px dashed rgb(0, 43, 91);\n"
"background-color: rgb(200, 198, 182);")
        self.mat_txt_lbl_1_frame.setFrameShape(QFrame.StyledPanel)
        self.mat_txt_lbl_1_frame.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_8.addWidget(self.mat_txt_lbl_1_frame)


        self.gridLayout_10.addWidget(self.frame_2, 0, 0, 1, 1)

        self.frame_3 = QFrame(self.puzzle_widget_frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(624, 193))
        self.frame_3.setStyleSheet(u"border: none;")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.mat_img_lbl_2 = QLabel(self.frame_3)
        self.mat_img_lbl_2.setObjectName(u"mat_img_lbl_2")
        self.mat_img_lbl_2.setMinimumSize(QSize(239, 171))
        self.mat_img_lbl_2.setStyleSheet(u"border: 2px solid rgb(0, 43, 91);")

        self.horizontalLayout_10.addWidget(self.mat_img_lbl_2)

        self.label_6 = QLabel(self.frame_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(111, 41))
        self.label_6.setMaximumSize(QSize(105, 171))
        self.label_6.setFont(font8)
        self.label_6.setStyleSheet(u"border: none;")
        self.label_6.setPixmap(QPixmap(u"../Images/connect_1.png"))
        self.label_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_6)

        self.mat_txt_lbl_2_frame = QFrame(self.frame_3)
        self.mat_txt_lbl_2_frame.setObjectName(u"mat_txt_lbl_2_frame")
        self.mat_txt_lbl_2_frame.setMinimumSize(QSize(238, 171))
        self.mat_txt_lbl_2_frame.setStyleSheet(u"border: 3px dashed rgb(0, 43, 91);\n"
"background-color: rgb(200, 198, 182);")
        self.mat_txt_lbl_2_frame.setFrameShape(QFrame.StyledPanel)
        self.mat_txt_lbl_2_frame.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_10.addWidget(self.mat_txt_lbl_2_frame)


        self.gridLayout_10.addWidget(self.frame_3, 0, 1, 1, 1)


        self.verticalLayout_6.addWidget(self.puzzle_widget_frame_2)

        self.stackedWidget.addWidget(self.matching_page)
        self.sequence_page = QWidget()
        self.sequence_page.setObjectName(u"sequence_page")
        self.verticalLayout_8 = QVBoxLayout(self.sequence_page)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.top_frame_6 = QFrame(self.sequence_page)
        self.top_frame_6.setObjectName(u"top_frame_6")
        self.top_frame_6.setMinimumSize(QSize(1280, 100))
        self.top_frame_6.setMaximumSize(QSize(16777215, 100))
        self.top_frame_6.setStyleSheet(u"background-color: #E07A5F;\n"
"color: #3D405B; ")
        self.top_frame_6.setFrameShape(QFrame.StyledPanel)
        self.top_frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_13 = QGridLayout(self.top_frame_6)
        self.gridLayout_13.setSpacing(0)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setContentsMargins(11, 11, 0, 4)
        self.lbl_lesson_headline_4 = QLabel(self.top_frame_6)
        self.lbl_lesson_headline_4.setObjectName(u"lbl_lesson_headline_4")
        self.lbl_lesson_headline_4.setMinimumSize(QSize(1189, 58))
        self.lbl_lesson_headline_4.setFont(font)
        self.lbl_lesson_headline_4.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 26pt \"Kalpurush\";")
        self.lbl_lesson_headline_4.setAlignment(Qt.AlignCenter)
        self.lbl_lesson_headline_4.setMargin(-10)

        self.gridLayout_13.addWidget(self.lbl_lesson_headline_4, 0, 0, 1, 1)

        self.lbl_lesson_sub_heading_4 = QLabel(self.top_frame_6)
        self.lbl_lesson_sub_heading_4.setObjectName(u"lbl_lesson_sub_heading_4")
        self.lbl_lesson_sub_heading_4.setMinimumSize(QSize(1189, 30))
        self.lbl_lesson_sub_heading_4.setFont(font1)
        self.lbl_lesson_sub_heading_4.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"padding-left: 5px;\n"
"font: 12pt \"Kalpurush\";")
        self.lbl_lesson_sub_heading_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_13.addWidget(self.lbl_lesson_sub_heading_4, 1, 0, 1, 1)


        self.verticalLayout_8.addWidget(self.top_frame_6)

        self.frame_7 = QFrame(self.sequence_page)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"background-color: none;\n"
"border: 2px solid blue;")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout_14 = QGridLayout(self.frame_7)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setHorizontalSpacing(30)
        self.gridLayout_14.setVerticalSpacing(10)
        self.frame_8 = QFrame(self.frame_7)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(1254, 221))
        self.frame_8.setStyleSheet(u"border: none;")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.seq_lbl_frame_1 = QFrame(self.frame_8)
        self.seq_lbl_frame_1.setObjectName(u"seq_lbl_frame_1")
        self.seq_lbl_frame_1.setStyleSheet(u"border: 3px dashed rgb(0, 43, 91);\n"
"background-color: rgb(200, 198, 182);")
        self.seq_lbl_frame_1.setFrameShape(QFrame.StyledPanel)
        self.seq_lbl_frame_1.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_6.addWidget(self.seq_lbl_frame_1)

        self.label_8 = QLabel(self.frame_8)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(71, 51))
        self.label_8.setMaximumSize(QSize(71, 51))
        self.label_8.setStyleSheet(u"border: none;")
        self.label_8.setPixmap(QPixmap(u"../Images/right_arrow.png"))
        self.label_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_8)

        self.seq_lbl_frame_2 = QFrame(self.frame_8)
        self.seq_lbl_frame_2.setObjectName(u"seq_lbl_frame_2")
        self.seq_lbl_frame_2.setStyleSheet(u"border: 3px dashed rgb(0, 43, 91);\n"
"background-color: rgb(200, 198, 182);")
        self.seq_lbl_frame_2.setFrameShape(QFrame.StyledPanel)
        self.seq_lbl_frame_2.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_6.addWidget(self.seq_lbl_frame_2)

        self.label_10 = QLabel(self.frame_8)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(71, 51))
        self.label_10.setMaximumSize(QSize(71, 51))
        self.label_10.setStyleSheet(u"border: none;")
        self.label_10.setPixmap(QPixmap(u"../Images/right_arrow.png"))
        self.label_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_10)

        self.seq_lbl_frame_3 = QFrame(self.frame_8)
        self.seq_lbl_frame_3.setObjectName(u"seq_lbl_frame_3")
        self.seq_lbl_frame_3.setStyleSheet(u"border: 3px dashed rgb(0, 43, 91);\n"
"background-color: rgb(200, 198, 182);")
        self.seq_lbl_frame_3.setFrameShape(QFrame.StyledPanel)
        self.seq_lbl_frame_3.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_6.addWidget(self.seq_lbl_frame_3)

        self.label_11 = QLabel(self.frame_8)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(71, 51))
        self.label_11.setMaximumSize(QSize(71, 51))
        self.label_11.setStyleSheet(u"border: none;")
        self.label_11.setPixmap(QPixmap(u"../Images/right_arrow.png"))
        self.label_11.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_11)

        self.seq_lbl_frame_4 = QFrame(self.frame_8)
        self.seq_lbl_frame_4.setObjectName(u"seq_lbl_frame_4")
        self.seq_lbl_frame_4.setStyleSheet(u"border: 3px dashed rgb(0, 43, 91);\n"
"background-color: rgb(200, 198, 182);")
        self.seq_lbl_frame_4.setFrameShape(QFrame.StyledPanel)
        self.seq_lbl_frame_4.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_6.addWidget(self.seq_lbl_frame_4)


        self.gridLayout_14.addWidget(self.frame_8, 0, 0, 1, 2)

        self.frame_9 = QFrame(self.frame_7)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(921, 351))
        self.frame_9.setStyleSheet(u"border: none;")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_9)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.seq_hint_lbl = QLabel(self.frame_9)
        self.seq_hint_lbl.setObjectName(u"seq_hint_lbl")
        self.seq_hint_lbl.setMinimumSize(QSize(891, 101))
        self.seq_hint_lbl.setStyleSheet(u"background-color: rgb(234, 231, 213);")
        self.seq_hint_lbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.seq_hint_lbl)

        self.frame_10 = QFrame(self.frame_9)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(911, 211))
        self.frame_10.setStyleSheet(u"border: none;")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.seq_img_frame_lbl_1 = QFrame(self.frame_10)
        self.seq_img_frame_lbl_1.setObjectName(u"seq_img_frame_lbl_1")
        self.seq_img_frame_lbl_1.setStyleSheet(u"border: 2px solid rgb(0, 43, 91);\n"
"background-color: rgb(200, 198, 182);")
        self.seq_img_frame_lbl_1.setFrameShape(QFrame.StyledPanel)
        self.seq_img_frame_lbl_1.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_14.addWidget(self.seq_img_frame_lbl_1)

        self.seq_img_frame_lbl_2 = QFrame(self.frame_10)
        self.seq_img_frame_lbl_2.setObjectName(u"seq_img_frame_lbl_2")
        self.seq_img_frame_lbl_2.setStyleSheet(u"border: 2px solid rgb(0, 43, 91);\n"
"background-color: rgb(200, 198, 182);")
        self.seq_img_frame_lbl_2.setFrameShape(QFrame.StyledPanel)
        self.seq_img_frame_lbl_2.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_14.addWidget(self.seq_img_frame_lbl_2)

        self.seq_img_frame_lbl_3 = QFrame(self.frame_10)
        self.seq_img_frame_lbl_3.setObjectName(u"seq_img_frame_lbl_3")
        self.seq_img_frame_lbl_3.setStyleSheet(u"border: 2px solid rgb(0, 43, 91);\n"
"background-color: rgb(200, 198, 182);")
        self.seq_img_frame_lbl_3.setFrameShape(QFrame.StyledPanel)
        self.seq_img_frame_lbl_3.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_14.addWidget(self.seq_img_frame_lbl_3)

        self.seq_img_frame_lbl_4 = QFrame(self.frame_10)
        self.seq_img_frame_lbl_4.setObjectName(u"seq_img_frame_lbl_4")
        self.seq_img_frame_lbl_4.setStyleSheet(u"border: 2px solid rgb(0, 43, 91);\n"
"background-color: rgb(200, 198, 182);")
        self.seq_img_frame_lbl_4.setFrameShape(QFrame.StyledPanel)
        self.seq_img_frame_lbl_4.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_14.addWidget(self.seq_img_frame_lbl_4)


        self.verticalLayout_9.addWidget(self.frame_10)


        self.gridLayout_14.addWidget(self.frame_9, 1, 0, 1, 1)

        self.label_17 = QLabel(self.frame_7)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(324, 351))
        self.label_17.setMaximumSize(QSize(324, 353))
        self.label_17.setStyleSheet(u"border: none;")
        self.label_17.setPixmap(QPixmap(u"../Images/sequence_1.png"))
        self.label_17.setAlignment(Qt.AlignCenter)

        self.gridLayout_14.addWidget(self.label_17, 1, 1, 1, 1)


        self.verticalLayout_8.addWidget(self.frame_7)

        self.stackedWidget.addWidget(self.sequence_page)

        self.horizontalLayout_15.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(3)
        self.mediaStackWidget.setCurrentIndex(0)


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
#if QT_CONFIG(shortcut)
        self.btn_next_lesson.setShortcut(QCoreApplication.translate("MainWindow", u"Space", None))
#endif // QT_CONFIG(shortcut)
        self.lbl_lesson_headline_2.setText(QCoreApplication.translate("MainWindow", u"\u09a7\u09be\u0981\u09a7\u09be", None))
        self.lbl_lesson_sub_heading_2.setText(QCoreApplication.translate("MainWindow", u"\u09aa\u09be\u09a0 \u09ae\u09c2\u09b2\u09cd\u09af\u09be\u09df\u09a8", None))
        self.c_lable.setText(QCoreApplication.translate("MainWindow", u"\u0985\u09ad\u09bf\u09a8\u09a8\u09cd\u09a6\u09a8!!!", None))
        self.c_gif.setText("")
        self.c_next_quiz_lbl.setText(QCoreApplication.translate("MainWindow", u"\u09aa\u09b0\u09ac\u09b0\u09cd\u09a4\u09c0 \u09ae\u09c2\u09b2\u09cd\u09af\u09be\u09df\u09a8", None))
        self.c_next_quiz.setText("")
#if QT_CONFIG(shortcut)
        self.c_next_quiz.setShortcut(QCoreApplication.translate("MainWindow", u"Space", None))
#endif // QT_CONFIG(shortcut)
        self.n_message.setText(QCoreApplication.translate("MainWindow", u"\u0985\u09ad\u09bf\u09a8\u09a8\u09cd\u09a6\u09a8!!! ", None))
        self.n_icon.setText("")
        self.n_type_lbl.setText(QCoreApplication.translate("MainWindow", u"\u09a7\u09be\u0981\u09a7\u09be", None))
        self.n_proceed_btn.setText("")
        self.lbl_lesson_sub_heading_3.setText(QCoreApplication.translate("MainWindow", u"\u09aa\u09be\u09a0 \u09ae\u09c2\u09b2\u09cd\u09af\u09be\u09df\u09a8", None))
        self.lbl_lesson_headline_3.setText(QCoreApplication.translate("MainWindow", u"\u09b6\u09ac\u09cd\u09a6 \u09ae\u09bf\u09b2\u09a8", None))
        self.mat_img_lbl_3.setText("")
        self.label_9.setText("")
        self.label_18.setText("")
        self.mat_img_lbl_4.setText("")
        self.label_12.setText("")
        self.mat_img_lbl_1.setText("")
        self.label_4.setText("")
        self.mat_img_lbl_2.setText("")
        self.label_6.setText("")
        self.lbl_lesson_headline_4.setText(QCoreApplication.translate("MainWindow", u"\u09a7\u09be\u09b0\u09be \u09ae\u09bf\u09b2\u09be\u0993", None))
        self.lbl_lesson_sub_heading_4.setText(QCoreApplication.translate("MainWindow", u"\u09aa\u09be\u09a0 \u09ae\u09c2\u09b2\u09cd\u09af\u09be\u09df\u09a8", None))
        self.label_8.setText("")
        self.label_10.setText("")
        self.label_11.setText("")
        self.seq_hint_lbl.setText("")
        self.label_17.setText("")
    # retranslateUi

