from os import scandir, rename
from os.path import splitext, exists
from shutil import move
from watchdog.events import FileSystemEventHandler as fileEventHandler
import logging

sourceDir = "path to source directory"
documentsDir = "path to document directory"
imageDir = "path to image directory"
videoDir = "path to video directory"
musicDir = "path to music directory"

imageExtensions = [".jpg", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi", ".png", ".gif", ".webp", ".tiff", ".tif", ".psd",".raw", ".arw", ".cr2", ".nrw", ".k25", ".bmp", ".dib", ".heif", ".heic", ".ind", ".indd", ".indt", ".jp2", ".j2k", ".jpf", ".jpf", ".jpx", ".jpm", ".mj2", ".svg", ".svgz", ".ai", ".eps", ".ico"]
videoExtensions = [".webm", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv", ".ogg", ".mp4", ".mp4v", ".m4v", ".avi", ".wmv", ".mov", ".qt", ".flv", ".swf", ".avchd"]
audioExtensions = [".m4a", ".flac", "mp3", ".wav", ".wma", ".aac"]
documentExtensions = [".doc", ".docx", ".odt", ".pdf", ".xls", ".xlsx", ".ppt", ".pptx"]

# If the filename already exist then add number to end of file
def makeUniquePath(path):
    filename, extension = splitext(path)
    counter = 1
    while exists(path):
        path = f"{filename} ({counter}{extension})"
        counter += 1
    return path

# Moving file to the destinated location
def moveFile(destination, entry, filename):
    if exists(f"{destination}/{filename}"):
        uniqueName = makeUniquePath(filename)
        rename(entry, uniqueName)
    move(entry, destination)

class FileHandler(fileEventHandler):
    # Pre-built function to monitor realtime changes to the directory
    def on_modified(self, event):
        with scandir(sourceDir) as files:
            for file in files:
                filename = file.name
                self.checkImageFiles(file, filename)
                self.checkAudioFiles(file, filename)
                self.checkVideoFiles(file, filename)
                self.checkDocumentFiles(file, filename)

    def checkAudioFiles(self, entry, filename):
        for extension in audioExtensions:
            if filename.endswith(extension) or filename.endswith(extension.upper()):
                moveFile(musicDir, entry, filename)
                logging.info(f"Moved audio file: {filename}")
    
    def checkVideoFiles(self, entry, filename):
        for extension in videoExtensions:
            if filename.endswith(extension) or filename.endswith(extension.upper()):
                moveFile(videoDir, entry, filename)
                logging.info(f"Moved video file: {filename}")
    
    def checkImageFiles(self, entry, filename):
        for extension in imageExtensions:
            if filename.endswith(extension) or filename.endswith(extension.upper()):
                moveFile(imageDir, entry, filename)
                logging.info(f"Moved image file: {filename}")
    
    def checkDocumentFiles(self, entry, filename):
        for extension in documentExtensions:
            if filename.endswith(extension) or filename.endswith(extension.upper()):
                moveFile(documentsDir, entry, filename)
                logging.info(f"Moved document file: {filename}")