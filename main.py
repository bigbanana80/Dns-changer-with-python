import token
from PyQt5 import QtCore, QtGui, QtWidgets
import PyQt5

#######
import sys
import psutil
import json
from os import listdir
from os.path import isfile, join
import os

#######
# variables that i should i not touch (prob) as they are for startup
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


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(429, 435)
        MainWindow.setMinimumSize(QtCore.QSize(429, 435))
        MainWindow.setMaximumSize(QtCore.QSize(429, 435))
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
            QtGui.QPixmap(
                "../../../Users/PC/OneDrive/Pictures/Icons/Windows office pro/CP - Network and Internet.ico"
            ),
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
        self.List_dns1.setGeometry(QtCore.QRect(310, 170, 47, 13))
        self.List_dns1.setObjectName("List_dns1")
        self.List_dns2 = QtWidgets.QLabel(self.centralwidget)
        self.List_dns2.setGeometry(QtCore.QRect(310, 190, 41, 20))
        self.List_dns2.setObjectName("List_dns2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(310, 260, 47, 13))
        self.label_3.setObjectName("label_3")
        self.Active_dns1 = QtWidgets.QLabel(self.centralwidget)
        self.Active_dns1.setGeometry(QtCore.QRect(310, 280, 47, 13))
        self.Active_dns1.setObjectName("Active_dns1")
        self.Active_dns2 = QtWidgets.QLabel(self.centralwidget)
        self.Active_dns2.setGeometry(QtCore.QRect(310, 300, 47, 13))
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
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 429, 21))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DNS Changer by Red Mage"))
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
        self.List_dns1.setText(_translate("MainWindow", "DNS 1 :"))
        self.List_dns2.setText(_translate("MainWindow", "DNS 2 :"))
        self.label_3.setText(_translate("MainWindow", "Active :"))
        self.Active_dns1.setText(_translate("MainWindow", "DNS 1"))
        self.Active_dns2.setText(_translate("MainWindow", "DNS 1"))
        self.flush_checkbox.setText(_translate("MainWindow", "Auto Flush"))
        self.btn_delete.setText(_translate("MainWindow", "DeL"))

    def connections(self):
        # signals #
        self.btn_add.clicked.connect(add)
        self.btn_edit.clicked.connect(edit)
        self.btn_delete.clicked.connect(delete)
        self.btn_activate.clicked.connect(
            activate(get_dns(self.list_dns), self.comboBox.currentText)
        )
        self.btn_flush.clicked.connect(flush)


class config(Ui_MainWindow):
    def __init__(self, name: str, dns1: str, dns2: str) -> None:
        self.name = name
        self.dns1 = dns1
        self.dns2 = dns2

    def save_json(self):
        values = {"name": self.name, "dns1": self.dns1, "dns2": self.dns2}
        with open(f"Configs/{self.name}.json", "w") as file:
            json.dump(values, file, indent=6)

        ###########


def add():
    dialog.show()


def edit():
    print("edit")


def delete():
    print("delete")


def get_dns(list_dns: QtWidgets.QListWidget):
    name = list_dns.currentItem().text()
    with open(f"Configs/{name}.json", "r") as file:
        data: dict = json.load(file)
    conf = config(data["name"], data["dns1"], data["dns2"])
    return conf


def activate(dns: config, interface):
    os.system(f'netsh interface ip set dns name="{interface}" static  {dns.dns1}')
    os.system(f'netsh interface ip add dns name="{interface}"  {dns.dns2} index="2"')
    os.system("ipconfig /flushdns")


def flush():
    os.system("ipconfig /flushdns")


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
###################################################
ui.btn_activate.setDisabled(True)
ui.connections()
MainWindow.show()
sys.exit(app.exec_())
