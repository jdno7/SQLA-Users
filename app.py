'''main app for Blogly exercise Part 1'''

from flask import Flask, request, redirect, render_template
from models import db, connect_db, User, Post
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

from flask_debugtoolbar import DebugToolbarExtension
app.config['SECRET_KEY'] = "SECRET!"
debug = DebugToolbarExtension(app)



@app.route("/")
def list_user():
    """List users and show add form.""" 

    users = User.query.all()

    return render_template("home.html", users=users)

@app.route("/", methods=["POST"])
def add_user():
    """Add user and redirect to list."""
    

    first_name = request.form['first_name']
    last_name = request.form['last_name']
    if request.form['image_url'] != '':
        image_url = request.form['image_url']
        user = User(first_name=first_name, last_name=last_name, image_url=image_url)
    # import pdb
    # pdb.set_trace()
    user = User(first_name=first_name, last_name=last_name)
    
    db.session.add(user)
    db.session.commit()

    return redirect(f"/user/{user.id}")

@app.route("/user/<int:user_id>")
def show_user(user_id):
    """Show info on a single user."""

    user = User.query.get_or_404(user_id)
    posts = User.query.get_or_404(user_id).posts
    
    return render_template("user_detail.html", user=user, posts=posts)

@app.route("/user/<int:user_id>", methods=["POST"])
def edit_user(user_id):
    """Submit Edit user form."""

    user = User.query.get_or_404(user_id)
    
    user.first_name = request.form['first_name']
    user.last_name = request.form['last_name']
    if request.form['image_url'] != '':
        user.image_url = request.form['image_url']
        # user = User(first_name=first_name, last_name=last_name, image_url=image_url)
    # import pdb
    # pdb.set_trace()
    # user = User(first_name=first_name, last_name=last_name)
    
    db.session.add(user)
    db.session.commit()

    return redirect(f"/user/{user.id}")

@app.route('/delete/<int:user_id>')
def delete_user(user_id):
    """Delete User"""
    
    User.query.filter_by(id=user_id).delete()
    db.session.commit()

    return redirect("/")

@app.route("/post/<int:post_id>")
def post_detail(post_id):
    """Show info on a single post."""
    # import pdb
    # pdb.set_trace()
    post = Post.query.get(post_id)
    user = User.query.get(post_id)
   
    
    return render_template("post_detail.html", post=post, user=user)

    # user = User.query.get_or_404(user_id)
    # return render_template("detail.html", user=user)

@app.route("/edit/<int:post_id>")
def edit_post(post_id):

    post = Post.query.get_or_404(post_id)

    return render_template("edit_post.html", post=post)

@app.route("/edit/<int:post_id>", methods=["POST"])
def save_edit_post(post_id):

    post = Post.query.get_or_404(post_id)
    
    post.title = request.form['title']
    post.content = request.form['content']
    user_id = post.user_id
    
    
    db.session.add(post)
    db.session.commit()

    return redirect(f"/user/{user_id}")

@app.route('/delete/post/<int:post_id>')
def delete_post(post_id):
    """Delete Post"""
    
    user = Post.query.get(post_id).user_id
    Post.query.filter_by(id=post_id).delete()
    db.session.commit()

    return redirect(f"/user/{user}")

@app.route("/user/<int:user_id>/add-post")
def new_post(user_id):

    return render_template("add_post.html", user_id=user_id)

@app.route("/user/<int:user_id>/add-post", methods={"POST"})
def add_post(user_id):

    title = request.form['title']
    content = request.form['content']
    created_at = datetime.utcnow()

    p = Post(title=title, content=content, user_id=user_id, created_at=created_at)

    db.session.add(p)
    db.session.commit()

    return redirect(f"/user/{user_id}")