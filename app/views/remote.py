from flask import Blueprint, render_template
from app.devices import *

mod = Blueprint('remote', __name__, url_prefix='/remote')


@mod.route('/<page>')
def xvm(page):
    return render_template('remote/%s.html' % page, value=getevent())


@mod.route('/<page>')
def programacao(page):
    return render_template('remote/%s.html' % page)


