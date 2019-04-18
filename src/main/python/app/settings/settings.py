from PyQt5.QtCore import QSettings


class Settings(QSettings):
    def initialize(self):
        if not self.contains('language'):
            self.setValue('language', 'es')

        if not self.contains('base_directory'):
            self.setValue('base_directory', 'selia')

        self.sync()
