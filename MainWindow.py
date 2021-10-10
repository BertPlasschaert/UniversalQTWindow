from PySide2 import QtWidgets, QtUiTools


class MainWindow(QtWidgets.QDialog):

    def __init__(self, Main, parent=None):
        super(MainWindow, self).__init__(parent)

        # self.window = QtUiTools.QUiLoader().load("C:\\Users\\Bert\\Desktop\\UniversalWindow\\MainWindow.ui")
        # mylayout = QtWidgets.QVBoxLayout()
        # mylayout.addWidget(self.window)
        # self.setLayout(mylayout)

        self.Main = Main
        self.initUi()
        self.connectUI()

    def initUi(self):
        main_layout = QtWidgets.QVBoxLayout()
        label = QtWidgets.QLabel("Click button to create a cylinder in the scene")
        main_layout.addWidget(label)

        self.cylinder_btn = QtWidgets.QPushButton("Cylinder")
        main_layout.addWidget(self.cylinder_btn)

        self.setLayout(main_layout)
        self.resize(250, 100)

    def connectUI(self):
        self.cylinder_btn.clicked.connect(self.Main.spawnAnimatedCylinder)
