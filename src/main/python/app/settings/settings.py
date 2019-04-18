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
            for key in defaults[section]:
                if not self.contains(key):
                    value = defaults[section][key]
                    config_key = '{}/{}'.format(section, key)
                    self.setValue(config_key, value)

        self.sync()

    def __repr__(self):
        return str(dir(self))
