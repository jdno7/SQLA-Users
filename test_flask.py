from unittest import TestCase

from app import app
from models import db, User, Post
from datetime import datetime

# Use test database and don't clutter tests with SQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly_db_test'
app.config['SQLALCHEMY_ECHO'] = False

# Make Flask errors be real errors, rather than HTML pages with error info
app.config['TESTING'] = True

# This is a bit of hack, but don't use Flask DebugToolbar
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

db.drop_all()
db.create_all()

class UserViewsTestCase(TestCase):
    """Tests for views for User."""

    def setUp(self):
        """Add sample User."""

        User.query.delete()

        user = User(first_name="Test", last_name="User")
        db.session.add(user)
        db.session.commit()

        self.user_id = user.id

    def tearDown(self):
        """Clean up any fouled transaction."""

        db.session.rollback()

    def test_list_users(self):
        with app.test_client() as client:
            resp = client.get("/")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('Test', html)

    def test_user_detail(self):
        with app.test_client() as client:
            resp = client.get(f"/user/{self.user_id}")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<h1>Test User</h1>', html)

    def test_default_img(self):
        with app.test_client() as client:
            resp = client.get(f"/user/{self.user_id}")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('https://www.pngitem.com/pimgs/m/150-1503945_transparent-user-png-default-user-image-png-png.png', html)

    def test_add_user(self):
        with app.test_client() as client:
            d = {"first_name": "Test2", "last_name": "User2", "image_url":""}
            resp = client.post("/", data=d, follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("<h1>Test2 User2</h1>", html)

db.drop_all()
db.create_all()

class PostViewsTestCase(TestCase):
    """Tests for views for Post."""

    def setUp(self):
        """Add sample User and Post."""

        # Post.query.delete()
        # User.query.delete()

        user = User(first_name="Test", last_name="User",)
        db.session.add(user)
        db.session.commit()

        self.user_id = user.id

        
        post = Post(title='testing', content='test content', created_at=datetime.utcnow(), user_id=user.id)
        db.session.add(post)
        db.session.commit()

        self.post_id = post.id

    def tearDown(self):
        """Clean up any fouled transaction."""

        db.session.rollback()

    # def test_list_users(self):
    #     with app.test_client() as client:
    #         resp = client.get("/")
    #         html = resp.get_data(as_text=True)

    #         self.assertEqual(resp.status_code, 200)
    #         self.assertIn('Users', html)

    def test_user_detail(self):
        with app.test_client() as client:
            resp = client.get(f"/user/{self.user_id}")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('testing', html)

    def test_default_img(self):
        with app.test_client() as client:
            resp = client.get(f"/post/{self.post_id}")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('test content', html)

    # def test_add_user(self):
    #     with app.test_client() as client:
    #         d = {"first_name": "Test2", "last_name": "User2", "image_url":""}
    #         resp = client.post("/", data=d, follow_redirects=True)
    #         html = resp.get_data(as_text=True)

    #         self.assertEqual(resp.status_code, 200)
    #         self.assertIn("<h1>Test2 User2</h1>", html)

    