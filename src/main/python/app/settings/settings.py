"""
Settings for Selia app
"""
import configparser
from PyQt5.QtCore import QSettings


class Settings(QSettings):
    """Simple wrapper around Qt Settings class"""

    def initialize(self, config_file):
        """Set default settings at startup"""
        defaults = configparser.ConfigParser()
        defaults.read(config_file)

        for section in defaults.sections():
            self.beginGroup(section)
            for key in defaults[section]:
                if not self.contains(key):
                    value = defaults[section][key]
                    self.setValue(key, value)
            self.endGroup()

        self.sync()

    def __repr__(self):
        return str(dir(self))
