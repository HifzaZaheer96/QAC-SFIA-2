from application import app
import random
import requests
from random import choice
from flask import render_template, request


@app.route('/randomtheme', methods=['GET','POST'])
def ending():
	

		list1 = ['Disney Party','Apocalypse Party','Meme Party','Candyland Party']
		list2 = ['in Metropolis', 'in Eerie', "in King's Landing", 'in Sunnydale', 'in Bedrock', 'in South Park', 'in Atlantis', 'in Mordor', 'in Olympus', 'in Dawnstar']
		r = list1[random.randrange(4)]
		j = list2[random.randrange(10)]
		if r == 'Disney Party':
			return "and the theme is Disney Party in King's Landing"
		else:
			return "and the theme is " + r + " " + j
