import sys
from task2.untitled import Ui_MainWindow
from PyQt5 import QtWidgets


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Mainwindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()

    ui.setupUi(Mainwindow)
    Mainwindow.show()
    sys.exit(app.exec_())