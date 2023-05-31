from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from random import choice
from stories import story


app = Flask(__name__)

app.config['SECRET_KEY'] = 'SECRET'
debug = DebugToolbarExtension(app)


@app.route('/')
def homepage():
    prompts = story.prompts
    return render_template('home.html', prompts=prompts)

@app.route('/story')
def story_page():
    text = story.generate(request.args)
    return render_template('story.html', text=text)