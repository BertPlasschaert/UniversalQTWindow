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
    obj = cmds.cylinder()
    return obj


def renameObject(obj, newName):
    # type: (object, str) -> object

    obj = cmds.rename(obj[0], newName)
    return obj


def setTranslationKeyframe(obj, frameNumber, translation, absolute):
    # type: (object, int, list, bool) -> object

    cmds.move(translation[0], translation[1], translation[2], obj, absolute=absolute)

    cmds.setKeyframe(obj, attribute="translateX", t=frameNumber)
    cmds.setKeyframe(obj, attribute="translateY", t=frameNumber)
    cmds.setKeyframe(obj, attribute="translateZ", t=frameNumber)

    return obj
