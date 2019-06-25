# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import gc

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtSvg import QSvgRenderer, QSvgWidget
from PyQt5.QtWidgets import QDialog, QFileDialog, QMessageBox

from engine import CoolParser, tokenizer

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModal)
        MainWindow.resize(1280, 728)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/Qt.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.tabWidget.setFont(font)
        self.tabWidget.setMouseTracking(False)
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setObjectName("tabWidget")
        #
        # Code Tab
        # 
        self.tabCode = QtWidgets.QWidget()
        self.tabCode.setObjectName("tabCode")
        self.gridLayout = QtWidgets.QGridLayout(self.tabCode)
        self.gridLayout.setObjectName("gridLayout")
        self.textEditCode = QtWidgets.QPlainTextEdit(self.tabCode)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.textEditCode.setFont(font)
        self.textEditCode.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.textEditCode.setPlainText("")
        self.textEditCode.setObjectName("textEditCode")
        self.gridLayout.addWidget(self.textEditCode, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tabCode, "")
        #
        # AST Tab
        #
        self.tabAST = QtWidgets.QWidget()
        self.tabAST.setObjectName("tabAST")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tabAST)
        self.gridLayout_3.setObjectName("gridLayout_3")
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(15)
        self.textAST = QtWidgets.QTextBrowser(self.tabAST)
        self.textAST.setObjectName("textAST")
        self.textAST.setFont(font)
        self.gridLayout_3.addWidget(self.textAST, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tabAST, "")
        #
        # Collector Tab
        #
        self.tabCollector = QtWidgets.QWidget()
        self.tabCollector.setObjectName("tabCollector")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tabCollector)
        self.gridLayout_4.setObjectName("gridLayout_4")
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(15)
        self.textCollector = QtWidgets.QTextBrowser(self.tabCollector)
        self.textCollector.setObjectName("textCollector")
        self.textCollector.setFont(font)
        self.gridLayout_4.addWidget(self.textCollector, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tabCollector, "")
        #
        # Builder Tab
        #
        self.tabBuilder = QtWidgets.QWidget()
        self.tabBuilder.setObjectName("tabBuilder")
        self.gridLayout_1 = QtWidgets.QGridLayout(self.tabBuilder)
        self.gridLayout_1.setObjectName("gridLayout_1")
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(15)
        self.textBuilder = QtWidgets.QTextBrowser(self.tabBuilder)
        self.textBuilder.setObjectName("textBuilder")
        self.textBuilder.setFont(font)
        self.gridLayout_1.addWidget(self.textBuilder, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tabBuilder, "")
        #
        # Checker Tab
        # 
        self.tabChecker = QtWidgets.QWidget()
        self.tabChecker.setObjectName("tabChecker")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tabChecker)
        self.gridLayout_5.setObjectName("gridLayout_5")
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(15)
        self.textChecker = QtWidgets.QTextBrowser(self.tabChecker)
        self.textChecker.setObjectName("textChecker")
        self.textChecker.setFont(font)
        self.gridLayout_5.addWidget(self.textChecker, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tabChecker, "")
        #
        # Inferer Tab 
        #
        self.tabInferer = QtWidgets.QWidget()
        self.tabInferer.setObjectName("tabInferer")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tabInferer)
        self.gridLayout_6.setObjectName("gridLayout_6")
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(15)
        self.textInferer = QtWidgets.QTextBrowser(self.tabInferer)
        self.textInferer.setObjectName("textInferer")
        self.textInferer.setFont(font)
        self.gridLayout_6.addWidget(self.textInferer, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tabInferer, "")
        # end add tabs

        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.statusbar.setFont(font)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolBar.sizePolicy().hasHeightForWidth())
        self.toolBar.setSizePolicy(sizePolicy)
        self.toolBar.setMinimumSize(QtCore.QSize(795, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.toolBar.setFont(font)
        self.toolBar.setMovable(False)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionNewCode = QtWidgets.QAction(MainWindow)
        self.actionNewCode.setObjectName("actionNewCode")
        self.actionSaveCode = QtWidgets.QAction(MainWindow)
        self.actionSaveCode.setObjectName("actionSaveCode")
        self.actionLoadCode = QtWidgets.QAction(MainWindow)
        self.actionLoadCode.setObjectName("actionLoadCode")
        self.actionExit = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/arrow-000.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon1)
        self.actionExit.setObjectName("actionExit")
        self.actionSaveCodeAs = QtWidgets.QAction(MainWindow)
        self.actionSaveCodeAs.setObjectName("actionSaveCodeAs")
        self.actionAnalyse = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.actionAnalyse.setObjectName("actionAnalyse")
        self.toolBar.addAction(self.actionAnalyse)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionNewCode)
        self.toolBar.addAction(self.actionLoadCode)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionSaveCode)
        self.toolBar.addAction(self.actionSaveCodeAs)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # my vars
        self.tabs = {}
        self._code = ''
        #

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Proyecto de Compilación II"))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tabCode), _translate("MainWindow", "Código")
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tabAST), _translate("MainWindow", "AST")
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tabCollector), _translate("MainWindow", "Collector")
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tabBuilder), _translate("MainWindow", "Builder")
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tabChecker), _translate("MainWindow", "Checker")
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tabInferer), _translate("MainWindow", "Inferer")
        )
        self.toolBar.setWindowTitle(_translate("MainWindow", "Herramientas"))
        self.actionNewCode.setText(_translate("MainWindow", "Nuevo"))
        self.actionNewCode.setStatusTip(_translate("MainWindow", "Nuevo"))
        self.actionNewCode.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionSaveCode.setText(_translate("MainWindow", "&Guardar"))
        self.actionSaveCode.setStatusTip(_translate("MainWindow", "Guardar"))
        self.actionSaveCode.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionLoadCode.setText(_translate("MainWindow", "&Cargar"))
        self.actionLoadCode.setStatusTip(_translate("MainWindow", "Cargar"))
        self.actionLoadCode.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionExit.setText(_translate("MainWindow", "&Salir"))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+F4"))
        self.actionSaveCodeAs.setText(_translate("MainWindow", "Guardar como ..."))
        self.actionSaveCodeAs.setStatusTip(_translate("MainWindow", "Guardar como"))
        self.actionSaveCodeAs.setShortcut(_translate("MainWindow", "Ctrl+Shift+S"))
        self.actionAnalyse.setText(_translate("MainWindow", "Analizar"))
        self.actionAnalyse.setToolTip(_translate("MainWindow", "Analizar"))
        self.actionAnalyse.setStatusTip(_translate("MainWindow", "Analizar"))
        self.actionAnalyse.setShortcut(_translate("MainWindow", "F5"))

    # utils funcs
    def _dialog(self, s, icon):
        dlg = QMessageBox(self)
        dlg.setText(s)
        dlg.setIcon(icon)
        dlg.show()

    def dialog_critical(self, s):
        self._dialog(s, QMessageBox.Critical)

    def dialog_warning(self, s):
        self._dialog(s, QMessageBox.Warning)

    @property
    def get_ready(self):
        try:
            self.parse, self.operations = None,None
            tokens = tokenizer(self.textEditCode.toPlainText())
            self.parse, self.operations = CoolParser(tokens)
        except:
            return None
        return self.operations

    def create_slot(self, name, info):
        _translate = QtCore.QCoreApplication.translate
        # create tab
        tab = QtWidgets.QWidget()
        tab.setObjectName(f"tab{name}")
        grid = QtWidgets.QGridLayout(tab)
        grid.setObjectName(f"grid{name}")
        self.tabWidget.addTab(tab, "")

        # add tab
        self.tabs[name] = [tab, grid, None]
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tabInferer) + len(self.tabs),
            _translate("MainWindow", name),
        )
        self.tabs[name][2] = QtWidgets.QTextBrowser(self.tabs[name][0])
        self.tabs[name][2].setObjectName(f"textBrowser{name}")
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(15)
        self.tabs[name][2].setFont(font)
        self.tabs[name][1].addWidget(self.textInferer, 0, 0, 1, 1)
        

    def _close_adicional_tabs(self):
        count = len(self.tabs)
        while count:
            self.tabWidget.removeTab(self.tabWidget.indexOf(self.tabInferer) + count)
            count -= 1

        for tab, _,tex_brows in self.tabs.values():
            tex_brows.deleteLater()
            del tex_brows

            tab.close()
            tab.deleteLater()
            del tab

        del self.tabs
        gc.collect()
        self.tabs = {}


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
