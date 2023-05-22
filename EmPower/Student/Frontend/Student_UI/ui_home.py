# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Frontend\PyQT_UI\home.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 719)
        MainWindow.setMinimumSize(QtCore.QSize(1280, 700))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(1280, 700))
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setMinimumSize(QtCore.QSize(1280, 700))
        self.stackedWidget.setStyleSheet("background-color: #F4F1DE;")
        self.stackedWidget.setObjectName("stackedWidget")
        self.home_page = QtWidgets.QWidget()
        self.home_page.setMinimumSize(QtCore.QSize(1280, 600))
        self.home_page.setObjectName("home_page")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.home_page)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.top_frame_3 = QtWidgets.QFrame(self.home_page)
        self.top_frame_3.setMinimumSize(QtCore.QSize(1300, 344))
        self.top_frame_3.setStyleSheet("")
        self.top_frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.top_frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top_frame_3.setObjectName("top_frame_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.top_frame_3)
        self.horizontalLayout.setContentsMargins(-1, 0, 0, 0)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_lesson = QtWidgets.QPushButton(self.top_frame_3)
        self.btn_lesson.setMaximumSize(QtCore.QSize(350, 280))
        self.btn_lesson.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_lesson.setStyleSheet("QPushButton {\n"
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
        self.btn_lesson.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\Frontend\\PyQT_UI\\../Images/lessons_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_lesson.setIcon(icon)
        self.btn_lesson.setIconSize(QtCore.QSize(400, 400))
        self.btn_lesson.setObjectName("btn_lesson")
        self.horizontalLayout.addWidget(self.btn_lesson)
        self.verticalLayout_3.addWidget(self.top_frame_3)
        self.bottom_frame_3 = QtWidgets.QFrame(self.home_page)
        self.bottom_frame_3.setMinimumSize(QtCore.QSize(1301, 151))
        self.bottom_frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bottom_frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bottom_frame_3.setObjectName("bottom_frame_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.bottom_frame_3)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.bottom_frame_3)
        self.label.setMinimumSize(QtCore.QSize(1280, 120))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(".\\Frontend\\PyQT_UI\\../Images/banner_icon.png"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.verticalLayout_3.addWidget(self.bottom_frame_3)
        self.stackedWidget.addWidget(self.home_page)
        self.lesson_page = QtWidgets.QWidget()
        self.lesson_page.setMinimumSize(QtCore.QSize(1280, 700))
        self.lesson_page.setObjectName("lesson_page")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.lesson_page)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.top_frame_2 = QtWidgets.QFrame(self.lesson_page)
        self.top_frame_2.setMinimumSize(QtCore.QSize(1280, 100))
        self.top_frame_2.setMaximumSize(QtCore.QSize(16777215, 100))
        self.top_frame_2.setStyleSheet("background-color: #E07A5F;\n"
"color: #3D405B; ")
        self.top_frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.top_frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top_frame_2.setObjectName("top_frame_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.top_frame_2)
        self.gridLayout_4.setContentsMargins(11, 11, 0, 4)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.lbl_lesson_headline = QtWidgets.QLabel(self.top_frame_2)
        self.lbl_lesson_headline.setMinimumSize(QtCore.QSize(1189, 58))
        font = QtGui.QFont()
        font.setFamily("Kalpurush")
        font.setPointSize(26)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lbl_lesson_headline.setFont(font)
        self.lbl_lesson_headline.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 26pt \"Kalpurush\";")
        self.lbl_lesson_headline.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_lesson_headline.setObjectName("lbl_lesson_headline")
        self.gridLayout_4.addWidget(self.lbl_lesson_headline, 0, 0, 1, 1)
        self.lbl_lesson_sub_heading = QtWidgets.QLabel(self.top_frame_2)
        self.lbl_lesson_sub_heading.setMinimumSize(QtCore.QSize(1189, 30))
        font = QtGui.QFont()
        font.setFamily("Kalpurush")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lbl_lesson_sub_heading.setFont(font)
        self.lbl_lesson_sub_heading.setStyleSheet("color: rgb(0, 0, 0);\n"
"padding-left: 5px;\n"
"font: 12pt \"Kalpurush\";")
        self.lbl_lesson_sub_heading.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_lesson_sub_heading.setObjectName("lbl_lesson_sub_heading")
        self.gridLayout_4.addWidget(self.lbl_lesson_sub_heading, 1, 0, 1, 1)
        self.gridLayout_3.addWidget(self.top_frame_2, 0, 0, 1, 1)
        self.frame = QtWidgets.QFrame(self.lesson_page)
        self.frame.setMinimumSize(QtCore.QSize(1280, 550))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setContentsMargins(11, 0, -1, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_prev_lesson = QtWidgets.QPushButton(self.frame)
        self.btn_prev_lesson.setMinimumSize(QtCore.QSize(70, 500))
        self.btn_prev_lesson.setMaximumSize(QtCore.QSize(60, 16777215))
        self.btn_prev_lesson.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_prev_lesson.setStyleSheet("QPushButton {\n"
"border: 3px solid #E07A5F;\n"
"border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover:!pressed {\n"
"background-color: #3D405B;\n"
"color: #F4F1DE;\n"
"}")
        self.btn_prev_lesson.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(".\\Frontend\\PyQT_UI\\../Images/backward.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_prev_lesson.setIcon(icon1)
        self.btn_prev_lesson.setIconSize(QtCore.QSize(150, 150))
        self.btn_prev_lesson.setObjectName("btn_prev_lesson")
        self.gridLayout.addWidget(self.btn_prev_lesson, 0, 0, 1, 1)
        self.middle_content_frame = QtWidgets.QFrame(self.frame)
        self.middle_content_frame.setMinimumSize(QtCore.QSize(1100, 585))
        self.middle_content_frame.setStyleSheet("background-color: rgb(244, 241, 222);\n"
"color: rgb(61, 64, 91);\n"
"border: none;")
        self.middle_content_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.middle_content_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.middle_content_frame.setObjectName("middle_content_frame")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.middle_content_frame)
        self.horizontalLayout_12.setContentsMargins(5, 10, 5, 10)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.mediaStackWidget = QtWidgets.QStackedWidget(self.middle_content_frame)
        self.mediaStackWidget.setMinimumSize(QtCore.QSize(651, 565))
        self.mediaStackWidget.setObjectName("mediaStackWidget")
        self.image_page = QtWidgets.QWidget()
        self.image_page.setObjectName("image_page")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.image_page)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.lsn_lbl_image = QtWidgets.QLabel(self.image_page)
        self.lsn_lbl_image.setMinimumSize(QtCore.QSize(690, 380))
        font = QtGui.QFont()
        font.setFamily("Kalpurush")
        font.setPointSize(30)
        self.lsn_lbl_image.setFont(font)
        self.lsn_lbl_image.setStyleSheet("border: 3px dotted rgb(227, 224, 207) ;\n"
"color: rgb(61, 64, 91);")
        self.lsn_lbl_image.setAlignment(QtCore.Qt.AlignCenter)
        self.lsn_lbl_image.setObjectName("lsn_lbl_image")
        self.horizontalLayout_9.addWidget(self.lsn_lbl_image)
        self.mediaStackWidget.addWidget(self.image_page)
        self.video_page = QtWidgets.QWidget()
        self.video_page.setObjectName("video_page")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.video_page)
        self.verticalLayout_5.setContentsMargins(0, 0, 5, 5)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.video_player_widget = QtWidgets.QHBoxLayout()
        self.video_player_widget.setObjectName("video_player_widget")
        self.verticalLayout_5.addLayout(self.video_player_widget)
        self.mediaStackWidget.addWidget(self.video_page)
        self.horizontalLayout_12.addWidget(self.mediaStackWidget)
        self.lsn_lbl_lesson_topic = QtWidgets.QLabel(self.middle_content_frame)
        self.lsn_lbl_lesson_topic.setMinimumSize(QtCore.QSize(434, 565))
        self.lsn_lbl_lesson_topic.setMaximumSize(QtCore.QSize(800, 16777215))
        font = QtGui.QFont()
        font.setFamily("Kalpurush")
        font.setPointSize(40)
        self.lsn_lbl_lesson_topic.setFont(font)
        self.lsn_lbl_lesson_topic.setStyleSheet("border: 3px dotted rgb(227, 224, 207) ;\n"
"color: rgb(61, 64, 91);")
        self.lsn_lbl_lesson_topic.setAlignment(QtCore.Qt.AlignCenter)
        self.lsn_lbl_lesson_topic.setWordWrap(True)
        self.lsn_lbl_lesson_topic.setObjectName("lsn_lbl_lesson_topic")
        self.horizontalLayout_12.addWidget(self.lsn_lbl_lesson_topic)
        self.gridLayout.addWidget(self.middle_content_frame, 0, 1, 1, 1)
        self.btn_next_lesson = QtWidgets.QPushButton(self.frame)
        self.btn_next_lesson.setMinimumSize(QtCore.QSize(70, 500))
        self.btn_next_lesson.setMaximumSize(QtCore.QSize(60, 16777215))
        self.btn_next_lesson.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_next_lesson.setStyleSheet("QPushButton {\n"
"border: 3px solid #E07A5F;\n"
"border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover:!pressed {\n"
"background-color: #3D405B;\n"
"color: #F4F1DE;\n"
"}")
        self.btn_next_lesson.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(".\\Frontend\\PyQT_UI\\../Images/forward.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_next_lesson.setIcon(icon2)
        self.btn_next_lesson.setIconSize(QtCore.QSize(150, 150))
        self.btn_next_lesson.setObjectName("btn_next_lesson")
        self.gridLayout.addWidget(self.btn_next_lesson, 0, 2, 1, 1)
        self.gridLayout_3.addWidget(self.frame, 1, 0, 1, 1)
        self.stackedWidget.addWidget(self.lesson_page)
        self.puzzle_page = QtWidgets.QWidget()
        self.puzzle_page.setObjectName("puzzle_page")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.puzzle_page)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.top_frame_4 = QtWidgets.QFrame(self.puzzle_page)
        self.top_frame_4.setMinimumSize(QtCore.QSize(1280, 100))
        self.top_frame_4.setMaximumSize(QtCore.QSize(16777215, 100))
        self.top_frame_4.setStyleSheet("background-color: #E07A5F;\n"
"color: #3D405B; ")
        self.top_frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.top_frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top_frame_4.setObjectName("top_frame_4")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.top_frame_4)
        self.gridLayout_5.setContentsMargins(11, 11, 0, 4)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.lbl_lesson_headline_2 = QtWidgets.QLabel(self.top_frame_4)
        self.lbl_lesson_headline_2.setMinimumSize(QtCore.QSize(1189, 58))
        font = QtGui.QFont()
        font.setFamily("Kalpurush")
        font.setPointSize(26)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lbl_lesson_headline_2.setFont(font)
        self.lbl_lesson_headline_2.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 26pt \"Kalpurush\";")
        self.lbl_lesson_headline_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_lesson_headline_2.setObjectName("lbl_lesson_headline_2")
        self.gridLayout_5.addWidget(self.lbl_lesson_headline_2, 0, 0, 1, 1)
        self.lbl_lesson_sub_heading_2 = QtWidgets.QLabel(self.top_frame_4)
        self.lbl_lesson_sub_heading_2.setMinimumSize(QtCore.QSize(1189, 30))
        font = QtGui.QFont()
        font.setFamily("Kalpurush")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lbl_lesson_sub_heading_2.setFont(font)
        self.lbl_lesson_sub_heading_2.setStyleSheet("color: rgb(0, 0, 0);\n"
"padding-left: 5px;\n"
"font: 12pt \"Kalpurush\";")
        self.lbl_lesson_sub_heading_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_lesson_sub_heading_2.setObjectName("lbl_lesson_sub_heading_2")
        self.gridLayout_5.addWidget(self.lbl_lesson_sub_heading_2, 1, 0, 1, 1)
        self.gridLayout_7.addWidget(self.top_frame_4, 0, 0, 1, 1)
        self.puzzle_main = QtWidgets.QFrame(self.puzzle_page)
        self.puzzle_main.setMinimumSize(QtCore.QSize(1280, 550))
        self.puzzle_main.setStyleSheet("")
        self.puzzle_main.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.puzzle_main.setFrameShadow(QtWidgets.QFrame.Raised)
        self.puzzle_main.setObjectName("puzzle_main")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.puzzle_main)
        self.gridLayout_2.setContentsMargins(11, 11, -1, -1)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.puzzle_frame = QtWidgets.QFrame(self.puzzle_main)
        self.puzzle_frame.setMinimumSize(QtCore.QSize(1100, 585))
        self.puzzle_frame.setStyleSheet("background-color: rgb(244, 241, 222);\n"
"color: rgb(61, 64, 91);\n"
"border: none;")
        self.puzzle_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.puzzle_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.puzzle_frame.setObjectName("puzzle_frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.puzzle_frame)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.puzzle_piece_frame = QtWidgets.QFrame(self.puzzle_frame)
        self.puzzle_piece_frame.setMinimumSize(QtCore.QSize(370, 571))
        self.puzzle_piece_frame.setMaximumSize(QtCore.QSize(291, 16777215))
        self.puzzle_piece_frame.setStyleSheet("")
        self.puzzle_piece_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.puzzle_piece_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.puzzle_piece_frame.setObjectName("puzzle_piece_frame")
        self.horizontalLayout_3.addWidget(self.puzzle_piece_frame)
        self.puzzle_widget_frame = QtWidgets.QFrame(self.puzzle_frame)
        self.puzzle_widget_frame.setMinimumSize(QtCore.QSize(865, 561))
        self.puzzle_widget_frame.setStyleSheet("")
        self.puzzle_widget_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.puzzle_widget_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.puzzle_widget_frame.setObjectName("puzzle_widget_frame")
        self.horizontalLayout_3.addWidget(self.puzzle_widget_frame)
        self.gridLayout_2.addWidget(self.puzzle_frame, 0, 0, 1, 1)
        self.gridLayout_7.addWidget(self.puzzle_main, 1, 0, 1, 1)
        self.stackedWidget.addWidget(self.puzzle_page)
        self.celebration_page = QtWidgets.QWidget()
        self.celebration_page.setObjectName("celebration_page")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.celebration_page)
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.celebration_frame = QtWidgets.QFrame(self.celebration_page)
        self.celebration_frame.setMinimumSize(QtCore.QSize(1280, 550))
        self.celebration_frame.setStyleSheet("border: 3px dot-dash rgb(61, 64, 91);\n"
"")
        self.celebration_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.celebration_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.celebration_frame.setObjectName("celebration_frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.celebration_frame)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.c_left_frame = QtWidgets.QFrame(self.celebration_frame)
        self.c_left_frame.setMinimumSize(QtCore.QSize(348, 691))
        self.c_left_frame.setMaximumSize(QtCore.QSize(384, 691))
        self.c_left_frame.setStyleSheet("border: none;\n"
"")
        self.c_left_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.c_left_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.c_left_frame.setObjectName("c_left_frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.c_left_frame)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(20, 250, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.c_prev_quiz_lbl = QtWidgets.QLabel(self.c_left_frame)
        self.c_prev_quiz_lbl.setMinimumSize(QtCore.QSize(369, 350))
        self.c_prev_quiz_lbl.setMaximumSize(QtCore.QSize(369, 16777215))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.c_prev_quiz_lbl.setFont(font)
        self.c_prev_quiz_lbl.setStyleSheet("")
        self.c_prev_quiz_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.c_prev_quiz_lbl.setWordWrap(True)
        self.c_prev_quiz_lbl.setObjectName("c_prev_quiz_lbl")
        self.verticalLayout_4.addWidget(self.c_prev_quiz_lbl)
        self.c_again = QtWidgets.QPushButton(self.c_left_frame)
        self.c_again.setMaximumSize(QtCore.QSize(359, 16777215))
        self.c_again.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.c_again.setStyleSheet("QPushButton {\n"
"border: 3px solid #E07A5F;\n"
"border-radius: 20px;\n"
"background-color:  #3D405B;\n"
"}\n"
"\n"
"QPushButton:hover:!pressed {\n"
"background-color: #3D405B;\n"
"background-color:  rgb(42, 44, 63);\n"
"}")
        self.c_again.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(".\\Frontend\\PyQT_UI\\../Images/repeat.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.c_again.setIcon(icon3)
        self.c_again.setIconSize(QtCore.QSize(35, 80))
        self.c_again.setObjectName("c_again")
        self.verticalLayout_4.addWidget(self.c_again)
        self.horizontalLayout_4.addWidget(self.c_left_frame)
        self.c_middle_frame = QtWidgets.QFrame(self.celebration_frame)
        self.c_middle_frame.setMinimumSize(QtCore.QSize(482, 691))
        self.c_middle_frame.setStyleSheet("border: none;\n"
"")
        self.c_middle_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.c_middle_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.c_middle_frame.setObjectName("c_middle_frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.c_middle_frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.c_lable = QtWidgets.QLabel(self.c_middle_frame)
        self.c_lable.setMinimumSize(QtCore.QSize(434, 194))
        self.c_lable.setMaximumSize(QtCore.QSize(16777215, 300))
        font = QtGui.QFont()
        font.setFamily("Kalpurush")
        font.setPointSize(61)
        self.c_lable.setFont(font)
        self.c_lable.setStyleSheet("background-color: none;")
        self.c_lable.setAlignment(QtCore.Qt.AlignCenter)
        self.c_lable.setObjectName("c_lable")
        self.verticalLayout.addWidget(self.c_lable)
        self.c_gif = QtWidgets.QLabel(self.c_middle_frame)
        self.c_gif.setMinimumSize(QtCore.QSize(390, 475))
        self.c_gif.setStyleSheet("background-color: none;")
        self.c_gif.setText("")
        self.c_gif.setObjectName("c_gif")
        self.verticalLayout.addWidget(self.c_gif)
        self.horizontalLayout_4.addWidget(self.c_middle_frame)
        self.c_right_frame = QtWidgets.QFrame(self.celebration_frame)
        self.c_right_frame.setMinimumSize(QtCore.QSize(360, 691))
        self.c_right_frame.setMaximumSize(QtCore.QSize(378, 691))
        self.c_right_frame.setStyleSheet("border: none;\n"
"")
        self.c_right_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.c_right_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.c_right_frame.setObjectName("c_right_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.c_right_frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(20, 306, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.c_next_quiz_lbl = QtWidgets.QLabel(self.c_right_frame)
        self.c_next_quiz_lbl.setMinimumSize(QtCore.QSize(369, 350))
        self.c_next_quiz_lbl.setMaximumSize(QtCore.QSize(369, 16777215))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.c_next_quiz_lbl.setFont(font)
        self.c_next_quiz_lbl.setStyleSheet("")
        self.c_next_quiz_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.c_next_quiz_lbl.setObjectName("c_next_quiz_lbl")
        self.verticalLayout_2.addWidget(self.c_next_quiz_lbl)
        self.c_next_quiz = QtWidgets.QPushButton(self.c_right_frame)
        self.c_next_quiz.setMaximumSize(QtCore.QSize(353, 16777215))
        self.c_next_quiz.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.c_next_quiz.setStyleSheet("QPushButton {\n"
"border: 3px solid #E07A5F;\n"
"border-radius: 20px;\n"
"background-color:  #3D405B;\n"
"}\n"
"\n"
"QPushButton:hover:!pressed {\n"
"background-color: #3D405B;\n"
"background-color:  rgb(42, 44, 63);\n"
"}")
        self.c_next_quiz.setText("")
        self.c_next_quiz.setIcon(icon2)
        self.c_next_quiz.setIconSize(QtCore.QSize(90, 80))
        self.c_next_quiz.setObjectName("c_next_quiz")
        self.verticalLayout_2.addWidget(self.c_next_quiz)
        self.horizontalLayout_4.addWidget(self.c_right_frame)
        self.gridLayout_9.addWidget(self.celebration_frame, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.celebration_page)
        self.navigation_page = QtWidgets.QWidget()
        self.navigation_page.setObjectName("navigation_page")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.navigation_page)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.navigation_frame = QtWidgets.QFrame(self.navigation_page)
        self.navigation_frame.setMinimumSize(QtCore.QSize(1280, 550))
        self.navigation_frame.setStyleSheet("border: 3px dot-dash rgb(61, 64, 91);\n"
"")
        self.navigation_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.navigation_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.navigation_frame.setObjectName("navigation_frame")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.navigation_frame)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.n_middle_frame = QtWidgets.QFrame(self.navigation_frame)
        self.n_middle_frame.setMinimumSize(QtCore.QSize(623, 691))
        self.n_middle_frame.setMaximumSize(QtCore.QSize(623, 691))
        self.n_middle_frame.setStyleSheet("border: none;")
        self.n_middle_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.n_middle_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.n_middle_frame.setObjectName("n_middle_frame")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.n_middle_frame)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.n_message = QtWidgets.QLabel(self.n_middle_frame)
        self.n_message.setMinimumSize(QtCore.QSize(434, 194))
        self.n_message.setMaximumSize(QtCore.QSize(16777215, 300))
        font = QtGui.QFont()
        font.setFamily("Kalpurush")
        font.setPointSize(39)
        font.setBold(False)
        font.setWeight(50)
        self.n_message.setFont(font)
        self.n_message.setStyleSheet("background-color: none;")
        self.n_message.setAlignment(QtCore.Qt.AlignCenter)
        self.n_message.setWordWrap(True)
        self.n_message.setObjectName("n_message")
        self.verticalLayout_7.addWidget(self.n_message)
        self.n_icon = QtWidgets.QLabel(self.n_middle_frame)
        self.n_icon.setMinimumSize(QtCore.QSize(390, 475))
        self.n_icon.setStyleSheet("background-color: none;\n"
"border: none;")
        self.n_icon.setText("")
        self.n_icon.setPixmap(QtGui.QPixmap(".\\Frontend\\PyQT_UI\\../Images/evaluation_icon.png"))
        self.n_icon.setAlignment(QtCore.Qt.AlignCenter)
        self.n_icon.setObjectName("n_icon")
        self.verticalLayout_7.addWidget(self.n_icon)
        self.horizontalLayout_5.addWidget(self.n_middle_frame)
        self.n_right_frame = QtWidgets.QFrame(self.navigation_frame)
        self.n_right_frame.setMinimumSize(QtCore.QSize(622, 691))
        self.n_right_frame.setMaximumSize(QtCore.QSize(630, 691))
        self.n_right_frame.setStyleSheet("border: none;\n"
"")
        self.n_right_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.n_right_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.n_right_frame.setObjectName("n_right_frame")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.n_right_frame)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.n_type_lbl = QtWidgets.QLabel(self.n_right_frame)
        self.n_type_lbl.setMinimumSize(QtCore.QSize(520, 520))
        self.n_type_lbl.setMaximumSize(QtCore.QSize(520, 520))
        font = QtGui.QFont()
        font.setPointSize(55)
        self.n_type_lbl.setFont(font)
        self.n_type_lbl.setStyleSheet("border: 3px solid rgb(61, 64, 91);")
        self.n_type_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.n_type_lbl.setObjectName("n_type_lbl")
        self.gridLayout_6.addWidget(self.n_type_lbl, 0, 0, 1, 1)
        self.n_proceed_btn = QtWidgets.QPushButton(self.n_right_frame)
        self.n_proceed_btn.setMinimumSize(QtCore.QSize(271, 101))
        self.n_proceed_btn.setMaximumSize(QtCore.QSize(353, 16777215))
        self.n_proceed_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.n_proceed_btn.setStyleSheet("QPushButton {\n"
"border: 3px solid #E07A5F;\n"
"border-radius: 20px;\n"
"background-color:  rgb(61, 64, 91);\n"
"}\n"
"\n"
"QPushButton:hover:!pressed {\n"
"background-color: #3D405B;\n"
"background-color:  rgb(35, 37, 53);\n"
"}")
        self.n_proceed_btn.setText("")
        self.n_proceed_btn.setIcon(icon2)
        self.n_proceed_btn.setIconSize(QtCore.QSize(90, 80))
        self.n_proceed_btn.setObjectName("n_proceed_btn")
        self.gridLayout_6.addWidget(self.n_proceed_btn, 1, 0, 1, 1)
        self.horizontalLayout_5.addWidget(self.n_right_frame)
        self.horizontalLayout_7.addWidget(self.navigation_frame)
        self.stackedWidget.addWidget(self.navigation_page)
        self.horizontalLayout_6.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(4)
        self.mediaStackWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lbl_lesson_headline.setText(_translate("MainWindow", "পাঠ ১"))
        self.lbl_lesson_sub_heading.setText(_translate("MainWindow", "নাম শিখন - মডিউল ১"))
        self.lsn_lbl_image.setText(_translate("MainWindow", "ছবি"))
        self.lsn_lbl_lesson_topic.setText(_translate("MainWindow", "পরিচয়"))
        self.btn_next_lesson.setShortcut(_translate("MainWindow", "Space"))
        self.lbl_lesson_headline_2.setText(_translate("MainWindow", "ধাঁধা"))
        self.lbl_lesson_sub_heading_2.setText(_translate("MainWindow", "পাঠ মূল্যায়ন"))
        self.c_prev_quiz_lbl.setText(_translate("MainWindow", "পুনরায় অংশগ্রহণ করুন "))
        self.c_lable.setText(_translate("MainWindow", "অভিনন্দন!!!"))
        self.c_next_quiz_lbl.setText(_translate("MainWindow", "পরবর্তী মূল্যায়ন"))
        self.n_message.setText(_translate("MainWindow", "অভিনন্দন!!! তুমি পাঠসমূহ সম্পন্ন করেছো"))
        self.n_type_lbl.setText(_translate("MainWindow", "ধাঁধা"))
        self.n_proceed_btn.setShortcut(_translate("MainWindow", "Space"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
