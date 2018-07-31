import json
import random
import requests

from flask import Flask
from flask import jsonify


app = Flask(__name__)


@app.route('/enlighten_me', methods = ('GET', 'POST'))
def enlighten_me():
	quotes = []
	file   = open("misunderstood_wisdom.txt", "r")
	
	for quote in file:
		quotes.append(quote.rstrip("\n"))

	file.close()

	quote   = random.choice(quotes)
	
	return jsonify(text = quote, response_type = "in_channel", delete_original = True)