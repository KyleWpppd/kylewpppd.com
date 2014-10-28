from pprint import pprint

from flask import Flask, session, g, render_template
from flask.globals import _request_ctx_stack, _app_ctx_stack


app = Flask(__name__)
app.config.from_object('kylewpppd_com_config')

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.context_processor
def wat(thing):
    return vars(thing)

def render_template_with_mtime(template_name_or_list, **context):
    ctx = _app_ctx_stack.top
    template = ctx.app.jinja_env.get_or_select_template(template_name_or_list)
    from StringIO import StringIO
    from os.path import getmtime
    buf = StringIO()
    pprint(vars(template), buf)
    return str(getmtime(template.filename))

app.jinja_env.globals.update(wat=wat)

from kylewpppd_com.views import main
from kylewpppd_com.views import blog
from kylewpppd_com.views import projects


app.register_blueprint(main.mod)
app.register_blueprint(blog.mod)
app.register_blueprint(projects.mod)


