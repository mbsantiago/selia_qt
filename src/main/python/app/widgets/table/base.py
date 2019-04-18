from ..base import SWidget
from PyQt5.QtWidgets import QVBoxLayout,QTableView,QApplication,QStyleFactory,QHeaderView
from PyQt5 import QtGui


class STableWidget(SWidget):
    def __init__(self,parent,name,model):
        super(STableWidget, self).__init__(parent,name)
        self.layout = QVBoxLayout(self)
        self.model = model
        self.buildTable()
        QApplication.setStyle(QStyleFactory.create('Cleanlooks'))
        self.setLayout(self.layout)

    def buildTable(self):
        self.table = QTableView(self)
        self.table.setModel(self.model)

        header = self.table.horizontalHeader()       
        for i in range(self.model.columnCount(None)):
        	header.setSectionResizeMode(i, QHeaderView.Stretch)

        self.layout.addWidget(self.table)




