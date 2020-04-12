from application import app
import random
import csv


@app.route('/randomcolor', methods=['GET', 'POST'])
def beginning():
	number = random.randrange(0,7)
	with open('/opt/service_2/application/colour.txt') as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		for row in csv_reader:
			colour = str(row[number])
	return colour


    
		# list = ['Red','Yellow','Blue','Grey','Orange','Pink','Black']
		
		# return "Your Outfit colour is " + list[random.randrange(7)]