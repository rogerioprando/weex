from flask import Blueprint, render_template

mod = Blueprint('manual', __name__, url_prefix='/manual')


@mod.route('/<page>')
def instalacao(page):
    return render_template('manual/%s.html' % page)


@mod.route('/<page>')
def manutencao(page):
    return render_template('manual/%s.html' % page)