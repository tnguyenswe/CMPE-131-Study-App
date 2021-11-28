from studyapp import studyapp_obj
from flask import render_template, flash, redirect,request
from studyapp.forms import LoginForm, SignupForm, UploadForm, ToDoForm,FlashCardForm
from studyapp.models import User,Post,ToDo,CreateFlashcard
from flask_login import current_user,login_user,logout_user,login_required
from studyapp import db
from werkzeug.utils import secure_filename
import pdfkit
from markdown import markdown
import os

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

#convert markdown to flash card
@studyapp_obj.route("/md_to_flashcard", methods=['GET', 'POST'])
def markdown_to_flashcard():
    import markdown.extensions.fenced_code
    form = UploadForm()
    if form.validate_on_submit():
        # get file name from form
        filename = secure_filename(form.file.data.filename)
        # save the md file in a flashcards directory
        form.file.data.save("studyapp/flashcards/" + filename)
        # open the md file
        open_file = open("studyapp/flashcards/" + filename, "r")
        # convert md to html so render template can render it
        md_template_string = markdown.markdown(
        open_file.read(), extensions=["fenced_code", "codehilite"]
        )
        return render_template('md_to_flashcard.html', form=form, success=True, md_file = md_template_string)
    return render_template('md_to_flashcard.html', form=form)

# convert flashcard (html) to pdf
@studyapp_obj.route('/flashcard_to_pdf', methods=['GET', 'POST'])
def flashcard_to_pdf():
    import pdfkit
    form = UploadForm()
    if form.validate_on_submit():
        filename = secure_filename(form.file.data.filename)
        # save the md file in a flashcards directory
        form.file.data.save("studyapp/flashcards/" + filename)
        input_filename = 'studyapp/flashcards/' + filename
        output_filename = input_filename.split(".html")
        output_filename = output_filename[0] + '.pdf'
        pdfkit.from_file(input_filename, output_filename)
        return render_template('flashcard_to_pdf.html', form=form, pdf=output_filename)        
    return render_template('flashcard_to_pdf.html', form=form)
    
# convert markdown to pdf
@studyapp_obj.route('/md_to_pdf', methods=['GET', 'POST'])
def md_to_pdf():
    form = UploadForm()
    if form.validate_on_submit():
        # get file name from form
        filename = secure_filename(form.file.data.filename)
        # save the md file in a flashcards directory
        form.file.data.save("studyapp/flashcards/" + filename)
        # save the md file name and change to pdf file name
        input_filename = 'studyapp/flashcards/' + filename
        output_filename = input_filename.split(".md")
        output_filename = output_filename[0] + '.pdf'
        
        #convert md file to pdf file
        with open(input_filename, 'r') as f:
            html_text = markdown(f.read(), output_format='html4')
        pdfkit.from_string(html_text, output_filename)
        return render_template('md_to_pdf.html', form=form, pdf=output_filename)
    
    return render_template('md_to_pdf.html', form=form)

#render markdown
@studyapp_obj.route('/render_md', methods=['GET', 'POST'])
def render_md():
    import markdown.extensions.fenced_code
    form = UploadForm()
    if form.validate_on_submit():
        # get file name from form
        filename = secure_filename(form.file.data.filename)
        # save the md file in a render_md directory
        form.file.data.save("studyapp/render_md/" + filename)
        # open the md file
        open_file = open("studyapp/render_md/" + filename, "r")
        # convert md to html
        md_template_string = markdown.markdown(
        open_file.read(), extensions=["fenced_code", "codehilite"]
        )
        return md_template_string
    return render_template('render_md.html', form=form)

@studyapp_obj.route("/pomorodo")
def pomorodotimer():
    return render_template("pomorodo.html")
@studyapp_obj.route("/todo",methods=['GET','POST'])
def todo_list():
    form=ToDoForm()
    todolist=ToDo.query.all()
    if form.validate_on_submit():
        item=ToDo(todo=form.todo.data)
        db.session.add(item)
        db.session.commit()
        return redirect ('/todo')
    return render_template('todo.html',form=form,todolist=todolist)

@studyapp_obj.route("/flashcard", methods=['GET', 'POST'])
def create_flashcards():
    form = FlashCardForm()
    user_flashcards = CreateFlashcard.query.filter_by(user=current_user).all()
    if form.validate_on_submit():
        flashcard = CreateFlashcard(front=form.front.data, back=form.back.data, user=current_user)
        db.session.add(CreateFlashcard)
        db.session.commit()
        flash('Flash Card Created Successfully', 'success')
        return redirect(url_for('create_flashcards'))
    return render_template('createflashcard.html', form=form, user_flashcards=user_flashcards)



