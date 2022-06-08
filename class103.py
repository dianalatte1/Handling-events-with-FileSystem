import sys
import time
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "/Users/dianabautista/Downloads"
to_dir = "/Users/dianabautista/Desktop/files"
# this a dictionary 
dir_tree = {
    "Image_Files": ['.jpg', '.jpeg','.png','.gif','jfif'],
    "Video_Files" : ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.xlsx' '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}

#creating class event handler
class FileMovementHandler(FileSystemEventHandler):
    # this is a method
    def on_created(self,event):
        # print(event)
        # Substract the name and extension with os.path.splitext
        name,extension = os.path.splitext(event.src_path)
        time.sleep(1)
        # reading each element in the list 
        for key, value in dir_tree.items():
            time.sleep(1)
            if extension in value:

                file_name = os.path.basename(event.src_path)
                print("Descargado " + file_name)
                # creating 3 variables for names path directory
                # name origin path
                path1 = from_dir + '/' + file_name
                # 
                path2 = to_dir + '/' + key
                path3 = to_dir + '/' + key + '/' + file_name

                if os.path.exists(path2):

                    print("El Directorio Existe...")
                    print("Moviendo " + file_name + "....")
                    shutil.move(path1, path3)
                    time.sleep(1)

                else:
                    print("Creando Directorio...")
                    os.makedirs(path2)
                    print("Moviendo " + file_name + "....")
                    shutil.move(path1, path3)
                    time.sleep(1)

    #code handler to create a new file in a directory
#Inicializing the class event handler
event_handler = FileMovementHandler()

# Observer
observer = Observer()

#observer progra
observer.schedule(event_handler,from_dir,recursive=True)

#Initialized observer
observer.start()
try:

    while True:
        time.sleep(2)
        print("Ejecutando....")
except KeyboardInterrupt:
    print("detenido!")
    observer.stop()
