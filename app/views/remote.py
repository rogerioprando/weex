from flask import Blueprint, render_template, request
from app.devices import *
from app.SocketServer import *


mod = Blueprint('remote', __name__, url_prefix='/remote')
conect_xvm = SocketServer()
conect_xvm.init_queues()


@mod.route('/<page>', methods=['GET', 'POST'])
def xvm(page):
    if request.method == 'POST':
        cmd_xvm = request.form['cmd_xvm']
        id_xvm = request.form['id_xvm']
        tuple = cmd_xvm, id_xvm
        conect_xvm.sendcommand(tuple)
        ans_request = conect_xvm.socketrecv_queue.get()
        # ans_request = request_xvm(cmd_xvm, id_xvm)
        return render_template('remote/%s.html' % page, ans_xvm=ans_request)
    return render_template('remote/%s.html' % page)


@mod.route('/<page>')
def programacao(page):
    return render_template('remote/%s.html' % page)


