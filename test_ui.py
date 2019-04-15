import sys
from firstry import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Mainwindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()

    ui.setupUi(Mainwindow)
    Mainwindow.show()
    sys.exit(app.exec_())