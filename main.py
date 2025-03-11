from flask import Flask
from routes.home import home_route
from routes.adm import adm_route
from routes.user import user_route
from routes.cadastro import cadastro_route
from datetime import timedelta

app = Flask(__name__)

app.permanent_session_lifetime = timedelta(minutes=30)
app.register_blueprint(home_route)
app.register_blueprint(adm_route)
app.register_blueprint(user_route)
app.register_blueprint(cadastro_route)

app.secret_key = 'chavesecreta'
app.run(debug=True)