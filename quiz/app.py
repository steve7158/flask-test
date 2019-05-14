import os
from flask import Flask, flash, request, redirect, url_for, render_template, jsonify
from werkzeug.utils import secure_filename
from termcolor import colored
app=Flask('__main__')

@app.route('/')
def home():
    numCorrect = request.args.get('numCorrect', 0, type=int)
    total = request.args.get('total', 0, type=int)
    print colored(numCorrect, 'red', 'on_white')
    print colored(total, 'red', 'on_white')
    return render_template('index.html')

if __name__=='__main__':
    app.secret_key='dsa123'
    app.run(debug=True)
