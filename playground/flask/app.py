from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    name="kwin"
    return render_template('play.html',name=name)
