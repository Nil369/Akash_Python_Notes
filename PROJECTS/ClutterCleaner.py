import os

def createIfNotExist(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def move(folderName, files):
    for file in files:
        os.replace(file, f"{folderName}/{file}") 

if __name__ == "__main__":
        
    files = os.listdir()

    # Check if "main.py" is in the list before trying to remove it
    if "main.py" in files:
        files.remove("main.py")
    else:
        print("'main.py' not found in the list of files.")

    createIfNotExist('Images')
    createIfNotExist('Docs')
    createIfNotExist('Media')
    createIfNotExist('Others')

    imgExts = [".png", ".jpg", ".jpeg"]
    images = [file for file in files if os.path.splitext(file)[1].lower() in imgExts ]
    print(f"Moving {len(images)} image files to 'Images' folder.")

    docExts = [".txt", ".docx", "doc", ".pdf"]
    docs = [file for file in files if os.path.splitext(file)[1].lower() in docExts]
    print(f"Moving {len(docs)} document files to 'Docs' folder.")

    mediaExts = [".mp4", ".mp3", ".flv"]
    medias = [file for file in files if os.path.splitext(file)[1].lower() in mediaExts]
    print(f"Moving {len(medias)} media files to 'Media' folder.")

    others = []
    for file in files:
        ext = os.path.splitext(file)[1].lower()
        if (ext not in mediaExts) and (ext not in docExts) and (ext not in imgExts) and os.path.isfile(file):
            others.append(file)
    print(f"Moving {len(others)} files to 'Others' folder.")

    move("Images", images)
    move("Docs", docs)
    move("Media", medias)
    move("Others", others)
