from flask import Blueprint, render_template, flash, redirect, request, url_for
from flask_login import login_required, current_user
from .create_db import Blog, User
from . import db

# don't know how to query with foreign key with sqlalchemy

views = Blueprint('views', __name__)
#Home Page Not Signed In
@views.route('/')
def home():
    blogs = Blog.query.all()
    print(blogs)
    return render_template("home.html", user=current_user, blogs_data=blogs)

@views.route('/dashboard')
def dashboard():
    blogs_data = Blog.query.filter_by(user_id = current_user.id)
    print(blogs_data)
    return render_template("dashboard.html", user=current_user, blogs_data=blogs_data)

@views.route('/blog/<id>')
def blog(id):
    blog = Blog.query.get(id)
    return render_template('blog.html', user=current_user, blog=blog)

@views.route('/add_blog', methods=['GET', 'POST'])
def add_blog():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')

        new_blog = Blog(title=title,content=content, user_id=current_user.id)
        db.session.add(new_blog)
        db.session.commit()
        flash("Posted!", category='success')
        return render_template("dashboard.html", user=current_user)

    return render_template('add_blog.html', user=current_user)

@views.route('/blog/delete/<int:id>')
def delete_blog(id):
    blog_to_delete = Blog.query.get_or_404(id)
    try:
        db.session.delete(blog_to_delete)
        db.session.commit()
        flash("Blog was deleted!", category="success")
        return render_template("dashboard.html", user=current_user)
    except:
        flash("it did not get deleted!", category="error")
    return render_template("dashboard.html", user=current_user)








