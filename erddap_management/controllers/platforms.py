from flask.ext.restful import Api, Resource, reqparse
from erddap_management.models.platform import Platform
from erddap_management import db

class PlatformController(Resource):
    def __init__(self):
        Resource.__init__(self)

        self.parser = reqparse.RequestParser()
        self.parser.add_argument('id', type=int)
        self.parser.add_argument('reference_designator', type=str)
        self.parser.add_argument('display_name', type=str)

    def get(self, platform_id):
        platform = Platform.query.filter_by(id=platform_id).first()
        if platform is None:
            return {}, 204
        return platform.serialize()

    def put(self, platform_id):
        platform = Platform.query.filter_by(id=platform_id).first()
        if platform is None:
            return {}, 204
        args = self.parser.parse_args()
        platform.reference_designator = args['reference_designator']
        platform.display_name = args['display_name']
        db.session.add(platform)
        db.session.commit()
        return platform.serialize(), 201

    def delete(self, platform_id):
        platform = Platform.query.filter_by(id=platform_id).first()
        if platform is None:
            return {}, 404
        db.session.delete(platform)
        db.session.commit()
        return {"status": "ok"}

class PlatformListController(Resource):
    def __init__(self):
        Resource.__init__(self)
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('reference_designator', type=str)
        self.parser.add_argument('display_name', type=str)

    def get(self):
        platforms = Platform.query.all()
        platforms = [p.serialize() for p in platforms]
        return platforms

    def post(self):
        args = self.parser.parse_args()
        reference_designator = args['reference_designator']
        display_name = args['display_name']
        platform = Platform(reference_designator, display_name)
        db.session.add(platform)
        db.session.commit()
        return platform.serialize()

