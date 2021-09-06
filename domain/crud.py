from contextlib import closing
from .conn import *
from .students import *

clas DAL():
    db = DataBase()

    def getStudents(self,id):
        students = []
        with closing( self.db.GetCursor() ) as cur:
            for row in cur.execute("""
            SELECT
                ID,
                Name,
                Birthdate,
                Gender
            FROM
                Students
            WHERE ID = {}
            """.format(id)):
                s = Student()
                s.ID = row[0]
                s.Name = row[1]
                s.Birthdate = row[2]
                s.Gender = row[3]

                students.append(s)

            for s in students:
                documents = {}
                for row in cur.execute("""
            SELECT
                ID,
                Document,
                Type
            FROM
                Documents
            WHERE
                ID_STUDENT = {}
            """.format(s.ID)):
                    doc = Document()
                    doc.ID = row[0]
                    doc.Document = row[1]
                    documents[row[2]] = doc
                s.Documents = documents

                contacts = []
                for row in cur.execute("""
            SELECT
                ID,
                Contact,
                Type
            FROM
                Contacts
            WHERE
                ID_STUDENT = {}
            """.format(s.ID)):
                    contact = Contact()
                    contact.ID = row[0]
                    contact.Contact = row[1]
                    contact.Type = row[2]
                    contacts.append(contact)

                s.Contacts = contacts

            return s

    def createStudents(self,students):
        pass
    def updateStudents(self,id,students):
        pass
    def deleteStudents(self,id,students):
        pass
    def Close(self):
        self.db.Close()
