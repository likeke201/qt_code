# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dialog.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(352, 263)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        Dialog.setFont(font)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setContentsMargins(11, 11, 11, 9)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox1 = QtWidgets.QGroupBox(Dialog)
        self.groupBox1.setTitle("")
        self.groupBox1.setObjectName("groupBox1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox1)
        self.horizontalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.chkBoxUnder = QtWidgets.QCheckBox(self.groupBox1)
        self.chkBoxUnder.setObjectName("chkBoxUnder")
        self.horizontalLayout_2.addWidget(self.chkBoxUnder)
        self.chkBoxItalic = QtWidgets.QCheckBox(self.groupBox1)
        self.chkBoxItalic.setObjectName("chkBoxItalic")
        self.horizontalLayout_2.addWidget(self.chkBoxItalic)
        self.chkBoxBold = QtWidgets.QCheckBox(self.groupBox1)
        self.chkBoxBold.setChecked(True)
        self.chkBoxBold.setObjectName("chkBoxBold")
        self.horizontalLayout_2.addWidget(self.chkBoxBold)
        self.verticalLayout.addWidget(self.groupBox1)
        self.groupBox2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox2.setTitle("")
        self.groupBox2.setObjectName("groupBox2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox2)
        self.horizontalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.radioBlack = QtWidgets.QRadioButton(self.groupBox2)
        self.radioBlack.setChecked(True)
        self.radioBlack.setObjectName("radioBlack")
        self.horizontalLayout_3.addWidget(self.radioBlack)
        self.radioRed = QtWidgets.QRadioButton(self.groupBox2)
        self.radioRed.setObjectName("radioRed")
        self.horizontalLayout_3.addWidget(self.radioRed)
        self.radioBlue = QtWidgets.QRadioButton(self.groupBox2)
        self.radioBlue.setChecked(False)
        self.radioBlue.setObjectName("radioBlue")
        self.horizontalLayout_3.addWidget(self.radioBlue)
        self.verticalLayout.addWidget(self.groupBox2)
        self.textEdit = QtWidgets.QPlainTextEdit(Dialog)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 10, -1, 10)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btnClear = QtWidgets.QPushButton(Dialog)
        self.btnClear.setObjectName("btnClear")
        self.horizontalLayout.addWidget(self.btnClear)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.btnOK = QtWidgets.QPushButton(Dialog)
        self.btnOK.setObjectName("btnOK")
        self.horizontalLayout.addWidget(self.btnOK)
        self.btnClose = QtWidgets.QPushButton(Dialog)
        self.btnClose.setObjectName("btnClose")
        self.horizontalLayout.addWidget(self.btnClose)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        self.btnOK.clicked.connect(Dialog.accept)
        self.btnClose.clicked.connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.chkBoxUnder, self.chkBoxItalic)
        Dialog.setTabOrder(self.chkBoxItalic, self.chkBoxBold)
        Dialog.setTabOrder(self.chkBoxBold, self.radioBlack)
        Dialog.setTabOrder(self.radioBlack, self.radioRed)
        Dialog.setTabOrder(self.radioRed, self.radioBlue)
        Dialog.setTabOrder(self.radioBlue, self.textEdit)
        Dialog.setTabOrder(self.textEdit, self.btnClear)
        Dialog.setTabOrder(self.btnClear, self.btnOK)
        Dialog.setTabOrder(self.btnOK, self.btnClose)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", " Demo2-3信号与槽"))
        self.chkBoxUnder.setText(_translate("Dialog", "Underline"))
        self.chkBoxItalic.setText(_translate("Dialog", "Italic"))
        self.chkBoxBold.setText(_translate("Dialog", "Bold"))
        self.radioBlack.setText(_translate("Dialog", "Black"))
        self.radioRed.setText(_translate("Dialog", "Red"))
        self.radioBlue.setText(_translate("Dialog", "Blue"))
        self.textEdit.setPlainText(_translate("Dialog", "PyQt5 编程指南\n"
"Python 和 Qt"))
        self.btnClear.setText(_translate("Dialog", "清空"))
        self.btnOK.setText(_translate("Dialog", "确 定"))
        self.btnClose.setText(_translate("Dialog", "退出"))


