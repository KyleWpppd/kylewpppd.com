from flask import Blueprint, render_template, session, redirect, url_for, \
     request, flash, g, jsonify, abort

from kylewpppd_com import render_template_with_mtime

mod = Blueprint('projects', __name__, url_prefix='/projects')

@mod.route('/')
def index():
    return render_template_with_mtime('projects/index.html')
