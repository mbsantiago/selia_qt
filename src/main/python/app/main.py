from .views import SMainView
from .dialogs import SAuthDialog


class Selia(object):
    def __init__(self):
        self.user = None
        self.pw = None
        self.current_collection = None
        self.init_datastore()
        self.authenticate()

    def authenticate(self):
        # Deberían de definirse las variables "user" y "pw"
        auth_dialog = SAuthDialog()
        auth_dialog.show()
        self.onAuth()
        pass

    def onAuth(self):
        self.init_ui()
        self.sync()

    def init_datastore(self):
        # Si las variables de user y pw ya están definidas se pasan a authenticate
        pass

    def init_ui(self):
        self.main_view = SMainView()
        self.main_view.show()

    def sync(self):
        pass


