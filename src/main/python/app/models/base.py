from abc import ABCMeta
from abc import abstractmethod


class Model():
    __metaclass__ = ABCMeta

    @abstractmethod
    def act(self, action):
        pass
