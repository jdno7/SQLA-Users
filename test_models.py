from unittest import TestCase

from app import app
from models import db, User

# Use test database and don't clutter tests with SQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///sqla_intro_test'
app.config['SQLALCHEMY_ECHO'] = False

db.drop_all()
db.create_all()

class UserModelTestCase(TestCase):
    """Tests for User Model"""

    def setUp(self):
        """Clean up any existing Users"""
        User.query.delete()

    def tearDown(self):
        """Clean up any session data"""

        db.session.rollback()

    