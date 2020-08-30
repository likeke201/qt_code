# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(906, 557)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralWidget)
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_6 = QtWidgets.QFrame(self.centralWidget)
        self.frame_6.setMaximumSize(QtCore.QSize(220, 16777215))
        self.frame_6.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.frame_6)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setContentsMargins(11, 5, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.spinDivCount = QtWidgets.QSpinBox(self.groupBox)
        self.spinDivCount.setMinimum(10)
        self.spinDivCount.setMaximum(500)
        self.spinDivCount.setProperty("value", 40)
        self.spinDivCount.setObjectName("spinDivCount")
        self.gridLayout.addWidget(self.spinDivCount, 0, 1, 1, 1)
        self.btnRefreshData = QtWidgets.QPushButton(self.groupBox)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/images/rotateleft.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnRefreshData.setIcon(icon)
        self.btnRefreshData.setObjectName("btnRefreshData")
        self.gridLayout.addWidget(self.btnRefreshData, 1, 0, 1, 2)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_3 = QtWidgets.QGroupBox(self.frame_6)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setContentsMargins(11, 5, 11, 11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.comboCm1 = QtWidgets.QComboBox(self.groupBox_3)
        self.comboCm1.setObjectName("comboCm1")
        self.verticalLayout_2.addWidget(self.comboCm1)
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.comboCm2 = QtWidgets.QComboBox(self.groupBox_3)
        self.comboCm2.setObjectName("comboCm2")
        self.verticalLayout_2.addWidget(self.comboCm2)
        self.label_7 = QtWidgets.QLabel(self.groupBox_3)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.comboCm3 = QtWidgets.QComboBox(self.groupBox_3)
        self.comboCm3.setObjectName("comboCm3")
        self.verticalLayout_2.addWidget(self.comboCm3)
        self.label_8 = QtWidgets.QLabel(self.groupBox_3)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        self.comboCm4 = QtWidgets.QComboBox(self.groupBox_3)
        self.comboCm4.setObjectName("comboCm4")
        self.verticalLayout_2.addWidget(self.comboCm4)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame_6)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setContentsMargins(11, 5, 11, 11)
        self.gridLayout_3.setHorizontalSpacing(6)
        self.gridLayout_3.setVerticalSpacing(10)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.chkBox3D_gridOn = QtWidgets.QCheckBox(self.groupBox_2)
        self.chkBox3D_gridOn.setChecked(True)
        self.chkBox3D_gridOn.setObjectName("chkBox3D_gridOn")
        self.gridLayout_3.addWidget(self.chkBox3D_gridOn, 1, 1, 1, 1)
        self.chkBox3D_invertZ = QtWidgets.QCheckBox(self.groupBox_2)
        self.chkBox3D_invertZ.setObjectName("chkBox3D_invertZ")
        self.gridLayout_3.addWidget(self.chkBox3D_invertZ, 1, 0, 1, 1)
        self.combo3D_type = QtWidgets.QComboBox(self.groupBox_2)
        self.combo3D_type.setObjectName("combo3D_type")
        self.combo3D_type.addItem("")
        self.combo3D_type.addItem("")
        self.combo3D_type.addItem("")
        self.gridLayout_3.addWidget(self.combo3D_type, 0, 1, 1, 1)
        self.chkBox3D_axisOn = QtWidgets.QCheckBox(self.groupBox_2)
        self.chkBox3D_axisOn.setChecked(True)
        self.chkBox3D_axisOn.setObjectName("chkBox3D_axisOn")
        self.gridLayout_3.addWidget(self.chkBox3D_axisOn, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.groupBox_4 = QtWidgets.QGroupBox(self.frame_6)
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_3.setContentsMargins(11, 5, 11, 11)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.groupBox_4)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.combo2D_type = QtWidgets.QComboBox(self.groupBox_4)
        self.combo2D_type.setObjectName("combo2D_type")
        self.combo2D_type.addItem("")
        self.combo2D_type.addItem("")
        self.combo2D_type.addItem("")
        self.combo2D_type.addItem("")
        self.combo2D_type.addItem("")
        self.horizontalLayout_3.addWidget(self.combo2D_type)
        self.verticalLayout.addWidget(self.groupBox_4)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addWidget(self.frame_6)
        self.widgetPlot = QmyFigureCanvas(self.centralWidget)
        self.widgetPlot.setObjectName("widgetPlot")
        self.horizontalLayout.addWidget(self.widgetPlot)
        MainWindow.setCentralWidget(self.centralWidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actQuit = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/images/exit_24.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actQuit.setIcon(icon1)
        self.actQuit.setObjectName("actQuit")
        self.actTightLayout = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/images/39.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actTightLayout.setIcon(icon2)
        self.actTightLayout.setObjectName("actTightLayout")
        self.actSetCursor = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/images/range.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actSetCursor.setIcon(icon3)
        self.actSetCursor.setObjectName("actSetCursor")

        self.retranslateUi(MainWindow)
        self.actQuit.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "QChart绘图详细功能"))
        self.groupBox.setTitle(_translate("MainWindow", "数据"))
        self.label.setText(_translate("MainWindow", "划分格数"))
        self.btnRefreshData.setText(_translate("MainWindow", "重新生成数据"))
        self.groupBox_3.setTitle(_translate("MainWindow", "多组colormap"))
        self.label_4.setText(_translate("MainWindow", "Perceptually Uniform"))
        self.label_6.setText(_translate("MainWindow", "Sequential colormap"))
        self.label_7.setText(_translate("MainWindow", "Sequential(2) colormap"))
        self.label_8.setText(_translate("MainWindow", "Diverging colormap"))
        self.groupBox_2.setTitle(_translate("MainWindow", "3D 子图"))
        self.chkBox3D_gridOn.setText(_translate("MainWindow", "显示网格"))
        self.chkBox3D_invertZ.setText(_translate("MainWindow", "Z轴反向"))
        self.combo3D_type.setItemText(0, _translate("MainWindow", "surface"))
        self.combo3D_type.setItemText(1, _translate("MainWindow", "wireframe"))
        self.combo3D_type.setItemText(2, _translate("MainWindow", "scatter"))
        self.chkBox3D_axisOn.setText(_translate("MainWindow", "显示坐标轴"))
        self.label_2.setText(_translate("MainWindow", "3D绘图类型"))
        self.groupBox_4.setTitle(_translate("MainWindow", "2D 子图"))
        self.label_3.setText(_translate("MainWindow", "2D绘图类型"))
        self.combo2D_type.setItemText(0, _translate("MainWindow", "pcolormaeh"))
        self.combo2D_type.setItemText(1, _translate("MainWindow", "pcolor"))
        self.combo2D_type.setItemText(2, _translate("MainWindow", "imshow"))
        self.combo2D_type.setItemText(3, _translate("MainWindow", "contour"))
        self.combo2D_type.setItemText(4, _translate("MainWindow", "contourf"))
        self.actQuit.setText(_translate("MainWindow", "退出"))
        self.actQuit.setToolTip(_translate("MainWindow", "退出"))
        self.actTightLayout.setText(_translate("MainWindow", "紧凑布局"))
        self.actTightLayout.setToolTip(_translate("MainWindow", "重新紧凑布局"))
        self.actSetCursor.setText(_translate("MainWindow", "十字光标"))
        self.actSetCursor.setToolTip(_translate("MainWindow", "设置为十字光标"))

from myFigureCanvas import QmyFigureCanvas
import res_rc
