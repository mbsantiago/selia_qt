import sys
from PyQt5.QtWidgets import QDialog, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QApplication
from PyQt5.QtCore import Qt

class SDialog(object):
	def __init__(self,title,form_config):
		self.form_config = form_config
		self.title = title
		self.dialog = None
		self.layout = None
		self.fields = {}
		self.buttons = {}
		self.buildDialog()

	def buildDialog(self):
		self.dialog = QDialog()
		self.dialog.setWindowTitle(self.title)
		self.layout = QVBoxLayout(self.dialog)
		self.buildForm()
		self.buildButtons()
		self.buildButtonsLayout()

	def buildForm(self):
		for key in self.form_config:
			if self.form_config[key]["type"] == "text":
				field_layout = QHBoxLayout()
				self.fields[key] = QLineEdit(self.dialog)
				field_layout.addWidget(QLabel(self.form_config[key]["label"]+":"))
				field_layout.addWidget(self.fields[key])
				self.layout.addLayout(field_layout)

	def buildButtons(self):
		self.buttons["OK"] = QPushButton(aname,self.dialog)
		self.buttons["OK"].clicked.connect(self.close)

	def buildButtonsLayout(self):
		button_layout = QHBoxLayout()
		for key in self.buttons:
			button_layout.addWidget(self.buttons[key])
		self.layout.addLayout(button_layout)

	def close(self):
		self.dialog.accept()

	def show(self):
		self.dialog.setWindowModality(Qt.ApplicationModal)
		self.dialog.exec_()

class SAuthDialog(SDialog):
	def __init__(self,cancel_label="Cancelar",enter_label="Acceder"):
		title = "Acceso Conabio"
		form_config = {"username":{"required":True,"label":"Usuario","type":"text"},"password":{"required":True,"label":"Contraseña","type":"text"}}
		self.cancel_label = cancel_label
		self.enter_label = enter_label
		super(SAuthDialog, self).__init__(title,form_config)
		self.dialog.resize(350, 200)

	def buildButtons(self):
		self.buttons["CANCEL"] = QPushButton(self.cancel_label,self.dialog)
		self.buttons["ENTER"] = QPushButton(self.enter_label,self.dialog)
		self.buttons["CANCEL"].clicked.connect(self.handleCancel)
		self.buttons["ENTER"].clicked.connect(self.handleEnter)

	def handleCancel(self):
		app = QApplication.instance()
		sys.exit(app.exec_())

	def handleEnter(self):
		self.dialog.accept()


