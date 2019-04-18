from PyQt5.QtWidgets import QMainWindow
from ..widgets import STabWidget

class SMainWindow(QMainWindow):
	def __init__(self,name,title,tabs,width=800,height=600,left=0,top=0):
		super().__init__()
		self.name = name
		self.title = title
		self.left = left
		self.top = top
		self.width = width
		self.height = height
		self.setWindowTitle(self.title)
		self.setGeometry(self.left, self.top, self.width, self.height)
		 
		self.tab_widget = STabWidget(self,name=self.name+"_tab_manager",tabs=tabs)
		self.setCentralWidget(self.tab_widget)
