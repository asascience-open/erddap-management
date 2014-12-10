from erddap_management import db

from flask.ext.sqlalchemy import SQLAlchemy
from erddap_management.models.serializer_mixin import SerializerMixin


class Platform(db.Model, SerializerMixin):
    id                   = db.Column(db.Integer, primary_key=True)
    reference_designator = db.Column(db.Text(), unique=True)
    display_name         = db.Column(db.Text())

    def __init__(self, reference_designator, display_name):
        self.reference_designator = reference_designator
        self.display_name = display_name

    def __repr__(self):
        return '<Platform %r>' % self.reference_designator

