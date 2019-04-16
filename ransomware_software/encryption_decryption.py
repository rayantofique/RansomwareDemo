import os

from Crypto.Cipher import AES
from Crypto import Rando

def generateEncryptionKey(bits):
	return os.urandom(bits)

def getCipher(key):
	iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CTR, iv)
    return cipher

def encryptFile(file, cipher):

	with open(file) as f:
		plaintext = f.read()

		#encrypt and overwrite file
		ciphertext = cipher.encrypt(plaintext)
		f.seek(-len(plaintext), 1)
		f.write(ciphertext)


def decryptFile(file, cipher):
	