import sys

sys.path.append("C://BackupHDD//Projects//UniversalWindow")

import PlatformManager


# importlib.reload(Platform)

class Main:

    def __init__(self):
        self.Platform = PlatformManager.GetPlatformModule()
        self.WindowManager = self.Platform.WindowManager(self)
        self.WindowManager.showWindow()

    def spawnAnimatedCylinder(self):
        cylinder = self.Platform.spawnCylinder()
        self.Platform.renameObject(cylinder, "animatedCylinder")


if __name__ == '__main__':
    Main = Main()
