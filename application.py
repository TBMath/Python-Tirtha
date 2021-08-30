import json
import sqlite3
from pathlib import Path
path = Path("FamilyData.json").read_text()
data = json.loads(path)
with sqlite3.connect("Family.sqlite3") as database:
    command = "INSERT INTO DATA VALUES(?, ?, ?)"
    for family in data:
        database.execute(command, tuple(family.values()))
    database.commit()
