
from flask import Flask
from flask.ext.restful import Api

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://luke@localhost:5432/erddap'
api = Api(app)

from flask.ext.sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)

from erddap_management.controllers.platforms import PlatformController, PlatformListController
api.add_resource(PlatformController, '/platforms/<int:platform_id>')
api.add_resource(PlatformListController, '/platforms')
