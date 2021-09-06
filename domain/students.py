from json import JSONEncoder


class Student:
    ID = 0
    Name = ""
    Birthdate = ""
    Gender = ""
    Badge = ""
    Documents = {}
    Contacts = []


class Document:
    ID = 0
    Document = ""
    Type = ""


class Contact:
    ID = 0
    Contact = ""
    Type = ""


class StudentEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__

