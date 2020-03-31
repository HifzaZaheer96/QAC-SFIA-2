from application import app
from flask import render_template, request
import requests
import random

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        details = request.form
        age = details['age']
        response = requests.get('http://service_3:5002?age='+age)



    response = requests.get('http://service_4:5003/randomoutfit')
    print(response)
    outfitgenerator = response.text
    return render_template('index.html', sentence = outfitgenerator, title = 'Home')


@app.route('/about')
def about():
    return render_template("about.html", title='About Us')
