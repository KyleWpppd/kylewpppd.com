from flask import Blueprint, render_template, session, redirect, url_for, \
     request, flash, g, jsonify, abort

mod = Blueprint('main', __name__)

@mod.route('/')
def index():
    return render_template('main/index.html')

@mod.route('/about')
def bio():
    return render_template('main/bio.html')

