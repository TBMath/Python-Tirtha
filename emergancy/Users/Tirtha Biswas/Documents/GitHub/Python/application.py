from os import write
from pathlib import Path
from zipfile import PyZipFile, ZipFile
with ZipFile("emergancy.zip", "w") as file:
    for p in Path(r"C:\Users\Tirtha Biswas\Documents\GitHub\Python").rglob("*.*"):
        file.write(p)




