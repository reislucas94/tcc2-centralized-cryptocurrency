# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/reisaolucas/Documents/GitHub/tcc2-centralized-cryptocurrency/MainMenu.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from AddTransactionsWindow import Ui_add_transactions_window1 as AddTransactionsWindow
from Central.CentralCore import check_blockchain_consistency as check_blockchain_consistency_central_core
from Central.CentralCore import check_all_balances as check_all_balances

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        #Main window
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")


        #Label centralized blockchain
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 110, 350, 90))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")

        #Show blocks button
        self.showBlocksButton = QtWidgets.QPushButton(self.centralwidget)
        self.showBlocksButton.setGeometry(QtCore.QRect(300, 360, 200, 32))
        self.showBlocksButton.setObjectName("showBlocksButton")

        #Add Transaction Button
        self.addTransactionsButton = QtWidgets.QPushButton(self.centralwidget)
        self.addTransactionsButton.setGeometry(QtCore.QRect(300, 400, 200, 32))
        self.addTransactionsButton.setObjectName("addTransactionsButton")

        #Check blockchain consistency button
        self.checkBlockchainConsistencyButton = QtWidgets.QPushButton(self.centralwidget)
        self.checkBlockchainConsistencyButton.setGeometry(QtCore.QRect(300, 440, 200, 32))
        self.checkBlockchainConsistencyButton.setObjectName("checkBlockchainConsistencyButton")


        #Check all account balances
        self.showAllBalancesButton = QtWidgets.QPushButton(self.centralwidget)
        self.showAllBalancesButton.setGeometry(QtCore.QRect(300, 480, 200, 32))
        self.showAllBalancesButton.setObjectName("showAllBalancesButton")
        
        MainWindow.setCentralWidget(self.centralwidget)

        #StatusBar
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        #Set names to buttons/labels
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.addTransactionsButton.clicked.connect(self.openAddTransactionsWindow)
        self.checkBlockchainConsistencyButton.clicked.connect(self.checkBlockchainConsistency)
        self.showBlocksButton.clicked.connect(self.showBlocks)
        self.showAllBalancesButton.clicked.connect(self.showAccountBalance)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.addTransactionsButton.setText(_translate("MainWindow", "Add Transactions"))
        self.label.setText(_translate("MainWindow", "Centralized Blockchain"))
        self.showBlocksButton.setText(_translate("MainWindow", "Show All Blocks"))
        self.checkBlockchainConsistencyButton.setText(_translate("MainWindow", "Check Blockchain Consistency"))
        self.showAllBalancesButton.setText(_translate("MainWindow", "Show All Balances"))

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
        if os.name == 'nt':
            import subprocess
            import pathlib
            basepath = pathlib.Path().absolute()
            subprocess.Popen('explorer "%s"' % str(basepath)+'\\Central\\Databases\\Blocks')
        else:
            path = "./Central/Databases/Blocks"
            os.system('open "%s"' % path)

    def showAccountBalance(self):
        try:
            check_all_balances()
        except Exception as ex:
            error_dialog_show_account_balance = QtWidgets.QErrorMessage()
            error_dialog_show_account_balance.showMessage(str(ex))
            error_dialog_show_account_balance.exec_()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
