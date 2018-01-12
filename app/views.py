from flask import render_template

from app import app

# this decorator to specify the path we'd like the view to be dispayed on
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/instalacao')
def instalacao():
    return render_template("instalacao.html")

@app.route('/manutencao')
def manutencao():
    return render_template("manutencao.html")

@app.route('/xvm')
def xvm():
    return render_template("xvm.html")

@app.route('/contato')
def contato():
    return render_template("contato.html")

"""
Flask provides a method, render_template, 
which we can use to specifiy which HTML file should be loaded in a particular view.
"""