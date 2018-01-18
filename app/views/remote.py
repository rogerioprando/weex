from flask import Blueprint, render_template, request
from app.devices import *
from app.forms import *


mod = Blueprint('remote', __name__, url_prefix='/remote')


@mod.route('/<page>', methods=['GET', 'POST'])
def xvm(page):
    if request.method == 'POST':
        cmd_xvm = request.form['cmd_xvm']
        id_xvm = request.form['id_xvm']
        ans_request = request_xvm(cmd_xvm, id_xvm)
        return render_template('remote/%s.html' % page, ans_xvm=ans_request)
    return render_template('remote/%s.html' % page)


@mod.route('/<page>')
def programacao(page):
    return render_template('remote/%s.html' % page)


