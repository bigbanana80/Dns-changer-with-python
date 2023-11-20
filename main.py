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


class config(Ui_MainWindow, Ui_Dialog):
    def __init__(self, name: str, dns1: str, dns2: str) -> None:
        super(config, self).__init__()
        self.name = name
        self.dns1 = dns1
        self.dns2 = dns2

    def save_json(self):
        values = {"name": self.name, "dns1": self.dns1, "dns2": self.dns2}
        with open(f"Configs/{self.name}.json", "w") as file:
            json.dump(values, file, indent=6)


# startup section
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)

for x in addrs.keys():
    ui.comboBox.addItem(x)
ui.comboBox.setCurrentText("Wi-Fi")

ui.list_dns.clear()
for x in configs:
    ui.list_dns.addItem(os.path.splitext(x)[0])

MainWindow.show()
sys.exit(app.exec_())
