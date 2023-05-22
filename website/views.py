from flask import Blueprint, render_template, url_for
from flask_login import login_required, current_user
from .create_db import Blog, User
from . import db

# don't know how to query with foreign key with sqlalchemy

dummy_blog = [{'title':'Ramen Ipsum', 'published_date': 'May 10, 2023','content':'Soy sauce salt miso butter roasted pork slices flavoured oil yuzu seasoned egg spicy bean paste, kamaboko Kumamoto Tokushima Nissin instant cup ramen rice scallions bean sprouts, chilli toasted sesame seeds lard sesame oil nori bamboo slices soy milk.', 'user_id':1},{'title' :'Bacon Ipsum', 'content' : 'Beef chicken pork bacon chuck shortloin sirloin shank aute turkey, hamhock eiusmod labore laboris anim et spareribs minim, stripsteak exercitation sausage deserunt filetmignon ut kevin magna. Do officia qui hamburger eiusmod porkbelly leberkas aliquip nisi, swine chuck nostrud venison dolore sausage ea velit nulla, beef fugiat tenderloin exercitation adipisicing quis sirloin.', 'user_id':2}]

views = Blueprint('views', __name__)
#Home Page Not Signed In
@views.route('/')
def home():
    return render_template("home.html", user=current_user, blogs_data=dummy_blog)

@views.route('/dashboard')
def dashboard():
    blogs_data = dummy_blog
    return render_template("dashboard.html", user=current_user, blogs_data=blogs_data)

@views.route('/add_blog')
def add_blog():
    return render_template('add_blog.html')




