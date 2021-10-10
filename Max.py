from PySide2 import QtWidgets, QtCore
from qtmax import GetQMaxMainWindow
from pymxs import runtime as mxs

from BaseWindowManager import BaseWindowManager


class WindowManager(BaseWindowManager):

    def __init__(self, Main):
        BaseWindowManager.__init__(self, Main)

    def createWindow(self):
        self.window = self.MainWindowClass(self.Main, parent=GetQMaxMainWindow())

    def showWindow(self):
        self.window.show()


def spawnCylinder():
    mxs.cylinder()
