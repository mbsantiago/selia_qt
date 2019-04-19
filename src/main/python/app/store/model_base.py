"""
Abstract class for models
"""
from abc import ABC
from abc import abstractmethod

from sqlalchemy.ext.declarative import declared_attr


class ModelBase(ABC):
    """A model represents a database tables

    This class provides auxiliary functions to
    translate between UI visualizations, DB
    entries and API json responses, all of which
    represent the same object
    """
    @declared_attr
    def __tablename__(cls): # pylint: disable=no-self-argument
        return cls.__name__.lower()  # pylint: disable=no-member

    @classmethod
    def name(cls):
        """Name of the model"""
        return cls.__name__.lower()

    @classmethod
    @abstractmethod
    def act(cls, action):
        """Main method that reacts to incoming actions from UI"""

    @classmethod
    @abstractmethod
    def get_type_info(cls):
        """Get column info"""

    @classmethod
    @abstractmethod
    def validate(cls, data):
        """Validate incoming data before inserting to database"""

    @property
    @abstractmethod
    def columns(self):
        """Columns of database table"""
