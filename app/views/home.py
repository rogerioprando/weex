from flask import Blueprint, render_template

mod = Blueprint('home', __name__, url_prefix='/home')


@mod.route('/<page>')
def index(page):
    return render_template('home/%s.html' % page)


@mod.route('/<page>')
def news(page):
    return render_template('home/%s.html' % page)



