from mainui import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import PyQt5
import sys


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())
