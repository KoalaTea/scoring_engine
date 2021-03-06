import os
import logging
from flask import Flask

from scoring_engine.config import config


app = Flask(__name__)

app.config.update(DEBUG=config.web_debug)
app.secret_key = os.urandom(128)

if not config.web_debug:
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.ERROR)

from scoring_engine.web.views import welcome, scoreboard, overview, services, admin, auth, profile, api, about

app.register_blueprint(welcome.mod)
app.register_blueprint(scoreboard.mod)
app.register_blueprint(overview.mod)
app.register_blueprint(services.mod)
app.register_blueprint(admin.mod)
app.register_blueprint(auth.mod)
app.register_blueprint(profile.mod)
app.register_blueprint(api.mod)
app.register_blueprint(about.mod)
