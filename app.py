from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from random import choice
from stories import stories


app = Flask(__name__)

app.config['SECRET_KEY'] = 'SECRET'
debug = DebugToolbarExtension(app)


@app.route('/')
def homepage():
    return render_template('select.html', stories=stories.values())

   

@app.route('/form')
def ask_questions():
    story_id = request.args["story_id"]
    story = stories[story_id]
    prompts = story.prompts
    return render_template("form.html", story_id=story_id, title=story.title, prompts=prompts)


@app.route('/story')
def story_page():
    
    story_id = request.args["story_id"]
    story = stories[story_id]

    text = story.generate(request.args)

    return render_template("story.html", title=story.title, text=text)