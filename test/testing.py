import pytest
import urllib3
from flask import Flask
import os

# def test_service():
#     http = urllib3.PoolManager()
#     r = http.request('GET', 'http://localhost:80/')
#     assert 200 == r.status
    
def test_home():
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://35.197.228.70/')
    assert 200 == r.status
    
def test_submittheme():
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://35.197.228.70/submittheme/')
    assert 200 == r.status
    
def test_aboutus():
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://35.197.228.70/about')
    assert 200 == r.status
    
def test_contactus():
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://35.197.228.70/contact')
    assert 404 == r.status

# # def test_db_insert_user():
#     with app.app_context():
#         cur = mysql.connection.cursor()
#         num_of_records = cur.execute("INSERT INTO USER (first_name, second_name,username, email,message) VALUES ('Mohammed','Zaheer','MZaheer','mzaheer@gmail.com','have mickey mouse theme')")
#         mysql.connection.commit()         
#         cur.close()
#         assert 1 == num_of_records 
