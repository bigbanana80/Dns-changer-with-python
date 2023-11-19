from mainui import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import PyQt5
import sys
import psutil

addrs = psutil.net_if_addrs()


# def get_adaptor_list:


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)

for x in addrs.keys():
    ui.comboBox.addItem(x)
ui.comboBox.setCurrentText("Wi-Fi")

MainWindow.show()
sys.exit(app.exec_())
