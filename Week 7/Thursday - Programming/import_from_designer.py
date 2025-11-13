from PySide6 import QtCore, QtWidgets, QtGui
import sys
from PySide6.QtWidgets import QApplication, QDialog
from ui_mainwindow import Ui_Dialog

class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    window = MainWindow()
    window.show()

    sys.exit(app.exec())