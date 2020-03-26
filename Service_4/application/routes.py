from application import app
import requests


@app.route('/randomoutfit', methods=['GET'])
def sentence():
    beginning = requests.get('http://localhost:5001/randomcolor')
    ending = requests.get('http://localhost:5002/randomtheme')
    response = beginning.text + " " + ending.text
    return response