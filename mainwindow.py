# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'simulation.ui'
#
# Created: Mon Jan 18 19:41:31 2016
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(1000, 800)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 800))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 800))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setMouseTracking(False)
        MainWindow.setFocusPolicy(QtCore.Qt.NoFocus)
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        MainWindow.setAcceptDrops(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../Expression.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QtGui.QTabWidget.Rounded)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.logConsole_2 = QtGui.QTabWidget(self.centralwidget)
        self.logConsole_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.logConsole_2.setObjectName(_fromUtf8("logConsole_2"))
        self.logTab = QtGui.QWidget()
        self.logTab.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.logTab.setObjectName(_fromUtf8("logTab"))
        self.logConsole = QtGui.QTextEdit(self.logTab)
        self.logConsole.setEnabled(True)
        self.logConsole.setGeometry(QtCore.QRect(0, 10, 951, 631))
        self.logConsole.setLineWrapMode(QtGui.QTextEdit.NoWrap)
        self.logConsole.setReadOnly(True)
        self.logConsole.setObjectName(_fromUtf8("logConsole"))
        self.logConsole_2.addTab(self.logTab, _fromUtf8(""))
        self.resultTab = QtGui.QWidget()
        self.resultTab.setObjectName(_fromUtf8("resultTab"))
        self.logConsole_2.addTab(self.resultTab, _fromUtf8(""))
        self.verticalLayout.addWidget(self.logConsole_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 31))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuNew = QtGui.QMenu(self.menuFile)
        self.menuNew.setObjectName(_fromUtf8("menuNew"))
        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
        self.menuView = QtGui.QMenu(self.menubar)
        self.menuView.setObjectName(_fromUtf8("menuView"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.toolBar_2 = QtGui.QToolBar(MainWindow)
        self.toolBar_2.setObjectName(_fromUtf8("toolBar_2"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_2)
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setCheckable(False)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionClose = QtGui.QAction(MainWindow)
        self.actionClose.setObjectName(_fromUtf8("actionClose"))
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionCritical_Value_Lookup_Table = QtGui.QAction(MainWindow)
        self.actionCritical_Value_Lookup_Table.setMenuRole(QtGui.QAction.TextHeuristicRole)
        self.actionCritical_Value_Lookup_Table.setObjectName(_fromUtf8("actionCritical_Value_Lookup_Table"))
        self.actionFixed_Trial_Simulation = QtGui.QAction(MainWindow)
        self.actionFixed_Trial_Simulation.setObjectName(_fromUtf8("actionFixed_Trial_Simulation"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionAbout_2 = QtGui.QAction(MainWindow)
        self.actionAbout_2.setObjectName(_fromUtf8("actionAbout_2"))
        self.actionResult = QtGui.QAction(MainWindow)
        self.actionResult.setObjectName(_fromUtf8("actionResult"))
        self.actionAdaptive_Trial_Simulation = QtGui.QAction(MainWindow)
        self.actionAdaptive_Trial_Simulation.setObjectName(_fromUtf8("actionAdaptive_Trial_Simulation"))
        self.actionClear_Log = QtGui.QAction(MainWindow)
        self.actionClear_Log.setObjectName(_fromUtf8("actionClear_Log"))
        self.menuNew.addAction(self.actionCritical_Value_Lookup_Table)
        self.menuNew.addAction(self.actionFixed_Trial_Simulation)
        self.menuFile.addAction(self.menuNew.menuAction())
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionClose)
        self.menuFile.addAction(self.actionQuit)
        self.menuAbout.addAction(self.actionAbout)
        self.menuAbout.addAction(self.actionAbout_2)
        self.menuView.addAction(self.actionResult)
        self.menuView.addAction(self.actionClear_Log)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.toolBar.addAction(self.actionFixed_Trial_Simulation)
        self.toolBar.addAction(self.actionSave)

        self.retranslateUi(MainWindow)
        self.logConsole_2.setCurrentIndex(0)
        QtCore.QObject.connect(self.actionQuit, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "BCTS", None))
        self.logConsole.setDocumentTitle(_translate("MainWindow", "Log Console", None))
        self.logConsole_2.setTabText(self.logConsole_2.indexOf(self.logTab), _translate("MainWindow", "Log", None))
        self.logConsole_2.setTabText(self.logConsole_2.indexOf(self.resultTab), _translate("MainWindow", "Result Viewer", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuNew.setTitle(_translate("MainWindow", "New", None))
        self.menuAbout.setTitle(_translate("MainWindow", "About", None))
        self.menuView.setTitle(_translate("MainWindow", "Edit", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.toolBar_2.setWindowTitle(_translate("MainWindow", "toolBar_2", None))
        self.actionSave.setText(_translate("MainWindow", "Save", None))
        self.actionClose.setText(_translate("MainWindow", "Close", None))
        self.actionQuit.setText(_translate("MainWindow", "Quit", None))
        self.actionCritical_Value_Lookup_Table.setText(_translate("MainWindow", "Critical Value Lookup Table", None))
        self.actionFixed_Trial_Simulation.setText(_translate("MainWindow", "Fixed Trial Simulation", None))
        self.actionAbout.setText(_translate("MainWindow", "Documentation", None))
        self.actionAbout_2.setText(_translate("MainWindow", "About", None))
        self.actionResult.setText(_translate("MainWindow", "View Result", None))
        self.actionAdaptive_Trial_Simulation.setText(_translate("MainWindow", "Adaptive Trial Simulation", None))
        self.actionClear_Log.setText(_translate("MainWindow", "Clear Log", None))

