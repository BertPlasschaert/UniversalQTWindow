from PySide2 import QtWidgets, QtCore
from PySide2 import QtUiTools
import sys

from MainWindow import MainWindow


class BaseWindowManager:

    def __init__(self, Main):
        self.Main = Main
        self.app = None
        self.window = None
        self.MainWindowClass = MainWindow

        self.createWindow()

    def createWindow(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.window = self.MainWindowClass(self.Main, parent=None)

    def showWindow(self):
        self.window.show()
        sys.exit(self.app.exec_())
