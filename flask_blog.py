from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
import os

app = Flask(__name__)

SECRET_KEY = os.urandom(16)
app.config['SECRET_KEY'] = SECRET_KEY
# app.config['SECRET KEY'] = '9a8e6170d72c4b360c1bf9a701640ef7'
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

if __name__ == "__main__":
    app.run(debug=True)
