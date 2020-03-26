from application import app
import random


@app.route('/randomtheme', methods=['GET'])
def ending():

	list = ['Party wear','Casual','amazing feels']
	
	return list[random.randrange(2)]