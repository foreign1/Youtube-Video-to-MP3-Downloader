from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired

#Initialize our app
app = Flask(__name__, instance_relative_config=False, template_folder='templates')
app.config.from_object('config.Config')

"""Form Class """
class URLForm(FlaskForm):
    downloadlink = StringField('', [InputRequired()])
    submit = SubmitField('Download')

#Routes
@app.route('/', methods = ['GET', 'POST'])
def home():
    form = URLForm()
    print(form.downloadlink)

    #If request method is post and form validates
    if form.validate_on_submit():
        return 'Hey, Good job!'
    return render_template('index.html', form=form, title='YouTube video to mp3 downloader.')