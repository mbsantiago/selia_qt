from PyQt5.QtWidgets import QWidget,QTabWidget,QVBoxLayout


class SWidget(QWidget):
	def __init__(self,parent,name):
		super(SWidget, self).__init__(parent)
		self.name = name

class STabWidget(SWidget):
	def __init__(self, parent,name,tabs):
		super(STabWidget, self).__init__(parent,name)
		self.layout = QVBoxLayout(self)
		self.tab_manager = QTabWidget()
		self.tab_manager.resize(300,200)

		for tab in tabs:
			self.tab_manager.addTab(tab,tab.name)
			tab.layout = QVBoxLayout(tab)
			tab.setLayout(tab.layout)
		 
		self.layout.addWidget(self.tab_manager)
		self.setLayout(self.layout)


