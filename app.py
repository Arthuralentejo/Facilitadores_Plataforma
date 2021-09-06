#!/bin/env python
from flask import Flask, request
from domain import crud,students
app = Flask(__name__)

@app.route('/create_students', methods = ['POST'])
def createStudents():
    pass

@app.route('/get_students', methods = ['GET'])
def getStudents():
    pass


@app.route('/edit_students', methods = ['PUT'])
def updateStudents():
    pass


@app.route('/remove_students', methods = ['DELETE'])
def removeStudents():
    pass


if __name__ == '__main__':
    app.run()
