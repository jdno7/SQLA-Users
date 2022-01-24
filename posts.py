'''Models for Blogly Exercise'''

from email.policy import default
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime 
from sqlalchemy.sql import func

db = SQLAlchemy()

def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)


class Post(db.Model):
    """Post."""

    __tablename__ = "posts"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    title = db.Column(db.text,
                     nullable=False
                     )
    content = db.Column(db.text,
                     nullable=False
                     )
    created_at = db.Column(db.DateTime, default=datetime.utcnow(),update=datetime.utcnow())

    # user_id = db.Column(db.String(), nullable=True, default='https://www.pngitem.com/pimgs/m/150-1503945_transparent-user-png-default-user-image-png-png.png')

    def __repr__(self):
        """Show info about post."""

        p = self
        return f"<Post {p.id} {p.title} {p.content} {p.created_at} {p.user_id}>"

    def time_stamp(self):
        time = datetime.now(tz=None)