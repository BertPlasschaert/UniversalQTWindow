from PySide2 import QtWidgets, QtCore
from PySide2 import QtUiTools
import sys

from MainWindow import TestDialog


class BaseWindowManager:

    def __init__(self):
        self.app = None
        self.window = None
        self.MainWindowClass = TestDialog
        self.createWindow()

    def createWindow(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.window = self.MainWindowClass()

    def showWindow(self):
        self.window.show()
        sys.exit(self.app.exec_())
