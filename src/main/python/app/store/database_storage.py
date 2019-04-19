"""
Storage to local database handlers
"""
import os
from contextlib import contextmanager

from PyQt5.QtCore import QStandardPaths

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from .model_base import Base

from ..settings import Settings


Base = declarative_base(cls=Base)  # pylint: disable=invalid-name


class LocalStorage():
    """File storage handler"""

    BD_BASE = Base

    def __init__(self, path):
        self.settings = self.get_settings()
        self.path = self.get_path(path)
        self.filename = self.get_filename()
        self.engine, self.session_maker = self.config_database()

        self.initialize()

    @contextmanager
    def session_context(self):
        """Database session context"""
        session = self.session_maker()
        try:
            yield session
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

    def get_session(self):
        """Get a database session"""
        return self.session_maker()

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
        engine = create_engine('sqlite:///{path}'.format(path=self.filename), echo=True)
        session_maker = sessionmaker()
        session_maker.configure(bind=engine)
        return engine, session_maker

    def initialize(self):
        """Build database if not previously configured"""
        conn = self.engine.connect()
        with self.session_context() as session:
            print('bla')
