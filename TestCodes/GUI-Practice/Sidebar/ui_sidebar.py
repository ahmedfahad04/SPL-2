# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sidebar.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)
import files_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1281, 825)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.icon_with_lbl_widget = QWidget(self.centralwidget)
        self.icon_with_lbl_widget.setObjectName(u"icon_with_lbl_widget")
        self.icon_with_lbl_widget.setMinimumSize(QSize(200, 803))
        self.icon_with_lbl_widget.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_4 = QVBoxLayout(self.icon_with_lbl_widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.sidebar_lbl = QLabel(self.icon_with_lbl_widget)
        self.sidebar_lbl.setObjectName(u"sidebar_lbl")
        font = QFont()
        font.setPointSize(15)
        self.sidebar_lbl.setFont(font)

        self.verticalLayout_4.addWidget(self.sidebar_lbl)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.home_large_btn = QPushButton(self.icon_with_lbl_widget)
        self.home_large_btn.setObjectName(u"home_large_btn")
        icon = QIcon()
        icon.addFile(u":/icons/resources/home-outline.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.home_large_btn.setIcon(icon)
        self.home_large_btn.setCheckable(True)
        self.home_large_btn.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.home_large_btn)

        self.files_large_btn = QPushButton(self.icon_with_lbl_widget)
        self.files_large_btn.setObjectName(u"files_large_btn")
        icon1 = QIcon()
        icon1.addFile(u":/icons/resources/list.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.files_large_btn.setIcon(icon1)
        self.files_large_btn.setCheckable(True)
        self.files_large_btn.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.files_large_btn)

        self.people_large_btn = QPushButton(self.icon_with_lbl_widget)
        self.people_large_btn.setObjectName(u"people_large_btn")
        icon2 = QIcon()
        icon2.addFile(u":/icons/resources/people.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.people_large_btn.setIcon(icon2)
        self.people_large_btn.setCheckable(True)
        self.people_large_btn.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.people_large_btn)

        self.records_large_btn = QPushButton(self.icon_with_lbl_widget)
        self.records_large_btn.setObjectName(u"records_large_btn")
        icon3 = QIcon()
        icon3.addFile(u":/icons/resources/bookmark.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.records_large_btn.setIcon(icon3)
        self.records_large_btn.setCheckable(True)

        self.verticalLayout_3.addWidget(self.records_large_btn)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.verticalSpacer_2 = QSpacerItem(20, 559, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.exit_large_btn = QPushButton(self.icon_with_lbl_widget)
        self.exit_large_btn.setObjectName(u"exit_large_btn")
        icon4 = QIcon()
        icon4.addFile(u":/icons/resources/close-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.exit_large_btn.setIcon(icon4)

        self.verticalLayout_4.addWidget(self.exit_large_btn)


        self.gridLayout.addWidget(self.icon_with_lbl_widget, 0, 1, 1, 1)

        self.main_widget = QWidget(self.centralwidget)
        self.main_widget.setObjectName(u"main_widget")
        self.main_widget.setMinimumSize(QSize(845, 803))
        self.main_widget.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout_3 = QHBoxLayout(self.main_widget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.menu_btn = QPushButton(self.main_widget)
        self.menu_btn.setObjectName(u"menu_btn")
        icon5 = QIcon()
        icon5.addFile(u":/icons/resources/ellipsis-vertical.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_btn.setIcon(icon5)
        self.menu_btn.setCheckable(True)
        self.menu_btn.setAutoExclusive(True)

        self.horizontalLayout.addWidget(self.menu_btn)

        self.prev_btn = QPushButton(self.main_widget)
        self.prev_btn.setObjectName(u"prev_btn")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prev_btn.sizePolicy().hasHeightForWidth())
        self.prev_btn.setSizePolicy(sizePolicy)
        self.prev_btn.setMinimumSize(QSize(50, 28))
        self.prev_btn.setMaximumSize(QSize(100, 28))

        self.horizontalLayout.addWidget(self.prev_btn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.lesson_linedit = QLineEdit(self.main_widget)
        self.lesson_linedit.setObjectName(u"lesson_linedit")
        self.lesson_linedit.setMinimumSize(QSize(300, 35))
        self.lesson_linedit.setMaximumSize(QSize(300, 28))
        self.lesson_linedit.setCursorPosition(8)
        self.lesson_linedit.setAlignment(Qt.AlignCenter)
        self.lesson_linedit.setReadOnly(True)

        self.horizontalLayout.addWidget(self.lesson_linedit)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.next_btn = QPushButton(self.main_widget)
        self.next_btn.setObjectName(u"next_btn")
        self.next_btn.setMinimumSize(QSize(50, 28))
        self.next_btn.setMaximumSize(QSize(100, 28))

        self.horizontalLayout.addWidget(self.next_btn)


        self.verticalLayout_5.addLayout(self.horizontalLayout)

        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_5.addItem(self.verticalSpacer_3)

        self.stackedWidget = QStackedWidget(self.main_widget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(820, 800))
        self.stackedWidget.setMaximumSize(QSize(16777215, 16777215))
        self.stackedWidget.setStyleSheet(u"background-color: rgb(230, 230, 230);")
        self.home_page_0 = QWidget()
        self.home_page_0.setObjectName(u"home_page_0")
        self.gridLayout_2 = QGridLayout(self.home_page_0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.home_lbl = QLabel(self.home_page_0)
        self.home_lbl.setObjectName(u"home_lbl")
        self.home_lbl.setMinimumSize(QSize(200, 50))
        self.home_lbl.setMaximumSize(QSize(16777215, 50))
        font1 = QFont()
        font1.setPointSize(25)
        self.home_lbl.setFont(font1)
        self.home_lbl.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.home_lbl, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.home_page_0)
        self.files__page_1 = QWidget()
        self.files__page_1.setObjectName(u"files__page_1")
        self.gridLayout_3 = QGridLayout(self.files__page_1)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.file_lbl = QLabel(self.files__page_1)
        self.file_lbl.setObjectName(u"file_lbl")
        self.file_lbl.setMaximumSize(QSize(16777215, 50))
        self.file_lbl.setFont(font1)
        self.file_lbl.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.file_lbl, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.files__page_1)
        self.students_page_2 = QWidget()
        self.students_page_2.setObjectName(u"students_page_2")
        self.gridLayout_4 = QGridLayout(self.students_page_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.student_lbl = QLabel(self.students_page_2)
        self.student_lbl.setObjectName(u"student_lbl")
        self.student_lbl.setMaximumSize(QSize(16777215, 50))
        self.student_lbl.setFont(font1)
        self.student_lbl.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.student_lbl, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.students_page_2)
        self.records_page_3 = QWidget()
        self.records_page_3.setObjectName(u"records_page_3")
        self.gridLayout_5 = QGridLayout(self.records_page_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.records_lbl = QLabel(self.records_page_3)
        self.records_lbl.setObjectName(u"records_lbl")
        self.records_lbl.setMaximumSize(QSize(16777215, 50))
        self.records_lbl.setFont(font1)
        self.records_lbl.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.records_lbl, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.records_page_3)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.horizontalLayout_3.addLayout(self.verticalLayout_5)


        self.gridLayout.addWidget(self.main_widget, 0, 2, 1, 1)

        self.icon_only_widget = QWidget(self.centralwidget)
        self.icon_only_widget.setObjectName(u"icon_only_widget")
        self.icon_only_widget.setMinimumSize(QSize(50, 803))
        self.icon_only_widget.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.icon_only_widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.logo_lbl = QLabel(self.icon_only_widget)
        self.logo_lbl.setObjectName(u"logo_lbl")
        self.logo_lbl.setMinimumSize(QSize(60, 30))
        self.logo_lbl.setMaximumSize(QSize(100, 30))
        self.logo_lbl.setStyleSheet(u"border-image: url(:/logo/resources/rsz_default.jpg);")

        self.verticalLayout_2.addWidget(self.logo_lbl)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.home_small_btn = QPushButton(self.icon_only_widget)
        self.home_small_btn.setObjectName(u"home_small_btn")
        self.home_small_btn.setIcon(icon)
        self.home_small_btn.setCheckable(True)
        self.home_small_btn.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.home_small_btn)

        self.files_small_btn = QPushButton(self.icon_only_widget)
        self.files_small_btn.setObjectName(u"files_small_btn")
        self.files_small_btn.setIcon(icon1)
        self.files_small_btn.setCheckable(True)
        self.files_small_btn.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.files_small_btn)

        self.people_small_btn = QPushButton(self.icon_only_widget)
        self.people_small_btn.setObjectName(u"people_small_btn")
        self.people_small_btn.setIcon(icon2)
        self.people_small_btn.setCheckable(True)
        self.people_small_btn.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.people_small_btn)

        self.record_small_btn = QPushButton(self.icon_only_widget)
        self.record_small_btn.setObjectName(u"record_small_btn")
        self.record_small_btn.setIcon(icon3)
        self.record_small_btn.setCheckable(True)
        self.record_small_btn.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.record_small_btn)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 559, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.exit_small_btn = QPushButton(self.icon_only_widget)
        self.exit_small_btn.setObjectName(u"exit_small_btn")
        self.exit_small_btn.setIcon(icon4)

        self.verticalLayout_2.addWidget(self.exit_small_btn)


        self.gridLayout.addWidget(self.icon_only_widget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.home_small_btn.toggled.connect(self.home_large_btn.setChecked)
        self.files_small_btn.toggled.connect(self.files_large_btn.setChecked)
        self.people_small_btn.toggled.connect(self.people_large_btn.setChecked)
        self.home_large_btn.toggled.connect(self.home_small_btn.setChecked)
        self.files_large_btn.toggled.connect(self.files_small_btn.setChecked)
        self.people_large_btn.toggled.connect(self.people_small_btn.setChecked)
        self.exit_small_btn.clicked.connect(MainWindow.close)
        self.exit_large_btn.clicked.connect(MainWindow.close)
        self.record_small_btn.toggled.connect(self.records_large_btn.setChecked)
        self.records_large_btn.toggled.connect(self.record_small_btn.setChecked)
        self.menu_btn.toggled.connect(self.icon_with_lbl_widget.setVisible)
        self.menu_btn.toggled.connect(self.icon_only_widget.setHidden)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.sidebar_lbl.setText(QCoreApplication.translate("MainWindow", u"Side Bar", None))
        self.home_large_btn.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.files_large_btn.setText(QCoreApplication.translate("MainWindow", u"Files", None))
        self.people_large_btn.setText(QCoreApplication.translate("MainWindow", u"Students", None))
        self.records_large_btn.setText(QCoreApplication.translate("MainWindow", u"Records", None))
        self.exit_large_btn.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.menu_btn.setText("")
        self.prev_btn.setText(QCoreApplication.translate("MainWindow", u"<< Previous", None))
        self.lesson_linedit.setInputMask("")
        self.lesson_linedit.setText(QCoreApplication.translate("MainWindow", u"Lesson 1", None))
        self.next_btn.setText(QCoreApplication.translate("MainWindow", u"Next >>", None))
        self.home_lbl.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.file_lbl.setText(QCoreApplication.translate("MainWindow", u"Files", None))
        self.student_lbl.setText(QCoreApplication.translate("MainWindow", u"Students", None))
        self.records_lbl.setText(QCoreApplication.translate("MainWindow", u"Records", None))
        self.logo_lbl.setText("")
        self.home_small_btn.setText("")
        self.files_small_btn.setText("")
        self.people_small_btn.setText("")
        self.record_small_btn.setText("")
        self.exit_small_btn.setText("")
    # retranslateUi

