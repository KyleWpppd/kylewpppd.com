from flask import Blueprint

from kylewpppd_com import render_template_with_mtime

mod = Blueprint('blog', __name__, url_prefix='/blog')

@mod.route('/')
def index():
    return render_template_with_mtime('blog/index.html')
