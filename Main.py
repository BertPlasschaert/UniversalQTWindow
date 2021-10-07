import sys
sys.path.append("C://Users//Bert//Desktop//UniversalWindow")

import PlatformManager


# importlib.reload(Platform)

__metaclass__ = type

if __name__ == '__main__':

    Platform = PlatformManager.GetPlatformModule()
    
    WindowManager = Platform.WindowManager()

    WindowManager.window.setWindowTitle("jajaja")

    WindowManager.showWindow()