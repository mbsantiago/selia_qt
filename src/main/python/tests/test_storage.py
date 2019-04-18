"""
Test module for storage object
"""
# pylint: disable=redefined-outer-name, unused-argument
import os
import platform
import shutil
import pytest

from PyQt5.QtWidgets import QApplication

from app.store.database_storage import LocalStorage
from app.settings import Settings


BASE_DIR = os.path.dirname(__file__)


def get_app_storage_dir():
    """Get default app storage directory"""
    system = platform.system()

    if system == 'Darwin':
        home = os.path.expanduser('~')
        directory = os.path.join(
            home,
            'Library',
            'Application Support',
            'selia')

    else:
        raise NotImplementedError

    return directory

@pytest.fixture()
def qt_app():
    """Create a Qt application for context"""
    app = QApplication([])
    yield
    del app


@pytest.fixture()
def initialize_settings():
    """Set default settings"""
    settings_file = os.path.join(
        os.path.dirname(os.path.dirname(BASE_DIR)),
        'resources',
        'base',
        'settings.ini')

    settings = Settings()
    settings.initialize(settings_file)

@pytest.fixture()
def local_test_dir():
    """Setup test directory in app storage dir"""
    app_dir = get_app_storage_dir()
    path = os.path.join(app_dir, 'test')

    if os.path.exists(path):
        shutil.rmtree(path)
    os.makedirs(path)

    yield

    shutil.rmtree(path)


class DummyStorage(LocalStorage):
    """Fake database storage class"""
    def __init__(self):  # pylint: disable=super-init-not-called
        self.settings = self.get_settings()


def test_database_path_setting(initialize_settings):
    """Check if path associated to database is correct when default"""
    storage = DummyStorage()
    path = storage.get_path('')
    expected_path = os.path.join(get_app_storage_dir(), '')
    assert path == expected_path


def test_database_creation(initialize_settings, local_test_dir, qt_app):
    """Check for creation of database"""
    storage = LocalStorage('test')

    app_dir = get_app_storage_dir()
    expected_filename = os.path.join(
        app_dir,
        'test',
        'selia.db')

    assert expected_filename == storage.filename
    assert os.path.exists(expected_filename)
