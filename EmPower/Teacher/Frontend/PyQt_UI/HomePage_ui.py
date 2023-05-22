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
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setMinimumSize(QSize(1280, 720))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(1280, 720))
        self.gridLayout_15 = QGridLayout(self.centralwidget)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setContentsMargins(0, 0, 0, 0)
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
        self.eval_left_frame.setMinimumSize(QSize(385, 636))
        self.eval_left_frame.setMaximumSize(QSize(385, 636))
        self.eval_left_frame.setStyleSheet(u"")
        self.eval_left_frame.setFrameShape(QFrame.StyledPanel)
        self.eval_left_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.eval_left_frame)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.verticalSpacer_3 = QSpacerItem(20, 164, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_3, 0, 1, 1, 1)

        self.task_btn_matching = QPushButton(self.eval_left_frame)
        self.task_btn_matching.setObjectName(u"task_btn_matching")
        self.task_btn_matching.setMinimumSize(QSize(261, 61))
        font14 = QFont()
        font14.setFamilies([u"Hind Siliguri Medium"])
        font14.setPointSize(12)
        font14.setBold(True)
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
        icon12 = QIcon()
        icon12.addFile(u"../Images/connect_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.task_btn_matching.setIcon(icon12)
        self.task_btn_matching.setIconSize(QSize(28, 50))

        self.gridLayout_5.addWidget(self.task_btn_matching, 1, 1, 1, 1)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_13, 1, 2, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_10, 1, 0, 1, 1)

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
        icon13 = QIcon()
        icon13.addFile(u"../Images/sequence_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.task_btn_sequence.setIcon(icon13)
        self.task_btn_sequence.setIconSize(QSize(26, 50))

        self.gridLayout_5.addWidget(self.task_btn_sequence, 2, 1, 1, 1)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_14, 2, 2, 1, 1)

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
        icon14 = QIcon()
        icon14.addFile(u"../Images/puzzle_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.task_btn_puzzle.setIcon(icon14)
        self.task_btn_puzzle.setIconSize(QSize(20, 30))

        self.gridLayout_5.addWidget(self.task_btn_puzzle, 3, 1, 1, 1)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_15, 3, 2, 1, 1)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_11, 2, 0, 1, 1)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_12, 3, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 163, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_4, 4, 1, 1, 1)


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
        self.puzzle_page = QWidget()
        self.puzzle_page.setObjectName(u"puzzle_page")
        self.gridLayout_7 = QGridLayout(self.puzzle_page)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.frame_3 = QFrame(self.puzzle_page)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"border: 2px solid rgb(160, 253, 230);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_16 = QGridLayout(self.frame_3)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.task_puzzle_image_lbl = QLabel(self.frame_3)
        self.task_puzzle_image_lbl.setObjectName(u"task_puzzle_image_lbl")
        self.task_puzzle_image_lbl.setMinimumSize(QSize(481, 384))
        font15 = QFont()
        font15.setPointSize(15)
        self.task_puzzle_image_lbl.setFont(font15)
        self.task_puzzle_image_lbl.setStyleSheet(u"color: rgb(0, 43, 91);")
        self.task_puzzle_image_lbl.setAlignment(Qt.AlignCenter)
        self.task_puzzle_image_lbl.setWordWrap(True)

        self.gridLayout_16.addWidget(self.task_puzzle_image_lbl, 0, 0, 1, 5)

        self.horizontalSpacer_22 = QSpacerItem(108, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_16.addItem(self.horizontalSpacer_22, 1, 0, 1, 1)

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

        self.gridLayout_16.addWidget(self.task_puzzle_q_set_lbl, 2, 0, 1, 3)

        self.horizontalSpacer_23 = QSpacerItem(128, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_16.addItem(self.horizontalSpacer_23, 1, 4, 1, 1)

        self.task_puzzle_show_set_btn = QPushButton(self.frame_3)
        self.task_puzzle_show_set_btn.setObjectName(u"task_puzzle_show_set_btn")
        self.task_puzzle_show_set_btn.setMinimumSize(QSize(211, 61))
        font17 = QFont()
        font17.setFamilies([u"Hind Siliguri Medium"])
        font17.setPointSize(10)
        self.task_puzzle_show_set_btn.setFont(font17)
        self.task_puzzle_show_set_btn.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout_16.addWidget(self.task_puzzle_show_set_btn, 1, 3, 1, 1)

        self.task_puzzle_save_set_btn = QPushButton(self.frame_3)
        self.task_puzzle_save_set_btn.setObjectName(u"task_puzzle_save_set_btn")
        self.task_puzzle_save_set_btn.setMinimumSize(QSize(100, 51))
        font18 = QFont()
        font18.setFamilies([u"Hind Siliguri Medium"])
        font18.setPointSize(10)
        font18.setBold(False)
        self.task_puzzle_save_set_btn.setFont(font18)
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

        self.gridLayout_16.addWidget(self.task_puzzle_save_set_btn, 2, 3, 1, 2)

        self.task_puzzle_select_img_btn = QPushButton(self.frame_3)
        self.task_puzzle_select_img_btn.setObjectName(u"task_puzzle_select_img_btn")
        self.task_puzzle_select_img_btn.setMinimumSize(QSize(211, 61))
        self.task_puzzle_select_img_btn.setFont(font12)
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

        self.gridLayout_16.addWidget(self.task_puzzle_select_img_btn, 1, 1, 1, 1)


        self.gridLayout_7.addWidget(self.frame_3, 0, 0, 1, 1)

        self.evalstackwidget.addWidget(self.puzzle_page)
        self.sequence_page = QWidget()
        self.sequence_page.setObjectName(u"sequence_page")
        self.gridLayout_12 = QGridLayout(self.sequence_page)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(11, 11, 11, 11)
        self.task_seq_video_frame_widget = QHBoxLayout()
        self.task_seq_video_frame_widget.setObjectName(u"task_seq_video_frame_widget")

        self.gridLayout_12.addLayout(self.task_seq_video_frame_widget, 0, 0, 1, 1)

        self.evalstackwidget.addWidget(self.sequence_page)
        self.matching_page = QWidget()
        self.matching_page.setObjectName(u"matching_page")
        self.gridLayout_14 = QGridLayout(self.matching_page)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.puzzle_pic_frame = QFrame(self.matching_page)
        self.puzzle_pic_frame.setObjectName(u"puzzle_pic_frame")
        self.puzzle_pic_frame.setStyleSheet(u"border: 2px solid rgb(160, 253, 230);")
        self.puzzle_pic_frame.setFrameShape(QFrame.StyledPanel)
        self.puzzle_pic_frame.setFrameShadow(QFrame.Raised)

        self.gridLayout_14.addWidget(self.puzzle_pic_frame, 0, 0, 1, 1)

        self.evalstackwidget.addWidget(self.matching_page)

        self.gridLayout_6.addWidget(self.evalstackwidget, 0, 0, 1, 1)


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
        font19 = QFont()
        font19.setFamilies([u"Hind Siliguri Medium"])
        font19.setPointSize(11)
        font19.setBold(False)
        self.label_4.setFont(font19)
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
        self.label_3.setFont(font19)
        self.label_3.setStyleSheet(u"color: rgb(132, 211, 184);\n"
"background-color: rgb(0, 43, 91);\n"
"padding: 5px;")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_3.setWordWrap(True)

        self.gridLayout_4.addWidget(self.label_3, 5, 1, 1, 3)

        self.label_2 = QLabel(self.mid_frame_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font19)
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
        __qtablewidgetitem6.setFont(font18);
        self.lsn_module_table_widget.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem7.setFont(font18);
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
        self.label.setFont(font19)
        self.label.setStyleSheet(u"color: rgb(132, 211, 184);\n"
"background-color: rgb(0, 43, 91);\n"
"padding: 5px;")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(True)

        self.gridLayout_4.addWidget(self.label, 1, 1, 1, 3)

        self.label_7 = QLabel(self.mid_frame_4)
        self.label_7.setObjectName(u"label_7")
        font20 = QFont()
        font20.setPointSize(7)
        self.label_7.setFont(font20)
        self.label_7.setPixmap(QPixmap(u"../Images/downward_icon.png"))

        self.gridLayout_4.addWidget(self.label_7, 6, 2, 1, 1)

        self.lsn_btn_remove_module = QPushButton(self.mid_frame_4)
        self.lsn_btn_remove_module.setObjectName(u"lsn_btn_remove_module")
        sizePolicy1.setHeightForWidth(self.lsn_btn_remove_module.sizePolicy().hasHeightForWidth())
        self.lsn_btn_remove_module.setSizePolicy(sizePolicy1)
        self.lsn_btn_remove_module.setMinimumSize(QSize(200, 58))
        self.lsn_btn_remove_module.setMaximumSize(QSize(200, 58))
        self.lsn_btn_remove_module.setFont(font18)
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
        icon15 = QIcon()
        icon15.addFile(u"../Images/remove_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.lsn_btn_remove_module.setIcon(icon15)
        self.lsn_btn_remove_module.setIconSize(QSize(20, 25))

        self.gridLayout_4.addWidget(self.lsn_btn_remove_module, 10, 4, 1, 1)

        self.lsn_lbl_lessons_5 = QLabel(self.mid_frame_4)
        self.lsn_lbl_lessons_5.setObjectName(u"lsn_lbl_lessons_5")
        self.lsn_lbl_lessons_5.setMinimumSize(QSize(371, 36))
        font21 = QFont()
        font21.setFamilies([u"Hind Siliguri Medium"])
        font21.setPointSize(16)
        font21.setBold(False)
        self.lsn_lbl_lessons_5.setFont(font21)
        self.lsn_lbl_lessons_5.setStyleSheet(u"color: rgb(149, 236, 215);")
        self.lsn_lbl_lessons_5.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.lsn_lbl_lessons_5, 0, 4, 1, 2)

        self.label_6 = QLabel(self.mid_frame_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font20)
        self.label_6.setPixmap(QPixmap(u"../Images/downward_icon.png"))

        self.gridLayout_4.addWidget(self.label_6, 4, 2, 1, 1)

        self.lsn_btn_finish_add_module = QPushButton(self.mid_frame_4)
        self.lsn_btn_finish_add_module.setObjectName(u"lsn_btn_finish_add_module")
        self.lsn_btn_finish_add_module.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.lsn_btn_finish_add_module.sizePolicy().hasHeightForWidth())
        self.lsn_btn_finish_add_module.setSizePolicy(sizePolicy1)
        self.lsn_btn_finish_add_module.setMinimumSize(QSize(200, 58))
        self.lsn_btn_finish_add_module.setMaximumSize(QSize(200, 58))
        self.lsn_btn_finish_add_module.setFont(font18)
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
        icon16 = QIcon()
        icon16.addFile(u"../Images/done.png", QSize(), QIcon.Normal, QIcon.Off)
        self.lsn_btn_finish_add_module.setIcon(icon16)
        self.lsn_btn_finish_add_module.setIconSize(QSize(20, 25))

        self.gridLayout_4.addWidget(self.lsn_btn_finish_add_module, 10, 5, 1, 1)

        self.horizontalSpacer_17 = QSpacerItem(160, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_17, 2, 1, 1, 1)

        self.label_5 = QLabel(self.mid_frame_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font20)
        self.label_5.setPixmap(QPixmap(u"../Images/downward_icon.png"))

        self.gridLayout_4.addWidget(self.label_5, 2, 2, 1, 1)

        self.horizontalSpacer_18 = QSpacerItem(160, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_18, 4, 1, 1, 1)

        self.horizontalSpacer_16 = QSpacerItem(159, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_16, 2, 3, 1, 1)

        self.lsn_lbl_lessons_3 = QLabel(self.mid_frame_4)
        self.lsn_lbl_lessons_3.setObjectName(u"lsn_lbl_lessons_3")
        self.lsn_lbl_lessons_3.setMinimumSize(QSize(451, 36))
        self.lsn_lbl_lessons_3.setFont(font21)
        self.lsn_lbl_lessons_3.setStyleSheet(u"color: rgb(149, 236, 215);")
        self.lsn_lbl_lessons_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.lsn_lbl_lessons_3, 0, 0, 1, 1)

        self.lsn_lbl_lessons_4 = QLabel(self.mid_frame_4)
        self.lsn_lbl_lessons_4.setObjectName(u"lsn_lbl_lessons_4")
        self.lsn_lbl_lessons_4.setMinimumSize(QSize(361, 36))
        self.lsn_lbl_lessons_4.setFont(font21)
        self.lsn_lbl_lessons_4.setStyleSheet(u"color: rgb(149, 236, 215);")
        self.lsn_lbl_lessons_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.lsn_lbl_lessons_4, 0, 1, 1, 3)

        self.lsn_new_module_list_view = QListView(self.mid_frame_4)
        self.lsn_new_module_list_view.setObjectName(u"lsn_new_module_list_view")
        self.lsn_new_module_list_view.setMinimumSize(QSize(424, 509))
        font22 = QFont()
        font22.setPointSize(10)
        self.lsn_new_module_list_view.setFont(font22)
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
        icon17 = QIcon()
        icon17.addFile(u"../Images/open_folders_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.lsn_btn_see_lessons.setIcon(icon17)
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
        self.lsn_lbl_lessons_6.setFont(font21)
        self.lsn_lbl_lessons_6.setStyleSheet(u"color: rgb(149, 236, 215);")
        self.lsn_lbl_lessons_6.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.lsn_lbl_lessons_6, 0, 1, 1, 1)

        self.lsn_table_assigning_lessons = QTableWidget(self.mid_frame_5)
        if (self.lsn_table_assigning_lessons.columnCount() < 4):
            self.lsn_table_assigning_lessons.setColumnCount(4)
        font23 = QFont()
        font23.setPointSize(12)
        font23.setBold(False)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem8.setFont(font23);
        self.lsn_table_assigning_lessons.setHorizontalHeaderItem(0, __qtablewidgetitem8)
        font24 = QFont()
        font24.setFamilies([u"Segoe UI"])
        font24.setPointSize(12)
        font24.setBold(False)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem9.setFont(font24);
        self.lsn_table_assigning_lessons.setHorizontalHeaderItem(1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem10.setFont(font24);
        self.lsn_table_assigning_lessons.setHorizontalHeaderItem(2, __qtablewidgetitem10)
        font25 = QFont()
        font25.setPointSize(12)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem11.setFont(font25);
        self.lsn_table_assigning_lessons.setHorizontalHeaderItem(3, __qtablewidgetitem11)
        self.lsn_table_assigning_lessons.setObjectName(u"lsn_table_assigning_lessons")
        self.lsn_table_assigning_lessons.setMinimumSize(QSize(830, 511))
        self.lsn_table_assigning_lessons.setFont(font25)
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
        self.lsn_lbl_lessons_8.setFont(font21)
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
        self.lsn_btn_assign_lesson.setFont(font18)
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
        self.lsn_btn_assign_lesson.setIcon(icon16)
        self.lsn_btn_assign_lesson.setIconSize(QSize(20, 25))

        self.gridLayout_10.addWidget(self.lsn_btn_assign_lesson, 2, 0, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(33, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer_8, 1, 2, 1, 1)

        self.lsn_list_students = QListWidget(self.mid_frame_5)
        self.lsn_list_students.setObjectName(u"lsn_list_students")
        self.lsn_list_students.setMinimumSize(QSize(401, 509))
        self.lsn_list_students.setMaximumSize(QSize(371, 16777215))
        font26 = QFont()
        font26.setPointSize(13)
        self.lsn_list_students.setFont(font26)
        self.lsn_list_students.setStyleSheet(u"color: rgb(143, 227, 190);\n"
"border: 2px solid rgb(0, 43, 91);")
        self.lsn_list_students.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.lsn_list_students.setDragEnabled(True)

        self.gridLayout_10.addWidget(self.lsn_list_students, 1, 0, 1, 1)


        self.verticalLayout_6.addWidget(self.mid_frame_5)


        self.gridLayout_9.addWidget(self.lesson_frame_3, 0, 0, 1, 1)


        self.gridLayout_11.addWidget(self.frame_2, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.lesson_assigning_page)

        self.gridLayout_15.addWidget(self.stackedWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(3)
        self.std_btn_back_to_home.setDefault(False)
        self.mediaStackWidget.setCurrentIndex(1)
        self.lsn_btn_back_to_home.setDefault(False)
        self.task_btn_back_to_home.setDefault(False)
        self.evalstackwidget.setCurrentIndex(1)
        self.lsn_btn_back_to_home_3.setDefault(False)
        self.lsn_btn_back_to_home_4.setDefault(False)


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
        self.task_btn_matching.setText(QCoreApplication.translate("MainWindow", u"\u09b6\u09ac\u09cd\u09a6 \u09ae\u09bf\u09b2\u09be\u0987", None))
        self.task_btn_sequence.setText(QCoreApplication.translate("MainWindow", u"\u0995\u09cd\u09b0\u09ae\u09a7\u09be\u09b0\u09be", None))
        self.task_btn_puzzle.setText(QCoreApplication.translate("MainWindow", u"\u09a7\u09be\u0981\u09a7\u09be", None))
        self.task_puzzle_image_lbl.setText(QCoreApplication.translate("MainWindow", u"\u09a7\u09be\u0981\u09a7\u09be\u09b0 \u099c\u09a8\u09cd\u09af \u09aa\u09cd\u09b0\u09df\u09cb\u099c\u09a8\u09c0\u09df \u099b\u09ac\u09bf\u09b8\u09ae\u09c2\u09b9 \u098f\u0996\u09be\u09a8\u09c7 \u09a8\u09bf\u09b0\u09cd\u09ac\u09be\u099a\u09a8 \u0995\u09b0\u09c1\u09a8 (\u098f\u0995\u09be\u09a7\u09bf\u0995 \u099b\u09ac\u09bf \u09a8\u09bf\u09b0\u09cd\u09ac\u09be\u099a\u09a8 \u0995\u09b0\u09be \u09af\u09be\u09ac\u09c7)", None))
        self.task_puzzle_q_set_lbl.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u09b8\u09c7\u099f \u09a8\u09ae\u09cd\u09ac\u09b0 \u09a6\u09bf\u09a8 (\u09af\u09c7\u09ae\u09a8 set1)", None))
        self.task_puzzle_show_set_btn.setText(QCoreApplication.translate("MainWindow", u"\u09a4\u09c8\u09b0\u09bf\u0995\u09c3\u09a4 \u09a7\u09be\u0981\u09a7\u09be\u09b0 \u09b8\u09c7\u099f\u0997\u09c1\u09b2\u09cb \u09a6\u09c7\u0996\u09c1\u09a8", None))
        self.task_puzzle_save_set_btn.setText(QCoreApplication.translate("MainWindow", u"\u09b8\u0982\u09b0\u0995\u09cd\u09b7\u09a8 \u0995\u09b0\u09c1\u09a8", None))
        self.task_puzzle_select_img_btn.setText(QCoreApplication.translate("MainWindow", u"\u099b\u09ac\u09bf \u09a8\u09bf\u09b0\u09cd\u09ac\u09be\u099a\u09a8 \u0995\u09b0\u09c1\u09a8", None))
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
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"\u09aa\u09be\u09a0 \u09aa\u09cd\u09b0\u09a6\u09be\u09a8\u09c7\u09b0 \u09b8\u09ae\u09df\u0995\u09be\u09b2", None));
        self.lsn_lbl_lessons_8.setText(QCoreApplication.translate("MainWindow", u"\u09b6\u09bf\u0995\u09cd\u09b7\u09be\u09b0\u09cd\u09a5\u09c0\u09a6\u09c7\u09b0 \u09a4\u09be\u09b2\u09bf\u0995\u09be", None))
        self.lsn_btn_assign_lesson.setText(QCoreApplication.translate("MainWindow", u"\u09aa\u09be\u09a0 \u09aa\u09cd\u09b0\u09a6\u09be\u09a8 \u0995\u09b0\u09c1\u09a8", None))
    # retranslateUi

