# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/reisaolucas/Documents/GitHub/tcc2-centralized-cryptocurrency/MainMenu.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from AddTransactionsWindow import Ui_add_transactions_window1 as AddTransactionsWindow

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.addTransactionsButton = QtWidgets.QPushButton(self.centralwidget)
        self.addTransactionsButton.setGeometry(QtCore.QRect(320, 400, 161, 32))
        self.addTransactionsButton.setObjectName("addTransactionsButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(310, 110, 341, 91))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(330, 360, 141, 32))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.addTransactionsButton.clicked.connect(self.openAddTransactionsWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.addTransactionsButton.setText(_translate("MainWindow", "Add Transactions"))
        self.label.setText(_translate("MainWindow", "Centralized Blockchain"))
        self.pushButton.setText(_translate("MainWindow", "Show All Blocks"))

    def openAddTransactionsWindow(self):
        print ("Opening AddTransactionsWindow ...")
        self.window = QtWidgets.QMainWindow()
        self.ui = AddTransactionsWindow()
        self.ui.setupUi(self.window)
        self.window.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
