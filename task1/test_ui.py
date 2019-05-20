import sys
import unittest
from PyQt5 import QtWidgets
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt
import firstry

# Dont finish, will not finish maybe.

def test_defaults(self):
    ok = self.pushButton_5
    QTest.mouseClick(ok,Qt.LeftButton)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Mainwindow = QtWidgets.QMainWindow()
    ui = firstry.Ui_MainWindow()

    ui.setupUi(Mainwindow)
    sys.exit(app.exec_())