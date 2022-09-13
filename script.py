from tkinter import filedialog
from pathlib import Path
import shutil
import json

p = filedialog.askdirectory()  # get Pathname as string
PATH = Path(p)  # FileSystem Path
f = open("./folder_structure.json")
folders_structure = json.load(f)

files = [i for i in PATH.iterdir() if i.is_file()]

for file in files:
    # iterate on the files extensions inside each key
    for key in folders_structure.keys():
        # if the file extension match any of the extension list inside the key
        if file.suffix in folders_structure[key]:
            # if the file extension is a book extension
            if key == "Books":
                # get te subjects and iterate through them
                books_subjects = folders_structure[key][5].get("subject")
                for subject in books_subjects:
                    subject_list = books_subjects.get(subject)
                    check = any(item in file.name for item in subject_list)
                    if check:
                        destiny_folder = PATH / f"{key}" / f"{subject}"
                        destiny_folder.mkdir(parent=True, exist_ok=True)
                        shutil.move(str(file.resolve()), str(destiny_folder))
                    break

            else:
                destiny_folder = PATH / f"{key}"
                destiny_folder.mkdir(exist_ok=True)
                shutil.move(str(file.resolve()), str(destiny_folder))

files = [i for i in PATH.iterdir() if i.is_file()]
for file in files:
    destiny_folder = PATH / "uncategorized"
    destiny_folder.mkdir(exist_ok=True)
    shutil.move(str(file.resolve()), str(destiny_folder))
