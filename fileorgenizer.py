import os
from pathlib import Path
import shutil
# make specifict path for each folder
audio = (".3ga", ".aac", ".ac3", ".aif", ".aiff",
         ".alac", ".amr", ".ape", ".au", ".dss",
         ".flac", ".flv", ".m4a", ".m4b", ".m4p",
         ".mp3", ".mpga", ".ogg", ".oga", ".mogg",
         ".opus", ".qcp", ".tta", ".voc", ".wav",
         ".wma", ".wv")

video = (".webm", ".MTS", ".M2TS", ".TS", ".mov",
         ".mp4", ".m4p", ".m4v", ".mxf")

img = (".jpg", ".jpeg", ".jfif", ".pjpeg", ".pjp", ".png",
       ".gif", ".webp", ".svg", ".apng", ".avif")

# truth functions
def is_audio(file):
    return os.path.splitext(file)[1] in audio

def is_video(file):
    return os.path.splitext(file)[1] in video

def is_image(file):
    return os.path.splitext(file)[1] in img

def is_screenshot(file):
    name, ext = os.path.splitext(file)
    return (ext in img) and "screenshot" in name.lower()


for file in os.listdir():
    print(file)
    if is_audio(file):
        shutil.move(file, "Users/HP/Desktop/training/audio")
    elif is_video(file):
        shutil.move(file, "Users/HP/Desktop/training/video")
    elif is_image(file):
        if is_screenshot(file):
            shutil.move(file, "Users/HP/Desktop/training/image")
        else:
            shutil.move(file, "Users/HP/Desktop/training/image")
    else:
        shutil.move(file, os.getcwd() + "elseee")