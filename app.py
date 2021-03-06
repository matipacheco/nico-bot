import json
import random
import requests
import unidecode

from flask import Flask
from flask import jsonify
from flask import request


app = Flask(__name__)


@app.route('/enlighten_me', methods = ('GET', 'POST'))
def enlighten_me():
	quotes = []

	text   = request.form.get("text").lower()
	text   = unidecode.unidecode(text)
	text   = text.replace("_","").replace("*","").replace("¿","").replace("?","").replace("!","").replace("¡","").replace("~","")
	
	valid_words = ["podria", "puedo", "podemos", "podriamos", "puede"]

	if (set(valid_words) & set(words)):
		file = open("absolutely_no.txt", "r")

	else:
		file = open("misunderstood_wisdom.txt", "r")
	

	for quote in file:
		quotes.append(quote.rstrip("\n"))

	file.close()
	quote = random.choice(quotes)

	return jsonify(text = quote, response_type = "in_channel")