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
        cylinder = self.Platform.renameObject(cylinder, "animatedCylinder")
        self.Platform.setTranslationKeyframe(cylinder, 10, [5, 0, 0], False)


if __name__ == '__main__':
    Main = Main()
