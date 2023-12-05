__author__ = "Sepehr Aghajani"
__copyright__ = "Copyright 2023, DNS changer with python Project"
__credits__ = ["Sepehr Aghajani"]
__license__ = "GPL"
__version__ = "1.232"
__maintainer__ = "Sepehr Aghajani"
__email__ = "sepehra90@gmail.com"
__status__ = "Finished"

import token
from PyQt5 import QtCore, QtGui, QtWidgets
import PyQt5
import dns.resolver

#######
import sys
import psutil
import json
from os import listdir
from os.path import isfile, join
import os
import time

# dirname = os.path.dirname(__file__)
# filename = os.path.join(dirname, "Configs\\")
# print(filename)
# if not os.path.exists(filename):
#     os.mkdir(filename)
#     time.sleep(3)

#######
# variables that i should not touch (prob) as they are for startup
addrs = psutil.net_if_addrs()
configs = [f for f in listdir("Configs") if isfile(join("Configs", f))]


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
        self.btnbox_k_or_cancel.accepted.connect(self.save_dns)  # type: ignore
        self.btnbox_k_or_cancel.rejected.connect(Dialog.reject)  # type: ignore
        self.btnbox_k_or_cancel.rejected.connect(self.clear)  # type: ignore
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

    def save_dns(self):
        name = self.name_input.text()
        dns1 = self.dns1_input.text()
        dns2 = self.dns2_input.text()
        values = config(name, dns1, dns2)
        values.save_json()
        refresh_list()

    def clear(self):
        dialog_ui.dns1_input.clear()
        dialog_ui.dns2_input.clear()
        dialog_ui.name_input.clear()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(429, 535)
        MainWindow.setMinimumSize(QtCore.QSize(429, 535))
        MainWindow.setMaximumSize(QtCore.QSize(429, 535))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        MainWindow.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        MainWindow.setFont(font)
        MainWindow.setMouseTracking(False)
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        MainWindow.setAcceptDrops(False)
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap("CP - Network and Internet.ico"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(
            "QPushButton{\n"
            "background-color:rgb(255, 255, 127);\n"
            "border: 2px solid black;\n"
            "border-radius:10px;\n"
            "}\n"
            "QPushButton:hover{\n"
            "background-color:rgb(179, 179, 0);\n"
            "}\n"
            "QPushButton:pressed{\n"
            "background-color:rgb(93, 93, 46);\n"
            "border-style:solid;\n"
            "border-width:2px;\n"
            "}\n"
            "\n"
            "QMainWindow{\n"
            "background-color:rgb(0, 0, 0);\n"
            "}\n"
            "\n"
            "QLabel{\n"
            "color: rgb(255, 255, 255);\n"
            "}"
        )
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.list_dns = QtWidgets.QListWidget(self.centralwidget)
        self.list_dns.setGeometry(QtCore.QRect(20, 10, 281, 401))
        self.list_dns.setStyleSheet("")
        self.list_dns.setObjectName("list_dns")
        item = QtWidgets.QListWidgetItem()
        self.list_dns.addItem(item)
        self.btn_flush = QtWidgets.QPushButton(self.centralwidget)
        self.btn_flush.setGeometry(QtCore.QRect(320, 370, 81, 31))
        self.btn_flush.setObjectName("btn_flush")
        self.btn_activate = QtWidgets.QPushButton(self.centralwidget)
        self.btn_activate.setGeometry(QtCore.QRect(320, 330, 81, 31))
        self.btn_activate.setObjectName("btn_activate")
        self.btn_add = QtWidgets.QPushButton(self.centralwidget)
        self.btn_add.setGeometry(QtCore.QRect(320, 60, 81, 31))
        self.btn_add.setObjectName("btn_add")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(320, 20, 81, 22))
        self.comboBox.setStyleSheet(
            "QComboBox{\n" "border:1px;\n" "border-radius: 5px;\n" "}"
        )
        self.comboBox.setObjectName("comboBox")
        self.btn_edit = QtWidgets.QPushButton(self.centralwidget)
        self.btn_edit.setGeometry(QtCore.QRect(320, 100, 81, 31))
        self.btn_edit.setObjectName("btn_edit")
        self.List_dns1 = QtWidgets.QLabel(self.centralwidget)
        self.List_dns1.setGeometry(QtCore.QRect(310, 170, 110, 13))
        self.List_dns1.setObjectName("List_dns1")
        self.List_dns2 = QtWidgets.QLabel(self.centralwidget)
        self.List_dns2.setGeometry(QtCore.QRect(310, 190, 110, 20))
        self.List_dns2.setObjectName("List_dns2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(310, 260, 47, 13))
        self.label_3.setObjectName("label_3")
        self.Active_dns1 = QtWidgets.QLabel(self.centralwidget)
        self.Active_dns1.setGeometry(QtCore.QRect(310, 280, 110, 13))
        self.Active_dns1.setObjectName("Active_dns1")
        self.Active_dns2 = QtWidgets.QLabel(self.centralwidget)
        self.Active_dns2.setGeometry(QtCore.QRect(310, 300, 110, 13))
        self.Active_dns2.setObjectName("Active_dns2")
        self.flush_checkbox = QtWidgets.QCheckBox(self.centralwidget)
        self.flush_checkbox.setGeometry(QtCore.QRect(320, 140, 70, 17))
        self.flush_checkbox.setStyleSheet(
            "QCheckBox{\n" "color: rgb(255, 255, 255);\n" "}"
        )
        self.flush_checkbox.setObjectName("flush_checkbox")
        self.btn_delete = QtWidgets.QPushButton(self.centralwidget)
        self.btn_delete.setGeometry(QtCore.QRect(390, 100, 31, 31))
        self.btn_delete.setObjectName("btn_delete")
        self.log = QtWidgets.QTextBrowser(self.centralwidget)
        self.log.setGeometry(QtCore.QRect(20, 420, 381, 91))
        self.log.setObjectName("log")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 429, 21))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(
            _translate("MainWindow", "DNS Changer by Red Mage v1.25")
        )
        self.list_dns.setSortingEnabled(True)
        __sortingEnabled = self.list_dns.isSortingEnabled()
        self.list_dns.setSortingEnabled(False)
        item = self.list_dns.item(0)
        item.setText(_translate("MainWindow", "Google"))
        self.list_dns.setSortingEnabled(__sortingEnabled)
        self.btn_flush.setText(_translate("MainWindow", "Flush dns"))
        self.btn_activate.setText(_translate("MainWindow", "Activate DNS"))
        self.btn_add.setText(_translate("MainWindow", "Add new dns"))
        self.btn_edit.setText(_translate("MainWindow", "Edit dns"))
        self.List_dns1.setText(_translate("MainWindow", "--"))
        self.List_dns2.setText(_translate("MainWindow", "--"))
        self.label_3.setText(_translate("MainWindow", "Active :"))
        self.Active_dns1.setText(_translate("MainWindow", "DNS 1"))
        self.Active_dns2.setText(_translate("MainWindow", "DNS 2"))
        self.flush_checkbox.setText(_translate("MainWindow", "Auto Flush"))
        self.btn_delete.setText(_translate("MainWindow", "DeL"))

    def connections(self):
        # signals #
        self.btn_add.clicked.connect(add)
        self.btn_edit.clicked.connect(edit)
        self.btn_delete.clicked.connect(delete)
        self.btn_activate.clicked.connect(activate)
        self.btn_flush.clicked.connect(flush)
        self.list_dns.clicked.connect(refresh_selected_dns_labels)
        self.list_dns.doubleClicked.connect(activate)


class config(Ui_MainWindow):
    def __init__(self, name: str, dns1: str, dns2: str) -> None:
        self.name = name
        self.dns1 = dns1
        self.dns2 = dns2

    def save_json(self):
        values = {"name": self.name, "dns1": self.dns1, "dns2": self.dns2}
        with open(f"Configs/{self.name}.json", "w") as file:
            json.dump(values, file, indent=6)
        dialog_ui.dns1_input.clear()
        dialog_ui.dns2_input.clear()
        dialog_ui.name_input.clear()
        ui.log.append(f"file added or modified: {self.name}")
        ###########


def add():
    dialog.show()


def edit():
    if ui.list_dns.currentItem() == None:
        ui.log.append("ERROR: Select one DNS profile")
    else:
        conf = get_dns()
        dialog_ui.name_input.setText(conf.name)
        dialog_ui.dns1_input.setText(conf.dns1)
        dialog_ui.dns2_input.setText(conf.dns2)
        dialog.show()


def delete():
    if ui.list_dns.currentItem() == None:
        ui.log.append("ERROR: Select one DNS profile")
    else:
        conf = get_dns()
        try:
            os.remove(f"Configs/{conf.name}.json")
            ui.log.append(f"File deleted: {conf.name}")
        except:
            print("no such file")
        refresh_list()


def get_dns():
    name = ui.list_dns.currentItem().text()
    with open(f"Configs/{name}.json", "r") as file:
        data: dict = json.load(file)
    conf = config(data["name"], data["dns1"], data["dns2"])
    return conf


def activate():
    if ui.list_dns.currentItem() == None:
        ui.log.append("ERROR: Select one DNS profile")
    else:
        dns = get_dns()
        interface = ui.comboBox.currentText()
        os.system(f'netsh interface ip set dns name="{interface}" static  {dns.dns1}')
        os.system(
            f'netsh interface ip add dns name="{interface}"  {dns.dns2} index="2"'
        )
        if ui.flush_checkbox.isChecked():
            os.system("ipconfig /flushdns")
            ui.log.append("Successfully flushed the DNS Resolver Cache.")
        else:
            pass


def flush():
    os.system("ipconfig /flushdns")
    ui.log.append("Successfully flushed the DNS Resolver Cache.")


def refresh_list():
    configs = [f for f in listdir("Configs") if isfile(join("Configs", f))]
    ui.list_dns.clear()
    for x in configs:
        ui.list_dns.addItem(os.path.splitext(x)[0])


def refresh_selected_dns_labels():
    conf = get_dns()
    ui.List_dns1.setText(f"{conf.dns1}")
    ui.List_dns2.setText(f"{conf.dns2}")


def refresh_active_dns_labels():
    dns_resolver = dns.resolver.Resolver()
    ui.Active_dns1.setText(dns_resolver.nameservers[0])
    ui.Active_dns2.setText(dns_resolver.nameservers[1])


if __name__ == "__main__":
    dns_token = config("", "", "")
    # startup section #
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ###################

    # dialogbox #
    dialog = QtWidgets.QDialog()
    dialog_ui = Ui_Dialog()
    dialog_ui.setup_dialogUi(dialog)
    dialog.hide()
    ############

    # startup tasks thats you probably shouldn't touch #
    for x in addrs.keys():
        ui.comboBox.addItem(x)
    ui.comboBox.setCurrentText("Wi-Fi")

    ui.list_dns.clear()
    for x in configs:
        ui.list_dns.addItem(os.path.splitext(x)[0])
    refresh_active_dns_labels()
    timer = QtCore.QTimer()
    timer.timeout.connect(refresh_active_dns_labels)
    timer.start(10000)
    ###################################################
    ui.connections()
    MainWindow.show()
    sys.exit(app.exec_())
