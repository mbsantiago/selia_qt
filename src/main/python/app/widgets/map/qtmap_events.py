def goCoords():
    def resetError():
        coordsEdit.setStyleSheet('')

    try:
        latitude, longitude = coordsEdit.text().split(",")
    except ValueError:
        coordsEdit.setStyleSheet("color: red;")
        QTimer.singleShot(500, resetError)
    else:
        map.centerAt(latitude, longitude)
        # map.moveMarker("MyDragableMark", latitude, longitude)


def onMarkerMoved(key, latitude, longitude):
    print("Moved!!", key, latitude, longitude)
    coordsEdit.setText("{}, {}".format(latitude, longitude))


def onMarkerRClick(key):
    print("RClick on ", key)
    # map.setMarkerOptions(key, draggable=False)


def onMarkerLClick(key):
    print("LClick on ", key)


def onMarkerDClick(key):
    print("DClick on ", key)
    # map.setMarkerOptions(key, draggable=True)


def onMapMoved(latitude, longitude):
    print("Moved to ", latitude, longitude)


def onMapRClick(latitude, longitude):
    print("RClick on ", latitude, longitude)


def onMapLClick(latitude, longitude):
    print("LClick on ", latitude, longitude)


def onMapDClick(latitude, longitude):
    print("DClick on ", latitude, longitude)