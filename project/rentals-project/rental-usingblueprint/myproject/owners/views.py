#Owners views.py
from flask import Blueprint, render_template, redirect, url_for
from myproject import db
from myproject.models import Owner
from myproject.owners.forms import AddForm, DelForm 

owners_blueprint = Blueprint('owners', __name__, template_folder='templates/owners')

@owners_blueprint.route('/add', methods=['GET', 'POST'])
def add_owner():
    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data

        # Add new owner to database
        new_owner = Owner(name, email)
        db.session.add(new_owner)
        db.session.commit()

        return redirect(url_for("owners.thankyou"))

    return render_template('add.html',form=form)

@owners_blueprint.route('/thankyou')   
def thankyou():
    return render_template('thankyou.html')  

@owners_blueprint.route('/owners') 
def all_owner():
    # Grab a list of vehicles from database.
    owners = Owner.query.all()
    return render_template('list.html', owners = owners)     

@owners_blueprint.route('/delete', methods=['GET', 'POST'])
def del_owner():

    form = DelForm()

    if form.validate_on_submit():
        owner_id = form.owner_id.data
        owner = Owner.query.get(owner_id)
        db.session.delete(owner)
        db.session.commit()

        return redirect(url_for('owners.all_owner'))

    return render_template('delete.html',form=form)      