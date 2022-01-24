'''Models for Blogly Exercise'''

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime 

db = SQLAlchemy()

def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)


class User(db.Model):
    """User."""

    __tablename__ = "users"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    first_name = db.Column(db.String(25),
                     nullable=False
                     )
    last_name = db.Column(db.String(25),
                     nullable=False
                     )
    image_url = db.Column(db.String(), nullable=True, default='https://www.pngitem.com/pimgs/m/150-1503945_transparent-user-png-default-user-image-png-png.png')

    posts = db.relationship("Post")

    def __repr__(self):
        """Show info about user."""

        u = self
        return f"<User {u.id} {u.first_name} {u.last_name} {u.image_url}>"


class Post(db.Model):
    """Post."""

    __tablename__ = "posts"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    title = db.Column(db.Text,
                     nullable=False
                     )
    content = db.Column(db.Text,
                     nullable=False
                     )
    created_at = db.Column(db.DateTime)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='cascade'))

    user = db.relationship("User",
                            backref="user" )

    

    



    def __repr__(self):
        """Show info about post."""

        p = self
        return f"<Post {p.id} {p.title} {p.content} {p.created_at} {p.user_id} >"

 