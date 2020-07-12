from flask import Flask
from flask import render_template, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
  title = "Cun"
  return render_template('test.html', title=title)

@app.route('/data')
def data():
  my_data = {
    'profile': "Cun",
    'badges': ['one','two','three']
  }
  return jsonify(my_data)