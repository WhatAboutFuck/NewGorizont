from PyQt5 import QtWidgets
from mydesign import Ui_Dialog

import sys


 
class mywindow(QtWidgets.QMainWindow):
	def __init__(self):
		super(mywindow, self).__init__()
		self.ui = Ui_Dialog()
		self.ui.setupUi(self)
		self.ui.pushNew.clicked.connect(self.newHuman)
		self.ui.pushConnect.clicked.connect(self.connectHuman)

	def newHuman(self):
		print("Вы новый")
	def connectHuman(self):
		print("Вы соеденены")
		
app = QtWidgets.QApplication([])
application = mywindow()
application.show()


sys.exit(app.exec())