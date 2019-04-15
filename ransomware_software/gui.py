#!/usr/bin/env python

from win32api import GetSystemMetrics
from functools import partial


import sys
import re
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
 
class App(QWidget):
 
	def __init__(self):
		super().__init__()
		self.title = 'Free Bitcoin Extractor!'
		self.left = GetSystemMetrics(0) / 2
		self.top = GetSystemMetrics(1) / 2
		self.width = 600
		self.height = 400
		self.initUI()

	def initUI(self):
		self.setWindowTitle(self.title)
		self.setGeometry(self.left, self.top, self.width, self.height)
		
		self.emailLine = self.setEmailLine()
		self.emailLine.textChanged.connect(self.changeEnableButtonStatus)

		self.decryptButton = self.setButton('Delete Viruses', self.decrypt, [150, 70], [320, 150])
		self.decryptButton.setEnabled(False)

		self.encryptButton = self.setButton('Scan Computer', self.encrypt, [150, 70], [120, 150])
		self.encryptButton.setEnabled(False)

	

		self.show()


	#Enables or disables the encryption button based on the email
	def changeEnableButtonStatus(self):
		#if len(self.emailLine.text()) > 5 and '@' in self.emailLine.text():
		if isValidEmail(self.emailLine.text()):
			self.encryptButton.setEnabled(True)
		else:
			self.encryptButton.setEnabled(False)
	
	def setEmailLine(self):
		self.emailLine = QLineEdit(self)
		self.emailLine.setPlaceholderText("Please enter your email here to use antivirus")
		self.emailLine.move(120, 80)
		self.emailLine.resize(340, 50)
		return self.emailLine

	def encrypt(self):
		print(self.emailLine.text())
		#encryption goes here
		#
		self.decryptButton.setEnabled(True)

	def decrypt(self):
		#decryption goes here
		print("decrypt")

	def setButton(self, title, method, size, position):
		button = QPushButton(title, self)
		button.clicked.connect(method)
		button.resize(size[0], size[1])
		button.move(position[0], position[1])
		return button


def isValidEmail(email):
	return bool(re.match("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email)) and len(email) > 7

if __name__ == '__main__':
	app = QApplication([])
	ex = App()
	ex.show()
	sys.exit(app.exec_())