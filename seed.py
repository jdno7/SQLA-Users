"""Seed file to make sample data for User db."""

from models import User, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
User.query.delete()

# Add Users
# whiskey = User(first_name='John', species="dog")
# bowser = User(first_name='r', species="dog", hunger=10)
# spike = User(first_name='', species="porcupine")

# # Add new objects to session, so they'll persist
# db.session.add(whiskey)
# db.session.add(bowser)
# db.session.add(spike)

# # Commit--otherwise, this never gets saved!
# db.session.commit()
