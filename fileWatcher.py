import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        print("File %s has been modified!"%event.src_path)
        self.copy_new_contents()

    def copy_new_contents(self):
        content = ''
        fileToRead = './test.txt'
        with open(fileToRead, 'r') as content_file:
            print('Reading From %s'%fileToRead)
            content = content_file.read()

        fileToWriteTo='../newTest.txt' 
        with open(fileToWriteTo, 'w') as filetowrite:
            try:
                print('Writing the new contents to %s'%fileToWriteTo)
                filetowrite.write(content)
                print('New contents successfully written to %s.'%fileToWriteTo)
                filetowrite.close()
            except:
                print('Error occured, could not write new contents to file!')

event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, path='.', recursive=False)
observer.start()
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()