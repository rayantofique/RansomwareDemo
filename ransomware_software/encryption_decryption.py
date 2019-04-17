#!/usr/bin/env python
# coding=UTF-8
import base64


import os

from Crypto.Cipher import AES
from Crypto.Util import Counter

from Crypto import Random


def pad(s):
	return s + b"\0" * (AES.block_size - len(s) % AES.block_size)

def generateEncryptionKey(bits):
	return os.urandom(bits)

def getCipher(key):
	iv = Random.new().read(AES.block_size)
	cipher = AES.new(key, AES.MODE_CBC, iv)
	return cipher

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

def encrypt_file(file_name, key):
	with open(file_name, 'rb') as fo:
	    plaintext = fo.read()
	enc = encrypt(plaintext, key)
	with open(file_name + ".enc", 'wb') as fo:
	    fo.write(enc)
	return file_name + ".enc"

def decrypt_file(file_name, key):
	with open(file_name, 'rb') as fo:
	    ciphertext = fo.read()
	dec = decrypt(ciphertext, key)
	with open(file_name[:-4], 'wb') as fo:
	   fo.write(dec)

	
		


def decryptFile(file, cipher):
	print("decrypt")

if __name__ == '__main__':
	#encrypt file and then decrtypt
	#key = generateEncryptionKey(16)	
	key = b'\x10\xcf6b\x1cD\x82\xd5\x86\x0e\xc5\xd3\x1c\\\xc2\xef'
	cipher = getCipher(key)

	print(key)

	#data = 'hello world 1234'.encode()


	#encd = encrypt(data, key)


	#print(data)
	#print(encd)

	#decd = decrypt(encd, key)

	#print(decd.decode())


	#decode 

	filePath = "C:/Users/rayan/590Ransomware/plaintext.txt.enc"
	#newFP = encrypt_file(filePath, key)
	decrypt_file(filePath, key)


	#print(plaintext.decode('cp437'))