from mainui import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import PyQt5
import sys
import psutil
import json
from os import listdir
from os.path import isfile, join
import os

addrs = psutil.net_if_addrs()
configs = [f for f in listdir("Configs") if isfile(join("Configs", f))]

# def get_adaptor_list:


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
