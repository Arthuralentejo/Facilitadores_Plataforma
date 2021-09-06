import sqlite3
import os.path
from contextlib import closing

class DataBase():
    DBName = 'impact.db'
    CREATE_DB = """
            CREATE TABLE IF NOT EXISTS "Students" (
                "ID"	INTEGER PRIMARY KEY AUTOINCREMENT,
                "Name"	TEXT NOT NULL,
                "Birthdate"	TEXT,
                "Gender"	TEXT,
                "Badge"     TEXT DEFAULT "Student"
            );
    
            CREATE TABLE IF NOT EXISTS "Documents" (
                "ID"	INTEGER PRIMARY KEY AUTOINCREMENT,
                "ID_Student"	INTEGER,
                "Document"	TEXT,
                "Type"	TEXT,
                FOREIGN KEY("ID_Student") REFERENCES Students(ID)
            );
    
            CREATE TABLE IF NOT EXISTS "Contacts" (
                "ID"	INTEGER PRIMARY KEY AUTOINCREMENT,
                "ID_Student"	INTEGER,
                "Contact"	TEXT,
                "Type"	TEXT,
                FOREIGN KEY("ID_Student") REFERENCES Students(ID)
            );
            """
    def __init__(self):
        newFile = False

        if os.path.isfile(self.DBName) == False:
            newFile = True
        self.conn = sqlite3.connect(self.DBName)
        with closing( self.conn.cursor() ) as cur:
            cur.execute(self.CREATE_DB)
    def getCursor(self):
        return self.conn.cursor()
    def close(self):
        self.conn.close()