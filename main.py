from PyQt5 import QtWidgets
from mydesign import Ui_Dialog
from full import Ui_Main_w
import sys
import time

global window_login
global main_login
 
class loginWindow(QtWidgets.QMainWindow):
	def __init__(self):
		super(loginWindow, self).__init__()
		self.log = Ui_Dialog()
		self.log.setupUi(self)
		self.log.pushNew.close()
		self.log.pushNew.clicked.connect(self.newHuman)
		self.log.pushConnect.clicked.connect(self.connectHuman)

	def newHuman(self):
		print("Вы новый")

	def connectHuman(self):
		print("Вы соеденены")
		
		window_login.close()
		main_login.show()


class mainWindow(QtWidgets.QMainWindow):
		def __init__(self):
			super(mainWindow, self).__init__()
			self.main = Ui_Main_w()
			self.main.setupUi(self)
			self.main.pushButton.clicked.connect(self.exit1)

		def exit1(self):
			print('Вы отсоедены')

			main_login.close()
			window_login.show()
			
				
app = QtWidgets.QApplication([])
window_login = loginWindow()
main_login = mainWindow()
window_login.show()



sys.exit(app.exec())