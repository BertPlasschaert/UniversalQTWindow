from PySide2 import QtWidgets, QtCore
from qtmax import GetQMaxMainWindow
from pymxs import runtime as rt
import pymxs

from BaseWindowManager import BaseWindowManager


class WindowManager(BaseWindowManager):

    def __init__(self, Main):
        BaseWindowManager.__init__(self, Main)

    def createWindow(self):
        self.window = self.MainWindowClass(self.Main, parent=GetQMaxMainWindow())

    def showWindow(self):
        self.window.show()


def spawnCylinder():
    # type: () -> object
    obj = rt.cylinder()
    return obj


def renameObject(obj, newName):
    # type: (object, str) -> object
    obj.name = newName

    return obj


def setTranslationKeyframe(obj, frameNumber, translation, absolute):
    # type: (object, int, list, bool) -> object


    if absolute:
        newPos = rt.Point3(translation[0], translation[1], translation[2])
    else:
        newPos = rt.Point3(obj.pos[0] + translation[0], obj.pos[1] + translation[1], obj.pos[2] + translation[2])

    with pymxs.animate(True):
        with pymxs.attime(frameNumber):
            obj.pos = newPos

    pymxs.redraw(True)

    return obj
