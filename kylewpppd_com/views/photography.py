from flask import Blueprint

from kylewpppd_com import render_template_with_mtime

mod = Blueprint('photography', __name__, url_prefix='/photography')

@mod.route('/')
def index():
    return render_template_with_mtime('photography/index.html')
