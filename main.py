import os
import shutil
from folder_module import Folder
from file_module import File

folder_to_track = Folder("input", "C:/Users/yemoe/Desktop/input")
folder_to_move = Folder("output","C:/Users/yemoe/Desktop/final")
existing_folders = {}


## need a way to somehow check if a folder already exists with that name ##

def checkFolderExists(folderName):
    if folderName in existing_folders:
        return True
    return False

def addFolder(folderName):
    existing_folders[folderName] = 1


def main():
    #go through each file in a directory you want to sort from
    for f in os.listdir(folder_to_track.path):
        
        #make file object
        file = File(f)
        
        #get the original path of file
        src = folder_to_track.path + "/" + file.filepath
        
        
        #check and add if the class folder already exists
        course = file.classCode
        if checkFolderExists(course) == False:
            addFolder(course)

        #create new directory 
        new_directory = folder_to_move.path + "/" + course
        if not os.path.exists(new_directory):
            os.makedirs(new_directory)

        #make new path
        dest = new_directory + "/" + file.filepath
        #move to new path
        os.rename(src, dest)


    print(os.listdir(folder_to_move.path))


if __name__ == '__main__':
    main()