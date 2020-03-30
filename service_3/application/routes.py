from application import app
import random
import requests
from random import choice
from flask import Flask, render_template, request, session

app.config['SECRET_KEY'] = 'secret'

session = []

@app.route('/', methods=['POST', 'GET'])
def age():
	print(request.args.get('age'))
	age = int(request.args.get('age'))
	session['age'] = session.append(age)
	return request.args.get('age')


@app.route('/randomtheme', methods=['GET','POST'])
def ending():
	print(session)
	list1 = ['Disney Party','Apocalypse Party','Princess Party','Candyland Party']
	list2 = ['in Metropolis', 'in Eerie', "in King's Landing", 'in Sunnydale', 'in Bedrock', 'in South Park', 'in Atlantis', 'in Mordor', 'in Olympus', 'in Dawnstar']
	list3 = ['Beach Party', 'BBQ Party', 'Unicorn Party', 'Halloween Party']
	ticket = f'{random.randint(1, 100)}'
	r = list1[random.randrange(4)]
	j = list2[random.randrange(10)]
	d = list3[random.randrange(4)] 
	if session == [] :
		return ". Please enter age for Specific Theme!"
	if session[-1] <= 12:
		for i in range(0,len(r)):
			letter = r[i][0]
			if (letter == "A" ):
				x = random.randrange(4)
				print(x)
				if x == 0:
					return "and the theme is " + r + " " + j +".Your ticket price is £100\n(25% chance)"
				if x > 0:
					return "and the theme is " + r + " " + j +" .Your ticket price is £50\n(75% chance)"
		if r == 'Disney Party':
			return "and the theme is Disney Party in King's Landing for FREE!\n" +" " + "You have been the Lucky Winner!" 
		if r =="Princess Party":
			return " and the theme is Princess Party. You get FREE Entry Princess!"
		else:
			return "and the theme is " + r + " " + j +". Your Ticket price is £" + ticket
	else:
		return "and the theme is " + d + " " + j +". Your Ticket price is £" + ticket

		

