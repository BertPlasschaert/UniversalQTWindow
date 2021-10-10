import sys, re, os


def GetPlatformModule():
# type: () -> Module

    if re.match("python\\.exe", os.path.basename(sys.executable), re.I):
        import Standalone as Platform

    if re.match("maya\\.exe", os.path.basename(sys.executable), re.I):
        import Maya as Platform
        reload(Platform)

    if re.match("3dsmax\\.exe", os.path.basename(sys.executable), re.I):
        import Max as Platform

    if re.match("blender\\.exe", os.path.basename(sys.executable), re.I):
        return 'blender'

    if re.match("UE4Editor\\.exe", os.path.basename(sys.executable), re.I):
        return 'unreal'

    if Platform != None:
        return Platform

    print("Platform not recognised")
    return None
