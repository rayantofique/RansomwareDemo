#!/usr/bin/env python

from win32api import GetSystemMetrics

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
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
		self.setButton('Scan Computer', self.encrypt, [150, 70], [100, 100])
		self.show()

	
	def encrypt(self):
		print("encrypt")

	def setButton(self, title, method, size, position):
		button = QPushButton('Scan Computer', self)
		button.clicked.connect(method)
		button.resize(size[0], size[1])
		button.move(position[0], position[1])




if __name__ == '__main__':
	app = QApplication([])
	ex = App()
	ex.show()
	sys.exit(app.exec_())