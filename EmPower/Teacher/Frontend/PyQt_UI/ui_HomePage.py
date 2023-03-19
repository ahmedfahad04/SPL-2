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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSlider,
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
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
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
        icon2 = QIcon()
        icon2.addFile(u"../Images/std_assessment.png", QSize(), QIcon.Normal, QIcon.Off)
        self.home_btn_quiz.setIcon(icon2)
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
        icon3 = QIcon()
        icon3.addFile(u"../Images/std_perfor.png", QSize(), QIcon.Normal, QIcon.Off)
        self.home_btn_progress.setIcon(icon3)
        self.home_btn_progress.setIconSize(QSize(250, 300))

        self.horizontalLayout_2.addWidget(self.home_btn_progress)

        self.home_btn_settings = QPushButton(self.frm_button)
        self.home_btn_settings.setObjectName(u"home_btn_settings")
        sizePolicy.setHeightForWidth(self.home_btn_settings.sizePolicy().hasHeightForWidth())
        self.home_btn_settings.setSizePolicy(sizePolicy)
        self.home_btn_settings.setMinimumSize(QSize(160, 150))
        self.home_btn_settings.setMaximumSize(QSize(200, 200))
        self.home_btn_settings.setCursor(QCursor(Qt.PointingHandCursor))
        self.home_btn_settings.setStyleSheet(u"QPushButton {\n"
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
        icon4.addFile(u"../Images/setting_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.home_btn_settings.setIcon(icon4)
        self.home_btn_settings.setIconSize(QSize(250, 300))

        self.horizontalLayout_2.addWidget(self.home_btn_settings)


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
        if (self.std_tableWidget.columnCount() < 5):
            self.std_tableWidget.setColumnCount(5)
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
        font4 = QFont()
        font4.setFamilies([u"Hind Siliguri Medium"])
        font4.setPointSize(13)
        font4.setKerning(True)
        font4.setStyleStrategy(QFont.PreferDefault)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem4.setFont(font4);
        self.std_tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
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
        self.std_tableWidget.setColumnCount(5)
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
        icon6.addFile(u"../Images/add_icon.png", QSize(), QIcon.Normal, QIcon.Off)
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
        self.bottom_top_frame.setStyleSheet(u"background-color: rgb(29, 88, 105);\n"
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
        self.middle_content_frame.setStyleSheet(u"background-color: rgb(30, 90, 108);")
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
        self.video_player_widget = QWidget(self.video_page)
        self.video_player_widget.setObjectName(u"video_player_widget")
        self.video_player_widget.setMinimumSize(QSize(690, 81))
        self.gridLayout_3 = QGridLayout(self.video_player_widget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.video_label = QLabel(self.video_player_widget)
        self.video_label.setObjectName(u"video_label")
        self.video_label.setMinimumSize(QSize(681, 371))
        self.video_label.setStyleSheet(u"border: 2px solid blue;")

        self.gridLayout_3.addWidget(self.video_label, 0, 0, 1, 4)

        self.horizontalSlider = QSlider(self.video_player_widget)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setMinimumSize(QSize(350, 0))
        self.horizontalSlider.setCursor(QCursor(Qt.PointingHandCursor))
        self.horizontalSlider.setStyleSheet(u"\n"
"\n"
"QSlider::groove:horizontal {\n"
"	\n"
"	background-color: rgb(43, 72, 101);\n"
"    border: 1px solid rgb(43, 72, 101);\n"
"    height: 5px;\n"
"    margin: 0px;\n"
"    }\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(160, 253, 230) ;\n"
"	color: rgb(137, 218, 199);\n"
"    border: 1px solid;\n"
"    height: 10px;\n"
"    width: 20px;\n"
"    margin: -8px 0px;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"	background-color: rgb(143, 227, 207);\n"
"}")
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_3.addWidget(self.horizontalSlider, 1, 0, 1, 2)

        self.playBtn = QPushButton(self.video_player_widget)
        self.playBtn.setObjectName(u"playBtn")
        self.playBtn.setEnabled(False)
        self.playBtn.setMinimumSize(QSize(41, 31))
        self.playBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.playBtn.setStyleSheet(u"QPushButton {\n"
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
        self.playBtn.setFlat(False)

        self.gridLayout_3.addWidget(self.playBtn, 2, 0, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(198, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_8, 2, 1, 1, 1)

        self.label = QLabel(self.video_player_widget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(81, 31))
        self.label.setMaximumSize(QSize(61, 31))
        self.label.setStyleSheet(u"background-color: #2B4865;\n"
"color:  rgb(160, 253, 230) ;\n"
"border-radius: 15px;")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label, 2, 2, 1, 1)

        self.volume_Slider = QSlider(self.video_player_widget)
        self.volume_Slider.setObjectName(u"volume_Slider")
        self.volume_Slider.setMinimumSize(QSize(109, 25))
        self.volume_Slider.setMaximumSize(QSize(109, 25))
        self.volume_Slider.setCursor(QCursor(Qt.PointingHandCursor))
        self.volume_Slider.setStyleSheet(u"\n"
"\n"
"QSlider::groove:horizontal {\n"
"	\n"
"	background-color: rgb(43, 72, 101);\n"
"    border: 1px solid rgb(43, 72, 101);\n"
"    height: 5px;\n"
"    margin: 0px;\n"
"    }\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(160, 253, 230) ;\n"
"	color: rgb(137, 218, 199);\n"
"    border: 1px solid;\n"
"    height: 10px;\n"
"    width: 20px;\n"
"    margin: -8px 0px;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"	background-color: rgb(143, 227, 207);\n"
"}")
        self.volume_Slider.setOrientation(Qt.Horizontal)

        self.gridLayout_3.addWidget(self.volume_Slider, 2, 3, 1, 1)


        self.verticalLayout_5.addWidget(self.video_player_widget)

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
        font12.setPointSize(15)
        font12.setBold(False)
        self.lsn_btn_add_lessons.setFont(font12)
        self.lsn_btn_add_lessons.setCursor(QCursor(Qt.PointingHandCursor))
        self.lsn_btn_add_lessons.setStyleSheet(u"QPushButton {\n"
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
        self.lsn_btn_add_lessons.setIcon(icon6)
        self.lsn_btn_add_lessons.setIconSize(QSize(30, 40))

        self.horizontalLayout_10.addWidget(self.lsn_btn_add_lessons)


        self.gridLayout_2.addWidget(self.bottom_frame_2, 2, 0, 1, 1)


        self.horizontalLayout_11.addWidget(self.lesson_frame)

        self.stackedWidget.addWidget(self.lesson_page)

        self.verticalLayout_3.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)
        self.std_btn_back_to_home.setDefault(False)
        self.lsn_btn_back_to_home.setDefault(False)
        self.mediaStackWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.home_lbl_ban_picture.setText("")
        self.home_btn_student.setText("")
        self.home_btn_lesson.setText("")
        self.home_btn_quiz.setText("")
        self.home_btn_progress.setText("")
        self.home_btn_settings.setText("")
        self.std_btn_back_to_home.setText("")
        self.std_lbl_headline.setText(QCoreApplication.translate("MainWindow", u"\u09b6\u09bf\u0995\u09cd\u09b7\u09be\u09b0\u09cd\u09a5\u09c0\u09b0 \u09a4\u09a5\u09cd\u09af\u09b8\u09ae\u09c2\u09b9 ", None))
        ___qtablewidgetitem = self.std_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u09b6\u09bf\u0995\u09cd\u09b7\u09be\u09b0\u09cd\u09a5\u09c0\u09b0 \u0986\u0987\u09a1\u09bf", None));
        ___qtablewidgetitem1 = self.std_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u09b6\u09bf\u0995\u09cd\u09b7\u09be\u09b0\u09cd\u09a5\u09c0\u09b0 \u09a8\u09be\u09ae", None));
        ___qtablewidgetitem2 = self.std_tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u09b6\u09bf\u0995\u09cd\u09b7\u09be\u09b0\u09cd\u09a5\u09c0\u09b0 \u09ac\u09df\u09b8 ", None));
        ___qtablewidgetitem3 = self.std_tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u0985\u09ad\u09bf\u09ad\u09be\u09ac\u0995\u09c7\u09b0 \u09a8\u09be\u09ae", None));
        ___qtablewidgetitem4 = self.std_tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u0985\u09ad\u09bf\u09ad\u09be\u09ac\u0995\u09c7\u09b0 \u09ae\u09cb\u09ac\u09be\u0987\u09b2 \u09a8\u09ae\u09cd\u09ac\u09b0", None));
        self.std_btn_add_student.setText(QCoreApplication.translate("MainWindow", u"\u09a8\u09a4\u09c1\u09a8 \u09b6\u09bf\u0995\u09cd\u09b7\u09be\u09b0\u09cd\u09a5\u09c0 \u09af\u09c1\u0995\u09cd\u09a4 \u0995\u09b0\u09c1\u09a8", None))
        self.std_btn_update_info.setText(QCoreApplication.translate("MainWindow", u"\u09b6\u09bf\u0995\u09cd\u09b7\u09be\u09b0\u09cd\u09a5\u09c0\u09b0 \u09a4\u09a5\u09cd\u09af \u0986\u09aa\u09a1\u09c7\u099f \u0995\u09b0\u09c1\u09a8", None))
        self.std_btn_remove_student.setText(QCoreApplication.translate("MainWindow", u"\u09b6\u09bf\u0995\u09cd\u09b7\u09be\u09b0\u09cd\u09a5\u09c0 \u098f\u09a8\u09cd\u099f\u09cd\u09b0\u09bf \u09ac\u09be\u09a4\u09bf\u09b2 \u0995\u09b0\u09c1\u09a8", None))
        self.lsn_btn_back_to_home.setText("")
        self.lsn_lbl_headline.setText(QCoreApplication.translate("MainWindow", u"\u09aa\u09be\u09a0\u09b8\u09c2\u099a\u09bf", None))
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
        self.video_label.setText("")
        self.playBtn.setText(QCoreApplication.translate("MainWindow", u"Play", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u09ad\u09b2\u09bf\u0989\u09ae", None))
        self.lsn_lbl_lesson_topic.setText(QCoreApplication.translate("MainWindow", u"\u09aa\u09b0\u09bf\u099a\u09df", None))
        self.lsn_btn_add_lessons.setText(QCoreApplication.translate("MainWindow", u"\u09a8\u09a4\u09c1\u09a8 \u09aa\u09be\u09a0 \u09af\u09c1\u0995\u09cd\u09a4 \u0995\u09b0\u09c1\u09a8", None))
    # retranslateUi

