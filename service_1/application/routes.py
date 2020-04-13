from application import app
from flask import Flask,render_template, request,redirect,url_for,flash, session
import requests
import random
from flask_mysqldb import MySQL
import os
from werkzeug.security import generate_password_hash, check_password_hash


app.config['MYSQL_HOST'] = os.environ.get('MYSQL')
app.config['MYSQL_USER'] = os.environ.get('USER')
app.config['MYSQL_PASSWORD'] = os.environ.get('PASSWORD')
app.config['MYSQL_DB'] = os.environ.get('DATABASE')
mysql = MySQL(app)
app.config['SECRET_KEY'] = 'secret'

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        details = request.form
        age = details['age']
        response = requests.get('http://service_3:5002?age='+age)

    response = requests.get('http://service_4:5003/randomoutfit')
    print(response)
    outfitgenerator = response.text
    outfit= str(outfitgenerator)
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO themesentence (theme_sentence) VALUES (%s)", [outfit])
    mysql.connection.commit()
    cur.close()
    return render_template('index.html', sentence = outfitgenerator, title = 'Home')
    


@app.route('/about')
def about():
    return render_template("about.html", title='About Us')

@app.route('/submittheme/', methods=['GET', 'POST'])
def submittheme():
    if request.method == 'POST':
        
        details=request.form
        first_name=details['first_name']
        second_name=details['second_name']
        username=details['username']
        email=details['email']
        message=details['message']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO USER (first_name,second_name, username, email,message) VALUES (%s,%s, %s, %s ,%s)", (first_name,second_name, username, email,message))
        mysql.connection.commit()
        cur.close()
        return redirect (url_for('submittheme'))

    return render_template('submittheme.html', title="submittheme")