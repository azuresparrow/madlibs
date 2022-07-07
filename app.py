from flask import Flask, render_template, request
from stories import story

app = Flask(__name__)

@app.route('/')
def give_prompts():

    return render_template('madlibs.html', prompts=story.prompts)

@app.route('/story')
def tell_story():
    text = story.generate(request.args)
    return render_template('story.html', text=text)