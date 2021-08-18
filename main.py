#!/bin/env python

import sqlite3
from flask import Flask, request, render_template, redirect
app = Flask(__name__)

@app.route('/')
def index():
    conn = sqlite3.connect('facilitadores.db')
    c = conn.cursor()
    c.execute("SELECT name FROM pragma_table_info('facilitadores')")
    keys = c.fetchall()
    key_list = []
    for i in keys:
        key_list.append(i[0])
    c.execute("SELECT * FROM facilitadores")
    values = c.fetchall()
    conn.commit()
    facilitadores = []
    for row in values:
        item = {}
        for i in range(len(key_list)):
            item[key_list[i]] = row[i]
        facilitadores.append(item)
    return render_template("index.html" , facilitadores = facilitadores)

@app.route('/send_data', methods = ['POST', 'GET'])
def send_data():
    if request.method == "GET":
        return render_template("add.html")
    elif request.method == "POST":
        nome = request.form['nome']
        email = request.form['email']
        cel = request.form['cel']
        nasc = request.form['nasc']
        conn = sqlite3.connect('facilitadores.db')
        c = conn.cursor()
        c.execute("INSERT INTO facilitadores (nome, email, cel, nasc) VALUES (?,?,?,?)", (nome, email,cel,nasc))
        conn.commit()
        return redirect('/')

@app.route('/show_data/<int:id>/', methods = ['GET'])
def show_data(id):
    conn = sqlite3.connect('facilitadores.db')
    c = conn.cursor()
    c.execute("SELECT name FROM pragma_table_info('facilitadores')")
    keys = c.fetchall()
    key_list = []
    for i in keys:
        key_list.append(i[0])
    c.execute("SELECT * FROM facilitadores WHERE id = {}".format(id))
    row = c.fetchall()
    item = {}
    for i in range(len(key_list)):
        item[key_list[i]] = row[0][i]
    conn.commit()
    return render_template("view.html", item = item)

@app.route('/edit/<int:id>/', methods = ['POST','GET'])
def edit(id):
    if request.method == "GET":
        conn = sqlite3.connect('facilitadores.db')
        c = conn.cursor()
        c.execute("SELECT name FROM pragma_table_info('facilitadores')")
        keys = c.fetchall()
        c.execute("SELECT * FROM facilitadores WHERE id = {}".format(id))
        row = c.fetchall()
        conn.commit()
        key_list = []
        for i in keys:
            key_list.append(i[0])
        item = {}
        for i in range(len(key_list)):
            item[key_list[i]] = row[0][i]
        return render_template("edit.html", item = item)
    elif request.method == "POST":
        conn = sqlite3.connect('facilitadores.db')
        c = conn.cursor()
        c.execute("SELECT name FROM pragma_table_info('facilitadores')")
        keys = c.fetchall()
        c.execute("SELECT * FROM facilitadores WHERE id = {}".format(id))
        row = c.fetchall()
        conn.commit()
        key_list = []
        for i in keys:
            key_list.append(i[0])
        item = {}
        for i in range(len(key_list)):
            item[key_list[i]] = row[0][i]
        for key in key_list:
            campo = request.form.get(key)
            if campo != item[key] and campo != None:
                item[key] = campo
                c.execute("UPDATE facilitadores SET {} = '{}' WHERE id = {} ".format(key, campo, id))
                conn.commit()
        fb = "Cadastro alterado com sucesso"
        return render_template("edit.html", item=item, fb = fb)

@app.route('/delete', methods = ['POST'])
def delete():
    conn = sqlite3.connect('facilitadores.db')
    c = conn.cursor()
    # c.execute("SELECT name FROM pragma_table_info('facilitadores')")
    # keys = c.fetchall()
    # key_list = []
    # for i in keys:
    #     key_list.append(i[0])
    # c.execute("SELECT * FROM facilitadores")
    # values = c.fetchall()
    # facilitadores = []
    # for row in values:
    #     item = {}
    #     for i in range(len(key_list)):
    #         item[key_list[i]] = row[i]
    #     facilitadores.append(item)
    apaga = request.form['id']
    c.execute("DELETE FROM facilitadores WHERE id = {}".format(apaga))
    conn.commit()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)