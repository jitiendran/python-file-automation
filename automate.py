from fileHandler import sourceDir, FileHandler, logging
from watchdog.observers import Observer
from time import sleep

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    observer = Observer()
    fileHandler = FileHandler()
    observer.schedule(fileHandler, sourceDir, recursive=True)
    observer.start()
    try:
        while True:
            sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
