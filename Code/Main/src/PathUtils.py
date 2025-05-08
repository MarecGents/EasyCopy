import pathlib

class PathUtils:
    def __init__(self):
        self.logPath = "Logs\\"
        self.imgPath = "res\\img\\"
        self.localesPath = "res\\locales\\"
        self.settingsPath = "res\\settings\\"
        self.configPath = "res\\config\\"
        pass

    @staticmethod
    def app_path():
        return pathlib.Path().parent.absolute()

    @staticmethod
    def open_path(path):

        pass

    pass