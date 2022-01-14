'''main app for Blogly exercise Part 1'''

from flask import Flask, request, redirect, render_template
from models import db, connect_db, User

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

    return redirect(f"/{user.id}")

@app.route("/<int:user_id>")
def show_user(user_id):
    """Show info on a single user."""

    user = User.query.get_or_404(user_id)
    
    return render_template("detail.html", user=user)

@app.route("/<int:user_id>", methods=["POST"])
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

    return redirect(f"/{user.id}")

@app.route('/delete/<int:user_id>')
def delete_user(user_id):
    """Delete User"""
    
    User.query.filter_by(id=user_id).delete()
    db.session.commit()

    return redirect("/")



    # user = User.query.get_or_404(user_id)
    # return render_template("detail.html", user=user)
