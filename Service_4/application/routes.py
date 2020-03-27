from application import app
import requests


@app.route('/randomoutfit', methods=['GET'])
def sentence():
    colour = requests.get('http://localhost:5001/randomcolor')
    theme = requests.get('http://localhost:5002/randomtheme')
    response = colour.text + " " + theme.text
    return response