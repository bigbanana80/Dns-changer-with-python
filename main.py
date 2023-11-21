import token
from mainui import Ui_MainWindow
from dialogbox import Ui_Dialog
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


class config:
    def __init__(self, name: str, dns1: str, dns2: str) -> None:
        self.name = name
        self.dns1 = dns1
        self.dns2 = dns2

    def save_json(self):
        values = {"name": self.name, "dns1": self.dns1, "dns2": self.dns2}
        with open(f"Configs/{self.name}.json", "w") as file:
            json.dump(values, file, indent=6)


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

# signals #
ui.btn_add.pressed.connect(add)
ui.btn_edit.pressed.connect(edit)
ui.btn_delete.pressed.connect(delete)
ui.btn_activate.pressed.connect(activate(get_dns(ui.list_dns), ui.comboBox.currentText))
ui.btn_flush.pressed.connect(flush)
###########

MainWindow.show()
sys.exit(app.exec_())
