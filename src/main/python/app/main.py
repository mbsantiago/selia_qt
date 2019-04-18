from .views import SAuthView, SMainView

class Selia(object):
	def __init__(self):
		self.pw = None
		self.user = None
		self.base_dir = None
		self.current_collection = None
		self.settings = None
		self.authenticate()

	def authenticate(self):
		self.auth_view = SAuthView(self)
		self.auth_view.show()

	def onAuth(self):
		self.loadSettings()
		self.initStorage()
		self.initUI()

	def initUI(self):
		self.main_view = SMainView(self)
		self.main_view.show()
		self.sync()

	def loadSettings(self):
		pass

	def initStorage(self):
		pass

	def sync(self):
		pass





