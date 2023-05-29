# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'HomePage.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QComboBox,
    QFrame, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QListView, QListWidget,
    QListWidgetItem, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QTableWidget, QTableWidgetItem,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setMinimumSize(QSize(1280, 720))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(1280, 720))
        self.gridLayout_30 = QGridLayout(self.centralwidget)
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.gridLayout_30.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(1280, 720))
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.home_page.setMinimumSize(QSize(0, 680))
        self.horizontalLayout_3 = QHBoxLayout(self.home_page)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.home_frame = QFrame(self.home_page)
        self.home_frame.setObjectName(u"home_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.home_frame.sizePolicy().hasHeightForWidth())
        self.home_frame.setSizePolicy(sizePolicy)
        self.home_frame.setMinimumSize(QSize(1280, 720))
        self.home_frame.setMaximumSize(QSize(16777215, 16777215))
        self.home_frame.setStyleSheet(u"background-color: rgb(0, 43, 91);")
        self.gridLayout = QGridLayout(self.home_frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer, 0, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(10, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_2, 2, 0, 1, 1)

        self.frm_banner_pic = QFrame(self.home_frame)
        self.frm_banner_pic.setObjectName(u"frm_banner_pic")
        self.frm_banner_pic.setMaximumSize(QSize(1200, 200))
        self.frm_banner_pic.setStyleSheet(u"border: none;")
        self.frm_banner_pic.setFrameShape(QFrame.StyledPanel)
        self.frm_banner_pic.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frm_banner_pic)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.home_lbl_ban_picture = QLabel(self.frm_banner_pic)
        self.home_lbl_ban_picture.setObjectName(u"home_lbl_ban_picture")
        self.home_lbl_ban_picture.setLayoutDirection(Qt.LeftToRight)
        self.home_lbl_ban_picture.setStyleSheet(u"border: none;")
        self.home_lbl_ban_picture.setFrameShape(QFrame.StyledPanel)
        self.home_lbl_ban_picture.setPixmap(QPixmap(u"../Images/banner_logo.png"))
        self.home_lbl_ban_picture.setScaledContents(False)
        self.home_lbl_ban_picture.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.home_lbl_ban_picture)


        self.gridLayout.addWidget(self.frm_banner_pic, 1, 0, 1, 1)

        self.frm_button = QFrame(self.home_frame)
        self.frm_button.setObjectName(u"frm_button")
        self.frm_button.setMinimumSize(QSize(1080, 190))
        self.frm_button.setMaximumSize(QSize(1270, 190))
        self.frm_button.setStyleSheet(u"")
        self.frm_button.setFrameShape(QFrame.StyledPanel)
        self.frm_button.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frm_button)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.home_btn_student = QPushButton(self.frm_button)
        self.home_btn_student.setObjectName(u"home_btn_student")
        sizePolicy.setHeightForWidth(self.home_btn_student.sizePolicy().hasHeightForWidth())
        self.home_btn_student.setSizePolicy(sizePolicy)
        self.home_btn_student.setMinimumSize(QSize(160, 150))
        self.home_btn_student.setMaximumSize(QSize(200, 200))
        font = QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setStyleStrategy(QFont.PreferDefault)
        self.home_btn_student.setFont(font)
        self.home_btn_student.setCursor(QCursor(Qt.PointingHandCursor))
        self.home_btn_student.setMouseTracking(True)
        self.home_btn_student.setAcceptDrops(True)
        self.home_btn_student.setStyleSheet(u"QPushButton {\n"
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
        icon.addFile(u"../Images/reg_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.home_btn_student.setIcon(icon)
        self.home_btn_student.setIconSize(QSize(250, 300))
        self.home_btn_student.setFlat(False)

        self.horizontalLayout_2.addWidget(self.home_btn_student)

        self.home_btn_lesson = QPushButton(self.frm_button)
        self.home_btn_lesson.setObjectName(u"home_btn_lesson")
        sizePolicy.setHeightForWidth(self.home_btn_lesson.sizePolicy().hasHeightForWidth())
        self.home_btn_lesson.setSizePolicy(sizePolicy)
        self.home_btn_lesson.setMinimumSize(QSize(160, 150))
        self.home_btn_lesson.setMaximumSize(QSize(200, 200))
        self.home_btn_lesson.setCursor(QCursor(Qt.PointingHandCursor))
        self.home_btn_lesson.setStyleSheet(u"QPushButton {\n"
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
        icon1.addFile(u"../Images/std_lsn.png", QSize(), QIcon.Normal, QIcon.Off)
        self.home_btn_lesson.setIcon(icon1)
        self.home_btn_lesson.setIconSize(QSize(250, 300))

        self.horizontalLayout_2.addWidget(self.home_btn_lesson)

        self.home_btn_lesson_assigns = QPushButton(self.frm_button)
        self.home_btn_lesson_assigns.setObjectName(u"home_btn_lesson_assigns")
        sizePolicy.setHeightForWidth(self.home_btn_lesson_assigns.sizePolicy().hasHeightForWidth())
        self.home_btn_lesson_assigns.setSizePolicy(sizePolicy)
        self.home_btn_lesson_assigns.setMinimumSize(QSize(160, 150))
        self.home_btn_lesson_assigns.setMaximumSize(QSize(200, 200))
        self.home_btn_lesson_assigns.setCursor(QCursor(Qt.PointingHandCursor))
        self.home_btn_lesson_assigns.setStyleSheet(u"QPushButton {\n"
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
        icon2.addFile(u"../Images/assign_records_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.home_btn_lesson_assigns.setIcon(icon2)
        self.home_btn_lesson_assigns.setIconSize(QSize(250, 300))

        self.horizontalLayout_2.addWidget(self.home_btn_lesson_assigns)

        self.home_btn_quiz = QPushButton(self.frm_button)
        self.home_btn_quiz.setObjectName(u"home_btn_quiz")
        sizePolicy.setHeightForWidth(self.home_btn_quiz.sizePolicy().hasHeightForWidth())
        self.home_btn_quiz.setSizePolicy(sizePolicy)
        self.home_btn_quiz.setMinimumSize(QSize(160, 150))
        self.home_btn_quiz.setMaximumSize(QSize(200, 200))
        self.home_btn_quiz.setCursor(QCursor(Qt.PointingHandCursor))
        self.home_btn_quiz.setStyleSheet(u"QPushButton {\n"
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
        icon3.addFile(u"../Images/std_assessment.png", QSize(), QIcon.Normal, QIcon.Off)
        self.home_btn_quiz.setIcon(icon3)
        self.home_btn_quiz.setIconSize(QSize(250, 300))

        self.horizontalLayout_2.addWidget(self.home_btn_quiz)

        self.home_btn_progress = QPushButton(self.frm_button)
        self.home_btn_progress.setObjectName(u"home_btn_progress")
        sizePolicy.setHeightForWidth(self.home_btn_progress.sizePolicy().hasHeightForWidth())
        self.home_btn_progress.setSizePolicy(sizePolicy)
        self.home_btn_progress.setMinimumSize(QSize(160, 150))
        self.home_btn_progress.setMaximumSize(QSize(200, 200))
        self.home_btn_progress.setCursor(QCursor(Qt.PointingHandCursor))
        self.home_btn_progress.setStyleSheet(u"QPushButton {\n"
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
        icon4.addFile(u"../Images/std_perfor.png", QSize(), QIcon.Normal, QIcon.Off)
        self.home_btn_progress.setIcon(icon4)
        self.home_btn_progress.setIconSize(QSize(250, 300))

        self.horizontalLayout_2.addWidget(self.home_btn_progress)


        self.gridLayout.addWidget(self.frm_button, 3, 0, 1, 1)


        self.horizontalLayout_3.addWidget(self.home_frame)

        self.stackedWidget.addWidget(self.home_page)
        self.student_page = QWidget()
        self.student_page.setObjectName(u"student_page")
        self.student_page.setMinimumSize(QSize(1280, 720))
        self.horizontalLayout = QHBoxLayout(self.student_page)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.student_frame = QFrame(self.student_page)
        self.student_frame.setObjectName(u"student_frame")
        self.student_frame.setMinimumSize(QSize(1280, 720))
        self.student_frame.setStyleSheet(u"border-radius: 0;")
        self.student_frame.setFrameShape(QFrame.StyledPanel)
        self.student_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.student_frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.top_frame = QFrame(self.student_frame)
        self.top_frame.setObjectName(u"top_frame")
        self.top_frame.setMinimumSize(QSize(1251, 91))
        self.top_frame.setStyleSheet(u"background-color: #2B4865;")
        self.top_frame.setFrameShape(QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.top_frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.std_btn_back_to_home = QPushButton(self.top_frame)
        self.std_btn_back_to_home.setObjectName(u"std_btn_back_to_home")
        sizePolicy.setHeightForWidth(self.std_btn_back_to_home.sizePolicy().hasHeightForWidth())
        self.std_btn_back_to_home.setSizePolicy(sizePolicy)
        self.std_btn_back_to_home.setMinimumSize(QSize(0, 60))
        self.std_btn_back_to_home.setMaximumSize(QSize(60, 60))
        self.std_btn_back_to_home.setBaseSize(QSize(0, 4))
        font1 = QFont()
        font1.setPointSize(11)
        self.std_btn_back_to_home.setFont(font1)
        self.std_btn_back_to_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.std_btn_back_to_home.setMouseTracking(True)
        self.std_btn_back_to_home.setStyleSheet(u"QPushButton {\n"
"	background-color: #2B4865 #256D85;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover:!pressed\n"
"{\n"
"	background-color:  #256D85;\n"
"	border-radius: 30px;\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u"../Images/back_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.std_btn_back_to_home.setIcon(icon5)
        self.std_btn_back_to_home.setIconSize(QSize(200, 200))
        self.std_btn_back_to_home.setAutoDefault(False)
        self.std_btn_back_to_home.setFlat(False)

        self.horizontalLayout_4.addWidget(self.std_btn_back_to_home)

        self.std_lbl_headline = QLabel(self.top_frame)
        self.std_lbl_headline.setObjectName(u"std_lbl_headline")
        font2 = QFont()
        font2.setFamilies([u"Hind Siliguri Medium"])
        font2.setPointSize(27)
        self.std_lbl_headline.setFont(font2)
        self.std_lbl_headline.setStyleSheet(u"color: #8FE3CF")
        self.std_lbl_headline.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.std_lbl_headline)


        self.verticalLayout.addWidget(self.top_frame)

        self.mid_frame = QFrame(self.student_frame)
        self.mid_frame.setObjectName(u"mid_frame")
        self.mid_frame.setMinimumSize(QSize(1251, 661))
        self.mid_frame.setStyleSheet(u"background-color: rgb(255, 220, 243);")
        self.mid_frame.setFrameShape(QFrame.StyledPanel)
        self.mid_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.mid_frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.std_tableWidget = QTableWidget(self.mid_frame)
        if (self.std_tableWidget.columnCount() < 6):
            self.std_tableWidget.setColumnCount(6)
        font3 = QFont()
        font3.setFamilies([u"Hind Siliguri Medium"])
        font3.setPointSize(13)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem.setFont(font3);
        self.std_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem1.setFont(font3);
        self.std_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem2.setFont(font3);
        self.std_tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem3.setFont(font3);
        self.std_tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem4.setFont(font3);
        self.std_tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        font4 = QFont()
        font4.setFamilies([u"Hind Siliguri Medium"])
        font4.setPointSize(13)
        font4.setKerning(True)
        font4.setStyleStrategy(QFont.PreferDefault)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem5.setFont(font4);
        self.std_tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.std_tableWidget.setObjectName(u"std_tableWidget")
        self.std_tableWidget.setFont(font1)
        self.std_tableWidget.setStyleSheet(u"QHeaderView::section {\n"
"	background-color: #002B5B;\n"
"    color: rgb(143, 227, 207);\n"
"}\n"
"\n"
"\n"
"\n"
"QTableWidget {\n"
"	background-color: #256D85;\n"
"	gridline-color: rgb(255, 255, 255);\n"
"	color: #fff;\n"
"}\n"
"\n"
"")
        self.std_tableWidget.setFrameShape(QFrame.NoFrame)
        self.std_tableWidget.setFrameShadow(QFrame.Raised)
        self.std_tableWidget.setLineWidth(1)
        self.std_tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.std_tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.std_tableWidget.setAlternatingRowColors(False)
        self.std_tableWidget.setTextElideMode(Qt.ElideLeft)
        self.std_tableWidget.setShowGrid(True)
        self.std_tableWidget.setGridStyle(Qt.SolidLine)
        self.std_tableWidget.setSortingEnabled(True)
        self.std_tableWidget.setCornerButtonEnabled(True)
        self.std_tableWidget.setRowCount(0)
        self.std_tableWidget.setColumnCount(6)
        self.std_tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.std_tableWidget.horizontalHeader().setDefaultSectionSize(170)
        self.std_tableWidget.horizontalHeader().setHighlightSections(True)
        self.std_tableWidget.horizontalHeader().setProperty("showSortIndicator", True)
        self.std_tableWidget.horizontalHeader().setStretchLastSection(True)
        self.std_tableWidget.verticalHeader().setVisible(False)
        self.std_tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.std_tableWidget.verticalHeader().setMinimumSectionSize(29)
        self.std_tableWidget.verticalHeader().setDefaultSectionSize(35)

        self.horizontalLayout_5.addWidget(self.std_tableWidget)


        self.verticalLayout.addWidget(self.mid_frame)

        self.bottom_frame = QFrame(self.student_frame)
        self.bottom_frame.setObjectName(u"bottom_frame")
        self.bottom_frame.setMinimumSize(QSize(1251, 83))
        self.bottom_frame.setStyleSheet(u"background-color: rgb(42, 70, 98);")
        self.bottom_frame.setFrameShape(QFrame.StyledPanel)
        self.bottom_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.bottom_frame)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_4 = QSpacerItem(38, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_4)

        self.std_btn_add_student = QPushButton(self.bottom_frame)
        self.std_btn_add_student.setObjectName(u"std_btn_add_student")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(230)
        sizePolicy1.setVerticalStretch(40)
        sizePolicy1.setHeightForWidth(self.std_btn_add_student.sizePolicy().hasHeightForWidth())
        self.std_btn_add_student.setSizePolicy(sizePolicy1)
        self.std_btn_add_student.setMinimumSize(QSize(251, 41))
        font5 = QFont()
        font5.setFamilies([u"Hind Siliguri Medium"])
        font5.setPointSize(12)
        font5.setBold(False)
        self.std_btn_add_student.setFont(font5)
        self.std_btn_add_student.setCursor(QCursor(Qt.PointingHandCursor))
        self.std_btn_add_student.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(160, 253, 230);\n"
"color:  #256D85 ;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	\n"
"	background-color: rgb(143, 227, 207);\n"
"	color: #2B4865;\n"
"\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u"../../../../../../Cache_Empower/V6/Teacher/Frontend/Images/add_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.std_btn_add_student.setIcon(icon6)
        self.std_btn_add_student.setIconSize(QSize(25, 25))

        self.horizontalLayout_6.addWidget(self.std_btn_add_student)

        self.horizontalSpacer = QSpacerItem(78, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.std_btn_update_info = QPushButton(self.bottom_frame)
        self.std_btn_update_info.setObjectName(u"std_btn_update_info")
        sizePolicy1.setHeightForWidth(self.std_btn_update_info.sizePolicy().hasHeightForWidth())
        self.std_btn_update_info.setSizePolicy(sizePolicy1)
        self.std_btn_update_info.setMinimumSize(QSize(290, 40))
        self.std_btn_update_info.setFont(font5)
        self.std_btn_update_info.setCursor(QCursor(Qt.PointingHandCursor))
        self.std_btn_update_info.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(160, 253, 230);\n"
"color:  #256D85 ;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	\n"
"	background-color: rgb(143, 227, 207);\n"
"	color: #2B4865;\n"
"\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u"../Images/edit_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.std_btn_update_info.setIcon(icon7)
        self.std_btn_update_info.setIconSize(QSize(20, 25))

        self.horizontalLayout_6.addWidget(self.std_btn_update_info)

        self.horizontalSpacer_2 = QSpacerItem(78, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)

        self.std_btn_remove_student = QPushButton(self.bottom_frame)
        self.std_btn_remove_student.setObjectName(u"std_btn_remove_student")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(230)
        sizePolicy2.setVerticalStretch(40)
        sizePolicy2.setHeightForWidth(self.std_btn_remove_student.sizePolicy().hasHeightForWidth())
        self.std_btn_remove_student.setSizePolicy(sizePolicy2)
        self.std_btn_remove_student.setMinimumSize(QSize(260, 40))
        font6 = QFont()
        font6.setFamilies([u"Hind Siliguri Medium"])
        font6.setPointSize(12)
        self.std_btn_remove_student.setFont(font6)
        self.std_btn_remove_student.setCursor(QCursor(Qt.PointingHandCursor))
        self.std_btn_remove_student.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(160, 253, 230);\n"
"color:  #256D85 ;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	\n"
"	background-color: rgb(143, 227, 207);\n"
"	color: #2B4865;\n"
"\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u"../Images/trash_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.std_btn_remove_student.setIcon(icon8)

        self.horizontalLayout_6.addWidget(self.std_btn_remove_student)

        self.horizontalSpacer_3 = QSpacerItem(38, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addWidget(self.bottom_frame)


        self.horizontalLayout.addWidget(self.student_frame)

        self.stackedWidget.addWidget(self.student_page)
        self.lesson_page = QWidget()
        self.lesson_page.setObjectName(u"lesson_page")
        self.horizontalLayout_11 = QHBoxLayout(self.lesson_page)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.lesson_frame = QFrame(self.lesson_page)
        self.lesson_frame.setObjectName(u"lesson_frame")
        self.lesson_frame.setMinimumSize(QSize(1280, 720))
        self.lesson_frame.setStyleSheet(u"")
        self.lesson_frame.setFrameShape(QFrame.StyledPanel)
        self.lesson_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.lesson_frame)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.mid_frame_2 = QFrame(self.lesson_frame)
        self.mid_frame_2.setObjectName(u"mid_frame_2")
        self.mid_frame_2.setMinimumSize(QSize(1180, 520))
        self.mid_frame_2.setStyleSheet(u"background-color:rgb(36, 105, 127);")
        self.mid_frame_2.setFrameShape(QFrame.StyledPanel)
        self.mid_frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.mid_frame_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.bottom_top_frame = QFrame(self.mid_frame_2)
        self.bottom_top_frame.setObjectName(u"bottom_top_frame")
        self.bottom_top_frame.setMinimumSize(QSize(0, 60))
        self.bottom_top_frame.setMaximumSize(QSize(16777215, 60))
        self.bottom_top_frame.setStyleSheet(u"background-color: rgb(36, 105, 127);\n"
"color: rgb(137, 218, 199);\n"
"")
        self.bottom_top_frame.setFrameShape(QFrame.StyledPanel)
        self.bottom_top_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.bottom_top_frame)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_5 = QSpacerItem(141, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_5)

        self.lsn_lbl_category = QLabel(self.bottom_top_frame)
        self.lsn_lbl_category.setObjectName(u"lsn_lbl_category")
        font7 = QFont()
        font7.setPointSize(16)
        self.lsn_lbl_category.setFont(font7)
        self.lsn_lbl_category.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.lsn_lbl_category)

        self.lsn_cmb_category = QComboBox(self.bottom_top_frame)
        self.lsn_cmb_category.addItem("")
        self.lsn_cmb_category.addItem("")
        self.lsn_cmb_category.addItem("")
        self.lsn_cmb_category.addItem("")
        self.lsn_cmb_category.addItem("")
        self.lsn_cmb_category.setObjectName(u"lsn_cmb_category")
        self.lsn_cmb_category.setMinimumSize(QSize(280, 40))
        font8 = QFont()
        font8.setFamilies([u"Hind Siliguri"])
        font8.setPointSize(10)
        font8.setBold(False)
        self.lsn_cmb_category.setFont(font8)
        self.lsn_cmb_category.setCursor(QCursor(Qt.PointingHandCursor))
        self.lsn_cmb_category.setStyleSheet(u"background-color: rgb(137, 218, 199);\n"
"padding-left: 15px;\n"
"border-radius: 10px;\n"
"color: rgb(43, 72, 101);")

        self.horizontalLayout_8.addWidget(self.lsn_cmb_category)

        self.horizontalSpacer_6 = QSpacerItem(143, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_6)

        self.lsn_lbl_lessons = QLabel(self.bottom_top_frame)
        self.lsn_lbl_lessons.setObjectName(u"lsn_lbl_lessons")
        self.lsn_lbl_lessons.setFont(font7)
        self.lsn_lbl_lessons.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.lsn_lbl_lessons)

        self.lsn_cmb_lessons = QComboBox(self.bottom_top_frame)
        self.lsn_cmb_lessons.addItem("")
        self.lsn_cmb_lessons.setObjectName(u"lsn_cmb_lessons")
        self.lsn_cmb_lessons.setMinimumSize(QSize(280, 40))
        font9 = QFont()
        font9.setPointSize(10)
        font9.setBold(False)
        self.lsn_cmb_lessons.setFont(font9)
        self.lsn_cmb_lessons.setCursor(QCursor(Qt.PointingHandCursor))
        self.lsn_cmb_lessons.setStyleSheet(u"background-color: rgb(137, 218, 199);\n"
"border-radius: 12px;\n"
"color: rgb(0, 43, 91);\n"
"padding-left: 10px;")

        self.horizontalLayout_8.addWidget(self.lsn_cmb_lessons)

        self.horizontalSpacer_7 = QSpacerItem(141, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_7)


        self.verticalLayout_4.addWidget(self.bottom_top_frame)

        self.middle_content_frame = QFrame(self.mid_frame_2)
        self.middle_content_frame.setObjectName(u"middle_content_frame")
        self.middle_content_frame.setMinimumSize(QSize(1241, 400))
        self.middle_content_frame.setStyleSheet(u"background-color: rgb(36, 105, 127)")
        self.middle_content_frame.setFrameShape(QFrame.StyledPanel)
        self.middle_content_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.middle_content_frame)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.mediaStackWidget = QStackedWidget(self.middle_content_frame)
        self.mediaStackWidget.setObjectName(u"mediaStackWidget")
        self.mediaStackWidget.setMinimumSize(QSize(690, 400))
        self.image_page = QWidget()
        self.image_page.setObjectName(u"image_page")
        self.horizontalLayout_9 = QHBoxLayout(self.image_page)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.lsn_lbl_lesson_image = QLabel(self.image_page)
        self.lsn_lbl_lesson_image.setObjectName(u"lsn_lbl_lesson_image")
        self.lsn_lbl_lesson_image.setMinimumSize(QSize(690, 380))
        font10 = QFont()
        font10.setPointSize(30)
        self.lsn_lbl_lesson_image.setFont(font10)
        self.lsn_lbl_lesson_image.setStyleSheet(u"border: 3px dotted  rgb(137, 218, 199);\n"
"color: rgb(137, 218, 199);")
        self.lsn_lbl_lesson_image.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.lsn_lbl_lesson_image)

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
        self.lsn_lbl_lesson_topic.setMinimumSize(QSize(520, 400))
        self.lsn_lbl_lesson_topic.setMaximumSize(QSize(500, 16777215))
        font11 = QFont()
        font11.setPointSize(25)
        self.lsn_lbl_lesson_topic.setFont(font11)
        self.lsn_lbl_lesson_topic.setStyleSheet(u"border: 3px dotted  rgb(137, 218, 199);\n"
"color: rgb(137, 218, 199);")
        self.lsn_lbl_lesson_topic.setAlignment(Qt.AlignCenter)
        self.lsn_lbl_lesson_topic.setWordWrap(True)

        self.horizontalLayout_12.addWidget(self.lsn_lbl_lesson_topic)


        self.verticalLayout_4.addWidget(self.middle_content_frame)


        self.gridLayout_2.addWidget(self.mid_frame_2, 1, 0, 1, 1)

        self.bottom_frame_2 = QFrame(self.lesson_frame)
        self.bottom_frame_2.setObjectName(u"bottom_frame_2")
        self.bottom_frame_2.setMinimumSize(QSize(1180, 71))
        self.bottom_frame_2.setMaximumSize(QSize(16777215, 70))
        self.bottom_frame_2.setStyleSheet(u"background-color: rgb(42, 70, 98);\n"
"")
        self.bottom_frame_2.setFrameShape(QFrame.StyledPanel)
        self.bottom_frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.bottom_frame_2)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.lsn_btn_add_lessons = QPushButton(self.bottom_frame_2)
        self.lsn_btn_add_lessons.setObjectName(u"lsn_btn_add_lessons")
        sizePolicy2.setHeightForWidth(self.lsn_btn_add_lessons.sizePolicy().hasHeightForWidth())
        self.lsn_btn_add_lessons.setSizePolicy(sizePolicy2)
        self.lsn_btn_add_lessons.setMinimumSize(QSize(250, 50))
        self.lsn_btn_add_lessons.setMaximumSize(QSize(16777215, 50))
        font12 = QFont()
        font12.setFamilies([u"Hind Siliguri Medium"])
        font12.setPointSize(13)
        font12.setBold(False)
        self.lsn_btn_add_lessons.setFont(font12)
        self.lsn_btn_add_lessons.setCursor(QCursor(Qt.PointingHandCursor))
        self.lsn_btn_add_lessons.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(160, 253, 230);\n"
"color:  #256D85 ;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton::hover:!pressed {\n"
"	\n"
"	background-color: rgb(143, 227, 207);\n"
"	color: #2B4865;\n"
"\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u"../Images/add_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.lsn_btn_add_lessons.setIcon(icon9)
        self.lsn_btn_add_lessons.setIconSize(QSize(30, 30))

        self.horizontalLayout_10.addWidget(self.lsn_btn_add_lessons)

        self.lsn_btn_make_lesson = QPushButton(self.bottom_frame_2)
        self.lsn_btn_make_lesson.setObjectName(u"lsn_btn_make_lesson")
        self.lsn_btn_make_lesson.setMinimumSize(QSize(300, 50))
        self.lsn_btn_make_lesson.setFont(font3)
        self.lsn_btn_make_lesson.setCursor(QCursor(Qt.PointingHandCursor))
        self.lsn_btn_make_lesson.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(160, 253, 230);\n"
"color:  #256D85 ;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton::hover:!pressed {\n"
"	\n"
"	background-color: rgb(143, 227, 207);\n"
"	color: #2B4865;\n"
"\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u"../Images/make_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.lsn_btn_make_lesson.setIcon(icon10)
        self.lsn_btn_make_lesson.setIconSize(QSize(40, 30))

        self.horizontalLayout_10.addWidget(self.lsn_btn_make_lesson)

        self.lsn_btn_reload_window = QPushButton(self.bottom_frame_2)
        self.lsn_btn_reload_window.setObjectName(u"lsn_btn_reload_window")
        self.lsn_btn_reload_window.setMinimumSize(QSize(50, 50))
        font13 = QFont()
        font13.setFamilies([u"Gill Sans MT Ext Condensed Bold"])
        font13.setPointSize(13)
        self.lsn_btn_reload_window.setFont(font13)
        self.lsn_btn_reload_window.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(42, 70, 98);\n"
"color:  #256D85 ;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton::hover:!pressed {\n"
"	background-color:  rgb(42, 70, 98);\n"
"	color: #2B4865;\n"
"	border: 2px solid rgb(56, 216, 187);\n"
"	border-radius: 20px;\n"
"}")
        icon11 = QIcon()
        icon11.addFile(u"../Images/reload_icon_2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.lsn_btn_reload_window.setIcon(icon11)
        self.lsn_btn_reload_window.setIconSize(QSize(40, 40))

        self.horizontalLayout_10.addWidget(self.lsn_btn_reload_window)


        self.gridLayout_2.addWidget(self.bottom_frame_2, 2, 0, 1, 1)

        self.top_frame_2 = QFrame(self.lesson_frame)
        self.top_frame_2.setObjectName(u"top_frame_2")
        self.top_frame_2.setMinimumSize(QSize(1180, 80))
        self.top_frame_2.setMaximumSize(QSize(16777215, 80))
        self.top_frame_2.setStyleSheet(u"background-color: #2B4865;")
        self.top_frame_2.setFrameShape(QFrame.StyledPanel)
        self.top_frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.top_frame_2)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.lsn_btn_back_to_home = QPushButton(self.top_frame_2)
        self.lsn_btn_back_to_home.setObjectName(u"lsn_btn_back_to_home")
        sizePolicy.setHeightForWidth(self.lsn_btn_back_to_home.sizePolicy().hasHeightForWidth())
        self.lsn_btn_back_to_home.setSizePolicy(sizePolicy)
        self.lsn_btn_back_to_home.setMinimumSize(QSize(0, 60))
        self.lsn_btn_back_to_home.setMaximumSize(QSize(60, 60))
        self.lsn_btn_back_to_home.setBaseSize(QSize(0, 4))
        self.lsn_btn_back_to_home.setFont(font1)
        self.lsn_btn_back_to_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.lsn_btn_back_to_home.setMouseTracking(True)
        self.lsn_btn_back_to_home.setStyleSheet(u"QPushButton {\n"
"	background-color: #2B4865 #256D85;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover:!pressed\n"
"{\n"
"	background-color:  #256D85;\n"
"	border-radius: 30px;\n"
"}")
        self.lsn_btn_back_to_home.setIcon(icon5)
        self.lsn_btn_back_to_home.setIconSize(QSize(200, 200))
        self.lsn_btn_back_to_home.setAutoDefault(False)
        self.lsn_btn_back_to_home.setFlat(False)

        self.horizontalLayout_7.addWidget(self.lsn_btn_back_to_home)

        self.lsn_lbl_headline = QLabel(self.top_frame_2)
        self.lsn_lbl_headline.setObjectName(u"lsn_lbl_headline")
        self.lsn_lbl_headline.setFont(font2)
        self.lsn_lbl_headline.setStyleSheet(u"color: #8FE3CF")
        self.lsn_lbl_headline.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.lsn_lbl_headline)


        self.gridLayout_2.addWidget(self.top_frame_2, 0, 0, 1, 1)


        self.horizontalLayout_11.addWidget(self.lesson_frame)

        self.stackedWidget.addWidget(self.lesson_page)
        self.task_page = QWidget()
        self.task_page.setObjectName(u"task_page")
        self.gridLayout_13 = QGridLayout(self.task_page)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setContentsMargins(0, 0, 0, 0)
        self.evaluation_frame = QFrame(self.task_page)
        self.evaluation_frame.setObjectName(u"evaluation_frame")
        self.evaluation_frame.setFrameShape(QFrame.StyledPanel)
        self.evaluation_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.evaluation_frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.top_frame_3 = QFrame(self.evaluation_frame)
        self.top_frame_3.setObjectName(u"top_frame_3")
        self.top_frame_3.setMinimumSize(QSize(1180, 80))
        self.top_frame_3.setMaximumSize(QSize(16777215, 80))
        self.top_frame_3.setStyleSheet(u"background-color: #2B4865;")
        self.top_frame_3.setFrameShape(QFrame.StyledPanel)
        self.top_frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.top_frame_3)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.task_btn_back_to_home = QPushButton(self.top_frame_3)
        self.task_btn_back_to_home.setObjectName(u"task_btn_back_to_home")
        sizePolicy.setHeightForWidth(self.task_btn_back_to_home.sizePolicy().hasHeightForWidth())
        self.task_btn_back_to_home.setSizePolicy(sizePolicy)
        self.task_btn_back_to_home.setMinimumSize(QSize(0, 60))
        self.task_btn_back_to_home.setMaximumSize(QSize(60, 60))
        self.task_btn_back_to_home.setBaseSize(QSize(0, 4))
        self.task_btn_back_to_home.setFont(font1)
        self.task_btn_back_to_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.task_btn_back_to_home.setMouseTracking(True)
        self.task_btn_back_to_home.setStyleSheet(u"QPushButton {\n"
"	background-color: #2B4865 #256D85;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover:!pressed\n"
"{\n"
"	background-color:  #256D85;\n"
"	border-radius: 30px;\n"
"}")
        self.task_btn_back_to_home.setIcon(icon5)
        self.task_btn_back_to_home.setIconSize(QSize(200, 200))
        self.task_btn_back_to_home.setAutoDefault(False)
        self.task_btn_back_to_home.setFlat(False)

        self.horizontalLayout_13.addWidget(self.task_btn_back_to_home)

        self.lsn_lbl_headline_2 = QLabel(self.top_frame_3)
        self.lsn_lbl_headline_2.setObjectName(u"lsn_lbl_headline_2")
        self.lsn_lbl_headline_2.setFont(font2)
        self.lsn_lbl_headline_2.setStyleSheet(u"color: #8FE3CF")
        self.lsn_lbl_headline_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_13.addWidget(self.lsn_lbl_headline_2)


        self.verticalLayout_3.addWidget(self.top_frame_3)

        self.body = QFrame(self.evaluation_frame)
        self.body.setObjectName(u"body")
        self.body.setStyleSheet(u"background-color: rgb(37, 109, 133);")
        self.body.setFrameShape(QFrame.StyledPanel)
        self.body.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.body)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.eval_left_frame = QFrame(self.body)
        self.eval_left_frame.setObjectName(u"eval_left_frame")
        self.eval_left_frame.setMinimumSize(QSize(300, 636))
        self.eval_left_frame.setMaximumSize(QSize(300, 636))
        self.eval_left_frame.setStyleSheet(u"")
        self.eval_left_frame.setFrameShape(QFrame.StyledPanel)
        self.eval_left_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.eval_left_frame)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.verticalSpacer_3 = QSpacerItem(20, 164, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_3, 0, 1, 1, 1)

        self.horizontalSpacer_11 = QSpacerItem(13, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_11, 1, 0, 1, 1)

        self.task_btn_mcq = QPushButton(self.eval_left_frame)
        self.task_btn_mcq.setObjectName(u"task_btn_mcq")
        self.task_btn_mcq.setMinimumSize(QSize(261, 61))
        font14 = QFont()
        font14.setFamilies([u"Hind Siliguri Medium"])
        font14.setPointSize(12)
        font14.setBold(True)
        self.task_btn_mcq.setFont(font14)
        self.task_btn_mcq.setCursor(QCursor(Qt.PointingHandCursor))
        self.task_btn_mcq.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(160, 253, 230);\n"
"color:  rgb(0, 43, 91) ;\n"
"border-radius: 15px;\n"
"border: 4px solid rgb(43, 72, 101);\n"
"}\n"
"\n"
"QPushButton::hover:!pressed {\n"
"	\n"
"	background-color: rgb(143, 227, 207);\n"
"	color: rgb(0, 43, 91);\n"
"\n"
"}")
        icon12 = QIcon()
        icon12.addFile(u"../Images/mcq.png", QSize(), QIcon.Normal, QIcon.Off)
        self.task_btn_mcq.setIcon(icon12)
        self.task_btn_mcq.setIconSize(QSize(20, 30))

        self.gridLayout_5.addWidget(self.task_btn_mcq, 1, 1, 1, 1)

        self.horizontalSpacer_25 = QSpacerItem(13, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_25, 1, 2, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_10, 2, 0, 1, 1)

        self.task_btn_matching = QPushButton(self.eval_left_frame)
        self.task_btn_matching.setObjectName(u"task_btn_matching")
        self.task_btn_matching.setMinimumSize(QSize(261, 61))
        self.task_btn_matching.setFont(font14)
        self.task_btn_matching.setCursor(QCursor(Qt.PointingHandCursor))
        self.task_btn_matching.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(160, 253, 230);\n"
"color:  rgb(0, 43, 91) ;\n"
"border-radius: 15px;\n"
"border: 4px solid rgb(43, 72, 101);\n"
"}\n"
"\n"
"QPushButton::hover:!pressed {\n"
"	\n"
"	background-color: rgb(143, 227, 207);\n"
"	color: rgb(0, 43, 91);\n"
"\n"
"}")
        icon13 = QIcon()
        icon13.addFile(u"../Images/connect_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.task_btn_matching.setIcon(icon13)
        self.task_btn_matching.setIconSize(QSize(28, 50))

        self.gridLayout_5.addWidget(self.task_btn_matching, 2, 1, 1, 1)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_13, 2, 2, 1, 1)

        self.horizontalSpacer_24 = QSpacerItem(13, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_24, 3, 0, 1, 1)

        self.task_btn_sequence = QPushButton(self.eval_left_frame)
        self.task_btn_sequence.setObjectName(u"task_btn_sequence")
        self.task_btn_sequence.setMinimumSize(QSize(261, 61))
        self.task_btn_sequence.setFont(font14)
        self.task_btn_sequence.setCursor(QCursor(Qt.PointingHandCursor))
        self.task_btn_sequence.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(160, 253, 230);\n"
"color:  rgb(0, 43, 91) ;\n"
"border-radius: 15px;\n"
"border: 4px solid rgb(43, 72, 101);\n"
"}\n"
"\n"
"QPushButton::hover:!pressed {\n"
"	\n"
"	background-color: rgb(143, 227, 207);\n"
"	color: rgb(0, 43, 91);\n"
"\n"
"}")
        icon14 = QIcon()
        icon14.addFile(u"../Images/sequence_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.task_btn_sequence.setIcon(icon14)
        self.task_btn_sequence.setIconSize(QSize(26, 50))

        self.gridLayout_5.addWidget(self.task_btn_sequence, 3, 1, 1, 1)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_14, 3, 2, 1, 1)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_12, 4, 0, 1, 1)

        self.task_btn_puzzle = QPushButton(self.eval_left_frame)
        self.task_btn_puzzle.setObjectName(u"task_btn_puzzle")
        self.task_btn_puzzle.setMinimumSize(QSize(261, 61))
        self.task_btn_puzzle.setFont(font14)
        self.task_btn_puzzle.setCursor(QCursor(Qt.PointingHandCursor))
        self.task_btn_puzzle.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(160, 253, 230);\n"
"color:  rgb(0, 43, 91) ;\n"
"border-radius: 15px;\n"
"border: 4px solid rgb(43, 72, 101);\n"
"}\n"
"\n"
"QPushButton::hover:!pressed {\n"
"	\n"
"	background-color: rgb(143, 227, 207);\n"
"	color: rgb(0, 43, 91);\n"
"\n"
"}")
        icon15 = QIcon()
        icon15.addFile(u"../Images/puzzle_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.task_btn_puzzle.setIcon(icon15)
        self.task_btn_puzzle.setIconSize(QSize(20, 30))

        self.gridLayout_5.addWidget(self.task_btn_puzzle, 4, 1, 1, 1)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_15, 4, 2, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 163, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_4, 5, 1, 1, 1)


        self.horizontalLayout_16.addWidget(self.eval_left_frame)

        self.eval_right_frame = QFrame(self.body)
        self.eval_right_frame.setObjectName(u"eval_right_frame")
        self.eval_right_frame.setMinimumSize(QSize(891, 621))
        self.eval_right_frame.setStyleSheet(u"")
        self.eval_right_frame.setFrameShape(QFrame.StyledPanel)
        self.eval_right_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.eval_right_frame)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.evalstackwidget = QStackedWidget(self.eval_right_frame)
        self.evalstackwidget.setObjectName(u"evalstackwidget")
        self.evalstackwidget.setStyleSheet(u"")
        self.puzzle_page = QWidget()
        self.puzzle_page.setObjectName(u"puzzle_page")
        self.gridLayout_7 = QGridLayout(self.puzzle_page)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.frame_3 = QFrame(self.puzzle_page)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_16 = QGridLayout(self.frame_3)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.label_9 = QLabel(self.frame_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(0, 50))
        self.label_9.setMaximumSize(QSize(16777215, 50))
        font15 = QFont()
        font15.setPointSize(21)
        self.label_9.setFont(font15)
        self.label_9.setStyleSheet(u"color: rgb(159, 251, 228);\n"
"background-color: rgb(0, 43, 91);")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.gridLayout_16.addWidget(self.label_9, 0, 0, 1, 2)

        self.task_puzzle_q_set_lbl = QLineEdit(self.frame_3)
        self.task_puzzle_q_set_lbl.setObjectName(u"task_puzzle_q_set_lbl")
        self.task_puzzle_q_set_lbl.setMinimumSize(QSize(326, 51))
        font16 = QFont()
        font16.setFamilies([u"Hind Siliguri"])
        font16.setPointSize(9)
        font16.setBold(False)
        self.task_puzzle_q_set_lbl.setFont(font16)
        self.task_puzzle_q_set_lbl.setStyleSheet(u"background-color: rgb(137, 218, 199);\n"
"border: 4px solid rgb(0, 43, 91);\n"
"padding-left: 15px;\n"
"border-radius: 10px;\n"
"color: black;")

        self.gridLayout_16.addWidget(self.task_puzzle_q_set_lbl, 1, 0, 1, 1)

        self.task_puzzle_save_set_btn = QPushButton(self.frame_3)
        self.task_puzzle_save_set_btn.setObjectName(u"task_puzzle_save_set_btn")
        self.task_puzzle_save_set_btn.setMinimumSize(QSize(100, 51))
        font17 = QFont()
        font17.setFamilies([u"Hind Siliguri Medium"])
        font17.setPointSize(10)
        font17.setBold(False)
        self.task_puzzle_save_set_btn.setFont(font17)
        self.task_puzzle_save_set_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.task_puzzle_save_set_btn.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(160, 253, 230);\n"
"color:  #256D85 ;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton::hover:!pressed {\n"
"	\n"
"	background-color: rgb(143, 227, 207);\n"
"	color: #2B4865;\n"
"\n"
"}")

        self.gridLayout_16.addWidget(self.task_puzzle_save_set_btn, 1, 1, 1, 1)

        self.task_puzzle_image_lbl = QLabel(self.frame_3)
        self.task_puzzle_image_lbl.setObjectName(u"task_puzzle_image_lbl")
        self.task_puzzle_image_lbl.setMinimumSize(QSize(481, 384))
        font18 = QFont()
        font18.setPointSize(14)
        self.task_puzzle_image_lbl.setFont(font18)
        self.task_puzzle_image_lbl.setStyleSheet(u"color: rgb(0, 43, 91);\n"
"border: 2px solid rgb(43, 72, 101);")
        self.task_puzzle_image_lbl.setAlignment(Qt.AlignCenter)
        self.task_puzzle_image_lbl.setWordWrap(True)

        self.gridLayout_16.addWidget(self.task_puzzle_image_lbl, 2, 0, 1, 2)

        self.task_puzzle_select_img_btn = QPushButton(self.frame_3)
        self.task_puzzle_select_img_btn.setObjectName(u"task_puzzle_select_img_btn")
        self.task_puzzle_select_img_btn.setMinimumSize(QSize(211, 61))
        self.task_puzzle_select_img_btn.setFont(font12)
        self.task_puzzle_select_img_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.task_puzzle_select_img_btn.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(160, 253, 230);\n"
"color:  #256D85 ;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton::hover:!pressed {\n"
"	\n"
"	background-color: rgb(143, 227, 207);\n"
"	color: #2B4865;\n"
"\n"
"}")

        self.gridLayout_16.addWidget(self.task_puzzle_select_img_btn, 3, 0, 1, 1)

        self.task_puzzle_show_set_btn = QPushButton(self.frame_3)
        self.task_puzzle_show_set_btn.setObjectName(u"task_puzzle_show_set_btn")
        self.task_puzzle_show_set_btn.setMinimumSize(QSize(211, 61))
        font19 = QFont()
        font19.setFamilies([u"Hind Siliguri Medium"])
        font19.setPointSize(11)
        self.task_puzzle_show_set_btn.setFont(font19)
        self.task_puzzle_show_set_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.task_puzzle_show_set_btn.setStyleSheet(u"QPushButton {\n"
"padding-left: 15px;\n"
"padding-right: 15px;\n"
"background-color: rgb(160, 253, 230);\n"
"color:  #256D85 ;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton::hover:!pressed {\n"
"	\n"
"	padding-left: 15px;\n"
"	padding-right: 15px;\n"
"	background-color: rgb(143, 227, 207);\n"
"	color: #2B4865;\n"
"\n"
"}")

        self.gridLayout_16.addWidget(self.task_puzzle_show_set_btn, 3, 1, 1, 1)


        self.gridLayout_7.addWidget(self.frame_3, 0, 0, 1, 1)

        self.evalstackwidget.addWidget(self.puzzle_page)
        self.sequence_page = QWidget()
        self.sequence_page.setObjectName(u"sequence_page")
        self.sequence_page.setStyleSheet(u"")
        self.gridLayout_12 = QGridLayout(self.sequence_page)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(11, 11, 11, 11)
        self.task_seq_video_frame_widget = QHBoxLayout()
        self.task_seq_video_frame_widget.setObjectName(u"task_seq_video_frame_widget")

        self.gridLayout_12.addLayout(self.task_seq_video_frame_widget, 1, 0, 1, 1)

        self.frame_4 = QFrame(self.sequence_page)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(390, 500))
        self.frame_4.setMaximumSize(QSize(430, 612))
        self.frame_4.setStyleSheet(u"border: 3px solid rgb(160, 253, 230);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_17 = QGridLayout(self.frame_4)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.task_seq_img_seq_edit = QLineEdit(self.frame_4)
        self.task_seq_img_seq_edit.setObjectName(u"task_seq_img_seq_edit")
        self.task_seq_img_seq_edit.setMinimumSize(QSize(300, 51))
        font20 = QFont()
        font20.setFamilies([u"Segoe UI Semibold"])
        font20.setPointSize(10)
        self.task_seq_img_seq_edit.setFont(font20)
        self.task_seq_img_seq_edit.setStyleSheet(u"background-color: rgb(137, 218, 199);\n"
"border: 4px solid rgb(0, 43, 91);\n"
"padding-left: 15px;\n"
"border-radius: 10px;\n"
"color: black;")

        self.gridLayout_17.addWidget(self.task_seq_img_seq_edit, 4, 0, 1, 3)

        self.task_seq_img_desc_edit = QLineEdit(self.frame_4)
        self.task_seq_img_desc_edit.setObjectName(u"task_seq_img_desc_edit")
        self.task_seq_img_desc_edit.setMinimumSize(QSize(300, 51))
        font21 = QFont()
        font21.setFamilies([u"Hind Siliguri Medium"])
        font21.setPointSize(10)
        self.task_seq_img_desc_edit.setFont(font21)
        self.task_seq_img_desc_edit.setStyleSheet(u"background-color: rgb(137, 218, 199);\n"
"border: 4px solid rgb(0, 43, 91);\n"
"padding-left: 15px;\n"
"border-radius: 10px;\n"
"color: black;")

        self.gridLayout_17.addWidget(self.task_seq_img_desc_edit, 3, 0, 1, 3)

        self.task_seq_img_view_lbl = QLabel(self.frame_4)
        self.task_seq_img_view_lbl.setObjectName(u"task_seq_img_view_lbl")
        self.task_seq_img_view_lbl.setMinimumSize(QSize(300, 180))
        font22 = QFont()
        font22.setPointSize(22)
        self.task_seq_img_view_lbl.setFont(font22)
        self.task_seq_img_view_lbl.setStyleSheet(u"border: 2px dotted rgb(0, 43, 91);")
        self.task_seq_img_view_lbl.setPixmap(QPixmap(u"../Images/image_template.png"))
        self.task_seq_img_view_lbl.setAlignment(Qt.AlignCenter)

        self.gridLayout_17.addWidget(self.task_seq_img_view_lbl, 1, 0, 1, 3)

        self.task_seq_img_save_btn = QPushButton(self.frame_4)
        self.task_seq_img_save_btn.setObjectName(u"task_seq_img_save_btn")
        self.task_seq_img_save_btn.setMinimumSize(QSize(156, 52))
        font23 = QFont()
        font23.setPointSize(11)
        font23.setBold(False)
        self.task_seq_img_save_btn.setFont(font23)
        self.task_seq_img_save_btn.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(160, 253, 230);\n"
"color:  #256D85 ;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton::hover:!pressed {\n"
"	\n"
"	background-color: rgb(143, 227, 207);\n"
"	color: #2B4865;\n"
"\n"
"}")

        self.gridLayout_17.addWidget(self.task_seq_img_save_btn, 6, 1, 1, 1)

        self.task_seq_instruction_lbl = QLabel(self.frame_4)
        self.task_seq_instruction_lbl.setObjectName(u"task_seq_instruction_lbl")
        self.task_seq_instruction_lbl.setMinimumSize(QSize(365, 50))
        font24 = QFont()
        font24.setFamilies([u"Hind Siliguri Medium"])
        font24.setPointSize(11)
        font24.setBold(False)
        self.task_seq_instruction_lbl.setFont(font24)
        self.task_seq_instruction_lbl.setStyleSheet(u"color: rgb(132, 211, 184);\n"
"background-color: rgb(0, 43, 91);\n"
"padding: 5px;\n"
"border: none;")
        self.task_seq_instruction_lbl.setAlignment(Qt.AlignCenter)
        self.task_seq_instruction_lbl.setWordWrap(True)

        self.gridLayout_17.addWidget(self.task_seq_instruction_lbl, 0, 0, 1, 3)

        self.horizontalSpacer_22 = QSpacerItem(250, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_17.addItem(self.horizontalSpacer_22, 6, 0, 1, 1)

        self.horizontalSpacer_23 = QSpacerItem(250, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_17.addItem(self.horizontalSpacer_23, 6, 2, 1, 1)

        self.task_seq_set_lbl = QLineEdit(self.frame_4)
        self.task_seq_set_lbl.setObjectName(u"task_seq_set_lbl")
        self.task_seq_set_lbl.setMinimumSize(QSize(300, 51))
        self.task_seq_set_lbl.setFont(font16)
        self.task_seq_set_lbl.setStyleSheet(u"background-color: rgb(137, 218, 199);\n"
"border: 4px solid rgb(0, 43, 91);\n"
"padding-left: 15px;\n"
"border-radius: 10px;\n"
"color: black;")

        self.gridLayout_17.addWidget(self.task_seq_set_lbl, 5, 0, 1, 3)

        self.verticalSpacer_6 = QSpacerItem(10, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_17.addItem(self.verticalSpacer_6, 2, 0, 1, 1)


        self.gridLayout_12.addWidget(self.frame_4, 1, 2, 1, 1)

        self.label_8 = QLabel(self.sequence_page)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(867, 50))
        self.label_8.setMaximumSize(QSize(16777215, 50))
        self.label_8.setFont(font15)
        self.label_8.setStyleSheet(u"color: rgb(159, 251, 228);\n"
"background-color: rgb(0, 43, 91);")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.gridLayout_12.addWidget(self.label_8, 0, 0, 1, 3)

        self.evalstackwidget.addWidget(self.sequence_page)
        self.matching_page = QWidget()
        self.matching_page.setObjectName(u"matching_page")
        self.gridLayout_14 = QGridLayout(self.matching_page)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.puzzle_pic_frame = QFrame(self.matching_page)
        self.puzzle_pic_frame.setObjectName(u"puzzle_pic_frame")
        self.puzzle_pic_frame.setStyleSheet(u"")
        self.puzzle_pic_frame.setFrameShape(QFrame.StyledPanel)
        self.puzzle_pic_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_22 = QGridLayout(self.puzzle_pic_frame)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.frame_6 = QFrame(self.puzzle_pic_frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(331, 230))
        self.frame_6.setMaximumSize(QSize(16777215, 16777215))
        self.frame_6.setStyleSheet(u"border: 3px solid rgb(160, 253, 230);")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_19 = QGridLayout(self.frame_6)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.task_matching_img_desc_edit_2 = QLineEdit(self.frame_6)
        self.task_matching_img_desc_edit_2.setObjectName(u"task_matching_img_desc_edit_2")
        self.task_matching_img_desc_edit_2.setMinimumSize(QSize(250, 40))
        self.task_matching_img_desc_edit_2.setFont(font21)
        self.task_matching_img_desc_edit_2.setStyleSheet(u"background-color:  rgb(43, 72, 101);\n"
"border: 3px solid rgb(0, 43, 91);\n"
"padding-left: 15px;\n"
"border-radius: 10px;\n"
"color: rgb(160, 253, 230);")

        self.gridLayout_19.addWidget(self.task_matching_img_desc_edit_2, 1, 0, 1, 1)

        self.task_matching_img_add_btn_2 = QPushButton(self.frame_6)
        self.task_matching_img_add_btn_2.setObjectName(u"task_matching_img_add_btn_2")
        self.task_matching_img_add_btn_2.setMinimumSize(QSize(50, 40))
        font25 = QFont()
        font25.setPointSize(18)
        font25.setBold(True)
        self.task_matching_img_add_btn_2.setFont(font25)
        self.task_matching_img_add_btn_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.task_matching_img_add_btn_2.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(160, 253, 230);\n"
"color:  #256D85 ;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton::hover:!pressed {\n"
"	\n"
"	background-color: rgb(143, 227, 207);\n"
"	color: #2B4865;\n"
"\n"
"}")
        icon16 = QIcon()
        icon16.addFile(u"../Images/add_image_2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.task_matching_img_add_btn_2.setIcon(icon16)
        self.task_matching_img_add_btn_2.setIconSize(QSize(30, 30))

        self.gridLayout_19.addWidget(self.task_matching_img_add_btn_2, 1, 1, 1, 1)

        self.task_matching_img_view_lbl_2 = QLabel(self.frame_6)
        self.task_matching_img_view_lbl_2.setObjectName(u"task_matching_img_view_lbl_2")
        self.task_matching_img_view_lbl_2.setMinimumSize(QSize(301, 140))
        self.task_matching_img_view_lbl_2.setFont(font22)
        self.task_matching_img_view_lbl_2.setStyleSheet(u"border: 2px dotted rgb(0, 43, 91);")
        self.task_matching_img_view_lbl_2.setPixmap(QPixmap(u"../Images/image_template.png"))
        self.task_matching_img_view_lbl_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_19.addWidget(self.task_matching_img_view_lbl_2, 0, 0, 1, 3)


        self.gridLayout_22.addWidget(self.frame_6, 2, 1, 1, 1)

        self.frame_7 = QFrame(self.puzzle_pic_frame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(331, 240))
        self.frame_7.setMaximumSize(QSize(16777215, 16777215))
        self.frame_7.setStyleSheet(u"border: 3px solid rgb(160, 253, 230);")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout_20 = QGridLayout(self.frame_7)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.task_matching_img_desc_edit_3 = QLineEdit(self.frame_7)
        self.task_matching_img_desc_edit_3.setObjectName(u"task_matching_img_desc_edit_3")
        self.task_matching_img_desc_edit_3.setMinimumSize(QSize(250, 40))
        self.task_matching_img_desc_edit_3.setFont(font21)
        self.task_matching_img_desc_edit_3.setStyleSheet(u"background-color:  rgb(43, 72, 101);\n"
"border: 3px solid rgb(0, 43, 91);\n"
"padding-left: 15px;\n"
"border-radius: 10px;\n"
"color: rgb(160, 253, 230);")

        self.gridLayout_20.addWidget(self.task_matching_img_desc_edit_3, 1, 0, 1, 1)

        self.task_matching_img_add_btn_3 = QPushButton(self.frame_7)
        self.task_matching_img_add_btn_3.setObjectName(u"task_matching_img_add_btn_3")
        self.task_matching_img_add_btn_3.setMinimumSize(QSize(50, 40))
        self.task_matching_img_add_btn_3.setFont(font25)
        self.task_matching_img_add_btn_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.task_matching_img_add_btn_3.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(160, 253, 230);\n"
"color:  #256D85 ;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton::hover:!pressed {\n"
"	\n"
"	background-color: rgb(143, 227, 207);\n"
"	color: #2B4865;\n"
"\n"
"}")
        self.task_matching_img_add_btn_3.setIcon(icon16)
        self.task_matching_img_add_btn_3.setIconSize(QSize(30, 30))

        self.gridLayout_20.addWidget(self.task_matching_img_add_btn_3, 1, 1, 1, 1)

        self.task_matching_img_view_lbl_3 = QLabel(self.frame_7)
        self.task_matching_img_view_lbl_3.setObjectName(u"task_matching_img_view_lbl_3")
        self.task_matching_img_view_lbl_3.setMinimumSize(QSize(301, 155))
        self.task_matching_img_view_lbl_3.setFont(font22)
        self.task_matching_img_view_lbl_3.setStyleSheet(u"border: 2px dotted rgb(0, 43, 91);")
        self.task_matching_img_view_lbl_3.setPixmap(QPixmap(u"../Images/image_template.png"))
        self.task_matching_img_view_lbl_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_20.addWidget(self.task_matching_img_view_lbl_3, 0, 0, 1, 3)


        self.gridLayout_22.addWidget(self.frame_7, 3, 0, 1, 1)

        self.frame_8 = QFrame(self.puzzle_pic_frame)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(331, 240))
        self.frame_8.setMaximumSize(QSize(16777215, 16777215))
        self.frame_8.setStyleSheet(u"border: 3px solid rgb(160, 253, 230);")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.gridLayout_21 = QGridLayout(self.frame_8)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.task_matching_img_desc_edit_4 = QLineEdit(self.frame_8)
        self.task_matching_img_desc_edit_4.setObjectName(u"task_matching_img_desc_edit_4")
        self.task_matching_img_desc_edit_4.setMinimumSize(QSize(250, 40))
        self.task_matching_img_desc_edit_4.setFont(font21)
        self.task_matching_img_desc_edit_4.setStyleSheet(u"background-color:  rgb(43, 72, 101);\n"
"border: 3px solid rgb(0, 43, 91);\n"
"padding-left: 15px;\n"
"border-radius: 10px;\n"
"color: rgb(160, 253, 230);")

        self.gridLayout_21.addWidget(self.task_matching_img_desc_edit_4, 1, 0, 1, 1)

        self.task_matching_img_add_btn_4 = QPushButton(self.frame_8)
        self.task_matching_img_add_btn_4.setObjectName(u"task_matching_img_add_btn_4")
        self.task_matching_img_add_btn_4.setMinimumSize(QSize(50, 40))
        self.task_matching_img_add_btn_4.setFont(font25)
        self.task_matching_img_add_btn_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.task_matching_img_add_btn_4.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(160, 253, 230);\n"
"color:  #256D85 ;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton::hover:!pressed {\n"
"	\n"
"	background-color: rgb(143, 227, 207);\n"
"	color: #2B4865;\n"
"\n"
"}")
        self.task_matching_img_add_btn_4.setIcon(icon16)
        self.task_matching_img_add_btn_4.setIconSize(QSize(30, 30))

        self.gridLayout_21.addWidget(self.task_matching_img_add_btn_4, 1, 1, 1, 1)

        self.task_matching_img_view_lbl_4 = QLabel(self.frame_8)
        self.task_matching_img_view_lbl_4.setObjectName(u"task_matching_img_view_lbl_4")
        self.task_matching_img_view_lbl_4.setMinimumSize(QSize(301, 150))
        self.task_matching_img_view_lbl_4.setFont(font22)
        self.task_matching_img_view_lbl_4.setStyleSheet(u"border: 2px dotted rgb(0, 43, 91);")
        self.task_matching_img_view_lbl_4.setPixmap(QPixmap(u"../Images/image_template.png"))
        self.task_matching_img_view_lbl_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_21.addWidget(self.task_matching_img_view_lbl_4, 0, 0, 1, 3)


        self.gridLayout_22.addWidget(self.frame_8, 3, 1, 1, 1)

        self.frame_5 = QFrame(self.puzzle_pic_frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(331, 230))
        self.frame_5.setMaximumSize(QSize(16777215, 16777215))
        self.frame_5.setStyleSheet(u"border: 3px solid rgb(160, 253, 230);")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_18 = QGridLayout(self.frame_5)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.task_matching_img_add_btn_1 = QPushButton(self.frame_5)
        self.task_matching_img_add_btn_1.setObjectName(u"task_matching_img_add_btn_1")
        self.task_matching_img_add_btn_1.setMinimumSize(QSize(50, 40))
        self.task_matching_img_add_btn_1.setFont(font25)
        self.task_matching_img_add_btn_1.setCursor(QCursor(Qt.PointingHandCursor))
        self.task_matching_img_add_btn_1.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(160, 253, 230);\n"
"color:  #256D85 ;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton::hover:!pressed {\n"
"	\n"
"	background-color: rgb(143, 227, 207);\n"
"	color: #2B4865;\n"
"\n"
"}")
        self.task_matching_img_add_btn_1.setIcon(icon16)
        self.task_matching_img_add_btn_1.setIconSize(QSize(40, 30))

        self.gridLayout_18.addWidget(self.task_matching_img_add_btn_1, 1, 1, 1, 1)

        self.task_matching_img_desc_edit_1 = QLineEdit(self.frame_5)
        self.task_matching_img_desc_edit_1.setObjectName(u"task_matching_img_desc_edit_1")
        self.task_matching_img_desc_edit_1.setMinimumSize(QSize(250, 40))
        self.task_matching_img_desc_edit_1.setFont(font21)
        self.task_matching_img_desc_edit_1.setStyleSheet(u"background-color:  rgb(43, 72, 101);\n"
"border: 3px solid rgb(0, 43, 91);\n"
"padding-left: 15px;\n"
"border-radius: 10px;\n"
"color: rgb(160, 253, 230);")

        self.gridLayout_18.addWidget(self.task_matching_img_desc_edit_1, 1, 0, 1, 1)

        self.task_matching_img_view_lbl_1 = QLabel(self.frame_5)
        self.task_matching_img_view_lbl_1.setObjectName(u"task_matching_img_view_lbl_1")
        self.task_matching_img_view_lbl_1.setMinimumSize(QSize(301, 140))
        self.task_matching_img_view_lbl_1.setFont(font22)
        self.task_matching_img_view_lbl_1.setStyleSheet(u"border: 2px dotted rgb(0, 43, 91);")
        self.task_matching_img_view_lbl_1.setPixmap(QPixmap(u"../Images/image_template.png"))
        self.task_matching_img_view_lbl_1.setAlignment(Qt.AlignCenter)

        self.gridLayout_18.addWidget(self.task_matching_img_view_lbl_1, 0, 0, 1, 3)


        self.gridLayout_22.addWidget(self.frame_5, 2, 0, 1, 1)

        self.label_10 = QLabel(self.puzzle_pic_frame)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(0, 50))
        self.label_10.setMaximumSize(QSize(16777215, 50))
        self.label_10.setFont(font15)
        self.label_10.setStyleSheet(u"color: rgb(159, 251, 228);\n"
"background-color: rgb(0, 43, 91);")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.gridLayout_22.addWidget(self.label_10, 0, 0, 1, 2)

        self.task_matching_set_edit = QLineEdit(self.puzzle_pic_frame)
        self.task_matching_set_edit.setObjectName(u"task_matching_set_edit")
        self.task_matching_set_edit.setMinimumSize(QSize(326, 51))
        self.task_matching_set_edit.setFont(font16)
        self.task_matching_set_edit.setStyleSheet(u"background-color:  rgb(43, 72, 101);\n"
"border: 3px solid rgb(0, 43, 91);\n"
"padding-left: 15px;\n"
"border-radius: 10px;\n"
"color: rgb(160, 253, 230);")

        self.gridLayout_22.addWidget(self.task_matching_set_edit, 1, 0, 1, 1)

        self.task_matching_save_set_btn = QPushButton(self.puzzle_pic_frame)
        self.task_matching_save_set_btn.setObjectName(u"task_matching_save_set_btn")
        self.task_matching_save_set_btn.setMinimumSize(QSize(100, 51))
        self.task_matching_save_set_btn.setFont(font17)
        self.task_matching_save_set_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.task_matching_save_set_btn.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(160, 253, 230);\n"
"color:  #256D85 ;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton::hover:!pressed {\n"
"	\n"
"	background-color: rgb(143, 227, 207);\n"
"	color: #2B4865;\n"
"\n"
"}")

        self.gridLayout_22.addWidget(self.task_matching_save_set_btn, 1, 1, 1, 1)


        self.gridLayout_14.addWidget(self.puzzle_pic_frame, 0, 0, 1, 1)

        self.evalstackwidget.addWidget(self.matching_page)
        self.mcq_page = QWidget()
        self.mcq_page.setObjectName(u"mcq_page")
        self.gridLayout_26 = QGridLayout(self.mcq_page)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.gridLayout_26.setContentsMargins(5, 5, 5, 5)
        self.frame_16 = QFrame(self.mcq_page)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.gridLayout_28 = QGridLayout(self.frame_16)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.label_13 = QLabel(self.frame_16)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(121, 51))
        self.label_13.setMaximumSize(QSize(142, 71))
        self.label_13.setFont(font18)
        self.label_13.setStyleSheet(u"color: rgb(132, 211, 184);\n"
"background-color: rgb(0, 43, 91);\n"
"padding: 5px;\n"
"border-radius: 10px;")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.gridLayout_28.addWidget(self.label_13, 1, 0, 1, 1)

        self.line_2 = QFrame(self.frame_16)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_28.addWidget(self.line_2, 7, 0, 1, 8)

        self.task_mcq_new_set_btn = QPushButton(self.frame_16)
        self.task_mcq_new_set_btn.setObjectName(u"task_mcq_new_set_btn")
        self.task_mcq_new_set_btn.setMinimumSize(QSize(150, 55))
        self.task_mcq_new_set_btn.setMaximumSize(QSize(172, 16777215))
        self.task_mcq_new_set_btn.setFont(font19)
        self.task_mcq_new_set_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.task_mcq_new_set_btn.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(160, 253, 230);\n"
"color:  rgb(0, 43, 91) ;\n"
"border-radius: 15px;\n"
"border: 4px solid rgb(43, 72, 101);\n"
"}\n"
"\n"
"QPushButton::hover:!pressed {\n"
"	\n"
"	background-color: rgb(143, 227, 207);\n"
"	color: rgb(0, 43, 91);\n"
"\n"
"}")

        self.gridLayout_28.addWidget(self.task_mcq_new_set_btn, 8, 0, 1, 2)

        self.label_14 = QLabel(self.frame_16)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(0, 50))
        self.label_14.setMaximumSize(QSize(16777215, 50))
        self.label_14.setFont(font15)
        self.label_14.setStyleSheet(u"color: rgb(159, 251, 228);\n"
"background-color: rgb(0, 43, 91);")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.gridLayout_28.addWidget(self.label_14, 0, 0, 1, 8)

        self.task_mcq_question_edit = QTextEdit(self.frame_16)
        self.task_mcq_question_edit.setObjectName(u"task_mcq_question_edit")
        self.task_mcq_question_edit.setEnabled(False)
        self.task_mcq_question_edit.setMinimumSize(QSize(791, 71))
        font26 = QFont()
        font26.setPointSize(12)
        self.task_mcq_question_edit.setFont(font26)
        self.task_mcq_question_edit.setStyleSheet(u"QTextEdit {\n"
"background-color: rgb(137, 218, 199);\n"
"border: 2px solid rgb(101, 161, 146);\n"
"padding: 10px;\n"
"border-radius: 10px;\n"
"color: rgb(43, 72, 101);                        \n"
" }\n"
"\n"
" QTextEdit:disabled {\n"
"      background-color: gray;\n"
"		border: 2px solid rgb(102, 102, 102);\n"
"}")

        self.gridLayout_28.addWidget(self.task_mcq_question_edit, 1, 1, 1, 7)

        self.task_mcq_next_ques_btn = QPushButton(self.frame_16)
        self.task_mcq_next_ques_btn.setObjectName(u"task_mcq_next_ques_btn")
        self.task_mcq_next_ques_btn.setEnabled(False)
        self.task_mcq_next_ques_btn.setMinimumSize(QSize(154, 55))
        self.task_mcq_next_ques_btn.setFont(font19)
        self.task_mcq_next_ques_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.task_mcq_next_ques_btn.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(160, 253, 230);\n"
"color:  rgb(0, 43, 91) ;\n"
"border-radius: 15px;\n"
"border: 4px solid rgb(43, 72, 101);\n"
"}\n"
"\n"
"QPushButton::hover:!pressed {\n"
"	\n"
"	background-color: rgb(143, 227, 207);\n"
"	color: rgb(0, 43, 91);\n"
"\n"
"}\n"
"\n"
" QPushButton:disabled {\n"
"                        color: gray;\n"
" }")
        icon17 = QIcon()
        icon17.addFile(u"../Images/right.png", QSize(), QIcon.Normal, QIcon.Off)
        self.task_mcq_next_ques_btn.setIcon(icon17)

        self.gridLayout_28.addWidget(self.task_mcq_next_ques_btn, 8, 7, 1, 1)

        self.horizontalSpacer_26 = QSpacerItem(302, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_28.addItem(self.horizontalSpacer_26, 8, 6, 1, 1)

        self.line = QFrame(self.frame_16)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_28.addWidget(self.line, 5, 0, 1, 8)

        self.frame_18 = QFrame(self.frame_16)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMinimumSize(QSize(941, 203))
        self.frame_18.setMaximumSize(QSize(16777215, 331))
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.gridLayout_29 = QGridLayout(self.frame_18)
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.frame_17 = QFrame(self.frame_18)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMinimumSize(QSize(445, 81))
        self.frame_17.setMaximumSize(QSize(16777215, 81))
        self.frame_17.setStyleSheet(u"border: 2px solid rgb(0, 43, 91);")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.gridLayout_27 = QGridLayout(self.frame_17)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.label_22 = QLabel(self.frame_17)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMinimumSize(QSize(101, 51))
        self.label_22.setFont(font26)
        self.label_22.setStyleSheet(u"color: rgb(132, 211, 184);\n"
"background-color: rgb(0, 43, 91);\n"
"padding: 5px;\n"
"border-radius: 10px;")
        self.label_22.setAlignment(Qt.AlignCenter)

        self.gridLayout_27.addWidget(self.label_22, 0, 0, 1, 1)

        self.task_mcq_set_no_edit = QTextEdit(self.frame_17)
        self.task_mcq_set_no_edit.setObjectName(u"task_mcq_set_no_edit")
        self.task_mcq_set_no_edit.setEnabled(True)
        self.task_mcq_set_no_edit.setMinimumSize(QSize(317, 55))
        font27 = QFont()
        font27.setPointSize(15)
        self.task_mcq_set_no_edit.setFont(font27)
        self.task_mcq_set_no_edit.setStyleSheet(u"QTextEdit {\n"
"background-color: rgb(137, 218, 199);\n"
"border: 2px solid rgb(101, 161, 146);\n"
"padding: 10px;\n"
"border-radius: 10px;\n"
"color: rgb(43, 72, 101);                        \n"
" }\n"
"\n"
" QTextEdit:disabled {\n"
"      background-color: gray;\n"
"		border: 2px solid rgb(102, 102, 102);\n"
"}")

        self.gridLayout_27.addWidget(self.task_mcq_set_no_edit, 0, 1, 1, 1)


        self.gridLayout_29.addWidget(self.frame_17, 4, 2, 1, 2)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_29.addItem(self.verticalSpacer_7, 0, 2, 1, 1)

        self.task_mcq_option_4_edit = QTextEdit(self.frame_18)
        self.task_mcq_option_4_edit.setObjectName(u"task_mcq_option_4_edit")
        self.task_mcq_option_4_edit.setEnabled(False)
        self.task_mcq_option_4_edit.setMinimumSize(QSize(341, 51))
        self.task_mcq_option_4_edit.setFont(font27)
        self.task_mcq_option_4_edit.setStyleSheet(u"QTextEdit {\n"
"background-color: rgb(137, 218, 199);\n"
"border: 2px solid rgb(101, 161, 146);\n"
"padding: 10px;\n"
"border-radius: 10px;\n"
"color: rgb(43, 72, 101);                        \n"
" }\n"
"\n"
" QTextEdit:disabled {\n"
"      background-color: gray;\n"
"		border: 2px solid rgb(102, 102, 102);\n"
"}")

        self.gridLayout_29.addWidget(self.task_mcq_option_4_edit, 2, 3, 1, 1)

        self.label_20 = QLabel(self.frame_18)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(101, 51))
        self.label_20.setFont(font18)
        self.label_20.setStyleSheet(u"color: rgb(132, 211, 184);\n"
"background-color: rgb(0, 43, 91);\n"
"padding: 5px;\n"
"border-radius: 10px;")
        self.label_20.setAlignment(Qt.AlignCenter)

        self.gridLayout_29.addWidget(self.label_20, 2, 2, 1, 1)

        self.task_mcq_option_1_edit = QTextEdit(self.frame_18)
        self.task_mcq_option_1_edit.setObjectName(u"task_mcq_option_1_edit")
        self.task_mcq_option_1_edit.setEnabled(False)
        self.task_mcq_option_1_edit.setMinimumSize(QSize(341, 51))
        self.task_mcq_option_1_edit.setFont(font27)
        self.task_mcq_option_1_edit.setStyleSheet(u"QTextEdit {\n"
"background-color: rgb(137, 218, 199);\n"
"border: 2px solid rgb(101, 161, 146);\n"
"padding: 10px;\n"
"border-radius: 10px;\n"
"color: rgb(43, 72, 101);                        \n"
" }\n"
"\n"
" QTextEdit:disabled {\n"
"      background-color: gray;\n"
"		border: 2px solid rgb(102, 102, 102);\n"
"}")

        self.gridLayout_29.addWidget(self.task_mcq_option_1_edit, 1, 1, 1, 1)

        self.task_mcq_option_3_edit = QTextEdit(self.frame_18)
        self.task_mcq_option_3_edit.setObjectName(u"task_mcq_option_3_edit")
        self.task_mcq_option_3_edit.setEnabled(False)
        self.task_mcq_option_3_edit.setMinimumSize(QSize(341, 51))
        self.task_mcq_option_3_edit.setFont(font27)
        self.task_mcq_option_3_edit.setStyleSheet(u"QTextEdit {\n"
"background-color: rgb(137, 218, 199);\n"
"border: 2px solid rgb(101, 161, 146);\n"
"padding: 10px;\n"
"border-radius: 10px;\n"
"color: rgb(43, 72, 101);                        \n"
" }\n"
"\n"
" QTextEdit:disabled {\n"
"      background-color: gray;\n"
"		border: 2px solid rgb(102, 102, 102);\n"
"}")

        self.gridLayout_29.addWidget(self.task_mcq_option_3_edit, 2, 1, 1, 1)

        self.label_17 = QLabel(self.frame_18)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(101, 51))
        self.label_17.setFont(font18)
        self.label_17.setStyleSheet(u"color: rgb(132, 211, 184);\n"
"background-color: rgb(0, 43, 91);\n"
"padding: 5px;\n"
"border-radius: 10px;")
        self.label_17.setAlignment(Qt.AlignCenter)

        self.gridLayout_29.addWidget(self.label_17, 1, 0, 1, 1)

        self.label_18 = QLabel(self.frame_18)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(101, 51))
        self.label_18.setFont(font18)
        self.label_18.setStyleSheet(u"color: rgb(132, 211, 184);\n"
"background-color: rgb(0, 43, 91);\n"
"padding: 5px;\n"
"border-radius: 10px;")
        self.label_18.setAlignment(Qt.AlignCenter)

        self.gridLayout_29.addWidget(self.label_18, 1, 2, 1, 1)

        self.label_21 = QLabel(self.frame_18)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMinimumSize(QSize(101, 51))
        self.label_21.setFont(font26)
        self.label_21.setStyleSheet(u"color: rgb(132, 211, 184);\n"
"background-color: rgb(0, 43, 91);\n"
"padding: 5px;\n"
"border-radius: 10px;")
        self.label_21.setAlignment(Qt.AlignCenter)

        self.gridLayout_29.addWidget(self.label_21, 4, 0, 1, 1)

        self.task_mcq_correct_option_edit = QTextEdit(self.frame_18)
        self.task_mcq_correct_option_edit.setObjectName(u"task_mcq_correct_option_edit")
        self.task_mcq_correct_option_edit.setEnabled(False)
        self.task_mcq_correct_option_edit.setMinimumSize(QSize(341, 63))
        self.task_mcq_correct_option_edit.setFont(font27)
        self.task_mcq_correct_option_edit.setStyleSheet(u"QTextEdit {\n"
"background-color: rgb(137, 218, 199);\n"
"border: 2px solid rgb(101, 161, 146);\n"
"padding: 10px;\n"
"border-radius: 10px;\n"
"color: rgb(43, 72, 101);                        \n"
" }\n"
"\n"
" QTextEdit:disabled {\n"
"      background-color: gray;\n"
"		border: 2px solid rgb(102, 102, 102);\n"
"}")

        self.gridLayout_29.addWidget(self.task_mcq_correct_option_edit, 4, 1, 1, 1)

        self.task_mcq_option_2_edit = QTextEdit(self.frame_18)
        self.task_mcq_option_2_edit.setObjectName(u"task_mcq_option_2_edit")
        self.task_mcq_option_2_edit.setEnabled(False)
        self.task_mcq_option_2_edit.setMinimumSize(QSize(341, 51))
        self.task_mcq_option_2_edit.setFont(font27)
        self.task_mcq_option_2_edit.setStyleSheet(u"QTextEdit {\n"
"background-color: rgb(137, 218, 199);\n"
"border: 2px solid rgb(101, 161, 146);\n"
"padding: 10px;\n"
"border-radius: 10px;\n"
"color: rgb(43, 72, 101);                        \n"
" }\n"
"\n"
" QTextEdit:disabled {\n"
"      background-color: gray;\n"
"		border: 2px solid rgb(102, 102, 102);\n"
"}")

        self.gridLayout_29.addWidget(self.task_mcq_option_2_edit, 1, 3, 1, 1)

        self.label_19 = QLabel(self.frame_18)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(101, 51))
        self.label_19.setFont(font18)
        self.label_19.setStyleSheet(u"color: rgb(132, 211, 184);\n"
"background-color: rgb(0, 43, 91);\n"
"padding: 5px;\n"
"border-radius: 10px;")
        self.label_19.setAlignment(Qt.AlignCenter)

        self.gridLayout_29.addWidget(self.label_19, 2, 0, 1, 1)

        self.line_5 = QFrame(self.frame_18)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.gridLayout_29.addWidget(self.line_5, 3, 0, 1, 4)


        self.gridLayout_28.addWidget(self.frame_18, 6, 0, 1, 8)

        self.task_mcq_finish_set_btn = QPushButton(self.frame_16)
        self.task_mcq_finish_set_btn.setObjectName(u"task_mcq_finish_set_btn")
        self.task_mcq_finish_set_btn.setEnabled(False)
        self.task_mcq_finish_set_btn.setMinimumSize(QSize(153, 55))
        self.task_mcq_finish_set_btn.setMaximumSize(QSize(153, 16777215))
        self.task_mcq_finish_set_btn.setFont(font24)
        self.task_mcq_finish_set_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.task_mcq_finish_set_btn.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(160, 253, 230);\n"
"color:  rgb(0, 43, 91) ;\n"
"border-radius: 15px;\n"
"border: 4px solid rgb(43, 72, 101);\n"
"}\n"
"\n"
"QPushButton::hover:!pressed {\n"
"	\n"
"	background-color: rgb(143, 227, 207);\n"
"	color: rgb(0, 43, 91);\n"
"\n"
"}\n"
"\n"
" QPushButton:disabled {\n"
"                        color: gray;\n"
" }")

        self.gridLayout_28.addWidget(self.task_mcq_finish_set_btn, 8, 2, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 180, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_28.addItem(self.verticalSpacer_8, 4, 0, 1, 1)

        self.task_mcq_upload_img_btn = QPushButton(self.frame_16)
        self.task_mcq_upload_img_btn.setObjectName(u"task_mcq_upload_img_btn")
        self.task_mcq_upload_img_btn.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.task_mcq_upload_img_btn.sizePolicy().hasHeightForWidth())
        self.task_mcq_upload_img_btn.setSizePolicy(sizePolicy1)
        self.task_mcq_upload_img_btn.setMinimumSize(QSize(290, 50))
        self.task_mcq_upload_img_btn.setMaximumSize(QSize(320, 50))
        self.task_mcq_upload_img_btn.setFont(font5)
        self.task_mcq_upload_img_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.task_mcq_upload_img_btn.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(160, 253, 230);\n"
"color:  rgb(0, 43, 91) ;\n"
"border-radius: 15px;\n"
"border: 4px solid rgb(43, 72, 101);\n"
"}\n"
"\n"
"QPushButton::hover:!pressed {\n"
"	\n"
"	background-color: rgb(143, 227, 207);\n"
"	color: rgb(0, 43, 91);\n"
"\n"
"}\n"
"\n"
" QPushButton:disabled {\n"
"                        color: gray;\n"
" }")
        self.task_mcq_upload_img_btn.setIcon(icon7)
        self.task_mcq_upload_img_btn.setIconSize(QSize(20, 25))

        self.gridLayout_28.addWidget(self.task_mcq_upload_img_btn, 2, 7, 1, 1)

        self.task_mcq_img_lbl = QLabel(self.frame_16)
        self.task_mcq_img_lbl.setObjectName(u"task_mcq_img_lbl")
        font28 = QFont()
        font28.setPointSize(10)
        self.task_mcq_img_lbl.setFont(font28)
        self.task_mcq_img_lbl.setStyleSheet(u"color: rgb(160, 253, 230);")
        self.task_mcq_img_lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_28.addWidget(self.task_mcq_img_lbl, 2, 6, 1, 1)


        self.gridLayout_26.addWidget(self.frame_16, 0, 0, 1, 1)

        self.evalstackwidget.addWidget(self.mcq_page)

        self.gridLayout_6.addWidget(self.evalstackwidget, 1, 0, 1, 1)


        self.horizontalLayout_16.addWidget(self.eval_right_frame)


        self.verticalLayout_3.addWidget(self.body)


        self.gridLayout_13.addWidget(self.evaluation_frame, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.task_page)
        self.lesson_making_page = QWidget()
        self.lesson_making_page.setObjectName(u"lesson_making_page")
        self.gridLayout_8 = QGridLayout(self.lesson_making_page)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.lesson_making_page)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(1280, 720))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.lesson_frame_2 = QFrame(self.frame)
        self.lesson_frame_2.setObjectName(u"lesson_frame_2")
        self.lesson_frame_2.setMinimumSize(QSize(1280, 720))
        self.lesson_frame_2.setStyleSheet(u"")
        self.lesson_frame_2.setFrameShape(QFrame.StyledPanel)
        self.lesson_frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.lesson_frame_2)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.top_frame_5 = QFrame(self.lesson_frame_2)
        self.top_frame_5.setObjectName(u"top_frame_5")
        self.top_frame_5.setMinimumSize(QSize(1278, 80))
        self.top_frame_5.setMaximumSize(QSize(16777215, 80))
        self.top_frame_5.setStyleSheet(u"background-color: #2B4865;")
        self.top_frame_5.setFrameShape(QFrame.StyledPanel)
        self.top_frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.top_frame_5)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.lsn_btn_back_to_home_3 = QPushButton(self.top_frame_5)
        self.lsn_btn_back_to_home_3.setObjectName(u"lsn_btn_back_to_home_3")
        sizePolicy.setHeightForWidth(self.lsn_btn_back_to_home_3.sizePolicy().hasHeightForWidth())
        self.lsn_btn_back_to_home_3.setSizePolicy(sizePolicy)
        self.lsn_btn_back_to_home_3.setMinimumSize(QSize(0, 60))
        self.lsn_btn_back_to_home_3.setMaximumSize(QSize(60, 60))
        self.lsn_btn_back_to_home_3.setBaseSize(QSize(0, 4))
        self.lsn_btn_back_to_home_3.setFont(font1)
        self.lsn_btn_back_to_home_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.lsn_btn_back_to_home_3.setMouseTracking(True)
        self.lsn_btn_back_to_home_3.setStyleSheet(u"QPushButton {\n"
"	background-color: #2B4865 #256D85;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover:!pressed\n"
"{\n"
"	background-color:  #256D85;\n"
"	border-radius: 30px;\n"
"}")
        self.lsn_btn_back_to_home_3.setIcon(icon5)
        self.lsn_btn_back_to_home_3.setIconSize(QSize(200, 200))
        self.lsn_btn_back_to_home_3.setAutoDefault(False)
        self.lsn_btn_back_to_home_3.setFlat(False)

        self.horizontalLayout_24.addWidget(self.lsn_btn_back_to_home_3)

        self.lsn_lbl_headline_4 = QLabel(self.top_frame_5)
        self.lsn_lbl_headline_4.setObjectName(u"lsn_lbl_headline_4")
        self.lsn_lbl_headline_4.setFont(font2)
        self.lsn_lbl_headline_4.setStyleSheet(u"color: #8FE3CF")
        self.lsn_lbl_headline_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_24.addWidget(self.lsn_lbl_headline_4)


        self.verticalLayout_9.addWidget(self.top_frame_5)

        self.mid_frame_4 = QFrame(self.lesson_frame_2)
        self.mid_frame_4.setObjectName(u"mid_frame_4")
        self.mid_frame_4.setMinimumSize(QSize(1306, 641))
        self.mid_frame_4.setStyleSheet(u"background-color:rgb(36, 105, 127);")
        self.mid_frame_4.setFrameShape(QFrame.StyledPanel)
        self.mid_frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.mid_frame_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.verticalSpacer_5 = QSpacerItem(20, 117, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_5, 8, 6, 1, 1)

        self.label_4 = QLabel(self.mid_frame_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(365, 68))
        self.label_4.setFont(font24)
        self.label_4.setStyleSheet(u"color: rgb(132, 211, 184);\n"
"background-color: rgb(0, 43, 91);\n"
"padding: 5px;")
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_4.setWordWrap(True)

        self.gridLayout_4.addWidget(self.label_4, 7, 1, 1, 3)

        self.horizontalSpacer_20 = QSpacerItem(160, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_20, 6, 1, 1, 1)

        self.horizontalSpacer_21 = QSpacerItem(159, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_21, 6, 3, 1, 1)

        self.label_3 = QLabel(self.mid_frame_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font24)
        self.label_3.setStyleSheet(u"color: rgb(132, 211, 184);\n"
"background-color: rgb(0, 43, 91);\n"
"padding: 5px;")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_3.setWordWrap(True)

        self.gridLayout_4.addWidget(self.label_3, 5, 1, 1, 3)

        self.label_2 = QLabel(self.mid_frame_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font24)
        self.label_2.setStyleSheet(u"color: rgb(132, 211, 184);\n"
"background-color: rgb(0, 43, 91);\n"
"padding: 5px;")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setWordWrap(True)

        self.gridLayout_4.addWidget(self.label_2, 3, 1, 1, 3)

        self.lsn_module_table_widget = QTableWidget(self.mid_frame_4)
        if (self.lsn_module_table_widget.columnCount() < 2):
            self.lsn_module_table_widget.setColumnCount(2)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem6.setFont(font17);
        self.lsn_module_table_widget.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem7.setFont(font17);
        self.lsn_module_table_widget.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        self.lsn_module_table_widget.setObjectName(u"lsn_module_table_widget")
        self.lsn_module_table_widget.setMinimumSize(QSize(451, 501))
        self.lsn_module_table_widget.viewport().setProperty("cursor", QCursor(Qt.OpenHandCursor))
        self.lsn_module_table_widget.setStyleSheet(u"QHeaderView::section {\n"
"	background-color: #002B5B;\n"
"    color: rgb(143, 227, 207);\n"
"}\n"
"\n"
"\n"
"\n"
"QTableWidget {\n"
"	background-color: #256D85;\n"
"	gridline-color: rgb(255, 255, 255);\n"
"	color: #fff;\n"
"	border: 2px solid rgb(0, 43, 91);\n"
"}\n"
"\n"
"")
        self.lsn_module_table_widget.horizontalHeader().setDefaultSectionSize(188)
        self.lsn_module_table_widget.horizontalHeader().setStretchLastSection(True)

        self.gridLayout_4.addWidget(self.lsn_module_table_widget, 1, 0, 8, 1)

        self.horizontalSpacer_9 = QSpacerItem(21, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_9, 4, 6, 1, 1)

        self.label = QLabel(self.mid_frame_4)
        self.label.setObjectName(u"label")
        self.label.setFont(font24)
        self.label.setStyleSheet(u"color: rgb(132, 211, 184);\n"
"background-color: rgb(0, 43, 91);\n"
"padding: 5px;")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(True)

        self.gridLayout_4.addWidget(self.label, 1, 1, 1, 3)

        self.label_7 = QLabel(self.mid_frame_4)
        self.label_7.setObjectName(u"label_7")
        font29 = QFont()
        font29.setPointSize(7)
        self.label_7.setFont(font29)
        self.label_7.setPixmap(QPixmap(u"../Images/downward_icon.png"))

        self.gridLayout_4.addWidget(self.label_7, 6, 2, 1, 1)

        self.lsn_btn_remove_module = QPushButton(self.mid_frame_4)
        self.lsn_btn_remove_module.setObjectName(u"lsn_btn_remove_module")
        sizePolicy1.setHeightForWidth(self.lsn_btn_remove_module.sizePolicy().hasHeightForWidth())
        self.lsn_btn_remove_module.setSizePolicy(sizePolicy1)
        self.lsn_btn_remove_module.setMinimumSize(QSize(200, 58))
        self.lsn_btn_remove_module.setMaximumSize(QSize(200, 58))
        self.lsn_btn_remove_module.setFont(font17)
        self.lsn_btn_remove_module.setCursor(QCursor(Qt.PointingHandCursor))
        self.lsn_btn_remove_module.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(160, 253, 230);\n"
"color:  #256D85 ;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	\n"
"	background-color: rgb(143, 227, 207);\n"
"	color: #2B4865;\n"
"\n"
"}")
        icon18 = QIcon()
        icon18.addFile(u"../Images/remove_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.lsn_btn_remove_module.setIcon(icon18)
        self.lsn_btn_remove_module.setIconSize(QSize(20, 25))

        self.gridLayout_4.addWidget(self.lsn_btn_remove_module, 10, 4, 1, 1)

        self.lsn_lbl_lessons_5 = QLabel(self.mid_frame_4)
        self.lsn_lbl_lessons_5.setObjectName(u"lsn_lbl_lessons_5")
        self.lsn_lbl_lessons_5.setMinimumSize(QSize(371, 36))
        font30 = QFont()
        font30.setFamilies([u"Hind Siliguri Medium"])
        font30.setPointSize(16)
        font30.setBold(False)
        self.lsn_lbl_lessons_5.setFont(font30)
        self.lsn_lbl_lessons_5.setStyleSheet(u"color: rgb(149, 236, 215);")
        self.lsn_lbl_lessons_5.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.lsn_lbl_lessons_5, 0, 4, 1, 2)

        self.label_6 = QLabel(self.mid_frame_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font29)
        self.label_6.setPixmap(QPixmap(u"../Images/downward_icon.png"))

        self.gridLayout_4.addWidget(self.label_6, 4, 2, 1, 1)

        self.lsn_btn_finish_add_module = QPushButton(self.mid_frame_4)
        self.lsn_btn_finish_add_module.setObjectName(u"lsn_btn_finish_add_module")
        self.lsn_btn_finish_add_module.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.lsn_btn_finish_add_module.sizePolicy().hasHeightForWidth())
        self.lsn_btn_finish_add_module.setSizePolicy(sizePolicy1)
        self.lsn_btn_finish_add_module.setMinimumSize(QSize(200, 58))
        self.lsn_btn_finish_add_module.setMaximumSize(QSize(200, 58))
        self.lsn_btn_finish_add_module.setFont(font17)
        self.lsn_btn_finish_add_module.setCursor(QCursor(Qt.PointingHandCursor))
        self.lsn_btn_finish_add_module.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(160, 253, 230);\n"
"color:  #256D85 ;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	\n"
"	background-color: rgb(143, 227, 207);\n"
"	color: #2B4865;\n"
"\n"
"}")
        icon19 = QIcon()
        icon19.addFile(u"../Images/done.png", QSize(), QIcon.Normal, QIcon.Off)
        self.lsn_btn_finish_add_module.setIcon(icon19)
        self.lsn_btn_finish_add_module.setIconSize(QSize(20, 25))

        self.gridLayout_4.addWidget(self.lsn_btn_finish_add_module, 10, 5, 1, 1)

        self.horizontalSpacer_17 = QSpacerItem(160, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_17, 2, 1, 1, 1)

        self.label_5 = QLabel(self.mid_frame_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font29)
        self.label_5.setPixmap(QPixmap(u"../Images/downward_icon.png"))

        self.gridLayout_4.addWidget(self.label_5, 2, 2, 1, 1)

        self.horizontalSpacer_18 = QSpacerItem(160, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_18, 4, 1, 1, 1)

        self.horizontalSpacer_16 = QSpacerItem(159, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_16, 2, 3, 1, 1)

        self.lsn_lbl_lessons_3 = QLabel(self.mid_frame_4)
        self.lsn_lbl_lessons_3.setObjectName(u"lsn_lbl_lessons_3")
        self.lsn_lbl_lessons_3.setMinimumSize(QSize(451, 36))
        self.lsn_lbl_lessons_3.setFont(font30)
        self.lsn_lbl_lessons_3.setStyleSheet(u"color: rgb(149, 236, 215);")
        self.lsn_lbl_lessons_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.lsn_lbl_lessons_3, 0, 0, 1, 1)

        self.lsn_lbl_lessons_4 = QLabel(self.mid_frame_4)
        self.lsn_lbl_lessons_4.setObjectName(u"lsn_lbl_lessons_4")
        self.lsn_lbl_lessons_4.setMinimumSize(QSize(361, 36))
        self.lsn_lbl_lessons_4.setFont(font30)
        self.lsn_lbl_lessons_4.setStyleSheet(u"color: rgb(149, 236, 215);")
        self.lsn_lbl_lessons_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.lsn_lbl_lessons_4, 0, 1, 1, 3)

        self.lsn_new_module_list_view = QListView(self.mid_frame_4)
        self.lsn_new_module_list_view.setObjectName(u"lsn_new_module_list_view")
        self.lsn_new_module_list_view.setMinimumSize(QSize(424, 509))
        self.lsn_new_module_list_view.setFont(font28)
        self.lsn_new_module_list_view.setStyleSheet(u"color: rgb(143, 227, 190);\n"
"border: 2px solid rgb(0, 43, 91);")
        self.lsn_new_module_list_view.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.lsn_new_module_list_view.setDragEnabled(True)

        self.gridLayout_4.addWidget(self.lsn_new_module_list_view, 1, 4, 9, 2)

        self.horizontalSpacer_19 = QSpacerItem(159, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_19, 4, 3, 1, 1)

        self.lsn_btn_see_lessons = QPushButton(self.mid_frame_4)
        self.lsn_btn_see_lessons.setObjectName(u"lsn_btn_see_lessons")
        self.lsn_btn_see_lessons.setMinimumSize(QSize(151, 41))
        self.lsn_btn_see_lessons.setFont(font1)
        self.lsn_btn_see_lessons.setCursor(QCursor(Qt.PointingHandCursor))
        self.lsn_btn_see_lessons.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(160, 253, 230);\n"
"color:  #256D85 ;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	\n"
"	background-color: rgb(143, 227, 207);\n"
"	color: #2B4865;\n"
"\n"
"}")
        icon20 = QIcon()
        icon20.addFile(u"../Images/open_folders_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.lsn_btn_see_lessons.setIcon(icon20)
        self.lsn_btn_see_lessons.setIconSize(QSize(30, 30))

        self.gridLayout_4.addWidget(self.lsn_btn_see_lessons, 9, 1, 2, 3)


        self.verticalLayout_9.addWidget(self.mid_frame_4)


        self.gridLayout_3.addWidget(self.lesson_frame_2, 0, 0, 1, 1)


        self.gridLayout_8.addWidget(self.frame, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.lesson_making_page)
        self.lesson_assigning_page = QWidget()
        self.lesson_assigning_page.setObjectName(u"lesson_assigning_page")
        self.gridLayout_11 = QGridLayout(self.lesson_assigning_page)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.lesson_assigning_page)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_2)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, -1, 0)
        self.lesson_frame_3 = QFrame(self.frame_2)
        self.lesson_frame_3.setObjectName(u"lesson_frame_3")
        self.lesson_frame_3.setMinimumSize(QSize(1280, 720))
        self.lesson_frame_3.setStyleSheet(u"")
        self.lesson_frame_3.setFrameShape(QFrame.StyledPanel)
        self.lesson_frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.lesson_frame_3)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.top_frame_6 = QFrame(self.lesson_frame_3)
        self.top_frame_6.setObjectName(u"top_frame_6")
        self.top_frame_6.setMinimumSize(QSize(1278, 80))
        self.top_frame_6.setMaximumSize(QSize(16777215, 80))
        self.top_frame_6.setStyleSheet(u"background-color: #2B4865;")
        self.top_frame_6.setFrameShape(QFrame.StyledPanel)
        self.top_frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.top_frame_6)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.lsn_btn_back_to_home_4 = QPushButton(self.top_frame_6)
        self.lsn_btn_back_to_home_4.setObjectName(u"lsn_btn_back_to_home_4")
        sizePolicy.setHeightForWidth(self.lsn_btn_back_to_home_4.sizePolicy().hasHeightForWidth())
        self.lsn_btn_back_to_home_4.setSizePolicy(sizePolicy)
        self.lsn_btn_back_to_home_4.setMinimumSize(QSize(0, 60))
        self.lsn_btn_back_to_home_4.setMaximumSize(QSize(60, 60))
        self.lsn_btn_back_to_home_4.setBaseSize(QSize(0, 4))
        self.lsn_btn_back_to_home_4.setFont(font1)
        self.lsn_btn_back_to_home_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.lsn_btn_back_to_home_4.setMouseTracking(True)
        self.lsn_btn_back_to_home_4.setStyleSheet(u"QPushButton {\n"
"	background-color: #2B4865 #256D85;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover:!pressed\n"
"{\n"
"	background-color:  #256D85;\n"
"	border-radius: 30px;\n"
"}")
        self.lsn_btn_back_to_home_4.setIcon(icon5)
        self.lsn_btn_back_to_home_4.setIconSize(QSize(200, 200))
        self.lsn_btn_back_to_home_4.setAutoDefault(False)
        self.lsn_btn_back_to_home_4.setFlat(False)

        self.horizontalLayout_25.addWidget(self.lsn_btn_back_to_home_4)

        self.lsn_lbl_headline_5 = QLabel(self.top_frame_6)
        self.lsn_lbl_headline_5.setObjectName(u"lsn_lbl_headline_5")
        self.lsn_lbl_headline_5.setFont(font2)
        self.lsn_lbl_headline_5.setStyleSheet(u"color: #8FE3CF")
        self.lsn_lbl_headline_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_25.addWidget(self.lsn_lbl_headline_5)


        self.verticalLayout_6.addWidget(self.top_frame_6)

        self.mid_frame_5 = QFrame(self.lesson_frame_3)
        self.mid_frame_5.setObjectName(u"mid_frame_5")
        self.mid_frame_5.setMinimumSize(QSize(1306, 641))
        self.mid_frame_5.setStyleSheet(u"background-color:rgb(36, 105, 127);")
        self.mid_frame_5.setFrameShape(QFrame.StyledPanel)
        self.mid_frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.mid_frame_5)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.lsn_lbl_lessons_6 = QLabel(self.mid_frame_5)
        self.lsn_lbl_lessons_6.setObjectName(u"lsn_lbl_lessons_6")
        self.lsn_lbl_lessons_6.setMinimumSize(QSize(451, 36))
        self.lsn_lbl_lessons_6.setFont(font30)
        self.lsn_lbl_lessons_6.setStyleSheet(u"color: rgb(149, 236, 215);")
        self.lsn_lbl_lessons_6.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.lsn_lbl_lessons_6, 0, 1, 1, 1)

        self.lsn_table_assigning_lessons = QTableWidget(self.mid_frame_5)
        if (self.lsn_table_assigning_lessons.columnCount() < 8):
            self.lsn_table_assigning_lessons.setColumnCount(8)
        font31 = QFont()
        font31.setPointSize(12)
        font31.setBold(False)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem8.setFont(font31);
        self.lsn_table_assigning_lessons.setHorizontalHeaderItem(0, __qtablewidgetitem8)
        font32 = QFont()
        font32.setFamilies([u"Segoe UI"])
        font32.setPointSize(12)
        font32.setBold(False)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem9.setFont(font32);
        self.lsn_table_assigning_lessons.setHorizontalHeaderItem(1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem10.setFont(font32);
        self.lsn_table_assigning_lessons.setHorizontalHeaderItem(2, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem11.setFont(font26);
        self.lsn_table_assigning_lessons.setHorizontalHeaderItem(3, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem12.setFont(font26);
        self.lsn_table_assigning_lessons.setHorizontalHeaderItem(4, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem13.setFont(font26);
        self.lsn_table_assigning_lessons.setHorizontalHeaderItem(5, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem14.setFont(font26);
        self.lsn_table_assigning_lessons.setHorizontalHeaderItem(6, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem15.setFont(font26);
        self.lsn_table_assigning_lessons.setHorizontalHeaderItem(7, __qtablewidgetitem15)
        self.lsn_table_assigning_lessons.setObjectName(u"lsn_table_assigning_lessons")
        self.lsn_table_assigning_lessons.setMinimumSize(QSize(830, 511))
        self.lsn_table_assigning_lessons.setFont(font26)
        self.lsn_table_assigning_lessons.viewport().setProperty("cursor", QCursor(Qt.OpenHandCursor))
        self.lsn_table_assigning_lessons.setStyleSheet(u"QHeaderView::section {\n"
"	background-color: #002B5B;\n"
"    color: rgb(143, 227, 207);\n"
"}\n"
"\n"
"\n"
"\n"
"QTableWidget {\n"
"	background-color: #256D85;\n"
"	gridline-color: rgb(255, 255, 255);\n"
"	color: #fff;\n"
"	border: 2px solid rgb(0, 43, 91);\n"
"}\n"
"\n"
"")
        self.lsn_table_assigning_lessons.horizontalHeader().setMinimumSectionSize(50)
        self.lsn_table_assigning_lessons.horizontalHeader().setDefaultSectionSize(180)
        self.lsn_table_assigning_lessons.horizontalHeader().setStretchLastSection(True)

        self.gridLayout_10.addWidget(self.lsn_table_assigning_lessons, 1, 1, 1, 1)

        self.lsn_lbl_lessons_8 = QLabel(self.mid_frame_5)
        self.lsn_lbl_lessons_8.setObjectName(u"lsn_lbl_lessons_8")
        self.lsn_lbl_lessons_8.setMinimumSize(QSize(250, 36))
        self.lsn_lbl_lessons_8.setFont(font30)
        self.lsn_lbl_lessons_8.setStyleSheet(u"color: rgb(149, 236, 215);")
        self.lsn_lbl_lessons_8.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.lsn_lbl_lessons_8, 0, 0, 1, 1)

        self.lsn_btn_assign_lesson = QPushButton(self.mid_frame_5)
        self.lsn_btn_assign_lesson.setObjectName(u"lsn_btn_assign_lesson")
        self.lsn_btn_assign_lesson.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.lsn_btn_assign_lesson.sizePolicy().hasHeightForWidth())
        self.lsn_btn_assign_lesson.setSizePolicy(sizePolicy1)
        self.lsn_btn_assign_lesson.setMinimumSize(QSize(200, 58))
        self.lsn_btn_assign_lesson.setMaximumSize(QSize(200, 58))
        self.lsn_btn_assign_lesson.setFont(font17)
        self.lsn_btn_assign_lesson.setCursor(QCursor(Qt.PointingHandCursor))
        self.lsn_btn_assign_lesson.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(160, 253, 230);\n"
"color:  #256D85 ;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	\n"
"	background-color: rgb(143, 227, 207);\n"
"	color: #2B4865;\n"
"\n"
"}")
        self.lsn_btn_assign_lesson.setIcon(icon19)
        self.lsn_btn_assign_lesson.setIconSize(QSize(20, 25))

        self.gridLayout_10.addWidget(self.lsn_btn_assign_lesson, 2, 0, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(33, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer_8, 1, 2, 1, 1)

        self.lsn_list_students = QListWidget(self.mid_frame_5)
        self.lsn_list_students.setObjectName(u"lsn_list_students")
        self.lsn_list_students.setMinimumSize(QSize(401, 509))
        self.lsn_list_students.setMaximumSize(QSize(371, 16777215))
        font33 = QFont()
        font33.setPointSize(13)
        self.lsn_list_students.setFont(font33)
        self.lsn_list_students.setStyleSheet(u"color: rgb(143, 227, 190);\n"
"border: 2px solid rgb(0, 43, 91);")
        self.lsn_list_students.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.lsn_list_students.setDragEnabled(True)

        self.gridLayout_10.addWidget(self.lsn_list_students, 1, 0, 1, 1)


        self.verticalLayout_6.addWidget(self.mid_frame_5)


        self.gridLayout_9.addWidget(self.lesson_frame_3, 0, 0, 1, 1)


        self.gridLayout_11.addWidget(self.frame_2, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.lesson_assigning_page)
        self.performance_page = QWidget()
        self.performance_page.setObjectName(u"performance_page")
        self.gridLayout_15 = QGridLayout(self.performance_page)
        self.gridLayout_15.setSpacing(0)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setContentsMargins(0, 0, 0, 0)
        self.top_frame_7 = QFrame(self.performance_page)
        self.top_frame_7.setObjectName(u"top_frame_7")
        self.top_frame_7.setMinimumSize(QSize(1280, 80))
        self.top_frame_7.setMaximumSize(QSize(16777215, 80))
        self.top_frame_7.setStyleSheet(u"background-color: #2B4865;")
        self.top_frame_7.setFrameShape(QFrame.StyledPanel)
        self.top_frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.top_frame_7)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.lsn_btn_back_to_home_5 = QPushButton(self.top_frame_7)
        self.lsn_btn_back_to_home_5.setObjectName(u"lsn_btn_back_to_home_5")
        sizePolicy.setHeightForWidth(self.lsn_btn_back_to_home_5.sizePolicy().hasHeightForWidth())
        self.lsn_btn_back_to_home_5.setSizePolicy(sizePolicy)
        self.lsn_btn_back_to_home_5.setMinimumSize(QSize(0, 60))
        self.lsn_btn_back_to_home_5.setMaximumSize(QSize(60, 60))
        self.lsn_btn_back_to_home_5.setBaseSize(QSize(0, 4))
        self.lsn_btn_back_to_home_5.setFont(font1)
        self.lsn_btn_back_to_home_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.lsn_btn_back_to_home_5.setMouseTracking(True)
        self.lsn_btn_back_to_home_5.setStyleSheet(u"QPushButton {\n"
"	background-color: #2B4865 #256D85;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover:!pressed\n"
"{\n"
"	background-color:  #256D85;\n"
"	border-radius: 30px;\n"
"}")
        self.lsn_btn_back_to_home_5.setIcon(icon5)
        self.lsn_btn_back_to_home_5.setIconSize(QSize(200, 200))
        self.lsn_btn_back_to_home_5.setAutoDefault(False)
        self.lsn_btn_back_to_home_5.setFlat(False)

        self.horizontalLayout_26.addWidget(self.lsn_btn_back_to_home_5)

        self.lsn_lbl_headline_6 = QLabel(self.top_frame_7)
        self.lsn_lbl_headline_6.setObjectName(u"lsn_lbl_headline_6")
        self.lsn_lbl_headline_6.setMinimumSize(QSize(1280, 78))
        self.lsn_lbl_headline_6.setFont(font2)
        self.lsn_lbl_headline_6.setStyleSheet(u"color: #8FE3CF")
        self.lsn_lbl_headline_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_26.addWidget(self.lsn_lbl_headline_6)


        self.gridLayout_15.addWidget(self.top_frame_7, 0, 0, 1, 1)

        self.mid_frame_6 = QFrame(self.performance_page)
        self.mid_frame_6.setObjectName(u"mid_frame_6")
        self.mid_frame_6.setMinimumSize(QSize(1280, 641))
        self.mid_frame_6.setStyleSheet(u"background-color:rgb(36, 105, 127);")
        self.mid_frame_6.setFrameShape(QFrame.StyledPanel)
        self.mid_frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.mid_frame_6)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.frame_9 = QFrame(self.mid_frame_6)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(281, 617))
        self.frame_9.setMaximumSize(QSize(288, 617))
        self.frame_9.setStyleSheet(u"")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_9)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_11 = QFrame(self.frame_9)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(260, 111))
        self.frame_11.setMaximumSize(QSize(241, 111))
        self.frame_11.setStyleSheet(u"border: 2px dashed rgb(43, 72, 101);\n"
"background-color: rgb(152, 240, 218)")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_11)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_11 = QLabel(self.frame_11)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(200, 31))
        self.label_11.setFont(font1)
        self.label_11.setStyleSheet(u"border: none;")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_11)

        self.performance_std_id_cmb = QComboBox(self.frame_11)
        self.performance_std_id_cmb.addItem("")
        self.performance_std_id_cmb.setObjectName(u"performance_std_id_cmb")
        self.performance_std_id_cmb.setMinimumSize(QSize(201, 31))
        self.performance_std_id_cmb.setFont(font28)
        self.performance_std_id_cmb.setStyleSheet(u"border: none;\n"
"background-color: rgb(61, 64, 91);\n"
"color: white;")

        self.verticalLayout_7.addWidget(self.performance_std_id_cmb)


        self.verticalLayout_11.addWidget(self.frame_11)

        self.performance_lesson_btn = QPushButton(self.frame_9)
        self.performance_lesson_btn.setObjectName(u"performance_lesson_btn")
        self.performance_lesson_btn.setMinimumSize(QSize(200, 40))
        self.performance_lesson_btn.setFont(font28)
        self.performance_lesson_btn.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(160, 253, 230);\n"
"color:  rgb(0, 43, 91) ;\n"
"border-radius: 15px;\n"
"border: 4px solid rgb(43, 72, 101);\n"
"}\n"
"\n"
"QPushButton::hover:!pressed {\n"
"	\n"
"	background-color: rgb(143, 227, 207);\n"
"	color: rgb(0, 43, 91);\n"
"\n"
"}")

        self.verticalLayout_11.addWidget(self.performance_lesson_btn)

        self.performance_module_btn = QPushButton(self.frame_9)
        self.performance_module_btn.setObjectName(u"performance_module_btn")
        self.performance_module_btn.setMinimumSize(QSize(200, 40))
        self.performance_module_btn.setFont(font28)
        self.performance_module_btn.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(160, 253, 230);\n"
"color:  rgb(0, 43, 91) ;\n"
"border-radius: 15px;\n"
"border: 4px solid rgb(43, 72, 101);\n"
"}\n"
"\n"
"QPushButton::hover:!pressed {\n"
"	\n"
"	background-color: rgb(143, 227, 207);\n"
"	color: rgb(0, 43, 91);\n"
"\n"
"}")

        self.verticalLayout_11.addWidget(self.performance_module_btn)

        self.performance_eval_btn = QPushButton(self.frame_9)
        self.performance_eval_btn.setObjectName(u"performance_eval_btn")
        self.performance_eval_btn.setMinimumSize(QSize(200, 40))
        self.performance_eval_btn.setFont(font28)
        self.performance_eval_btn.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(160, 253, 230);\n"
"color:  rgb(0, 43, 91) ;\n"
"border-radius: 15px;\n"
"border: 4px solid rgb(43, 72, 101);\n"
"}\n"
"\n"
"QPushButton::hover:!pressed {\n"
"	\n"
"	background-color: rgb(143, 227, 207);\n"
"	color: rgb(0, 43, 91);\n"
"\n"
"}")

        self.verticalLayout_11.addWidget(self.performance_eval_btn)

        self.label_12 = QLabel(self.frame_9)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(261, 261))
        self.label_12.setFont(font28)
        self.label_12.setStyleSheet(u"color: rgb(132, 211, 184);\n"
"background-color: rgb(0, 43, 91);\n"
"padding: 5px;")
        self.label_12.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_12.setWordWrap(True)

        self.verticalLayout_11.addWidget(self.label_12)

        self.performance_report_btn = QPushButton(self.frame_9)
        self.performance_report_btn.setObjectName(u"performance_report_btn")
        self.performance_report_btn.setMinimumSize(QSize(260, 60))
        self.performance_report_btn.setMaximumSize(QSize(250, 60))
        self.performance_report_btn.setFont(font26)
        self.performance_report_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.performance_report_btn.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(160, 253, 230);\n"
"color:  #256D85 ;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	\n"
"	background-color: rgb(143, 227, 207);\n"
"	color: #2B4865;\n"
"\n"
"}")
        icon21 = QIcon()
        icon21.addFile(u"../../../Student/Frontend/Images/report.png", QSize(), QIcon.Normal, QIcon.Off)
        self.performance_report_btn.setIcon(icon21)
        self.performance_report_btn.setIconSize(QSize(35, 30))

        self.verticalLayout_11.addWidget(self.performance_report_btn)


        self.horizontalLayout_15.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.mid_frame_6)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(961, 617))
        self.frame_10.setStyleSheet(u"")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.gridLayout_24 = QGridLayout(self.frame_10)
        self.gridLayout_24.setSpacing(2)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.gridLayout_24.setContentsMargins(3, 3, 3, 3)
        self.performance_stackwidget = QStackedWidget(self.frame_10)
        self.performance_stackwidget.setObjectName(u"performance_stackwidget")
        self.performance_stackwidget.setStyleSheet(u"border: none;")
        self.lesson_stk_widget = QWidget()
        self.lesson_stk_widget.setObjectName(u"lesson_stk_widget")
        self.lesson_stk_widget.setStyleSheet(u"border: 2px solid rgb(152, 240, 218);")
        self.gridLayout_25 = QGridLayout(self.lesson_stk_widget)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.gridLayout_25.setContentsMargins(0, 0, 0, 0)
        self.frame_14 = QFrame(self.lesson_stk_widget)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_14)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(5, 5, 5, 5)
        self.frame_15 = QFrame(self.frame_14)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMinimumSize(QSize(900, 471))
        self.frame_15.setStyleSheet(u"border: none;")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.p_lesson_left_graph_lbl = QLabel(self.frame_15)
        self.p_lesson_left_graph_lbl.setObjectName(u"p_lesson_left_graph_lbl")
        self.p_lesson_left_graph_lbl.setMinimumSize(QSize(430, 380))
        self.p_lesson_left_graph_lbl.setStyleSheet(u"border: 3px solid rgb(43, 72, 101);")
        self.p_lesson_left_graph_lbl.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_19.addWidget(self.p_lesson_left_graph_lbl)

        self.p_lesson_right_graph_lbl = QLabel(self.frame_15)
        self.p_lesson_right_graph_lbl.setObjectName(u"p_lesson_right_graph_lbl")
        self.p_lesson_right_graph_lbl.setMinimumSize(QSize(430, 380))
        self.p_lesson_right_graph_lbl.setStyleSheet(u"border: 3px solid rgb(43, 72, 101);")
        self.p_lesson_right_graph_lbl.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_19.addWidget(self.p_lesson_right_graph_lbl)


        self.verticalLayout_10.addWidget(self.frame_15)


        self.gridLayout_25.addWidget(self.frame_14, 0, 0, 1, 1)

        self.performance_stackwidget.addWidget(self.lesson_stk_widget)
        self.module_stk_widget = QWidget()
        self.module_stk_widget.setObjectName(u"module_stk_widget")
        self.module_stk_widget.setStyleSheet(u"border: 2px solid rgb(160, 253, 230);")
        self.gridLayout_31 = QGridLayout(self.module_stk_widget)
        self.gridLayout_31.setObjectName(u"gridLayout_31")
        self.gridLayout_31.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_11 = QSpacerItem(20, 7, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_31.addItem(self.verticalSpacer_11, 0, 2, 1, 1)

        self.horizontalSpacer_30 = QSpacerItem(332, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_31.addItem(self.horizontalSpacer_30, 1, 0, 1, 2)

        self.p_lesson_id_cmb = QComboBox(self.module_stk_widget)
        self.p_lesson_id_cmb.addItem("")
        self.p_lesson_id_cmb.setObjectName(u"p_lesson_id_cmb")
        self.p_lesson_id_cmb.setMinimumSize(QSize(256, 50))
        self.p_lesson_id_cmb.setFont(font33)
        self.p_lesson_id_cmb.setStyleSheet(u"border: none;\n"
"background-color: rgb(61, 64, 91);\n"
"color: white;")

        self.gridLayout_31.addWidget(self.p_lesson_id_cmb, 1, 2, 1, 1)

        self.horizontalSpacer_29 = QSpacerItem(352, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_31.addItem(self.horizontalSpacer_29, 1, 3, 1, 2)

        self.verticalSpacer_9 = QSpacerItem(20, 18, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_31.addItem(self.verticalSpacer_9, 2, 2, 1, 1)

        self.p_module_graph_lbl = QLabel(self.module_stk_widget)
        self.p_module_graph_lbl.setObjectName(u"p_module_graph_lbl")
        self.p_module_graph_lbl.setMinimumSize(QSize(500, 500))
        self.p_module_graph_lbl.setStyleSheet(u"border: 3px solid rgb(43, 72, 101);")
        self.p_module_graph_lbl.setAlignment(Qt.AlignCenter)

        self.gridLayout_31.addWidget(self.p_module_graph_lbl, 3, 1, 2, 3)

        self.horizontalSpacer_28 = QSpacerItem(230, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_31.addItem(self.horizontalSpacer_28, 3, 4, 1, 1)

        self.horizontalSpacer_27 = QSpacerItem(210, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_31.addItem(self.horizontalSpacer_27, 4, 0, 1, 1)

        self.verticalSpacer_10 = QSpacerItem(20, 47, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_31.addItem(self.verticalSpacer_10, 5, 2, 1, 1)

        self.performance_stackwidget.addWidget(self.module_stk_widget)
        self.eval_stk_widget = QWidget()
        self.eval_stk_widget.setObjectName(u"eval_stk_widget")
        self.eval_stk_widget.setStyleSheet(u"border: 2px solid rgb(160, 253, 230);")
        self.verticalLayout_8 = QVBoxLayout(self.eval_stk_widget)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(5, 5, 5, 5)
        self.frame_12 = QFrame(self.eval_stk_widget)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(932, 130))
        self.frame_12.setMaximumSize(QSize(16777215, 144))
        self.frame_12.setStyleSheet(u"border: none;")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.p_eval_puzzle_btn = QPushButton(self.frame_12)
        self.p_eval_puzzle_btn.setObjectName(u"p_eval_puzzle_btn")
        self.p_eval_puzzle_btn.setMinimumSize(QSize(239, 65))
        self.p_eval_puzzle_btn.setFont(font27)
        self.p_eval_puzzle_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.p_eval_puzzle_btn.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(160, 253, 230);\n"
"color:  #256D85 ;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	\n"
"	background-color: rgb(143, 227, 207);\n"
"	color: #2B4865;\n"
"\n"
"}")

        self.horizontalLayout_14.addWidget(self.p_eval_puzzle_btn)

        self.p_eval_seq_btn = QPushButton(self.frame_12)
        self.p_eval_seq_btn.setObjectName(u"p_eval_seq_btn")
        self.p_eval_seq_btn.setMinimumSize(QSize(0, 65))
        self.p_eval_seq_btn.setFont(font18)
        self.p_eval_seq_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.p_eval_seq_btn.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(160, 253, 230);\n"
"color:  #256D85 ;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	\n"
"	background-color: rgb(143, 227, 207);\n"
"	color: #2B4865;\n"
"\n"
"}")

        self.horizontalLayout_14.addWidget(self.p_eval_seq_btn)

        self.p_eval_matching_btn = QPushButton(self.frame_12)
        self.p_eval_matching_btn.setObjectName(u"p_eval_matching_btn")
        self.p_eval_matching_btn.setMinimumSize(QSize(0, 65))
        self.p_eval_matching_btn.setFont(font33)
        self.p_eval_matching_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.p_eval_matching_btn.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(160, 253, 230);\n"
"color:  #256D85 ;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	\n"
"	background-color: rgb(143, 227, 207);\n"
"	color: #2B4865;\n"
"\n"
"}")

        self.horizontalLayout_14.addWidget(self.p_eval_matching_btn)

        self.p_eval_mcq_btn = QPushButton(self.frame_12)
        self.p_eval_mcq_btn.setObjectName(u"p_eval_mcq_btn")
        self.p_eval_mcq_btn.setMinimumSize(QSize(0, 65))
        self.p_eval_mcq_btn.setFont(font33)
        self.p_eval_mcq_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.p_eval_mcq_btn.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(160, 253, 230);\n"
"color:  #256D85 ;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	\n"
"	background-color: rgb(143, 227, 207);\n"
"	color: #2B4865;\n"
"\n"
"}")

        self.horizontalLayout_14.addWidget(self.p_eval_mcq_btn)


        self.verticalLayout_8.addWidget(self.frame_12)

        self.frame_13 = QFrame(self.eval_stk_widget)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMinimumSize(QSize(931, 446))
        self.frame_13.setStyleSheet(u"border: none;")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(5, 0, 5, 0)
        self.p_eval_left_graph_lbl = QLabel(self.frame_13)
        self.p_eval_left_graph_lbl.setObjectName(u"p_eval_left_graph_lbl")
        self.p_eval_left_graph_lbl.setMinimumSize(QSize(450, 400))
        self.p_eval_left_graph_lbl.setStyleSheet(u"border: 3px solid rgb(43, 72, 101);")
        self.p_eval_left_graph_lbl.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_18.addWidget(self.p_eval_left_graph_lbl)

        self.p_eval_right_graph_lbl = QLabel(self.frame_13)
        self.p_eval_right_graph_lbl.setObjectName(u"p_eval_right_graph_lbl")
        self.p_eval_right_graph_lbl.setMinimumSize(QSize(450, 400))
        self.p_eval_right_graph_lbl.setStyleSheet(u"border: 3px solid rgb(43, 72, 101);")
        self.p_eval_right_graph_lbl.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_18.addWidget(self.p_eval_right_graph_lbl)


        self.verticalLayout_8.addWidget(self.frame_13)

        self.performance_stackwidget.addWidget(self.eval_stk_widget)

        self.gridLayout_24.addWidget(self.performance_stackwidget, 0, 0, 1, 1)


        self.horizontalLayout_15.addWidget(self.frame_10)


        self.gridLayout_15.addWidget(self.mid_frame_6, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.performance_page)

        self.gridLayout_30.addWidget(self.stackedWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(5)
        self.std_btn_back_to_home.setDefault(False)
        self.mediaStackWidget.setCurrentIndex(0)
        self.lsn_btn_back_to_home.setDefault(False)
        self.task_btn_back_to_home.setDefault(False)
        self.evalstackwidget.setCurrentIndex(3)
        self.lsn_btn_back_to_home_3.setDefault(False)
        self.lsn_btn_back_to_home_4.setDefault(False)
        self.lsn_btn_back_to_home_5.setDefault(False)
        self.performance_stackwidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.home_lbl_ban_picture.setText("")
        self.home_btn_student.setText("")
        self.home_btn_lesson.setText("")
        self.home_btn_lesson_assigns.setText("")
        self.home_btn_quiz.setText("")
        self.home_btn_progress.setText("")
        self.std_btn_back_to_home.setText("")
        self.std_lbl_headline.setText(QCoreApplication.translate("MainWindow", u"\u09b6\u09bf\u0995\u09cd\u09b7\u09be\u09b0\u09cd\u09a5\u09c0\u09b0 \u09a4\u09a5\u09cd\u09af\u09b8\u09ae\u09c2\u09b9 ", None))
        ___qtablewidgetitem = self.std_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u09b6\u09bf\u0995\u09cd\u09b7\u09be\u09b0\u09cd\u09a5\u09c0\u09b0 \u0986\u0987\u09a1\u09bf", None));
        ___qtablewidgetitem1 = self.std_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u09b6\u09bf\u0995\u09cd\u09b7\u09be\u09b0\u09cd\u09a5\u09c0\u09b0 \u09a8\u09be\u09ae", None));
        ___qtablewidgetitem2 = self.std_tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u09b6\u09bf\u0995\u09cd\u09b7\u09be\u09b0\u09cd\u09a5\u09c0\u09b0 \u09ac\u09df\u09b8 ", None));
        ___qtablewidgetitem3 = self.std_tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u09a0\u09bf\u0995\u09be\u09a8\u09be", None));
        ___qtablewidgetitem4 = self.std_tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u0985\u09ad\u09bf\u09ad\u09be\u09ac\u0995\u09c7\u09b0 \u09a8\u09be\u09ae", None));
        ___qtablewidgetitem5 = self.std_tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u0985\u09ad\u09bf\u09ad\u09be\u09ac\u0995\u09c7\u09b0 \u09ae\u09cb\u09ac\u09be\u0987\u09b2 \u09a8\u09ae\u09cd\u09ac\u09b0", None));
        self.std_btn_add_student.setText(QCoreApplication.translate("MainWindow", u"\u09a8\u09a4\u09c1\u09a8 \u09b6\u09bf\u0995\u09cd\u09b7\u09be\u09b0\u09cd\u09a5\u09c0 \u09af\u09c1\u0995\u09cd\u09a4 \u0995\u09b0\u09c1\u09a8", None))
        self.std_btn_update_info.setText(QCoreApplication.translate("MainWindow", u"\u09b6\u09bf\u0995\u09cd\u09b7\u09be\u09b0\u09cd\u09a5\u09c0\u09b0 \u09a4\u09a5\u09cd\u09af \u0986\u09aa\u09a1\u09c7\u099f \u0995\u09b0\u09c1\u09a8", None))
        self.std_btn_remove_student.setText(QCoreApplication.translate("MainWindow", u"\u09b6\u09bf\u0995\u09cd\u09b7\u09be\u09b0\u09cd\u09a5\u09c0 \u098f\u09a8\u09cd\u099f\u09cd\u09b0\u09bf \u09ac\u09be\u09a4\u09bf\u09b2 \u0995\u09b0\u09c1\u09a8", None))
        self.lsn_lbl_category.setText(QCoreApplication.translate("MainWindow", u"\u0995\u09cd\u09af\u09be\u099f\u09be\u0997\u09b0\u09bf", None))
        self.lsn_cmb_category.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0995\u09cd\u09af\u09be\u099f\u09be\u0997\u09b0\u09bf \u09a8\u09bf\u09b0\u09cd\u09ac\u09be\u099a\u09a8 \u0995\u09b0\u09c1\u09a8", None))
        self.lsn_cmb_category.setItemText(1, QCoreApplication.translate("MainWindow", u"\u09a8\u09be\u09ae \u09b6\u09bf\u0996\u09a8 (Noun)", None))
        self.lsn_cmb_category.setItemText(2, QCoreApplication.translate("MainWindow", u"\u0995\u09cd\u09b0\u09bf\u09df\u09be \u09b6\u09bf\u0996\u09a8 (Verb)", None))
        self.lsn_cmb_category.setItemText(3, QCoreApplication.translate("MainWindow", u"\u09b8\u09ae\u09cd\u09aa\u09b0\u09cd\u0995 \u09b6\u09bf\u0996\u09a8 (Association)", None))
        self.lsn_cmb_category.setItemText(4, QCoreApplication.translate("MainWindow", u"\u0995\u09b0\u09cd\u09ae\u09a7\u09be\u09b0\u09be \u09b6\u09bf\u0996\u09a8 (Activity)", None))

        self.lsn_cmb_category.setCurrentText(QCoreApplication.translate("MainWindow", u"\u0995\u09cd\u09af\u09be\u099f\u09be\u0997\u09b0\u09bf \u09a8\u09bf\u09b0\u09cd\u09ac\u09be\u099a\u09a8 \u0995\u09b0\u09c1\u09a8", None))
        self.lsn_lbl_lessons.setText(QCoreApplication.translate("MainWindow", u"\u09aa\u09be\u09a0\u09b8\u09ae\u09c2\u09b9", None))
        self.lsn_cmb_lessons.setItemText(0, QCoreApplication.translate("MainWindow", u"\u09aa\u09be\u09a0 \u0995\u09cd\u09b0\u09ae \u09a8\u09bf\u09b0\u09cd\u09ac\u09be\u099a\u09a8 \u0995\u09b0\u09c1\u09a8", None))

        self.lsn_lbl_lesson_image.setText(QCoreApplication.translate("MainWindow", u"\u099b\u09ac\u09bf", None))
        self.lsn_lbl_lesson_topic.setText(QCoreApplication.translate("MainWindow", u"\u09aa\u09b0\u09bf\u099a\u09df", None))
        self.lsn_btn_add_lessons.setText(QCoreApplication.translate("MainWindow", u"\u09a8\u09a4\u09c1\u09a8 \u09ae\u09a1\u09bf\u0989\u09b2 \u09af\u09c1\u0995\u09cd\u09a4 \u0995\u09b0\u09c1\u09a8", None))
        self.lsn_btn_make_lesson.setText(QCoreApplication.translate("MainWindow", u"\u09aa\u09be\u09a0 \u09a4\u09c8\u09b0\u09bf \u0995\u09b0\u09c1\u09a8", None))
        self.lsn_btn_reload_window.setText("")
        self.lsn_btn_back_to_home.setText("")
        self.lsn_lbl_headline.setText(QCoreApplication.translate("MainWindow", u"\u09aa\u09be\u09a0\u09b8\u09c2\u099a\u09bf", None))
        self.task_btn_back_to_home.setText("")
        self.lsn_lbl_headline_2.setText(QCoreApplication.translate("MainWindow", u"\u09aa\u09be\u09a0 \u09ae\u09c2\u09b2\u09cd\u09af\u09be\u09df\u09a8", None))
        self.task_btn_mcq.setText(QCoreApplication.translate("MainWindow", u"\u09ac\u09b9\u09c1\u09a8\u09bf\u09b0\u09cd\u09ac\u099a\u09a8\u09c0", None))
        self.task_btn_matching.setText(QCoreApplication.translate("MainWindow", u"\u09b6\u09ac\u09cd\u09a6 \u09ae\u09bf\u09b2\u09be\u0987", None))
        self.task_btn_sequence.setText(QCoreApplication.translate("MainWindow", u"\u0995\u09cd\u09b0\u09ae\u09a7\u09be\u09b0\u09be", None))
        self.task_btn_puzzle.setText(QCoreApplication.translate("MainWindow", u"\u09a7\u09be\u0981\u09a7\u09be", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u09a7\u09be\u0981\u09a7\u09be", None))
        self.task_puzzle_q_set_lbl.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u09b8\u09c7\u099f \u09a8\u09ae\u09cd\u09ac\u09b0 \u09a6\u09bf\u09a8 (\u09af\u09c7\u09ae\u09a8 set1)", None))
        self.task_puzzle_save_set_btn.setText(QCoreApplication.translate("MainWindow", u"\u09b8\u0982\u09b0\u0995\u09cd\u09b7\u09a8 \u0995\u09b0\u09c1\u09a8", None))
        self.task_puzzle_image_lbl.setText(QCoreApplication.translate("MainWindow", u"\u09a7\u09be\u0981\u09a7\u09be\u09b0 \u099c\u09a8\u09cd\u09af \u09af\u09c7\u0995\u09cb\u09a8 \u098f\u0995\u099f\u09bf \u099b\u09ac\u09bf \u09a8\u09bf\u09b0\u09cd\u09ac\u09be\u099a\u09a8 \u0995\u09b0\u09c1\u09a8", None))
        self.task_puzzle_select_img_btn.setText(QCoreApplication.translate("MainWindow", u"\u099b\u09ac\u09bf \u09a8\u09bf\u09b0\u09cd\u09ac\u09be\u099a\u09a8 \u0995\u09b0\u09c1\u09a8", None))
        self.task_puzzle_show_set_btn.setText(QCoreApplication.translate("MainWindow", u"\u09a4\u09c8\u09b0\u09bf\u0995\u09c3\u09a4 \u09a7\u09be\u0981\u09a7\u09be\u09b0 \u09b8\u09c7\u099f\u0997\u09c1\u09b2\u09cb \u09a6\u09c7\u0996\u09c1\u09a8", None))
        self.task_seq_img_seq_edit.setText("")
        self.task_seq_img_seq_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0995\u09cd\u09b0\u09ae\u09bf\u0995 \u09a8\u09ae\u09cd\u09ac\u09b0 (\u09af\u09c7\u09ae\u09a8\u0983 1/2)", None))
        self.task_seq_img_desc_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u099b\u09ac\u09bf\u09b0 \u09b8\u0982\u0995\u09cd\u09b7\u09bf\u09aa\u09cd\u09a4 \u09ac\u09bf\u09ac\u09b0\u09a3 (\u09e9-\u09eb \u09b6\u09ac\u09cd\u09a6\u09c7)", None))
        self.task_seq_img_view_lbl.setText("")
        self.task_seq_img_save_btn.setText(QCoreApplication.translate("MainWindow", u"\u09b8\u0982\u09b0\u0995\u09cd\u09b7\u09a8 \u0995\u09b0\u09c1\u09a8", None))
#if QT_CONFIG(shortcut)
        self.task_seq_img_save_btn.setShortcut(QCoreApplication.translate("MainWindow", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.task_seq_instruction_lbl.setText(QCoreApplication.translate("MainWindow", u"\u09aa\u09cd\u09b0\u09a4\u09bf \u09b8\u09c7\u099f\u09c7\u09b0 \u099c\u09a8\u09cd\u09af \u0986\u09ae\u09b0\u09be \u09b8\u09b0\u09cd\u09ac\u09cb\u099a\u09cd\u099a \u09ea\u099f\u09bf \u099b\u09ac\u09bf \u09a8\u09bf\u09b0\u09cd\u09ac\u09be\u099a\u09a8 \u0995\u09b0\u09ac\u0964 \u099b\u09ac\u09bf\u09b0 \u09a8\u09bf\u099a\u09c7 \u09b8\u0982\u0995\u09cd\u09b7\u09bf\u09aa\u09cd\u09a4 \u09ac\u09bf\u09ac\u09b0\u09a3 \u098f\u09ac\u09a8 \u0995\u09cd\u09b0\u09ae\u09bf\u0995 \u09a8\u0982 \u0989\u09b2\u09cd\u09b2\u09c7\u0996 \u0995\u09b0\u09ac", None))
        self.task_seq_set_lbl.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u09a7\u09be\u09b0\u09be\u09b0 \u09ac\u09bf\u09b7\u09df\u09ac\u09b8\u09cd\u09a4\u09c1 \u09b2\u09bf\u0996\u09c1\u09a8 (\u09af\u09c7\u09ae\u09a8\u0983 \u09ab\u09c1\u09b2 \u0997\u09be\u099b\u09c7 \u09aa\u09be\u09a8\u09bf \u09a6\u09c7\u09df\u09be)", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u0995\u09cd\u09b0\u09ae\u09a7\u09be\u09b0\u09be ", None))
        self.task_matching_img_desc_edit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u099b\u09ac\u09bf\u09b0 \u09b8\u0982\u0995\u09cd\u09b7\u09bf\u09aa\u09cd\u09a4 \u09ac\u09bf\u09ac\u09b0\u09a3 (\u09e9-\u09eb \u09b6\u09ac\u09cd\u09a6\u09c7)", None))
        self.task_matching_img_add_btn_2.setText("")
        self.task_matching_img_view_lbl_2.setText("")
        self.task_matching_img_desc_edit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u099b\u09ac\u09bf\u09b0 \u09b8\u0982\u0995\u09cd\u09b7\u09bf\u09aa\u09cd\u09a4 \u09ac\u09bf\u09ac\u09b0\u09a3 (\u09e9-\u09eb \u09b6\u09ac\u09cd\u09a6\u09c7)", None))
        self.task_matching_img_add_btn_3.setText("")
        self.task_matching_img_view_lbl_3.setText("")
        self.task_matching_img_desc_edit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u099b\u09ac\u09bf\u09b0 \u09b8\u0982\u0995\u09cd\u09b7\u09bf\u09aa\u09cd\u09a4 \u09ac\u09bf\u09ac\u09b0\u09a3 (\u09e9-\u09eb \u09b6\u09ac\u09cd\u09a6\u09c7)", None))
        self.task_matching_img_add_btn_4.setText("")
        self.task_matching_img_view_lbl_4.setText("")
        self.task_matching_img_add_btn_1.setText("")
        self.task_matching_img_desc_edit_1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u099b\u09ac\u09bf\u09b0 \u09b8\u0982\u0995\u09cd\u09b7\u09bf\u09aa\u09cd\u09a4 \u09ac\u09bf\u09ac\u09b0\u09a3 (\u09e9-\u09eb \u09b6\u09ac\u09cd\u09a6\u09c7)", None))
        self.task_matching_img_view_lbl_1.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u09b6\u09ac\u09cd\u09a6 \u09ae\u09bf\u09b2\u09be\u0987", None))
        self.task_matching_set_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u09b8\u09c7\u099f \u09a8\u09ae\u09cd\u09ac\u09b0 \u09a6\u09bf\u09a8 (\u09af\u09c7\u09ae\u09a8 set1)", None))
        self.task_matching_save_set_btn.setText(QCoreApplication.translate("MainWindow", u"\u09b8\u0982\u09b0\u0995\u09cd\u09b7\u09a8 \u0995\u09b0\u09c1\u09a8", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u09aa\u09cd\u09b0\u09b6\u09cd\u09a8", None))
        self.task_mcq_new_set_btn.setText(QCoreApplication.translate("MainWindow", u"\u09a8\u09a4\u09c1\u09a8 \u09aa\u09cd\u09b0\u09b6\u09cd\u09a8 \u09b8\u09c7\u099f", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u09ac\u09b9\u09c1\u09a8\u09bf\u09b0\u09cd\u09ac\u099a\u09a8\u09c0", None))
        self.task_mcq_question_edit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p></body></html>", None))
        self.task_mcq_next_ques_btn.setText(QCoreApplication.translate("MainWindow", u"\u09aa\u09b0\u09ac\u09b0\u09cd\u09a4\u09c0 \u09aa\u09cd\u09b0\u09b6\u09cd\u09a8 ", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"\u09b8\u09c7\u099f \u09a8\u09ae\u09cd\u09ac\u09b0", None))
        self.task_mcq_set_no_edit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:15pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p></body></html>", None))
        self.task_mcq_option_4_edit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:15pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p></body></html>", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"\u0998", None))
        self.task_mcq_option_1_edit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:15pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p></body></html>", None))
        self.task_mcq_option_3_edit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:15pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p></body></html>", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u0995", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u0996", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"\u09b8\u09a0\u09bf\u0995 \u0989\u09a4\u09cd\u09a4\u09b0", None))
        self.task_mcq_correct_option_edit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:15pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p></body></html>", None))
        self.task_mcq_option_2_edit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:15pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p></body></html>", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"\u0997", None))
        self.task_mcq_finish_set_btn.setText(QCoreApplication.translate("MainWindow", u"\u09b8\u09c7\u099f \u09b6\u09c7\u09b7 \u0995\u09b0\u09c1\u09a8", None))
        self.task_mcq_upload_img_btn.setText(QCoreApplication.translate("MainWindow", u"\u099b\u09ac\u09bf \u09a8\u09bf\u09b0\u09cd\u09ac\u09be\u099a\u09a8 \u0995\u09b0\u09c1\u09a8", None))
        self.task_mcq_img_lbl.setText("")
        self.lsn_btn_back_to_home_3.setText("")
        self.lsn_lbl_headline_4.setText(QCoreApplication.translate("MainWindow", u"\u09aa\u09be\u09a0\u09b8\u09c2\u099a\u09bf", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u09b8\u0995\u09b2 \u09aa\u09be\u09a0\u09b8\u09ae\u09c2\u09b9 \u09a6\u09c7\u0996\u09be\u09b0 \u099c\u09a8\u09cd\u09af \u09a8\u09bf\u099a\u09c7\u09b0 \u0986\u0987\u0995\u09a8\u09c7 \u0995\u09cd\u09b2\u09bf\u0995 \u0995\u09b0\u09c1\u09a8", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u09ae\u09a1\u09bf\u0989\u09b2 \u09af\u09c1\u0995\u09cd\u09a4 \u0995\u09b0\u09be \u09b6\u09c7\u09b7 \u09b9\u09b2\u09c7 \"\u09aa\u09be\u09a0 \u09a4\u09c8\u09b0\u09bf \u09b8\u09ae\u09cd\u09aa\u09a8\u09cd\u09a8 \u0995\u09b0\u09c1\u09a8\" \u09ac\u09be\u099f\u09a8\u09c7 \u09aa\u09cd\u09b0\u09c7\u09b8 \u0995\u09b0\u09c1\u09a8", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u09b8\u09bf\u09b2\u09c7\u0995\u09cd\u099f\u09c7\u09a1 \u0995\u09cb\u09a8 \u09ae\u09a1\u09bf\u0989\u09b2 \u09ac\u09be\u09a4\u09bf\u09b2 \u0995\u09b0\u09be\u09b0 \u0995\u09b0\u09be\u09b0 \u099c\u09a8\u09cd\u09af \u09a8\u09bf\u099a\u09c7\u09b0 \u0990 \u09ae\u09a1\u09bf\u0989\u09b2\u099f\u09bf \u09b8\u09bf\u09b2\u09c7\u0995\u09cd\u099f \u0995\u09b0\u09c7 \"\u09b8\u09bf\u09b2\u09c7\u0995\u09b6\u09a8 \u09ac\u09be\u09a4\u09bf\u09b2 \u0995\u09b0\u09c1\u09a8\" \u09ac\u09be\u099f\u09a8\u09c7 \u09aa\u09cd\u09b0\u09c7\u09b8 \u0995\u09b0\u09c1\u09a8", None))
        ___qtablewidgetitem6 = self.lsn_module_table_widget.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u09ae\u09a1\u09bf\u0989\u09b2\u09c7\u09b0 \u09a8\u09be\u09ae", None));
        ___qtablewidgetitem7 = self.lsn_module_table_widget.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\u09ae\u09a1\u09bf\u0989\u09b2\u09c7\u09b0 \u09ac\u09bf\u09ac\u09b0\u09a3 ", None));
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u09a8\u09a4\u09c1\u09a8 \u09aa\u09be\u09a0\u09c7 \u09ae\u09a1\u09bf\u0989\u09b2 \u09af\u09c1\u0995\u09cd\u09a4 \u0995\u09b0\u09be\u09b0 \u099c\u09a8\u09cd\u09af \u09b6\u09c1\u09a7\u09c1\u09ae\u09be\u09a4\u09cd\u09b0 \"\u09ae\u09a1\u09bf\u0989\u09b2 \u09a8\u09be\u09ae\" \u098f\u09b0 \u0989\u09aa\u09b0 \u0995\u09cd\u09b2\u09bf\u0995 \u0995\u09b0\u09c7 \"\u09a8\u09a4\u09c1\u09a8 \u09aa\u09be\u09a0\u09c7\u09b0 \u09ae\u09a1\u09bf\u0989\u09b2 \u09b8\u09ae\u09c2\u09b9\"  \u0989\u0987\u09a8\u09cd\u09a1\u09cb\u09a4\u09c7 \u09a1\u09cd\u09b0\u09cd\u09af\u09be\u0997 \u0995\u09b0\u09c1\u09a8", None))
        self.label_7.setText("")
        self.lsn_btn_remove_module.setText(QCoreApplication.translate("MainWindow", u"\u09b8\u09bf\u09b2\u09c7\u0995\u09b6\u09a8 \u09ac\u09be\u09a4\u09bf\u09b2 \u0995\u09b0\u09c1\u09a8", None))
        self.lsn_lbl_lessons_5.setText(QCoreApplication.translate("MainWindow", u"\u09a8\u09a4\u09c1\u09a8 \u09aa\u09be\u09a0\u09c7\u09b0 \u09ae\u09a1\u09bf\u0989\u09b2 \u09b8\u09ae\u09c2\u09b9", None))
        self.label_6.setText("")
        self.lsn_btn_finish_add_module.setText(QCoreApplication.translate("MainWindow", u"\u09aa\u09be\u09a0 \u09a4\u09c8\u09b0\u09bf \u09b8\u09ae\u09cd\u09aa\u09a8\u09cd\u09a8 \u0995\u09b0\u09c1\u09a8", None))
        self.label_5.setText("")
        self.lsn_lbl_lessons_3.setText(QCoreApplication.translate("MainWindow", u"\u09ae\u09a1\u09bf\u0989\u09b2\u09c7\u09b0 \u09a4\u09be\u09b2\u09bf\u0995\u09be\u09b8\u09ae\u09c2\u09b9", None))
        self.lsn_lbl_lessons_4.setText(QCoreApplication.translate("MainWindow", u"\u09a8\u09a4\u09c1\u09a8 \u09aa\u09be\u09a0 \u09a4\u09c8\u09b0\u09bf\u09b0 \u09a8\u09bf\u09df\u09ae", None))
        self.lsn_btn_see_lessons.setText(QCoreApplication.translate("MainWindow", u"\u09aa\u09be\u09a0\u09b8\u09ae\u09c2\u09b9 \u09a6\u09c7\u0996\u09c1\u09a8", None))
        self.lsn_btn_back_to_home_4.setText("")
        self.lsn_lbl_headline_5.setText(QCoreApplication.translate("MainWindow", u"\u09aa\u09be\u09a0 \u09aa\u09cd\u09b0\u09a6\u09be\u09a8\u09c7\u09b0 \u09b0\u09c7\u0995\u09b0\u09cd\u09a1", None))
        self.lsn_lbl_lessons_6.setText(QCoreApplication.translate("MainWindow", u"\u09aa\u09be\u09a0 \u09aa\u09cd\u09b0\u09a6\u09be\u09a8\u09c7\u09b0 \u09ac\u09bf\u09b8\u09cd\u09a4\u09be\u09b0\u09bf\u09a4 \u09a4\u09be\u09b2\u09bf\u0995\u09be", None))
        ___qtablewidgetitem8 = self.lsn_table_assigning_lessons.horizontalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"\u09b6\u09bf\u0995\u09cd\u09b7\u09be\u09b0\u09cd\u09a5\u09c0\u09b0 \u0986\u0987\u09a1\u09bf ", None));
        ___qtablewidgetitem9 = self.lsn_table_assigning_lessons.horizontalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"\u09b6\u09bf\u0995\u09cd\u09b7\u09be\u09b0\u09cd\u09a5\u09c0\u09b0 \u09a8\u09be\u09ae", None));
        ___qtablewidgetitem10 = self.lsn_table_assigning_lessons.horizontalHeaderItem(2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"\u09aa\u09be\u09a0 \u09a8\u0982  ", None));
        ___qtablewidgetitem11 = self.lsn_table_assigning_lessons.horizontalHeaderItem(3)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"\u09ac\u09b9\u09c1\u09a8\u09bf\u09b0\u09cd\u09ac\u099a\u09a8\u09bf \u09b8\u09c7\u099f", None));
        ___qtablewidgetitem12 = self.lsn_table_assigning_lessons.horizontalHeaderItem(4)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"\u09a7\u09be\u09a7\u09be\u09b0 \u09b8\u09c7\u099f", None));
        ___qtablewidgetitem13 = self.lsn_table_assigning_lessons.horizontalHeaderItem(5)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"\u09a7\u09be\u09b0\u09be\u09b0 \u09b8\u09c7\u099f ", None));
        ___qtablewidgetitem14 = self.lsn_table_assigning_lessons.horizontalHeaderItem(6)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"\u09b6\u09ac\u09cd\u09a6 \u09ae\u09bf\u09b2\u09be\u09a8\u09cb'\u09b0 \u09b8\u09c7\u099f", None));
        ___qtablewidgetitem15 = self.lsn_table_assigning_lessons.horizontalHeaderItem(7)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"\u09aa\u09be\u09a0 \u09aa\u09cd\u09b0\u09a6\u09be\u09a8\u09c7\u09b0 \u09b8\u09ae\u09df\u0995\u09be\u09b2", None));
        self.lsn_lbl_lessons_8.setText(QCoreApplication.translate("MainWindow", u"\u09b6\u09bf\u0995\u09cd\u09b7\u09be\u09b0\u09cd\u09a5\u09c0\u09a6\u09c7\u09b0 \u09a4\u09be\u09b2\u09bf\u0995\u09be", None))
        self.lsn_btn_assign_lesson.setText(QCoreApplication.translate("MainWindow", u"\u09aa\u09be\u09a0 \u09aa\u09cd\u09b0\u09a6\u09be\u09a8 \u0995\u09b0\u09c1\u09a8", None))
        self.lsn_btn_back_to_home_5.setText("")
        self.lsn_lbl_headline_6.setText(QCoreApplication.translate("MainWindow", u"\u09b6\u09bf\u0995\u09cd\u09b7\u09be\u09b0\u09cd\u09a5\u09c0\u09b0 \u09aa\u09be\u09b0\u09ab\u09b0\u09ae\u09cd\u09af\u09be\u09a8\u09cd\u09b8", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u09b6\u09bf\u0995\u09cd\u09b7\u09be\u09b0\u09cd\u09a5\u09c0 \u09a8\u09bf\u09b0\u09cd\u09ac\u09be\u099a\u09a8 \u0995\u09b0\u09c1\u09a8", None))
        self.performance_std_id_cmb.setItemText(0, QCoreApplication.translate("MainWindow", u"\u09b8\u09bf\u09b2\u09c7\u0995\u09cd\u099f \u0995\u09b0\u09c1\u09a8", None))

        self.performance_lesson_btn.setText(QCoreApplication.translate("MainWindow", u"\u09aa\u09be\u09a0 \u09b8\u0982\u0995\u09cd\u09b0\u09be\u09a8\u09cd\u09a4 \u09a1\u09c7\u099f\u09be", None))
        self.performance_module_btn.setText(QCoreApplication.translate("MainWindow", u"\u09ae\u09a1\u09bf\u0989\u09b2 \u09b8\u0982\u0995\u09cd\u09b0\u09be\u09a8\u09cd\u09a4 \u09a1\u09c7\u099f\u09be", None))
        self.performance_eval_btn.setText(QCoreApplication.translate("MainWindow", u"\u09ae\u09c2\u09b2\u09cd\u09af\u09be\u09df\u09a8 \u09b8\u0982\u0995\u09cd\u09b0\u09be\u09a8\u09cd\u09a4 \u09a1\u09c7\u099f\u09be", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u09a8\u09bf\u09b0\u09cd\u09a6\u09c7\u09b6\u09a8\u09be\u0983 \n"
"\u09e7\u0964 \u09aa\u09cd\u09b0\u09a5\u09ae\u09c7 \u09b6\u09bf\u0995\u09cd\u09b7\u09be\u09b0\u09cd\u09a5\u09c0 \u09a8\u09bf\u09b0\u09cd\u09ac\u09be\u099a\u09a8 \u0995\u09b0\u09c1\u09a8\n"
"\u09e8\u0964 \u098f\u09b0\u09aa\u09b0 \u09aa\u09be\u09a0 \u0985\u09a5\u09ac\u09be \u09ae\u09c2\u09b2\u09cd\u09af\u09be\u09df\u09a8 \u09af\u09c7\u0995\u09cb\u09a8 \u098f\u0995\u099f\u09bf \u0985\u09aa\u09b6\u09a8 \u09a8\u09bf\u09b0\u09cd\u09ac\u09be\u099a\u09a8 \u0995\u09b0\u09c1\u09a8 \n"
"\u09e9\u0964 \u098f\u09b0\u09aa\u09b0 \u09aa\u09be\u09b6\u09c7\u09b0 \u09ac\u0995\u09cd\u09b8\u09c7 \u09a5\u09be\u0995\u09be \u09ac\u09be\u099f\u09a8 \u0997\u09c1\u09b2\u09cb\u09a4\u09c7 \u0995\u09cd\u09b2\u09bf\u0995 \u0995\u09b0\u09c7 \u09a8\u09bf\u09b0\u09cd\u09a7\u09be\u09b0\u09bf\u09a4 \u0997\u09cd\u09b0\u09be\u09ab \u09a6\u09c7\u0996\u09c1\u09a8\n"
"\u09ea\u0964 \u09b8\u09ae\u09cd\u09aa\u09c2\u09b0\u09cd\u09a3 \u09b0\u09bf\u09aa\u09cb\u09b0\u09cd\u099f \u09a6\u09c7\u0996"
                        "\u09a4\u09c7 \u099a\u09be\u0987\u09b2\u09c7 \u09a8\u09bf\u099a\u09c7\u09b0 \u09ac\u09be\u099f\u09a8\u09c7 \u0995\u09cd\u09b2\u09bf\u0995 \u0995\u09b0\u09c1\u09a8", None))
        self.performance_report_btn.setText(QCoreApplication.translate("MainWindow", u"\u09b0\u09bf\u09aa\u09cb\u09b0\u09cd\u099f \u09a4\u09c8\u09b0\u09bf \u0995\u09b0\u09c1\u09a8", None))
        self.p_lesson_left_graph_lbl.setText("")
        self.p_lesson_right_graph_lbl.setText("")
        self.p_lesson_id_cmb.setItemText(0, QCoreApplication.translate("MainWindow", u"\u09aa\u09be\u09a0 \u09a8\u09bf\u09b0\u09cd\u09ac\u09be\u099a\u09a8 \u0995\u09b0\u09c1\u09a8", None))

        self.p_module_graph_lbl.setText("")
        self.p_eval_puzzle_btn.setText(QCoreApplication.translate("MainWindow", u"\u09a7\u09be\u0981\u09a7\u09be \u09b8\u0982\u0995\u09cd\u09b0\u09be\u09a8\u09cd\u09a4", None))
        self.p_eval_seq_btn.setText(QCoreApplication.translate("MainWindow", u"\u0995\u09cd\u09b0\u09ae\u09a7\u09be\u09b0\u09be \u09b8\u0982\u0995\u09cd\u09b0\u09be\u09a8\u09cd\u09a4", None))
        self.p_eval_matching_btn.setText(QCoreApplication.translate("MainWindow", u"\u09b6\u09ac\u09cd\u09a6 \u09ae\u09bf\u09b2\u09be\u09a8\u09cb \u09b8\u0982\u0995\u09cd\u09b0\u09be\u09a8\u09cd\u09a4", None))
        self.p_eval_mcq_btn.setText(QCoreApplication.translate("MainWindow", u"\u09ac\u09b9\u09c1\u09a8\u09bf\u09b0\u09cd\u09ac\u099a\u09a8\u09c0 \u09b8\u0982\u0995\u09cd\u09b0\u09be\u09a8\u09cd\u09a4", None))
        self.p_eval_left_graph_lbl.setText("")
        self.p_eval_right_graph_lbl.setText("")
    # retranslateUi

