from flask import Flask, render_template, url_for, redirect, request
import json
import os
from datetime import date

now = date.today()  # end date


app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('test.html')

@app.route('/home', methods=['GET'])
def back_home():
    return redirect(url_for('hello_world'));

@app.route('/<place>', methods=['GET'])
def get_trends_today(place):
    filename = os.path.join(app.static_folder, 'data', f'{place}_{now}.json')
    data = json.load(open(filename))
    return render_template('list.html', data=data)
