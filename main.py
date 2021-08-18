
import sqlite3
from flask import Flask, request, render_template
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
        cel = request.form['celular']
        nasc = request.form['nasc']
        conn = sqlite3.connect('facilitadores.db')
        c = conn.cursor()
        c.execute("INSERT INTO facilitadores (nome, email, cel, nasc) VALUES (?,?,?,?)", (nome, email,cel,nasc))
        conn.commit()
        return render_template("add.html", fb = "Facilitador Cadastrado")

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

if __name__ == '__main__':
    app.run(debug=True)


# api = Api(app)
#
#
# class Cadastrar(Resource):
#     def get(self):
#         headers = {'Content-Type': 'text/html'}
#         return make_response(render_template("add.html"),200,headers)
#
#     def post(self):
#         nome = request.form['nome']
#         email = request.form['email']
#         cel = request.form['celular']
#         nasc = request.form['nasc']
#         conn = sqlite3.connect('jedi.db')
#         c = conn.cursor()
#         c.execute("INSERT INTO jedi (nome, email, cel, nasc) VALUES (?,?,?,?)", (nome, email,cel,nasc))
#         conn.commit()
#         headers = {'Content-Type': 'text/html'}
#         return make_response(render_template("add.html", fb = "Jedi Cadastrado"), 200, headers)
#
# api.add_resource(Cadastrar, '/')