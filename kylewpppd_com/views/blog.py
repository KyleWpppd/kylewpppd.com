from flask import Blueprint, render_template, session, redirect, url_for, \
     request, flash, g, jsonify, abort

mod = Blueprint('blog', __name__, url_prefix='/blog')

@mod.route('/')
def index():
    return render_template('blog/index.html')
