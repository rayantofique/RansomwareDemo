#!/usr/bin/env python

import os

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
		

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)