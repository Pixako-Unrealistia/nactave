from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])

def greetings():
    return render_template('cover.html')

@app.route('/home', methods =['GET'])
def index():
    return render_template('index.html')


@app.route('/trash')

def trash():
    return render_template('trash.html')

@app.route('/Surface_Pro')

def surface():
    return render_template('surface.html')

@app.route('/Swift_7')

def swift():
    return render_template('swift.html')

@app.route('/XPS')

def xps():
    return render_template('XPS.html')


@app.route('/Zenbook')
def Zenbook():
    return render_template('Zenbook.html')


if __name__ == "__main__":
        app.run(debug=True)
