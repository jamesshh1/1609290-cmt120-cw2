from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# The Flask Instance
app = Flask(__name__)
app.config['SECRET_KEY'] = '770022098636920ad892c570cbd0923343af21326dd8c943'
# Set the directory
basedir = os.path.abspath(os.path.dirname(__file__))
# Set the database URI that should be used for connection - sqlite for local use and the mysql for openshift deployment``
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'blog.db')

uniusername = "c1609290"
sql_db_password = "Flasktime24"
db_name = "c1609290_cmt120_cw2"

app_config_sql_db_uri = f"mysql+pymysql://{uniusername}:{sql_db_password}@csmysql.cs.cf.ac.uk:3306/{uniusername}_{db_name}"

app.config['SQLALCHEMY_DATABASE_URI'] = app_config_sql_db_uri


# Integrate SQLAlchemy to our application
db = SQLAlchemy(app)
# Configure the app with LoginManager
login_manager = LoginManager()
login_manager.init_app(app)
# Import routes from blog
from blog import routes
