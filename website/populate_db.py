from .create_db import Blog, User
from . import db
from . import create_app
from werkzeug.security import generate_password_hash

def populateDB():
    app = create_app()
    with app.app_context():
        blog1 = Blog(title='Ramen Ipsum', content='Soy sauce salt miso butter roasted pork slices flavoured oil yuzu seasoned egg spicy bean paste, kamaboko Kumamoto Tokushima Nissin instant cup ramen rice scallions bean sprouts, chilli toasted sesame seeds lard sesame oil nori bamboo slices soy milk.', user_id=1)
        blog2 = Blog(title ='Bacon Ipsum', content = 'Beef chicken pork bacon chuck shortloin sirloin shank aute turkey, hamhock eiusmod labore laboris anim et spareribs minim, stripsteak exercitation sausage deserunt filetmignon ut kevin magna. Do officia qui hamburger eiusmod porkbelly leberkas aliquip nisi, swine chuck nostrud venison dolore sausage ea velit nulla, beef fugiat tenderloin exercitation adipisicing quis sirloin.', user_id=2)
        user1 = User(email='swalters@gmail.com', name='Sasha Walters', password=generate_password_hash(
                    'sfisdfo12', method='sha256'))
        user2 = User(email='vbender132@yahoo.com', name='Vance Bender', password=generate_password_hash(
                    '!sfsi13', method='sha256')),
    
        db.session.add(blog1)
        db.session.add(blog2)
        db.session.add(user1)
        db.session.add(user2)
        db.session.commit()
    print("populate tables successfully")

if __name__ == "__main__":
    populateDB()