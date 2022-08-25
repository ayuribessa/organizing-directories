from tkinter import filedialog
from pathlib import Path
import shutil
import json

p = filedialog.askdirectory()  # get Pathname as string
PATH = Path(p)  # FileSystem Path
f = open('./folder_structure.json')
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
                for book_subject in folders_structure[key].keys():
                    if file.name in folders_structure[key][book_subject]:
                        destiny_folder = PATH / f"{key}" / f"{book_subject}"
                        destiny_folder.mkdir(exist_ok=True)
                        shutil.move(str(file.resolve()), str(destiny_folder))
            else:
                destiny_folder = PATH / f"{key}"
                destiny_folder.mkdir(exist_ok=True)
                shutil.move(str(file.resolve()), str(destiny_folder))
        else:
            destiny_folder = PATH / "uncategorized"
            destiny_folder.mkdir(exist_ok=True)
            shutil.move(str(file.resolve()), str(destiny_folder))

    # if any key value the matches with the file extension on the file,create the dir(if no created yet) with the dict key's name
    # if it is a book file extension,
    #  # iterate through the books subject and check if the books name contains the values in each keys(with our without case)
    #  # if yes, create the folder(if note created) and move the file to that folder
    # move the file to that folder
    # else, create(if not created yet) and move to the Other folder
