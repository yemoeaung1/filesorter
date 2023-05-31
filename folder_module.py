import shutil
import os

class Folder:
    def __init__(self, name, path):
        # self.path = path
        self.name = name
        self.path = path

    def printFilepath(self):
        print(f"file path is: {self.filepath}")

    def createNewFolder(self):
        os.makedirs(name, exist_ok=False)
