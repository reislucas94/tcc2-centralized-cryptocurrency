# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/reisaolucas/Documents/GitHub/tcc2-centralized-cryptocurrency/AddTransactionsWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import Central.PushTransactionToNextBlock as PushTransactionToNextBlock

class Ui_add_transactions_window1(object):
    def setupUi(self, add_transactions_window1):
        add_transactions_window1.setObjectName("add_transactions_window1")
        add_transactions_window1.resize(900, 400)
        self.centralwidget = QtWidgets.QWidget(add_transactions_window1)
        self.centralwidget.setObjectName("centralwidget")
        self.transfered_from_input1 = QtWidgets.QLineEdit(self.centralwidget)
        self.transfered_from_input1.setGeometry(QtCore.QRect(50, 200, 150, 21))
        self.transfered_from_input1.setText("")
        self.transfered_from_input1.setObjectName("transfered_from_input1")
        self.from_label1 = QtWidgets.QLabel(self.centralwidget)
        self.from_label1.setGeometry(QtCore.QRect(50, 180, 60, 16))
        self.from_label1.setObjectName("from_label1")
        self.transfered_to_input1 = QtWidgets.QLineEdit(self.centralwidget)
        self.transfered_to_input1.setGeometry(QtCore.QRect(450, 200, 150, 21))
        self.transfered_to_input1.setObjectName("transfered_to_input1")
        self.amount_transfered_input1 = QtWidgets.QLineEdit(self.centralwidget)
        self.amount_transfered_input1.setGeometry(QtCore.QRect(250, 200, 150, 24))
        self.amount_transfered_input1.setObjectName("amount_transfered_input1")
        self.amount_transfered_input1.setValidator(QtGui.QDoubleValidator(0.0, 99999.99, 2, self.amount_transfered_input1))
        self.amount_transfered_input1
        self.amount_label1 = QtWidgets.QLabel(self.centralwidget)
        self.amount_label1.setGeometry(QtCore.QRect(250, 180, 60, 16))
        self.amount_label1.setObjectName("amount_label1")
        self.to_label1 = QtWidgets.QLabel(self.centralwidget)
        self.to_label1.setGeometry(QtCore.QRect(450, 180, 60, 16))
        self.to_label1.setObjectName("to_label1")
        self.add_transaction_button1 = QtWidgets.QPushButton(self.centralwidget)
        self.add_transaction_button1.setGeometry(QtCore.QRect(640, 195, 200, 32))
        self.add_transaction_button1.setObjectName("add_transaction_button1")
        add_transactions_window1.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(add_transactions_window1)
        self.statusbar.setObjectName("statusbar")
        add_transactions_window1.setStatusBar(self.statusbar)

        self.retranslateUi(add_transactions_window1)
        QtCore.QMetaObject.connectSlotsByName(add_transactions_window1)

        self.add_transaction_button1.clicked.connect(self.openAddTransactionsWindow)

    def retranslateUi(self, add_transactions_window1):
        _translate = QtCore.QCoreApplication.translate
        add_transactions_window1.setWindowTitle(_translate("add_transactions_window1", "Add Transactions"))
        self.from_label1.setText(_translate("add_transactions_window1", "From"))
        self.amount_label1.setText(_translate("add_transactions_window1", "Amount"))
        self.to_label1.setText(_translate("add_transactions_window1", "To"))
        self.add_transaction_button1.setText(_translate("add_transactions_window1", "Add Transaction to Block"))

    def openAddTransactionsWindow(self):
        try:
            PushTransactionToNextBlock.push(self.transfered_from_input1.text(), self.transfered_to_input1.text(), float(self.amount_transfered_input1.text()))
        except:
            pass

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    add_transactions_window1 = QtWidgets.QMainWindow()
    ui = Ui_add_transactions_window1()
    ui.setupUi(add_transactions_window1)
    add_transactions_window1.show()
    sys.exit(app.exec_())
