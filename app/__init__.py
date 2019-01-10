from app.flask_app import app
from werkzeug.contrib.fixers import ProxyFix
from flask_cors import CORS
from app.service import api


CORS(app)
app.wsgi_app = ProxyFix(app.wsgi_app)

api.init_app(app)
