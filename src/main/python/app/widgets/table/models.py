from PyQt5.QtCore import Qt, QAbstractTableModel,QVariant

class SEventsTableModel(QAbstractTableModel):
    def __init__(self,dataArr,headerArr):
        super().__init__()
        self.arraydata = dataArr
        self.headerdata = headerArr
        
        self.setHeaderData(0, Qt.Horizontal, "ID")
        self.setHeaderData(1, Qt.Horizontal, "Fecha")
        self.setHeaderData(2, Qt.Horizontal, "Sitio")
        
    def data(self, index, role):
        if not index.isValid():
            return QVariant()
        elif role != Qt.DisplayRole:
            return QVariant()
        return QVariant(self.arraydata[index.row()][index.column()])

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return QVariant(self.headerdata[col])
        return QVariant()

    def rowCount(self, parent):
        return len(self.arraydata)

    def columnCount(self, parent):
        if len(self.arraydata) > 0: 
            return len(self.arraydata[0]) 
        return 0