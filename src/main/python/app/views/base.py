from ..widgets import SWidget,SMapWidget,STableWidget,SEventsTableModel
from ..windows import STabMainWindow

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
		super(SEventsView, self).__init__("Eventos de muestreo")
	def setWidget(self):
		self.widget = STableWidget(None,self.name,SEventsTableModel(dataArr=[["alksjdñalksdñflkasdñfloiqief32","2017-01-18","34341lkjñlkjñlkfñlk23kl23hyu"]],headerArr=["ID","Fecha","Sitio"]))


class SSitesView(SSingleView):
	def __init__(self):
		super(SSitesView, self).__init__("Sitios")
	def setWidget(self):
		self.widget = SMapWidget(None,self.name,(21.4121622297254,-101.38183593750001),4)


class SDevicesView(SSingleView):
	def __init__(self):
		super(SDevicesView, self).__init__("Dispositivos")


class SItemsView(SSingleView):
	def __init__(self):
		super(SItemsView, self).__init__("Multimedia")


class SMainView(SMultiView):
	def __init__(self):
		super(SMainView, self).__init__("Selia",[SSitesView(),SEventsView(),SDevicesView(),SItemsView()])
		widgets = [self.views[key].widget for key in ["Sitios","Eventos de muestreo","Dispositivos","Multimedia"]]
		self.window = STabMainWindow(self.name,title="Bases de datos Conabio",widgets=widgets)

	def show(self):
		self.window.show()

