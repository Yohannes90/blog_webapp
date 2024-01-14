from flask import render_template, url_for, flash, redirect
from flask_blog import app
from flask_blog.forms import RegistrationForm, LoginForm
from flask_blog.models import User, Post


posts = [
    {
        'author': 'Yohannes Mekonnen',
        'title': 'blog post 1',
        'content': 'first post content',
        'date_posted': 'April 2, 2024'
    },
    {
        'author': 'Jane Doe',
        'title': 'blog post 2',
        'content': 'post content',
        'date_posted': 'April 20, 2024'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='about')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Successfully created new account for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash(f'You have Successfully Logged In!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)
