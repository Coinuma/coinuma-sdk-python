import inspect
import pprint
from typing import Iterable


class Model:

    def to_dict(self) -> dict:
        """Returns the model properties as a dict"""
        attrs = inspect.getmembers(self, lambda a: not(inspect.isroutine(a)))
        properties = [a[0] for a in attrs if not(a[0].startswith('_') and a[0].endswith('__')) and not a[0].startswith('_')]
        return {p: getattr(self, p) for p in properties}

    def to_str(self) -> str:
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __iter__(self) -> Iterable:
        return iter(self.to_dict().items())

    def __repr__(self) -> str:
        return self.to_str()

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: object) -> bool:
        return not self == other
