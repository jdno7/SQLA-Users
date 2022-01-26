'''main app for Blogly exercise Part 1'''

from flask import Flask, request, redirect, render_template
from models import db, connect_db, User, Post, Tag, PostTag
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
    p = Post.query.get(post_id)
    db.session.delete(p)
    db.session.commit()

    return redirect(f"/user/{user}")

@app.route("/user/<int:user_id>/add-post")
def new_post(user_id):

    tags = Tag.query.all()

    return render_template("add_post.html", user_id=user_id, tags=tags)

@app.route("/user/<int:user_id>/add-post", methods={"POST"})
def add_post(user_id):
   
    title = request.form['title']
    content = request.form['content']
    created_at = datetime.utcnow()

    p = Post(title=title, content=content, user_id=user_id, created_at=created_at)
    
    db.session.add(p)
    db.session.commit()
    
    tags = Tag.query.all()

    for tag in tags:
        
        if request.form.get(f"{tag.name}"):
            t = Tag.query.filter_by(name=tag.name).first()
            p.p_tags.append(t)

            
    db.session.commit()

    return redirect(f"/user/{user_id}")

@app.route("/tags")
def list_tags():
    
    tags = Tag.query.all()
    
    return render_template("list_tags.html", tags=tags)

@app.route("/tags/<int:tag_id>")
def tag_detail(tag_id):
    
    tag = Tag.query.get(tag_id)
    
    return render_template("tag_detail.html", tag=tag)

@app.route("/tags/<int:tag_id>/edit")
def edit_tag(tag_id):
    
    tag = Tag.query.get(tag_id)
    
    return render_template("edit_tag.html", tag=tag)

@app.route("/tags/<int:tag_id>/edit", methods=['POST'])
def edit_tag_post(tag_id):
    
    tag = Tag.query.get(tag_id)
    tag.name = request.form["tag_name"]

   
    db.session.add(tag)
    db.session.commit()

    return redirect("/tags")

@app.route("/tags/<int:tag_id>/delete", methods=['POST'])
def delete_tag_post(tag_id):
    # import pdb
    # pdb.set_trace()

    Tag.query.filter_by(id=tag_id).delete()
    
    db.session.commit()

    return redirect("/tags")

@app.route("/tags/new")
def create_tag_form():

    return render_template("create_tag.html")

@app.route("/tags/new", methods=['POST'])
def create_tag_():

    name = request.form['tag_name']
    tag = Tag(name=name)

    db.session.add(tag)
    db.session.commit()

    return redirect("/tags")