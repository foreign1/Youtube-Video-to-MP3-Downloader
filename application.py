import os, re
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired
from pytube import YouTube
from moviepy.editor import * 
from utilFunct import *
#Initialize our app
app = Flask(__name__, instance_relative_config=False, template_folder='templates')
app.config.from_object('config.Config')

"""Form Class """
class URLForm(FlaskForm):
    downloadlink = StringField('', [InputRequired()])
    safeFileIn = StringField('', [InputRequired()])
    submit = SubmitField('Download')

#Routes
@app.route('/', methods = ['GET', 'POST'])
def home():
    form = URLForm()
    print(form.downloadlink)

    #If request method is post and form validates
    if form.validate_on_submit():
        # Download video from youtube
        downloadLink = form.downloadlink.data
        safeFileIn = form.safeFileIn.data
        #Notify user of program action
        print('Creating youtube object...')
        print('Verifying youtube video link...')
        # Create youtube object
        yt = YouTube(f'https://youtu.be/sXJXLq1lN7U')
        # Get video title
        title = yt.title
        # Normalize title
        title = titleNormalizer(title)
        # Get video with lowest resolution
        myVid = yt.streams.filter(res='360p').first()
        # Notify user of download commencement 
        print('Downloading...')
        try:
            # Download video
            myVid.download(output_path=safeFileIn, filename=title)
            # Show download status and 
            print('Download complete. File saved in: ')
            print(safeFileIn)
        except:
            print('Connection error!\nPlease try again.')


        # Convert downloaded video to audio file
        print("Converting your file, please wait a moment...")
        video = VideoFileClip(os.path.join(safeFileIn, title + '.mp4'))
        video.audio.write_audiofile(os.path.join(safeFileIn, title + '.mp3'))

        print(f'File converted. You may now access your file titled "{title}.mp3" in {safeFileIn}!')

        return 'Hey, Good job!'
    return render_template('index.html', form=form, title='YouTube video to mp3 downloader.')