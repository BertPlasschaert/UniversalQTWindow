from PySide2 import QtWidgets, QtUiTools

class TestDialog(QtWidgets.QDialog):

    def __init__(self, parent=None):
        super(TestDialog, self).__init__(parent)

        # self.window = QtUiTools.QUiLoader().load("C:\\Users\\Bert\\Desktop\\UniversalWindow\\MainWindow.ui")
        # mylayout = QtWidgets.QVBoxLayout()
        # mylayout.addWidget(self.window)
        # self.setLayout(mylayout)

        self.init_ui()

    def init_ui(self):
        """ Prepare Qt UI layout for custom dialog """
        main_layout = QtWidgets.QVBoxLayout()
        label = QtWidgets.QLabel("Click button to create a cylinder in the scene")
        main_layout.addWidget(label)

        cylinder_btn = QtWidgets.QPushButton("Cylinder")
        main_layout.addWidget(cylinder_btn)

        self.setLayout(main_layout)
        self.resize(250, 100)
