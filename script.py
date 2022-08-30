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
            if key == "books":
                # iterate through de subjects
                a = folders_structure[key][5].get("subject").keys()
                b = file.name.split()
                has_it = [True for a_ in a if a_ in b or a_.lower() in b]

                if hast_it:
                    # if file.name in folders_structure[key][book_subject] or file.name:
                    destiny_folder = PATH / f"{key}" / f"{book_subject}"
                    destiny_folder.mkdir(exist_ok=True)
                    shutil.move(str(file.resolve()), str(destiny_folder))
            else:
                destiny_folder = PATH / f"{key}"
                destiny_folder.mkdir(exist_ok=True)
                shutil.move(str(file.resolve()), str(destiny_folder))

files = [i for i in PATH.iterdir() if i.is_file()]
for file in files:
    destiny_folder = PATH / "uncategorized"
    destiny_folder.mkdir(exist_ok=True)
    shutil.move(str(file.resolve()), str(destiny_folder))

