from application import app
import random
from random import choice


@app.route('/randomtheme', methods=['GET'])
def ending():

	list = ['and the theme is Disney Party','and the theme is Apocalypse Party','and the theme is Meme Party','and the theme is Candyland Party']
	
	return list[random.randrange(4)]

# def random_colour_code():
# 	hex_chars=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
# 	colour_code = '#'
# 	for i in range(0,6):
# 		colour_code = colour_code + choice(hex_chars)
# 	return colour_code
# print("The color is: ", random_colour_code())

