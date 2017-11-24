from flask_app import db
from datetime import datetime
from slugify import slugify

class Post(db.Model):

    __tablename__ = "post"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    body = db.Column(db.Text)
    posted = db.Column(db.DateTime, default=datetime.now)
    slug = db.Column(db.String(80), unique=True)
    live = db.Column(db.Boolean)

    def __init__(self, title, body, posted=None, slug=None, live=True):
            self.title = title
            self.body = body
            if posted is None:
                self.posted = datetime.utcnow()
            if slug is None:
                self.slug = slugify(title)
            self.live = live

    def __repr__(self):
        return '<Post %r>' % self.title