from ..widgets import SWidget
from ..windows import SMainWindow

class SView(object):
	def __init__(self,name):
		self.name = name

	def refresh(self):
		pass

	def clear(self):
		pass

class SSingleView(SView):
	def __init__(self,name):
		super(SSingleView, self).__init__(name)
		self.setWidget()

	def setWidget(self):
		self.widget = SWidget(None,self.name)


class SMultiView(SView):
	def __init__(self,name,views):
		self.views = {}
		self.setViews(views)
		super(SMultiView, self).__init__(name)

	def setViews(self,views):
		for v in views:
			self.views[v.name] = v

	def refresh(self):
		for key in self.view:
			self.views[key].refresh()

	def clear(self):
		for key in self.view:
			self.views[key].clear()


class SEventsView(SSingleView):
	def __init__(self):
		super(SEventsView, self).__init__("EVENTS")


class SSitesView(SSingleView):
	def __init__(self):
		super(SSitesView, self).__init__("SITES")


class SDevicesView(SSingleView):
	def __init__(self):
		super(SDevicesView, self).__init__("DEVICES")


class SItemsView(SSingleView):
	def __init__(self):
		super(SItemsView, self).__init__("ITEMS")


class SMainView(SMultiView):
	def __init__(self):
		super(SMainView, self).__init__("Selia",[SSitesView(),SEventsView(),SDevicesView(),SItemsView()])
		print(self.views)
		self.window = SMainWindow(self.name,title="Bases de datos Conabio",tabs=[self.views["SITES"].widget,self.views["EVENTS"].widget,self.views["DEVICES"].widget,self.views["ITEMS"].widget])
		
	def show(self):
		self.window.show()

