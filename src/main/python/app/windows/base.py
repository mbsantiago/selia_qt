from PyQt5.QtWidgets import QMainWindow
from ..widgets import STabWidget

class SMainWindow(QMainWindow):
	def __init__(self,name,title,views,width=300,height=200,left=0,top=0):
		super().__init__()
		self.name = name
		self.title = title
		self.left = left
		self.top = top
		self.width = width
		self.height = height
		self.setWindowTitle(self.title)
		self.setGeometry(self.left, self.top, self.width, self.height)

		self.widgets = {}
		for w in widgets:
			self.widgets[w.name] = w
		 
		self.tab_widget = TabWidget(self,name=self.name+"_tab_manager",tabs=widgets)
		self.setCentralWidget(self.tab_widget)
