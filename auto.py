import os
import shutil
from platformdirs import user_downloads_dir

def search_folders(destination):
    folder_paths = [os.path.join(downloadsDirectory, f) for f in os.listdir(downloadsDirectory) if os.path.isdir(os.path.join(downloadsDirectory, f))]
    if destination in folder_paths:
        return False
    elif destination == None:
        return False
    else:
        return True
def get_file_dir(file_category):
    if file_category in dest_dirs:
        return dest_dirs[file_category]
    return None

def get_category(extension):
    for category,extensions in filetypes_dict.items():
        if extension.lower() in [ext.lower() for ext in extensions]:
            return category
    return None

downloadsDirectory = user_downloads_dir()

dest_dirs = {
    "document": downloadsDirectory+"\\"+"documents",
    "archive": downloadsDirectory+"\\"+"archives",
    "software": downloadsDirectory+"\\"+"softwares",
    "music": downloadsDirectory+"\\"+"music",
    "video": downloadsDirectory+"\\"+"videos",
    "image": downloadsDirectory+"\\"+"images",
    "code": downloadsDirectory+"\\"+"code",
    "torrent": downloadsDirectory+"\\"+"torrents"
}

filetypes_dict = {
    "document": ['.pdf', '.docx', '.xlsx', '.pptx', '.txt'],
    "archive": ['.zip', '.rar', '.7z'],
    "software": ['.msi','.exe', '.apk', '.dmg', '.iso'],
    "music": ['.mp3', '.wav', '.m4a', '.alac', '.mid', '.midi'],
    "video": ['.mp4', '.mkv'],
    "image": ['.avif','.jpg', '.jpeg', '.png', '.gif','.webp'],
    "code": ['.html', '.css', '.js', '.py', '.json','.ini'],
    "torrent": ['.torrent']
}

with os.scandir(downloadsDirectory) as entries:
    for entry in entries:
        filename = entry.name
        root,ext = os.path.splitext(filename)
        file_category = get_category(ext)
        destination = get_file_dir(file_category)
        if search_folders(destination):
            os.mkdir(destination)
            old_path = downloadsDirectory+ "\\" +filename
            shutil.move(old_path,destination)
        elif destination == None:
            continue
        else:
            old_path = downloadsDirectory+ "\\" +filename
            shutil.move(old_path,destination)