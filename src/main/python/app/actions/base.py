# pylint: disable=too-many-arguments
"""
Module with base class for actions.
"""
from abc import ABCMeta
from abc import abstractmethod
import inspect


class ActionNames:  # pylint: disable=too-few-public-methods
    """Basic action names"""
    CREATE = 'create'
    UPDATE = 'update'
    LIST = 'list'
    DESTROY = 'destroy'
    RETRIEVE = 'retrieve'


class ActionSpec():
    """Object representing an action.

    These correspond one-to-one with api endpoints
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    @property
    def name(self):
        """Name of action used for represtation and debug"""

    @abstractmethod
    @property
    def model(self):
        """Model which is beign affected by action"""

    @abstractmethod
    @property
    def query_parameters(self):
        """List of possible query parameters"""

    @abstractmethod
    @property
    def detail(self):
        """List of possible query parameters"""

    @abstractmethod
    @property
    def request_body_parameters(self):
        """Parameters for body of action request"""


class ActionSet():
    """Set of actions with common endpoint"""
    def is_action(self, action):  # pylint: disable=no-self-use
        """Is action filter"""
        return isinstance(action, ActionSpec)

    def get_actions(self):
        """Get all children that are actions"""
        actions = inspect.getmembers(self, self.is_action)
        return actions
