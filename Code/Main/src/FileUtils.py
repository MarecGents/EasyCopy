import shutil

class FileUtils:

    def __init__(self, source, target):
        self.source = source
        self.target = target
        pass

    def copyFolder(self):
        shutil.copytree(self.source, self.target, dirs_exist_ok=True)
        pass

    def cutFolder(self):
        shutil.move(self.source, self.target)
        pass

    pass