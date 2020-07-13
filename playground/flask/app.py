from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('test.html')

@app.route('/data/')
def data():
    return 'hello world'

if __name__ == "__main__":
    app.run(debug=True)