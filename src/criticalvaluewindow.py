# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CriticalValueWindow.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CriticalValueTableWindow(object):
    def setupUi(self, CriticalValueTableWindow):
        CriticalValueTableWindow.setObjectName("CriticalValueTableWindow")
        CriticalValueTableWindow.resize(850, 900)
        self.verticalLayout = QtWidgets.QVBoxLayout(CriticalValueTableWindow)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.settingArea = QtWidgets.QScrollArea(CriticalValueTableWindow)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Emoji")
        font.setPointSize(10)
        self.settingArea.setFont(font)
        self.settingArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.settingArea.setWidgetResizable(True)
        self.settingArea.setObjectName("settingArea")
        self.settingContent = QtWidgets.QWidget()
        self.settingContent.setGeometry(QtCore.QRect(0, 0, 848, 898))
        self.settingContent.setObjectName("settingContent")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.settingContent)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem, 4, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.settingContent)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Emoji")
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setWordWrap(True)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 15, 1, 1, 1)
        self.saveCVL_btn = QtWidgets.QToolButton(self.settingContent)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.saveCVL_btn.sizePolicy().hasHeightForWidth())
        self.saveCVL_btn.setSizePolicy(sizePolicy)
        self.saveCVL_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.saveCVL_btn.setStyleSheet("QToolButton{\n"
"    height: 30px;\n"
"    width: 30px;\n"
"}")
        self.saveCVL_btn.setObjectName("saveCVL_btn")
        self.gridLayout_2.addWidget(self.saveCVL_btn, 15, 6, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.settingContent)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Emoji")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 6, 1, 1, 3)
        self.label_9 = QtWidgets.QLabel(self.settingContent)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Emoji")
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setWordWrap(True)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 9, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.settingContent)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Emoji")
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setWordWrap(True)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 11, 1, 1, 1)
        self.saveCVL_textCtl = QtWidgets.QLineEdit(self.settingContent)
        self.saveCVL_textCtl.setMaximumSize(QtCore.QSize(702, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segue UI Emoji")
        font.setPointSize(10)
        self.saveCVL_textCtl.setFont(font)
        self.saveCVL_textCtl.setStyleSheet("QLineEdit{\n"
"   min-width: 180px;\n"
"   max-width: 700px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    border: 1px solid #2a4d69; \n"
"}\n"
"")
        self.saveCVL_textCtl.setReadOnly(True)
        self.saveCVL_textCtl.setObjectName("saveCVL_textCtl")
        self.gridLayout_2.addWidget(self.saveCVL_textCtl, 15, 3, 1, 3)
        self.clinSig_textCtl = QtWidgets.QLineEdit(self.settingContent)
        font = QtGui.QFont()
        font.setFamily("Segue UI Emoji")
        font.setPointSize(10)
        self.clinSig_textCtl.setFont(font)
        self.clinSig_textCtl.setUpdatesEnabled(True)
        self.clinSig_textCtl.setVisible(True)
        self.clinSig_textCtl.setWindowTitle("")
        self.clinSig_textCtl.setWindowIconText("")
        self.clinSig_textCtl.setWindowOpacity(1.0)
        self.clinSig_textCtl.setWindowModified(False)
        self.clinSig_textCtl.setWindowFilePath("")
        self.clinSig_textCtl.setModified(False)
        self.clinSig_textCtl.setObjectName("clinSig_textCtl")
        self.gridLayout_2.addWidget(self.clinSig_textCtl, 13, 3, 1, 2)
        self.nTreatment_textCtl = QtWidgets.QLineEdit(self.settingContent)
        font = QtGui.QFont()
        font.setFamily("Segue UI Emoji")
        font.setPointSize(10)
        self.nTreatment_textCtl.setFont(font)
        self.nTreatment_textCtl.setObjectName("nTreatment_textCtl")
        self.gridLayout_2.addWidget(self.nTreatment_textCtl, 9, 3, 1, 2)
        self.label_17 = QtWidgets.QLabel(self.settingContent)
        self.label_17.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Emoji")
        font.setPointSize(10)
        self.label_17.setFont(font)
        self.label_17.setWordWrap(True)
        self.label_17.setObjectName("label_17")
        self.gridLayout_2.addWidget(self.label_17, 13, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 8, 1, 1, 1)
        self.nControl_textCtl = QtWidgets.QLineEdit(self.settingContent)
        font = QtGui.QFont()
        font.setFamily("Segue UI Emoji")
        font.setPointSize(10)
        self.nControl_textCtl.setFont(font)
        self.nControl_textCtl.setObjectName("nControl_textCtl")
        self.gridLayout_2.addWidget(self.nControl_textCtl, 11, 3, 1, 2)
        spacerItem2 = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 3, 1, 1, 1)
        self.line_4 = QtWidgets.QFrame(self.settingContent)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_4.sizePolicy().hasHeightForWidth())
        self.line_4.setSizePolicy(sizePolicy)
        self.line_4.setMaximumSize(QtCore.QSize(16777215, 2))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.line_4.setFont(font)
        self.line_4.setStyleSheet("QWidget{\n"
"     background-color:#399ee5;\n"
"}")
        self.line_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_4.setLineWidth(-3)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setObjectName("line_4")
        self.gridLayout_2.addWidget(self.line_4, 7, 1, 1, 7)
        self.line_3 = QtWidgets.QFrame(self.settingContent)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_3.sizePolicy().hasHeightForWidth())
        self.line_3.setSizePolicy(sizePolicy)
        self.line_3.setMaximumSize(QtCore.QSize(16777215, 2))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.line_3.setFont(font)
        self.line_3.setStyleSheet("QWidget{\n"
"     background-color:#399ee5;\n"
"}")
        self.line_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_3.setLineWidth(-3)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setObjectName("line_3")
        self.gridLayout_2.addWidget(self.line_3, 2, 1, 1, 7)
        spacerItem3 = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 3, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.settingContent)
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 10000))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Emoji")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 1, 1, 1)
        self.seed_textCtl = QtWidgets.QLineEdit(self.settingContent)
        self.seed_textCtl.setEnabled(False)
        self.seed_textCtl.setMinimumSize(QtCore.QSize(202, 0))
        self.seed_textCtl.setMaximumSize(QtCore.QSize(202, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segue UI Emoji")
        font.setPointSize(10)
        self.seed_textCtl.setFont(font)
        self.seed_textCtl.setText("")
        self.seed_textCtl.setObjectName("seed_textCtl")
        self.gridLayout_2.addWidget(self.seed_textCtl, 4, 3, 1, 2)
        spacerItem4 = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 5, 1, 1, 1)
        self.seed_checkBox = QtWidgets.QCheckBox(self.settingContent)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.seed_checkBox.sizePolicy().hasHeightForWidth())
        self.seed_checkBox.setSizePolicy(sizePolicy)
        self.seed_checkBox.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Emoji")
        font.setPointSize(10)
        self.seed_checkBox.setFont(font)
        self.seed_checkBox.setToolTipDuration(-1)
        self.seed_checkBox.setChecked(False)
        self.seed_checkBox.setObjectName("seed_checkBox")
        self.gridLayout_2.addWidget(self.seed_checkBox, 4, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem5, 2, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem6, 0, 1, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem7, 16, 1, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem8, 11, 0, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem9, 6, 0, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem10, 9, 0, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem11, 12, 1, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem12, 14, 1, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem13, 10, 1, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem14, 13, 0, 1, 1)
        spacerItem15 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem15, 15, 0, 1, 1)
        spacerItem16 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem16, 4, 2, 1, 1)
        self.settingArea.setWidget(self.settingContent)
        self.verticalLayout.addWidget(self.settingArea)

        self.retranslateUi(CriticalValueTableWindow)
        QtCore.QMetaObject.connectSlotsByName(CriticalValueTableWindow)
        CriticalValueTableWindow.setTabOrder(self.seed_checkBox, self.seed_textCtl)
        CriticalValueTableWindow.setTabOrder(self.seed_textCtl, self.nTreatment_textCtl)
        CriticalValueTableWindow.setTabOrder(self.nTreatment_textCtl, self.nControl_textCtl)
        CriticalValueTableWindow.setTabOrder(self.nControl_textCtl, self.clinSig_textCtl)
        CriticalValueTableWindow.setTabOrder(self.clinSig_textCtl, self.saveCVL_textCtl)
        CriticalValueTableWindow.setTabOrder(self.saveCVL_textCtl, self.saveCVL_btn)
        CriticalValueTableWindow.setTabOrder(self.saveCVL_btn, self.settingArea)

    def retranslateUi(self, CriticalValueTableWindow):
        _translate = QtCore.QCoreApplication.translate
        CriticalValueTableWindow.setWindowTitle(_translate("CriticalValueTableWindow", "Form"))
        self.label_8.setText(_translate("CriticalValueTableWindow", "Output File:"))
        self.saveCVL_btn.setText(_translate("CriticalValueTableWindow", "..."))
        self.label_3.setText(_translate("CriticalValueTableWindow", "Trial Parameters"))
        self.label_9.setText(_translate("CriticalValueTableWindow", "Number of Patients in Treatment："))
        self.label_10.setText(_translate("CriticalValueTableWindow", "Number of Patients in Control:"))
        self.clinSig_textCtl.setPlaceholderText(_translate("CriticalValueTableWindow", "0-1"))
        self.label_17.setText(_translate("CriticalValueTableWindow", "Clinically Significant Difference:"))
        self.label_4.setText(_translate("CriticalValueTableWindow", "Table Setting"))
        self.seed_textCtl.setPlaceholderText(_translate("CriticalValueTableWindow", "0~999999"))
        self.seed_checkBox.setToolTip(_translate("CriticalValueTableWindow", "The seed to generate the table"))
        self.seed_checkBox.setText(_translate("CriticalValueTableWindow", "Seed:"))

