from flask import Flask, render_template
from note_storage import notes_list

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", notes_list =notes_list, enumerate=enumerate)


@app.route('/about')
def about():
    return render_template("about.html")
