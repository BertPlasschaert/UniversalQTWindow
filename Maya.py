from PySide2 import QtWidgets, QtCore
from PySide2 import QtUiTools
import maya.OpenMayaUI as omui
import shiboken2

import maya.cmds as cmds

from BaseWindowManager import BaseWindowManager


class WindowManager(BaseWindowManager):

    def __init__(self, Main):
        BaseWindowManager.__init__(self, Main)

    def createWindow(self):
        self.window = self.MainWindowClass(self.Main, parent=self.getMayaInstance())

    def showWindow(self):
        self.window.show()

    def getMayaInstance(self):
        # type: () -> shiboken2.wrapInstance()

        pointer = omui.MQtUtil.mainWindow()
        if pointer is not None:
            return shiboken2.wrapInstance(long(pointer), QtWidgets.QWidget)


def spawnCylinder():
    cmds.cylinder()
