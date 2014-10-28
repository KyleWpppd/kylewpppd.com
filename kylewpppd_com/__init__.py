from flask import Flask, session, g, render_template

app = Flask(__name__)
app.config.from_object('kylewpppd_com_config')

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

from kylewpppd_com.views import main
from kylewpppd_com.views import blog

app.register_blueprint(main.mod)
app.register_blueprint(blog.mod)

