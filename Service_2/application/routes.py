from application import app
import random


@app.route('/randomcolor', methods=['GET'])
def beginning():

	list = ['Red','Yellow','Blue']
	
	return list[random.randrange(2)]