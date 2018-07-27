import json
import random
import requests

from flask import Flask

app = Flask(__name__)


@app.route('/enlighten_me')
def enlighten_me():
	quotes = []
	file   = open("misunderstood_wisdom.txt", "r")
	
	for quote in file:
		quotes.append(quote.rstrip("\n"))

	file.close()

	quote   = random.choice(quotes)
	payload = { "text" : quote }
	payload = json.dumps(payload)
	
	slack_webhook_url = "https://hooks.slack.com/services/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"
	requests.post(slack_webhook_url, data = payload, headers = { 'Content-type': 'application/json' })

	return quote
