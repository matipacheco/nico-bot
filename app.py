import random

from flask import Flask
from flask import jsonify
from flask import render_template

app = Flask(__name__)


@app.route('/enlighten_me')
def enlighten_me():
	quotes = []
	file   = open("misunderstood_wisdom.txt", "r")
	
	for quote in file:
		quotes.append(quote.rstrip("\n"))

	file.close()

	return jsonify(quote = random.choice(quotes))
