from app import app, db
from flask import Flask, render_template, request, redirect, url_for
from app.model.tables import Cliente
import requests

usuarios = [
    {'login': 'GOVEG', 'senha': 'ronetto'}
]

@app.route("/", methods = ["GET"])
def login():
    return render_template("login.html", mensagem = "Acesse sua conta")


@app.route("/form", methods = ["PUT", "POST"])
def form_teste():
    login = request.form["login"]
    senha = request.form["password"]
    for user in usuarios:
        if user['login'] == login and user['senha'] == senha:
            return render_template("index.html", login = login)
    return render_template("login.html", mensagem = "Login inválido")

def pega_cep(cep):
    resposta = requests.get('https://viacep.com.br/ws/'+cep+'/json')
    #resposta = requests.get(f"https://api.postmon.com.br/v1/cep/{cep}")
    dicionario = resposta.json()
    return dicionario['logradouro']


@app.route("/form")
def index():
    # selecionar todos - select * from
    clientes = Cliente.query.all()
    return render_template("index.html", clientes=clientes)


@app.route("/form/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        # crio um objeto cliente com os dados do formulario
        cliente = Cliente(request.form['nome'], request.form['comentario'], request.form['quantidade'],pega_cep(request.form['cep']), request.form['numero'], request.form['valor'])
        # adiciono o cliente (insert into)
        db.session.add(cliente)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template("add.html")


@app.route("/form/edit/<int:id>", methods=['GET', 'POST'])
def edit(id):
    # select from
    cliente = Cliente.query.get(id)
    if request.method == 'POST':
        cliente.name = request.form['nome']
        cliente.comment = request.form['comentario']
        cliente.quantidade = request.form['quantidade']
        cliente.cep = pega_cep(request.form['cep'])
        cliente.numero = request.form['numero']
        cliente.valor = request.form['valor']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template("edit.html", cliente=cliente)


@app.route("/form/delete/<int:id>")
def delete(id):
    cliente = Cliente.query.get(id)
    db.session.delete(cliente)
    db.session.commit()
    return redirect(url_for('index'))
