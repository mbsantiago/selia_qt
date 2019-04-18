from abc import ABC
from abc import abstractmethod



class Field(ABC):
    @property
    @abstractmethod
    def required(self):
        pass

    @property
    @abstractmethod
    def type(self):
        pass


class Model(ABC):
    @classmethod
    def name(cls):
        return str(cls.__name__).lower()

    @abstractmethod
    def act(self, action):
        pass

    @classmethod
    @abstractmethod
    def get_type_info(cls):
        pass

    @classmethod
    @abstractmethod
    def validate(self, data):
        pass
