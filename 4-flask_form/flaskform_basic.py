from flask import Flask, render_template, session, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateTimeField, RadioField, SelectField, 
                     TextField, TextAreaField, SubmitField)
from wtforms.validators import DataRequired                     

app = Flask(__name__)

app.config['SECRET_KEY'] = 'dcn'

class InfoForm(FlaskForm):
    workedonit    = BooleanField("Have you worked on Software field?")
    workedoncloud = RadioField('Worked on any cloud:', choices = [('Y', 'Yes'), ('N', 'No')])
    cloud         = StringField("InWhich Public Cloud you are working?",validators=[DataRequired()])
    cloudchoices  = SelectField(u'Pick public cloud', choices = [('gcp', 'GCP'), ('aws', 'AWS'), ('azure', 'Azure')])
    feedback      = TextAreaField()
    submit        = SubmitField("Submit")

@app.route('/', methods = ['GET', 'POST'])
def index():

    form = InfoForm()
    if form.validate_on_submit():
        session['workedonit']    = form.workedonit.data
        session['workedoncloud'] = form.workedoncloud.data
        session['cloud']         = form.cloud.data
        session['cloudchoices']  = form.cloudchoices.data
        session['feedback']      = form.feedback.data

        flash(f"You worked in cloud {session['cloud']}")

        return redirect(url_for("thankyou"))

    return render_template('formindex.html', form = form)

@app.route('/thankyou')    
def thankyou():

    return render_template('formthankyou.html')

if __name__ == '__main__':
    app.run(debug=True)    