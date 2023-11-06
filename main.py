import sys
from PyQt5 import QtWidgets
from model import elevate_expression
from view import MainWindow
from controler import CalculatorController

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = MainWindow()
    ui.setupUi(window)
    window.show()

    CalculatorController(model=elevate_expression, view=ui)

    sys.exit(app.exec_())
