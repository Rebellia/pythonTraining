#!/usr/bin/env python3

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('hello.html')

@app.route('/hello/<user>')
def hello_name(user):
    return render_template('hello.html', namey5 = user)

@app.route('/score/<int: score>')
def report_score(score):
    return render_template('score.html', marks = score)

if __name__ == '__main__':
    app.run(port=5060)
