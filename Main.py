import sys

sys.path.append("C://Users//Bert//Desktop//UniversalWindow")

import PlatformManager


# importlib.reload(Platform)

class Main:

    def __init__(self):
        self.Platform = PlatformManager.GetPlatformModule()
        self.WindowManager = self.Platform.WindowManager(self)
        self.WindowManager.showWindow()

    def spawnAnimatedCylinder(self):
        self.Platform.spawnCylinder()


if __name__ == '__main__':
    Main = Main()
