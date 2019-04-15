from flask import Flask
from flask import request
from flask import json

import keyscript as ks

app = Flask(__name__)

@app.route('/')
def api_root():
	return 'Hello World'

@app.route('/savekey', methods = ['POST'])
def api_savekey():
	if request.headers['Content-Type'] == 'application/json':
		ks.saveKey(request.json)
		return ""

@app.route('/fetchkey', methods = ['POST'])
def api_fetchkey():
	if request.headers['Content-Type'] == 'application/json':
		return ks.fetchKey(request.json)
		