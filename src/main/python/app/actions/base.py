from abc import ABCMeta
from abc import abstractmethod


class ActionNames():
    CREATE = 'create'
    UPDATE = 'UPDATE'
    LIST = 'list'
    DESTROY = 'destroy'


class Action():
    __metaclass__ = ABCMeta

    @abstractmethod
    @property
    def name(self):
        pass

    @abstractmethod
    @property
    def model(self):
        pass

    @abstractmethod
    @property
    def method(self):
        pass
