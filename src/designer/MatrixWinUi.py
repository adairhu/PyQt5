# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MatrixWinUi.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MatrixWin(object):
    def setupUi(self, MatrixWin):
        MatrixWin.setObjectName("MatrixWin")
        MatrixWin.resize(590, 416)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MatrixWin.sizePolicy().hasHeightForWidth())
        MatrixWin.setSizePolicy(sizePolicy)
        self.groupBox = QtWidgets.QGroupBox(MatrixWin)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 561, 151))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 30, 54, 12))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 61, 16))
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(20, 120, 54, 12))
        self.label_4.setObjectName("label_4")
        self.iceHorizontalSlider = QtWidgets.QSlider(self.groupBox)
        self.iceHorizontalSlider.setGeometry(QtCore.QRect(100, 120, 160, 22))
        self.iceHorizontalSlider.setMaximum(7)
        self.iceHorizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.iceHorizontalSlider.setObjectName("iceHorizontalSlider")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(20, 90, 54, 12))
        self.label_7.setObjectName("label_7")
        self.juiceLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.juiceLineEdit.setGeometry(QtCore.QRect(100, 90, 113, 20))
        self.juiceLineEdit.setObjectName("juiceLineEdit")
        self.tripleSpinBox = QtWidgets.QSpinBox(self.groupBox)
        self.tripleSpinBox.setGeometry(QtCore.QRect(100, 60, 91, 22))
        self.tripleSpinBox.setObjectName("tripleSpinBox")
        self.tequilaHorizontalScrollBar = QtWidgets.QScrollBar(self.groupBox)
        self.tequilaHorizontalScrollBar.setGeometry(QtCore.QRect(100, 30, 160, 16))
        self.tequilaHorizontalScrollBar.setMaximum(11)
        self.tequilaHorizontalScrollBar.setOrientation(QtCore.Qt.Horizontal)
        self.tequilaHorizontalScrollBar.setObjectName("tequilaHorizontalScrollBar")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(500, 60, 61, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(500, 30, 54, 12))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setGeometry(QtCore.QRect(500, 90, 54, 12))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setGeometry(QtCore.QRect(500, 120, 54, 12))
        self.label_11.setObjectName("label_11")
        self.SliderLbl = QtWidgets.QLabel(self.groupBox)
        self.SliderLbl.setGeometry(QtCore.QRect(430, 120, 54, 12))
        self.SliderLbl.setText("")
        self.SliderLbl.setObjectName("SliderLbl")
        self.ScrollBarLbl = QtWidgets.QLabel(self.groupBox)
        self.ScrollBarLbl.setGeometry(QtCore.QRect(430, 30, 54, 12))
        self.ScrollBarLbl.setText("")
        self.ScrollBarLbl.setObjectName("ScrollBarLbl")
        self.speedGroup = QtWidgets.QGroupBox(MatrixWin)
        self.speedGroup.setGeometry(QtCore.QRect(10, 180, 331, 141))
        self.speedGroup.setObjectName("speedGroup")
        self.widget = QtWidgets.QWidget(self.speedGroup)
        self.widget.setGeometry(QtCore.QRect(20, 30, 281, 91))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.radioButton = QtWidgets.QRadioButton(self.widget)
        self.radioButton.setObjectName("radioButton")
        self.speedButtonGroup = QtWidgets.QButtonGroup(MatrixWin)
        self.speedButtonGroup.setObjectName("speedButtonGroup")
        self.speedButtonGroup.addButton(self.radioButton)
        self.gridLayout.addWidget(self.radioButton, 0, 0, 1, 1)
        self.radioButton_5 = QtWidgets.QRadioButton(self.widget)
        self.radioButton_5.setObjectName("radioButton_5")
        self.speedButtonGroup.addButton(self.radioButton_5)
        self.gridLayout.addWidget(self.radioButton_5, 0, 1, 1, 1)
        self.radioButton_8 = QtWidgets.QRadioButton(self.widget)
        self.radioButton_8.setObjectName("radioButton_8")
        self.speedButtonGroup.addButton(self.radioButton_8)
        self.gridLayout.addWidget(self.radioButton_8, 0, 2, 1, 1)
        self.radioButton_2 = QtWidgets.QRadioButton(self.widget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.speedButtonGroup.addButton(self.radioButton_2)
        self.gridLayout.addWidget(self.radioButton_2, 1, 0, 1, 1)
        self.radioButton_6 = QtWidgets.QRadioButton(self.widget)
        self.radioButton_6.setObjectName("radioButton_6")
        self.speedButtonGroup.addButton(self.radioButton_6)
        self.gridLayout.addWidget(self.radioButton_6, 1, 1, 1, 1)
        self.radioButton_9 = QtWidgets.QRadioButton(self.widget)
        self.radioButton_9.setObjectName("radioButton_9")
        self.speedButtonGroup.addButton(self.radioButton_9)
        self.gridLayout.addWidget(self.radioButton_9, 1, 2, 1, 1)
        self.radioButton_3 = QtWidgets.QRadioButton(self.widget)
        self.radioButton_3.setObjectName("radioButton_3")
        self.speedButtonGroup.addButton(self.radioButton_3)
        self.gridLayout.addWidget(self.radioButton_3, 2, 0, 1, 1)
        self.radioButton_4 = QtWidgets.QRadioButton(self.widget)
        self.radioButton_4.setObjectName("radioButton_4")
        self.speedButtonGroup.addButton(self.radioButton_4)
        self.gridLayout.addWidget(self.radioButton_4, 2, 1, 1, 1)
        self.radioButton_7 = QtWidgets.QRadioButton(self.widget)
        self.radioButton_7.setObjectName("radioButton_7")
        self.speedButtonGroup.addButton(self.radioButton_7)
        self.gridLayout.addWidget(self.radioButton_7, 2, 2, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(MatrixWin)
        self.groupBox_3.setGeometry(QtCore.QRect(370, 180, 201, 141))
        self.groupBox_3.setObjectName("groupBox_3")
        self.resultText = QtWidgets.QTextEdit(self.groupBox_3)
        self.resultText.setGeometry(QtCore.QRect(10, 20, 181, 111))
        self.resultText.setObjectName("resultText")
        self.widget1 = QtWidgets.QWidget(MatrixWin)
        self.widget1.setGeometry(QtCore.QRect(10, 350, 239, 25))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.okButton = QtWidgets.QPushButton(self.widget1)
        self.okButton.setObjectName("okButton")
        self.horizontalLayout.addWidget(self.okButton)
        self.clearButton = QtWidgets.QPushButton(self.widget1)
        self.clearButton.setObjectName("clearButton")
        self.horizontalLayout.addWidget(self.clearButton)
        self.cancleButton = QtWidgets.QPushButton(self.widget1)
        self.cancleButton.setObjectName("cancleButton")
        self.horizontalLayout.addWidget(self.cancleButton)

        self.retranslateUi(MatrixWin)
        self.okButton.clicked.connect(MatrixWin.uiAccept)
        self.clearButton.clicked.connect(MatrixWin.uiClear)
        self.cancleButton.clicked.connect(MatrixWin.uiReject)
        self.tequilaHorizontalScrollBar.valueChanged['int'].connect(MatrixWin.uiScrollBarValueChanged)
        self.iceHorizontalSlider.valueChanged['int'].connect(MatrixWin.uiIceSliderValueChanged)
        QtCore.QMetaObject.connectSlotsByName(MatrixWin)

    def retranslateUi(self, MatrixWin):
        _translate = QtCore.QCoreApplication.translate
        MatrixWin.setWindowTitle(_translate("MatrixWin", "玛格丽特鸡尾酒*调酒器"))
        self.groupBox.setTitle(_translate("MatrixWin", "原料"))
        self.label.setText(_translate("MatrixWin", "龙舌兰酒"))
        self.label_2.setText(_translate("MatrixWin", "三重蒸馏酒"))
        self.label_4.setText(_translate("MatrixWin", "冰块"))
        self.label_7.setText(_translate("MatrixWin", "柠檬汁"))
        self.label_8.setText(_translate("MatrixWin", "升"))
        self.label_9.setText(_translate("MatrixWin", "升"))
        self.label_10.setText(_translate("MatrixWin", "升"))
        self.label_11.setText(_translate("MatrixWin", "个"))
        self.speedGroup.setTitle(_translate("MatrixWin", "9种搅拌速度"))
        self.radioButton.setText(_translate("MatrixWin", "1"))
        self.radioButton_5.setText(_translate("MatrixWin", "4"))
        self.radioButton_8.setText(_translate("MatrixWin", "7"))
        self.radioButton_2.setText(_translate("MatrixWin", "2"))
        self.radioButton_6.setText(_translate("MatrixWin", "5"))
        self.radioButton_9.setText(_translate("MatrixWin", "8"))
        self.radioButton_3.setText(_translate("MatrixWin", "3"))
        self.radioButton_4.setText(_translate("MatrixWin", "6"))
        self.radioButton_7.setText(_translate("MatrixWin", "9"))
        self.groupBox_3.setTitle(_translate("MatrixWin", "操作结果"))
        self.okButton.setText(_translate("MatrixWin", "OK"))
        self.clearButton.setText(_translate("MatrixWin", "Clear"))
        self.cancleButton.setText(_translate("MatrixWin", "Cancle"))

