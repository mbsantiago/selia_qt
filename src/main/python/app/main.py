from PyQt5.QtWidgets import QMainWindow


class Selia(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(600, 600)
        self.setWindowTitle('Selia')
        self.show()
