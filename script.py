from tkinter import filedialog
from pathlib import Path
import json

p = filedialog.askdirectory()#get Pathname as string
PATH = Path(p)#FileSystem Path
dest = PATH / "Organized"
dest.mkdir(exist_ok=True)

f = open('./folder_structure.json')
folders_structure = json.load(f)

files = [i for i in PATH.iterdir() if i.is_file()]

for file in files:
    

