from flask import Blueprint, render_template

mod = Blueprint('remote', __name__, url_prefix='/remote')


@mod.route('/<page>')
def xvm(page):
    return render_template('remote/%s.html' % page)


@mod.route('/<page>')
def programacao(page):
    return render_template('remote/%s.html' % page)
