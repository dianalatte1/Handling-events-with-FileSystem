import sys
import time
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "/Users/dianabautista/Downloads"


#creating class event handler
class FileMovementHandler(FileSystemEventHandler):
    # this is a method
    def on_created(self,event):
        print(event)
    #code handler to create a new file in a directory
#Inicializing the class event handler
event_handler = FileMovementHandler()

# Observer
observer = Observer()

#observer program
observer.schedule(event_handler,from_dir,recursive=True)

#Initialized observer
observer.start()

while True:
    time.sleep(2)
    print("Ejecutando....")
