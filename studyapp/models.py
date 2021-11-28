from studyapp import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from studyapp import login


class User(UserMixin,db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(64),unique=True,index=True)
    password = db.Column(db.String(128))
    posts= db.relationship('Post',backref='author',lazy='dynamic')

    def set_password(self,password):
        self.password = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f'<User {self.id}:{self.username}>'

class Post(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    body = db.Column(db.String(256))
    timespam = db.Column(db.DateTime, default = datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'<Post:{self.id}:{self.body}>'

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class Flashcard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(256))
    
    def __repr__(self):
        return f'{self.body}'

class ToDo(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    todo=db.Column(db.String(64), index=True)
    
    def __repr__(self):
        return "{}".format(self.todo)

class CreateFlashcard(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    front= db.Column(db.Text)
    back = db.Column(db.Text)
    
     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

