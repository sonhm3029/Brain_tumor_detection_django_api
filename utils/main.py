import os
import datetime

UPLOAD_FOLDER = 'uploads'
UPLOAD_FOLDER_TYPE = ['images', 'videos', 'texts', 'others', 'docs', 'audios']
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def generateUniquePrefix():
    currentTime = datetime.datetime.now()
    prefixDate = "_".join(str(currentTime.date()).split("-"))
    prefixTimestamp = "".join(str(currentTime.timestamp()).split("."))
    return f"{prefixDate}_{prefixTimestamp}"


def createUploadFolders():
    if not os.path.exists(UPLOAD_FOLDER):
        os.mkdir(UPLOAD_FOLDER)
        for typeFolder in UPLOAD_FOLDER_TYPE:
            os.mkdir(f'{UPLOAD_FOLDER}/{typeFolder}')
        print("Uploads folder was created!")


def allowed_file(filename):
    return '.' in filename and\
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
        

def createFilePath():
    prefixFolder = generateUniquePrefix()
    os.mkdir(f"uploads/images/{prefixFolder}")
    return f"uploads/images/{prefixFolder}"