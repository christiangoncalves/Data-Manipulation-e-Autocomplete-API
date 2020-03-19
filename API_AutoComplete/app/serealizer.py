from flask_marshmallow import Marshmallow
from .model import Timeline

marsh = Marshmallow()

def configure(app):
    marsh.init_app(app)


class TimelineSchema(marsh.ModelSchema):
    class Meta:
        model = Timeline