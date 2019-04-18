import sys
import os
from PyQt5.QtWidgets import QMainWindow,QAction,QMenu,QApplication
from PyQt5.QtGui import QIcon
from ..widgets import STabWidget


class SMainWindow(QMainWindow):
    def __init__(self,name,title,widgets,width=800,height=600,left=0,top=0):
        super().__init__()
        self.name = name
        self.title = title
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.widget_organizer = None
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.buildMenus()
        self.buildToolbar()
        self.setWidgets(widgets)

    def buildMenus(self):
        menu_bar = self.menuBar()
        # Construcción de menúes
        file_menu = QMenu("Archivo",self)
        preference_menu = QMenu("Preferencias",self)
        account_menu = QMenu("Cuenta",self)

        # Construcción de acciones
        close_action = QAction("Cerrar",self)
        close_action.setShortcut("Ctrl+Q")
        close_action.triggered.connect(self.close)
        change_dir_action = QAction("Cambiar directorio base",self)
        change_dir_action.setShortcut("Ctrl+D")
        change_dir_action.triggered.connect(self.changeBaseDir)
        edit_account_action = QAction("Editar",self)
        edit_account_action.setShortcut("Ctrl+E")
        edit_account_action.triggered.connect(self.editUserAccount)

        # Asociación de acciones
        file_menu.addAction(close_action)
        preference_menu.addAction(change_dir_action)
        account_menu.addAction(edit_account_action)

        # Asociación de menúes
        menu_bar.addMenu(file_menu)
        menu_bar.addMenu(preference_menu)
        menu_bar.addMenu(account_menu)
    
    def buildToolbar(self):
        nav_tbar = self.addToolBar("Navegación")
        img_path = os.path.join("/home/evr/Conabio/snmb/acoustics/code/selia_qt/src/main/icons/base/home_32.png")
        home_action = QAction(QIcon(img_path),"Inicio",self)
        nav_tbar.addAction(home_action)




    def close(self):
        app = QApplication.instance()
        sys.exit(app.exec_())

    def changeBaseDir(self):
        pass

    def editUserAccount(self):
        pass

    def setWidgets(self,widgets):
        pass


class STabMainWindow(SMainWindow):
    def setWidgets(self,widgets):
        self.widget_organizer = STabWidget(self,name=self.name+"_tab_manager",tabs=widgets)
        self.setCentralWidget(self.widget_organizer)


