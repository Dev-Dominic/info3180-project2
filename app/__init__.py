# Python Modules

import os

# Flask Modules

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# Environment variable setup

from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

# Database Configuration

app.config['SQLAlCHEMY_DATABASE_URI'] = os.getenv('DB_URI')
db = SQLAlchemy
migrate = Migrate(db)

# Login Manager Configuration

login_manager = LoginManager()
login_manager.init_app(app)

from . import views
from . import models
