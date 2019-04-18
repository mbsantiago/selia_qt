from PyQt5.QtWidgets import QVBoxLayout,QHBoxLayout,QSizePolicy
from ..base import SWidget
from .qtmap import Map
from .qtmap_events import *

class SMapWidget(SWidget):
    def __init__(self, parent,name,init_center,init_zoom):
        super(SMapWidget, self).__init__(parent,name)
        self.layout = QVBoxLayout(self)
        self.init_zoom = init_zoom
        self.init_center = init_center
        self.buildMap()
        self.setLayout(self.layout)

    def buildMap(self):
        self.map = Map(self)
        self.map.mapMoved.connect(onMapMoved)
        self.map.markerMoved.connect(onMarkerMoved)
        self.map.mapClicked.connect(onMapLClick)
        self.map.mapDoubleClicked.connect(onMapDClick)
        self.map.mapRightClicked.connect(onMapRClick)
        self.map.markerClicked.connect(onMarkerLClick)
        self.map.markerDoubleClicked.connect(onMarkerDClick)
        self.map.markerRightClicked.connect(onMarkerRClick)
        self.layout.addWidget(self.map)
        self.map.setSizePolicy(QSizePolicy.MinimumExpanding,QSizePolicy.MinimumExpanding)
        self.map.waitUntilReady()
        self.map.centerAt(*self.init_center)
        self.map.setZoom(self.init_zoom)



