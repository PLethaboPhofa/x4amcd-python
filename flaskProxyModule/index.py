from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

import logging

index = Blueprint('simple_page', __name__,
                        template_folder='templates')

@index.route('/', defaults={'page': 'index'})
@index.route('/<page>')
def home(page):
    logging.info("home"+ page)
    try:
        return render_template('index.html')
    except TemplateNotFound:
        abort(404)

def test():
    print("test")