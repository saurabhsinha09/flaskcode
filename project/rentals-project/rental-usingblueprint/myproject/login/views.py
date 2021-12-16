from myproject import db
from flask import Blueprint, render_template, redirect, request, url_for, flash, abort
from flask_login import login_user, login_required, logout_user
from myproject.models import Login
from myproject.login.forms import LoginForm, RegistrationForm

login_blueprint = Blueprint('login', __name__, template_folder='templates/login')

@login_blueprint.route('/welcome')
@login_required
def welcome():
    return render_template('welcome.html')    

@login_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You logged out!')
    #return redirect(url_for('home'))
    return render_template('home.html')

@login_blueprint.route('/login', methods=['GET', 'POST'])
def login():

    form = LoginForm()
    if form.validate_on_submit():
        # Grab the user from our User Models table
        user = Login.query.filter_by(email=form.email.data).first()

        try:
            if user.check_password(form.password.data) and user is not None:

                login_user(user)
                flash('Logged in successfully.')

                # If a user was trying to visit a page that requires a login
                # flask saves that URL as 'next'.
                next = request.args.get('next')

                # Check if that next exists, otherwise we'll go to
                # the welcome page.
                if next == None or not next[0]=='/':
                    next = url_for('login.welcome')

                return redirect(next)
        except:
            print('User does not exist')
            return '<h1>User does not exist</h1>'
    return render_template('login.html', form=form)      

@login_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        user = Login(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)

        db.session.add(user)
        db.session.commit()
        flash('Thanks for registering! Now you can login!')
        return redirect(url_for('login.login'))
    return render_template('register.html', form=form)