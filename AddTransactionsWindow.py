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
import json

XSIZE = 1200
YSIZE = 800



class Ui_add_transactions_window1(object):
    def setupUi(self, add_transactions_window1):
        add_transactions_window1.setObjectName("add_transactions_window1")
        add_transactions_window1.resize(XSIZE, YSIZE)
        self.init_has_been_added = False
        self.centralwidget = QtWidgets.QWidget(add_transactions_window1)
        self.centralwidget.setObjectName("centralwidget")

        #### Init Destination Label ####
        self.init_dest_label1 = QtWidgets.QLabel(self.centralwidget)
        self.init_dest_label1.setGeometry(QtCore.QRect(50, 70, 100, 16))
        self.init_dest_label1.setObjectName("init_dest_label1")

        #### Init Destination Field ####
        self.init_dest_input1 = QtWidgets.QLineEdit(self.centralwidget)
        self.init_dest_input1.setGeometry(QtCore.QRect(50, 90, 150, 21))
        self.init_dest_input1.setText("17040189003")
        self.init_dest_input1.setObjectName("transfered_from_input1")

        #### Init Value Label ####
        self.init_value_label1 = QtWidgets.QLabel(self.centralwidget)
        self.init_value_label1.setGeometry(QtCore.QRect(250, 70, 60, 16))
        self.init_value_label1.setObjectName("init_value_label1")

        #### Init Value Field ####
        self.init_value_input1 = QtWidgets.QLineEdit(self.centralwidget)
        self.init_value_input1.setGeometry(QtCore.QRect(250, 90, 150, 24))
        self.init_value_input1.setObjectName("amount_transfered_input1")
        self.init_value_input1.setValidator(QtGui.QDoubleValidator(0.0, 99999.99, 2, self.init_value_input1))

        #### Add Init Button #### 
        self.add_init_button1 = QtWidgets.QPushButton(self.centralwidget)
        self.add_init_button1.setGeometry(QtCore.QRect(450, 85, 200, 32))
        self.add_init_button1.setObjectName("add_init_button1")

        #### From Label #### 
        self.from_label1 = QtWidgets.QLabel(self.centralwidget)
        self.from_label1.setGeometry(QtCore.QRect(50, 180, 60, 16))
        self.from_label1.setObjectName("from_label1")

        #### From Field
        self.transfered_from_input1 = QtWidgets.QLineEdit(self.centralwidget)
        self.transfered_from_input1.setGeometry(QtCore.QRect(50, 200, 150, 21))
        self.transfered_from_input1.setText("17040189003")
        self.transfered_from_input1.setObjectName("transfered_from_input1")

        #### Amount Label #### 
        self.amount_label1 = QtWidgets.QLabel(self.centralwidget)
        self.amount_label1.setGeometry(QtCore.QRect(250, 180, 60, 16))
        self.amount_label1.setObjectName("amount_label1")

        #### Amount Field #### 
        self.amount_transfered_input1 = QtWidgets.QLineEdit(self.centralwidget)
        self.amount_transfered_input1.setGeometry(QtCore.QRect(250, 200, 150, 24))
        self.amount_transfered_input1.setObjectName("amount_transfered_input1")
        self.amount_transfered_input1.setValidator(QtGui.QDoubleValidator(0.0, 99999.99, 2, self.amount_transfered_input1))

        #### To Label #### 
        self.to_label1 = QtWidgets.QLabel(self.centralwidget)
        self.to_label1.setGeometry(QtCore.QRect(450, 180, 60, 16))
        self.to_label1.setObjectName("to_label1")
        
        #### To Field #### 
        self.transfered_to_input1 = QtWidgets.QLineEdit(self.centralwidget)
        self.transfered_to_input1.setGeometry(QtCore.QRect(450, 200, 150, 21))
        self.transfered_to_input1.setText("39620880080")
        self.transfered_to_input1.setObjectName("transfered_to_input1")

        #### Add Transaction Button #### 
        self.add_transaction_button1 = QtWidgets.QPushButton(self.centralwidget)
        self.add_transaction_button1.setGeometry(QtCore.QRect(640, 195, 200, 32))
        self.add_transaction_button1.setObjectName("add_transaction_button1")

        #### Text Area Label ####
        self.current_block_label1 = QtWidgets.QLabel(self.centralwidget)
        self.current_block_label1.setGeometry(QtCore.QRect(50, 250, 100, 16))
        self.current_block_label1.setObjectName("current_block_label1")

        #### Text Area #### 
        self.current_block_textarea = QtWidgets.QTextEdit(self.centralwidget)
        self.current_block_textarea.setReadOnly(True)
        self.current_block_textarea.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.log_font = self.current_block_textarea.font()
        self.log_font.setFamily("Courier")
        self.log_font.setPointSize(10)
        self.current_block_textarea.setGeometry(QtCore.QRect(50, 280, XSIZE-2*50, YSIZE-350))
        self.current_block_textarea.setText("Empty.")


        self.cancel_button1 = QtWidgets.QPushButton(self.centralwidget)
        self.cancel_button1.setGeometry(QtCore.QRect(950, 730, 100, 32))
        self.cancel_button1.setObjectName("cancel_button1")

        self.push_block_button1 = QtWidgets.QPushButton(self.centralwidget)
        self.push_block_button1.setGeometry(QtCore.QRect(1050, 730, 100, 32))
        self.push_block_button1.setObjectName("push_block_button1")


        add_transactions_window1.setCentralWidget(self.centralwidget)

        self.statusbar = QtWidgets.QStatusBar(add_transactions_window1)
        self.statusbar.setObjectName("statusbar")
        add_transactions_window1.setStatusBar(self.statusbar)

        self.retranslateUi(add_transactions_window1)
        QtCore.QMetaObject.connectSlotsByName(add_transactions_window1)

        self.add_transactions_window1 = add_transactions_window1

        self.add_init_button1.clicked.connect(self.clickedAddInit)

        self.add_transaction_button1.clicked.connect(self.clickedAddTransaction)

        self.push_block_button1.clicked.connect(self.clickedPushBlock)

        self.cancel_button1.clicked.connect(self.clickedCancel)

    def retranslateUi(self, add_transactions_window1):
        _translate = QtCore.QCoreApplication.translate
        add_transactions_window1.setWindowTitle(_translate("add_transactions_window1", "Add Transactions"))
        self.init_dest_label1.setText(_translate("add_transactions_window1", "Init Destination"))
        self.init_value_label1.setText(_translate("add_transactions_window1", "Init Value"))
        self.add_init_button1.setText(_translate("add_transactions_window1", "Add Init to Block"))
        self.from_label1.setText(_translate("add_transactions_window1", "From"))
        self.amount_label1.setText(_translate("add_transactions_window1", "Amount"))
        self.to_label1.setText(_translate("add_transactions_window1", "To"))
        self.add_transaction_button1.setText(_translate("add_transactions_window1", "Add Transaction to Block"))
        self.current_block_label1.setText(_translate("add_transactions_window1", "Current Block:"))
        self.push_block_button1.setText(_translate("push_block_button1", "Push Block"))
        self.cancel_button1.setText(_translate("cancel_button1", "Cancel"))
        
    def clickedAddInit(self):
        try:
            if PushTransactionToNextBlock._check_if_valid_account(self.init_dest_input1.text()) and \
                float(self.init_value_input1.text()) > 0:

                PushTransactionToNextBlock.CURRENT_BLOCK_INIT_DESTINATION = self.init_dest_input1.text()
                PushTransactionToNextBlock.CURRENT_BLOCK_INIT_VALUE = float(self.init_value_input1.text())

                self.init_dest_input1.setDisabled(True)
                self.init_value_input1.setDisabled(True)
                self.add_init_button1.setDisabled(True)

                self.init_has_been_added = True

                self.add_transactions_window1.repaint()


        except Exception as ex:
            error_dialog_add_init = QtWidgets.QErrorMessage()
            error_dialog_add_init.showMessage(str(ex))
            error_dialog_add_init.exec_()

    def clickedAddTransaction(self):
        try:
            if PushTransactionToNextBlock._check_if_valid_account(self.transfered_from_input1.text()) and \
                PushTransactionToNextBlock._check_if_valid_account(self.transfered_to_input1.text()):

                tx = form_transaction(time.time(), self.transfered_from_input1.text(), float(self.amount_transfered_input1.text()), self.transfered_to_input1.text())

                PushTransactionToNextBlock.push_transaction(tx, Transaction(tx).get_sender_idn(), Transaction(tx).get_receiver_idn(), Transaction(tx).get_amount_transfered(), sign_transaction(tx))
        
                if json.dumps(PushTransactionToNextBlock.CURRENT_BLOCK_TRANSACTIONS) != '':
                    self.current_block_textarea.setText(json.dumps(PushTransactionToNextBlock.CURRENT_BLOCK_TRANSACTIONS, indent=4, sort_keys=True))
                    self.add_transactions_window1.repaint()
        except Exception as ex:
            error_dialog_add_transaction = QtWidgets.QErrorMessage()
            error_dialog_add_transaction.showMessage(str(ex))
            error_dialog_add_transaction.exec_()

    def clickedPushBlock(self):
        try:
            if len(PushTransactionToNextBlock.CURRENT_BLOCK_TRANSACTIONS) > 0 and \
                self.init_has_been_added:
                
                PushTransactionToNextBlock.push_block()
                
                self.add_transactions_window1.repaint()

                success_dialog_pushed_block = QtWidgets.QMessageBox()
                success_dialog_pushed_block.setText('The block has been successfully pushed to the Blockchain.')
                success_dialog_pushed_block.exec_()

                self.add_transactions_window1.close()

        except Exception as ex:
            error_dialog_clicked_push = QtWidgets.QErrorMessage()
            error_dialog_clicked_push.showMessage(str(ex))
            error_dialog_clicked_push.exec_()

    def clickedCancel(self):
        self.add_transactions_window1.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    add_transactions_window1 = QtWidgets.QMainWindow()
    ui = Ui_add_transactions_window1()
    ui.setupUi(add_transactions_window1)
    add_transactions_window1.show()
    sys.exit(app.exec_())
