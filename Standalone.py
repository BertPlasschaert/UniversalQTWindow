from PySide2 import QtWidgets, QtCore
from PySide2 import QtUiTools
import sys
import __future__

from BaseWindowManager import BaseWindowManager

from MainWindow import TestDialog

class WindowManager(BaseWindowManager):

    def __init__(self):

        if issubclass(BaseWindowManager, object):
            # new style class, call super
            super(WindowManager, self).__init__()
        else:
            # old style class, call __init__ manually
            BaseWindowManager.__init__(self)
