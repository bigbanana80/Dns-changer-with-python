# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialogbox.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setup_dialogUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(248, 251)
        Dialog.setStyleSheet(
            "QDialog{\n"
            "color:rgb(255, 255, 255);\n"
            "background-color:rgb(0, 0, 0)\n"
            "}\n"
            "QLabel{\n"
            "color:rgb(255, 255, 255);\n"
            "}"
        )
        self.btnbox_k_or_cancel = QtWidgets.QDialogButtonBox(Dialog)
        self.btnbox_k_or_cancel.setGeometry(QtCore.QRect(60, 210, 161, 32))
        self.btnbox_k_or_cancel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnbox_k_or_cancel.setAutoFillBackground(False)
        self.btnbox_k_or_cancel.setOrientation(QtCore.Qt.Horizontal)
        self.btnbox_k_or_cancel.setStandardButtons(
            QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok
        )
        self.btnbox_k_or_cancel.setObjectName("btnbox_k_or_cancel")
        self.name_input = QtWidgets.QLineEdit(Dialog)
        self.name_input.setGeometry(QtCore.QRect(90, 50, 113, 20))
        self.name_input.setObjectName("name_input")
        self.dns1_input = QtWidgets.QLineEdit(Dialog)
        self.dns1_input.setGeometry(QtCore.QRect(90, 100, 113, 20))
        self.dns1_input.setObjectName("dns1_input")
        self.dns2_input = QtWidgets.QLineEdit(Dialog)
        self.dns2_input.setGeometry(QtCore.QRect(90, 150, 113, 20))
        self.dns2_input.setObjectName("dns2_input")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 50, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 100, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 150, 47, 13))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(30, 10, 201, 31))
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Dialog)
        self.btnbox_k_or_cancel.accepted.connect(Dialog.accept)  # type: ignore
        self.btnbox_k_or_cancel.rejected.connect(Dialog.reject)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Name :"))
        self.label_2.setText(_translate("Dialog", "1st DNS :"))
        self.label_3.setText(_translate("Dialog", "2nd DNS :"))
        self.label_4.setText(
            _translate("Dialog", 'Don\'t forget to write dns in "# . # . # . #" ')
        )


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setup_dialogUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())