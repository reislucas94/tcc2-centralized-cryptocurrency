# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/reisaolucas/Documents/GitHub/tcc2-centralized-cryptocurrency/AddTransactionsWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import Central.PushTransactionToNextBlock as PushTransactionToNextBlock
from Central.CentralCore import form_transaction as form_transaction
from Central.CentralCore import sign_transaction as sign_transaction
import time
from Central.Entities.Transaction import Transaction as Transaction

XSIZE = 1200
YSIZE = 800

class Ui_add_transactions_window1(object):
    def setupUi(self, add_transactions_window1):
        add_transactions_window1.setObjectName("add_transactions_window1")
        add_transactions_window1.resize(XSIZE, YSIZE)
        self.centralwidget = QtWidgets.QWidget(add_transactions_window1)
        self.centralwidget.setObjectName("centralwidget")

        self.transfered_from_input1 = QtWidgets.QLineEdit(self.centralwidget)
        self.transfered_from_input1.setGeometry(QtCore.QRect(50, 200, 150, 21))
        self.transfered_from_input1.setText("39620880080")
        self.transfered_from_input1.setObjectName("transfered_from_input1")

        self.from_label1 = QtWidgets.QLabel(self.centralwidget)
        self.from_label1.setGeometry(QtCore.QRect(50, 180, 60, 16))
        self.from_label1.setObjectName("from_label1")

        self.amount_transfered_input1 = QtWidgets.QLineEdit(self.centralwidget)
        self.amount_transfered_input1.setGeometry(QtCore.QRect(250, 200, 150, 24))
        self.amount_transfered_input1.setObjectName("amount_transfered_input1")
        self.amount_transfered_input1.setValidator(QtGui.QDoubleValidator(0.0, 99999.99, 2, self.amount_transfered_input1))

        self.transfered_to_input1 = QtWidgets.QLineEdit(self.centralwidget)
        self.transfered_to_input1.setGeometry(QtCore.QRect(450, 200, 150, 21))
        self.transfered_to_input1.setText("17040189003")
        self.transfered_to_input1.setObjectName("transfered_to_input1")

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


        #### TEXT AREA #### 
        self.current_block_textarea = QtWidgets.QTextEdit(self.centralwidget)
        self.current_block_textarea.setReadOnly(True)
        self.current_block_textarea.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.log_font = self.current_block_textarea.font()
        self.log_font.setFamily("Courier")
        self.log_font.setPointSize(10)
        self.current_block_textarea.setGeometry(QtCore.QRect(50, 250, XSIZE-2*50, 100))
        self.current_block_textarea.setText("Empty.")


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
            if PushTransactionToNextBlock._check_if_valid_account(self.transfered_from_input1.text()) and \
                PushTransactionToNextBlock._check_if_valid_account(self.transfered_to_input1.text()):

                tx = form_transaction(time.time(), self.transfered_from_input1.text(), float(self.amount_transfered_input1.text()), self.transfered_to_input1.text())

                PushTransactionToNextBlock.push(Transaction(tx).get_sender_idn(), Transaction(tx).get_receiver_idn(), Transaction(tx).get_amount_transfered(), sign_transaction(tx))
        except Exception as ex:
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage(str(ex))
            error_dialog.exec_()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    add_transactions_window1 = QtWidgets.QMainWindow()
    ui = Ui_add_transactions_window1()
    ui.setupUi(add_transactions_window1)
    add_transactions_window1.show()
    sys.exit(app.exec_())
