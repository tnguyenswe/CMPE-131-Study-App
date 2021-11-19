from studyapp import studyapp_obj
from flask import render_template, flash, redirect,request
from studyapp.forms import LoginForm, SignupForm
from studyapp.models import User,Post
from flask_login import current_user,login_user,logout_user,login_required
from studyapp import db


@studyapp_obj.route("/loggedin")
@login_required
def log():
    return render_template('loggedin.html')

@studyapp_obj.route("/loggedout")
def logout():
    logout_user()
    return redirect('/')


@studyapp_obj.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user=User.query.filter_by(username=form.username.data).first()
        login_user(user)
        return redirect('/loggedin')
    return render_template('login.html',form=form)


@studyapp_obj.route('/signup',methods=['GET','POST'])
def signup():
    form=SignupForm()
    all_users=User.query.all()
    if form.validate_on_submit():
        u=User(username=form.username.data,password=form.password.data)
        db.session.add(u)
        db.session.commit()
        return redirect ('/login')
    return render_template('signup.html',form=form)


@studyapp_obj.route('/')
def home():
    title = "Homepage"
    return render_template('home.html',title=title)
