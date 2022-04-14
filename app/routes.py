from flask import render_template
from app import app
from flask import render_template

@app.route('/')
@app.route('/index')

def index():
    nome = "Alba"
    dados = {"Profissão": "Professora", "Teste": "Teste"}
    return render_template('index.html', nome=nome, dados=dados)

@app.route('/contato')    
def contato():
    return render_template('contato.html')