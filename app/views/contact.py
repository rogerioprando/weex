from flask import Blueprint, render_template

mod = Blueprint('contact', __name__, url_prefix='/contact')


@mod.route('/', defaults={'page': 'contato'})
@mod.route('/<page>')
def contact(page):
    return render_template('contact/%s.html' % page)
