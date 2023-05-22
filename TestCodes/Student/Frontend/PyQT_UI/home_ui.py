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
        MainWindow.resize(1280, 719)
        MainWindow.setMinimumSize(QSize(1280, 700))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(1280, 700))
        self.horizontalLayout_6 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
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
        self.c_left_frame = QFrame(self.celebration_frame)
        self.c_left_frame.setObjectName(u"c_left_frame")
        self.c_left_frame.setMinimumSize(QSize(348, 691))
        self.c_left_frame.setMaximumSize(QSize(384, 691))
        self.c_left_frame.setStyleSheet(u"border: none;\n"
"")
        self.c_left_frame.setFrameShape(QFrame.StyledPanel)
        self.c_left_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.c_left_frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalSpacer_4 = QSpacerItem(20, 250, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_4)

        self.c_prev_quiz_lbl = QLabel(self.c_left_frame)
        self.c_prev_quiz_lbl.setObjectName(u"c_prev_quiz_lbl")
        self.c_prev_quiz_lbl.setMinimumSize(QSize(369, 350))
        self.c_prev_quiz_lbl.setMaximumSize(QSize(369, 16777215))
        font4 = QFont()
        font4.setPointSize(30)
        self.c_prev_quiz_lbl.setFont(font4)
        self.c_prev_quiz_lbl.setStyleSheet(u"")
        self.c_prev_quiz_lbl.setAlignment(Qt.AlignCenter)
        self.c_prev_quiz_lbl.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.c_prev_quiz_lbl)

        self.c_again = QPushButton(self.c_left_frame)
        self.c_again.setObjectName(u"c_again")
        self.c_again.setMaximumSize(QSize(359, 16777215))
        self.c_again.setCursor(QCursor(Qt.PointingHandCursor))
        self.c_again.setStyleSheet(u"QPushButton {\n"
"border: 3px solid #E07A5F;\n"
"border-radius: 20px;\n"
"background-color:  #3D405B;\n"
"}\n"
"\n"
"QPushButton:hover:!pressed {\n"
"background-color: #3D405B;\n"
"background-color:  rgb(42, 44, 63);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"../Images/repeat.png", QSize(), QIcon.Normal, QIcon.Off)
        self.c_again.setIcon(icon3)
        self.c_again.setIconSize(QSize(35, 80))

        self.verticalLayout_4.addWidget(self.c_again)


        self.horizontalLayout_4.addWidget(self.c_left_frame)

        self.c_middle_frame = QFrame(self.celebration_frame)
        self.c_middle_frame.setObjectName(u"c_middle_frame")
        self.c_middle_frame.setMinimumSize(QSize(482, 691))
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
        font5 = QFont()
        font5.setFamilies([u"Kalpurush"])
        font5.setPointSize(61)
        self.c_lable.setFont(font5)
        self.c_lable.setStyleSheet(u"background-color: none;")
        self.c_lable.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.c_lable)

        self.c_gif = QLabel(self.c_middle_frame)
        self.c_gif.setObjectName(u"c_gif")
        self.c_gif.setMinimumSize(QSize(390, 475))
        self.c_gif.setStyleSheet(u"background-color: none;")

        self.verticalLayout.addWidget(self.c_gif)


        self.horizontalLayout_4.addWidget(self.c_middle_frame)

        self.c_right_frame = QFrame(self.celebration_frame)
        self.c_right_frame.setObjectName(u"c_right_frame")
        self.c_right_frame.setMinimumSize(QSize(360, 691))
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
        self.c_next_quiz_lbl.setFont(font4)
        self.c_next_quiz_lbl.setStyleSheet(u"")
        self.c_next_quiz_lbl.setAlignment(Qt.AlignCenter)

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
        self.navigation_frame.setMinimumSize(QSize(1280, 550))
        self.navigation_frame.setStyleSheet(u"border: 3px dot-dash rgb(61, 64, 91);\n"
"")
        self.navigation_frame.setFrameShape(QFrame.StyledPanel)
        self.navigation_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.navigation_frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.n_middle_frame = QFrame(self.navigation_frame)
        self.n_middle_frame.setObjectName(u"n_middle_frame")
        self.n_middle_frame.setMinimumSize(QSize(623, 691))
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
        self.n_icon.setMinimumSize(QSize(390, 475))
        self.n_icon.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.n_icon.setPixmap(QPixmap(u"../Images/evaluation_icon.png"))
        self.n_icon.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.n_icon)


        self.horizontalLayout_5.addWidget(self.n_middle_frame)

        self.n_right_frame = QFrame(self.navigation_frame)
        self.n_right_frame.setObjectName(u"n_right_frame")
        self.n_right_frame.setMinimumSize(QSize(622, 691))
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

        self.horizontalLayout_6.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(4)
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
#if QT_CONFIG(shortcut)
        self.btn_next_lesson.setShortcut(QCoreApplication.translate("MainWindow", u"Space", None))
#endif // QT_CONFIG(shortcut)
        self.lbl_lesson_headline_2.setText(QCoreApplication.translate("MainWindow", u"\u09a7\u09be\u0981\u09a7\u09be", None))
        self.lbl_lesson_sub_heading_2.setText(QCoreApplication.translate("MainWindow", u"\u09aa\u09be\u09a0 \u09ae\u09c2\u09b2\u09cd\u09af\u09be\u09df\u09a8", None))
        self.c_prev_quiz_lbl.setText(QCoreApplication.translate("MainWindow", u"\u09aa\u09c1\u09a8\u09b0\u09be\u09df \u0985\u0982\u09b6\u0997\u09cd\u09b0\u09b9\u09a3 \u0995\u09b0\u09c1\u09a8 ", None))
        self.c_again.setText("")
        self.c_lable.setText(QCoreApplication.translate("MainWindow", u"\u0985\u09ad\u09bf\u09a8\u09a8\u09cd\u09a6\u09a8!!!", None))
        self.c_gif.setText("")
        self.c_next_quiz_lbl.setText(QCoreApplication.translate("MainWindow", u"\u09aa\u09b0\u09ac\u09b0\u09cd\u09a4\u09c0 \u09ae\u09c2\u09b2\u09cd\u09af\u09be\u09df\u09a8", None))
        self.c_next_quiz.setText("")
        self.n_message.setText(QCoreApplication.translate("MainWindow", u"\u0985\u09ad\u09bf\u09a8\u09a8\u09cd\u09a6\u09a8!!! \u09a4\u09c1\u09ae\u09bf \u09aa\u09be\u09a0\u09b8\u09ae\u09c2\u09b9 \u09b8\u09ae\u09cd\u09aa\u09a8\u09cd\u09a8 \u0995\u09b0\u09c7\u099b\u09cb", None))
        self.n_icon.setText("")
        self.n_type_lbl.setText(QCoreApplication.translate("MainWindow", u"\u09a7\u09be\u0981\u09a7\u09be", None))
        self.n_proceed_btn.setText("")
#if QT_CONFIG(shortcut)
        self.n_proceed_btn.setShortcut(QCoreApplication.translate("MainWindow", u"Space", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi
