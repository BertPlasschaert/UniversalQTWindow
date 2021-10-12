from PySide2 import QtWidgets, QtCore
from PySide2 import QtUiTools
import sys
import __future__

from BaseWindowManager import BaseWindowManager

from MainWindow import MainWindow


class WindowManager(BaseWindowManager):

    def __init__(self, Main):

        if issubclass(BaseWindowManager, object):
            # new style class, call super --> Python 3.X
            super(WindowManager, self).__init__(Main)
        else:
            # old style class, call __init__ manually --> Python 2.7
            BaseWindowManager.__init__(self, Main)


def spawnCylinder():
    print("spawn Cylinder")


def renameObject(obj, newName):
    # type: (object, str) -> None
    print("renamed Object to: " + newName)


def setTranslationKeyframe(obj, frameNumber, translation, absolute):
    # type: (object, int, list, bool) -> None

    print("Keyframe placed on:{} at frame: {} ,relative= {}".format(translation, frameNumber, absolute))
