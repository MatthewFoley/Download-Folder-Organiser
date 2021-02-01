import os
import shutil
import time
import getpass

folder_to_clean = "/home/" + getpass.getuser() + "/Downloads"
document_destination = "/home/" + getpass.getuser() + "/Documents"
image_destination = "/home/" + getpass.getuser() + "/Pictures"
music_destination = "/home/" + getpass.getuser() + "/Music"
dda_destination = "/home/" + getpass.getuser() + "/Documents/Cyberpunk/DungeonDraft Assets"

class Cleaner():

    def cleanerfunc():
        for filename in os.listdir(folder_to_clean):
            if filename.endswith(".txt") or filename.endswith(".pdf") or filename.endswith(".doc") or filename.endswith(".docx") or filename.endswith(".word"):
                file_number = 0
                src = folder_to_clean + "/" + filename
                new_destination = document_destination + "/" + filename
                while os.path.isfile(new_destination):
                    file_number +=1
                    new_destination = document_destination + "/" + str(file_number) + filename               
                os.rename(src, new_destination)
            elif filename.endswith(".png") or filename.endswith(".jpeg") or filename.endswith(".jpg") or filename.endswith(".gif"):
                file_number = 0
                src = folder_to_clean + "/" + filename
                new_destination = image_destination + "/" + filename
                while os.path.isfile(new_destination):
                    file_number +=1
                    new_destination = document_destination + "/" + str(file_number) + filename
                os.rename(src, new_destination)
            elif filename.endswith(".mp3"):
                file_number = 0
                src = folder_to_clean + "/" + filename
                new_destination = music_destination + "/" + filename
                while os.path.isfile(new_destination):
                    file_number +=1
                    new_destination = document_destination + "/" + str(file_number) + filename
                os.rename(src, new_destination)
            elif filename.endswith(".dungeondraft_pack"):
                file_number = 0
                src = folder_to_clean + "/" + filename
                new_destination = dda_destination + "/" + filename
                while os.path.isfile(new_destination):
                    file_number +=1
                    new_destination = document_destination + "/" + str(file_number) + filename
                os.rename(src, new_destination)
    
    while True:
        cleanerfunc()
        
        time.sleep(10)
    