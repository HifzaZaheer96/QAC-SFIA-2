from application import app
import random


@app.route('/randomcolor', methods=['GET', 'POST'])
def beginning():
	
	list = ['Red','Yellow','Blue','Grey','Orange','Pink','Black']
	
	return "Your Outfit colour is " + list[random.randrange(7)]