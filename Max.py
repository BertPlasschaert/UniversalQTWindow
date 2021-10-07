from PySide2 import QtWidgets, QtCore
from qtmax import GetQMaxMainWindow
import shiboken2

from BaseWindowManager import BaseWindowManager

from MainWindow import TestDialog


class WindowManager(BaseWindowManager):

    def __init__(self):
        BaseWindowManager.__init__(self)

    def createWindow(self):
        self.window = TestDialog(GetQMaxMainWindow())

    def showWindow(self):
        self.window.show()