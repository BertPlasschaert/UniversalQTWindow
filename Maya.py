from PySide2 import QtWidgets, QtCore
from PySide2 import QtUiTools
import maya.OpenMayaUI as omui
import shiboken2
import sys

from BaseWindowManager import BaseWindowManager


class WindowManager(BaseWindowManager):

    def __init__(self):
        BaseWindowManager.__init__(self)

    def createWindow(self):
        self.window = self.MainWindowClass(self.getMayaInstance())

    def showWindow(self):
        self.window.show()

    def getMayaInstance(self):
        # type: () -> shiboken2.wrapInstance()

        pointer = omui.MQtUtil.mainWindow()
        if pointer is not None:
            return shiboken2.wrapInstance(long(pointer), QtWidgets.QWidget)