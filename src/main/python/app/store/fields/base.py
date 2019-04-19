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

    @abstractmethod
    def to_sql(self):
        pass

    @abstractmethod
    def to_json(self):
        pass

    @abstractmethod
    def from_json(self):
        pass

    @abstractmethod
    def validate(self):
        pass
