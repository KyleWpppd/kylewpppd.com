from flask import Blueprint

from kylewpppd_com import render_template_with_mtime

mod = Blueprint('main', __name__)

@mod.route('/')
def index():
    return render_template_with_mtime('main/index.html')

@mod.route('/about')
def bio():
    return render_template_with_mtime('main/bio.html')

@mod.route('/black-techies')
def techies():
    return render_template_with_mtime('main/techies.html')

@mod.route('/contact')
def contact():
    return render_template_with_mtime('main/contact.html')

