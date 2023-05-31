import os
import shutil
from folder_module import Folder
from file_module import File

folder_to_track = Folder("input", "C:/Users/yemoe/Desktop/input")
folder_to_move = Folder("output","C:/Users/yemoe/Desktop/final")

#go through each file in a directory you want to sort from
for f in os.listdir(folder_to_track.path):
    #get name of the file
    file = File(f)
    #get the original path of file
    src = folder_to_track.path + "/" + file.filepath
    #create new directory 
    new_directory = folder_to_move.path + "/" + file.name
    if not os.path.exists(new_directory):
        os.makedirs(new_directory)
    #make new path
    dest = new_directory + "/" + file.filepath
    #move to new path
    os.rename(src, dest)


print(os.listdir(folder_to_move.path))