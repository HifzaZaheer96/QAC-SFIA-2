from application import app
import random
import csv


@app.route('/randomcolor', methods=['GET', 'POST'])
def beginning():
	with open('/opt/service_2/application/colour.txt') as exampleFile: 
		m = []
		exampleReader = csv.reader(exampleFile)
		colour =list(exampleReader)
		for i in colour:
			for j in i:
				m.append(j)
		colouroutfit=m[random.randrange(8)]
	return "Your Outfit colour is " + colouroutfit
