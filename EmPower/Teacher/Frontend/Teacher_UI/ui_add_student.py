# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Frontend\PyQt_UI\add_new_student.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(552, 720)
        Form.setMinimumSize(QtCore.QSize(550, 720))
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.top_frame = QtWidgets.QFrame(Form)
        self.top_frame.setMinimumSize(QtCore.QSize(530, 70))
        self.top_frame.setStyleSheet("background-color: rgb(43, 72, 101);\n"
"border-radius: 20px;")
        self.top_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top_frame.setObjectName("top_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.top_frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lbl_heading = QtWidgets.QLabel(self.top_frame)
        font = QtGui.QFont()
        font.setFamily("Hind Siliguri Medium")
        font.setPointSize(19)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_heading.setFont(font)
        self.lbl_heading.setStyleSheet("color: rgb(143, 227, 207);")
        self.lbl_heading.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_heading.setObjectName("lbl_heading")
        self.horizontalLayout.addWidget(self.lbl_heading)
        self.verticalLayout.addWidget(self.top_frame)
        self.middle_frame = QtWidgets.QFrame(Form)
        self.middle_frame.setMinimumSize(QtCore.QSize(530, 560))
        self.middle_frame.setStyleSheet("background-color: rgb(32, 94, 115);\n"
"border-radius: 20px;")
        self.middle_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.middle_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.middle_frame.setObjectName("middle_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.middle_frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.input_id = QtWidgets.QLineEdit(self.middle_frame)
        self.input_id.setMinimumSize(QtCore.QSize(280, 55))
        font = QtGui.QFont()
        font.setFamily("Hind Siliguri Medium")
        font.setPointSize(11)
        self.input_id.setFont(font)
        self.input_id.setStyleSheet("background-color: rgb(137, 218, 199);\n"
"border: 2px solid rgb(101, 161, 146);\n"
"padding-left: 15px;\n"
"border-radius: 10px;\n"
"color: rgb(43, 72, 101);")
        self.input_id.setText("")
        self.input_id.setObjectName("input_id")
        self.verticalLayout_2.addWidget(self.input_id)
        self.input_name = QtWidgets.QLineEdit(self.middle_frame)
        self.input_name.setMinimumSize(QtCore.QSize(330, 50))
        font = QtGui.QFont()
        font.setFamily("Hind Siliguri Medium")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.input_name.setFont(font)
        self.input_name.setStyleSheet("background-color: rgb(137, 218, 199);\n"
"border: 2px solid rgb(101, 161, 146);\n"
"padding-left: 15px;\n"
"border-radius: 10px;\n"
"color: rgb(43, 72, 101);")
        self.input_name.setObjectName("input_name")
        self.verticalLayout_2.addWidget(self.input_name)
        self.input_age = QtWidgets.QLineEdit(self.middle_frame)
        self.input_age.setMinimumSize(QtCore.QSize(330, 50))
        font = QtGui.QFont()
        font.setFamily("Hind Siliguri Medium")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.input_age.setFont(font)
        self.input_age.setStyleSheet("background-color: rgb(137, 218, 199);\n"
"border: 2px solid rgb(101, 161, 146);\n"
"padding-left: 15px;\n"
"border-radius: 10px;\n"
"color: rgb(43, 72, 101);")
        self.input_age.setObjectName("input_age")
        self.verticalLayout_2.addWidget(self.input_age)
        self.input_address = QtWidgets.QLineEdit(self.middle_frame)
        self.input_address.setMinimumSize(QtCore.QSize(330, 50))
        font = QtGui.QFont()
        font.setFamily("Hind Siliguri Medium")
        font.setPointSize(11)
        self.input_address.setFont(font)
        self.input_address.setStyleSheet("background-color: rgb(137, 218, 199);\n"
"border: 2px solid rgb(101, 161, 146);\n"
"padding-left: 15px;\n"
"border-radius: 10px;\n"
"color: rgb(43, 72, 101);")
        self.input_address.setObjectName("input_address")
        self.verticalLayout_2.addWidget(self.input_address)
        self.input_guardian = QtWidgets.QLineEdit(self.middle_frame)
        self.input_guardian.setMinimumSize(QtCore.QSize(330, 50))
        font = QtGui.QFont()
        font.setFamily("Hind Siliguri Medium")
        font.setPointSize(11)
        self.input_guardian.setFont(font)
        self.input_guardian.setStyleSheet("background-color: rgb(137, 218, 199);\n"
"border: 2px solid rgb(101, 161, 146);\n"
"padding-left: 15px;\n"
"border-radius: 10px;\n"
"color: rgb(43, 72, 101);")
        self.input_guardian.setObjectName("input_guardian")
        self.verticalLayout_2.addWidget(self.input_guardian)
        self.input_phone = QtWidgets.QLineEdit(self.middle_frame)
        self.input_phone.setMinimumSize(QtCore.QSize(330, 50))
        font = QtGui.QFont()
        font.setFamily("Hind Siliguri Medium")
        font.setPointSize(11)
        self.input_phone.setFont(font)
        self.input_phone.setStyleSheet("background-color: rgb(137, 218, 199);\n"
"border: 2px solid rgb(101, 161, 146);\n"
"padding-left: 15px;\n"
"border-radius: 10px;\n"
"color: rgb(43, 72, 101);")
        self.input_phone.setObjectName("input_phone")
        self.verticalLayout_2.addWidget(self.input_phone)
        self.btn_submit = QtWidgets.QPushButton(self.middle_frame)
        self.btn_submit.setMinimumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setFamily("Hind Siliguri Medium")
        font.setPointSize(13)
        self.btn_submit.setFont(font)
        self.btn_submit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_submit.setStyleSheet("QPushButton {\n"
"border: 3px solid rgb(43, 72, 101);\n"
"border-radius: 10px;\n"
"background-color:  #002B5B;\n"
"color: rgb(137, 218, 199)\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"background-color: rgb(43, 72, 101);\n"
"border: 3px solid rgb(0, 43, 91); \n"
"}")
        self.btn_submit.setFlat(True)
        self.btn_submit.setObjectName("btn_submit")
        self.verticalLayout_2.addWidget(self.btn_submit)
        self.verticalLayout.addWidget(self.middle_frame)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lbl_heading.setText(_translate("Form", "শিক্ষার্থীর তথ্য প্রদান করুন"))
        self.input_id.setPlaceholderText(_translate("Form", "শিক্ষার্থীর আইডি"))
        self.input_name.setPlaceholderText(_translate("Form", "শিক্ষার্থীর নাম "))
        self.input_age.setPlaceholderText(_translate("Form", "শিক্ষার্থীর বয়স"))
        self.input_address.setPlaceholderText(_translate("Form", "ঠিকানা"))
        self.input_guardian.setPlaceholderText(_translate("Form", "অভিভাবকের নাম"))
        self.input_phone.setPlaceholderText(_translate("Form", "অভিভাবকের মোবাইল নম্বর"))
        self.btn_submit.setText(_translate("Form", "তথ্য যুক্ত করুন "))
        self.btn_submit.setShortcut(_translate("Form", "Return"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
