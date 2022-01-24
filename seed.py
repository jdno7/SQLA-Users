"""Seed file to make sample data for User and Post tables in db."""

from models import User, Post, db
from datetime import datetime
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
User.query.delete()
Post.query.delete()

# Add Users
JD = User(first_name='John', last_name="Hans")
Chad = User(first_name='Chad', last_name="Christian")
Bill = User(first_name='Bill', last_name="Christian")

# Add new objects to session, so they'll persist
db.session.add(JD)
db.session.add(Chad)
db.session.add(Bill)

# Commit--otherwise, this never gets saved!
db.session.commit()

# Add Posts
p1 = Post(title="Montana", content="I love Montana", user_id=1, created_at=datetime.utcnow())
p2 = Post(title="Biden", content="What the hell is going on here", user_id=1, created_at=datetime.utcnow())
p3 = Post(title="Ice Walleyes", content="nightime shallow bit is better than you think", user_id=1, created_at=datetime.utcnow())
p4 = Post(title="Lumber Prices", content="Tough to build homes when the Lumber Prices are so un-stable", user_id=2, created_at=datetime.utcnow())
p5 = Post(title="Lions Club", content="Its not all that its cracked up to be", user_id=2, created_at=datetime.utcnow())


# Add new objects to session, so they'll persist
db.session.add(p1)
db.session.add(p2)
db.session.add(p3)
db.session.add(p4)
db.session.add(p5)


# Commit--otherwise, this never gets saved!
db.session.commit()
