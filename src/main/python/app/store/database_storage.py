"""
Storage to local database handlers
"""
import os
from PyQt5 import QtSql
from PyQt5.QtCore import QStandardPaths
from ..exceptions import DatabaseError
from ..settings import Settings


class LocalStorage():
    """File storage handler"""
    def __init__(self, path):
        self.settings = self.get_settings()
        self.path = self.get_path(path)
        self.filename = self.get_filename()
        self.database = self.config_database()

    def get_settings(self):  # pylint: disable=no-self-use
        """Extract storage settings from global settings file"""
        settings = Settings()
        return settings

    def get_filename(self):
        """Get name of sqlite file"""
        name = self.settings.value('storage/database_name')
        filename = os.path.join(self.path, name)
        return filename

    def get_path(self, path):
        """Get directory containing the database"""
        base_dir = self.settings.value('storage/base_dir')

        if base_dir == 'default':
            location_name = QStandardPaths.AppDataLocation
            app_storage_dir = QStandardPaths.standardLocations(location_name)[0]
            base_dir = os.path.join(app_storage_dir, 'selia')

            self.settings.setValue('storage/base_dir', base_dir)

        path = os.path.join(base_dir, path)
        if not os.path.exists(path):
            os.makedirs(path)

        return path

    def config_database(self):
        """Create and configure sqlite database"""
        database = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        database.setDatabaseName(self.filename)

        if not database.open():
            raise DatabaseError("Database could not be created correctly")

        return database
