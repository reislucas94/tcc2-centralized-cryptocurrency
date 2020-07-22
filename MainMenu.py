# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/reisaolucas/Documents/GitHub/tcc2-centralized-cryptocurrency/MainMenu.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from AddTransactionsWindow import Ui_add_transactions_window1 as AddTransactionsWindow
from Central.CentralCore import check_blockchain_consistency as check_blockchain_consistency_central_core

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        #Main window
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        #Add Transaction Button
        self.addTransactionsButton = QtWidgets.QPushButton(self.centralwidget)
        self.addTransactionsButton.setGeometry(QtCore.QRect(320, 400, 161, 32))
        self.addTransactionsButton.setObjectName("addTransactionsButton")


        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(310, 110, 341, 91))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")

        #Show blocks button
        self.showBlocksButton = QtWidgets.QPushButton(self.centralwidget)
        self.showBlocksButton.setGeometry(QtCore.QRect(330, 360, 141, 32))
        self.showBlocksButton.setObjectName("showBlocksButton")
        MainWindow.setCentralWidget(self.centralwidget)

        #Check blockchain consistency button
        self.checkBlockchainConsistencyButton = QtWidgets.QPushButton(self.centralwidget)
        self.checkBlockchainConsistencyButton.setGeometry(QtCore.QRect(290, 440, 220, 32))
        self.checkBlockchainConsistencyButton.setObjectName("checkBlockchainConsistencyButton")
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
        self.checkBlockchainConsistencyButton.clicked.connect(self.checkBlockchainConsistency)
        self.showBlocksButton.clicked.connect(self.showBlocks)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.addTransactionsButton.setText(_translate("MainWindow", "Add Transactions"))
        self.label.setText(_translate("MainWindow", "Centralized Blockchain"))
        self.showBlocksButton.setText(_translate("MainWindow", "Show All Blocks"))
        self.checkBlockchainConsistencyButton.setText(_translate("MainWindow", "Check Blockchain Consistency"))

    def openAddTransactionsWindow(self):
        print ("Opening AddTransactionsWindow ...")
        self.window = QtWidgets.QMainWindow()
        self.ui = AddTransactionsWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def checkBlockchainConsistency(self): 
        try:
            check_blockchain_consistency_central_core()
            success_dialog_check_consistency = QtWidgets.QMessageBox()
            success_dialog_check_consistency.setText('All blocks have been checked and they are all valid.')
            success_dialog_check_consistency.exec_()
        except Exception as ex:
            error_dialog_check_consistency = QtWidgets.QErrorMessage()
            error_dialog_check_consistency.showMessage(str(ex))
            error_dialog_check_consistency.exec_()

    def showBlocks(self):
        import os
        import subprocess
        path = "./Central/Databases/Blocks"
        os.system('open "%s"' % path)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
