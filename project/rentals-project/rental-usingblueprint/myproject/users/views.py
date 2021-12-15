#Users views.py
from flask import Blueprint, render_template, redirect, url_for
from myproject import db
from myproject.models import User
from myproject.users.forms import AddForm, DelForm 

users_blueprint = Blueprint('users', __name__, template_folder='templates/users')

@users_blueprint.route('/add', methods=['GET', 'POST'])
def add_user():
    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data

        # Add new owner to database
        new_user = User(name, email)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for("users.thankyou"))

    return render_template('user.html',form=form) 

@users_blueprint.route('/thankyou')   
def thankyou():
    return render_template('thankyou.html')      

@users_blueprint.route('/users') 
def all_user():
    # Grab a list of vehicles from database.
    users = User.query.all()
    return render_template('list_u.html', users = users) 

@users_blueprint.route('/delete', methods=['GET', 'POST'])    
def del_user():

    form = DelForm()

    if form.validate_on_submit():
        user_id = form.user_id.data
        user = User.query.get(user_id)
        db.session.delete(user)
        db.session.commit()

        return redirect(url_for('users.all_user'))

    return render_template('delete_u.html',form=form)