from application import app
from flask import render_template, request
import requests
import random

@app.route('/', methods=['GET'])
def home():
    
    response = requests.get('http://localhost:5003/randomoutfit')
    print(response)
    outfitgenerator = response.text
    return render_template('index.html', sentence = outfitgenerator, title = 'Home')

