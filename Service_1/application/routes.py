from application import app
from flask import render_template, request
import requests
import random

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        details = request.form
        age = details['age']
        response = requests.get('http://localhost:5002?age='+age)



    response = requests.get('http://localhost:5003/randomoutfit')
    print(response)
    outfitgenerator = response.text
    return render_template('index.html', sentence = outfitgenerator, title = 'Home')

    
