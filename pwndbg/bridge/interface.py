from abc import ABCMeta, abstractmethod
from typing import Optional


class IDbg(metaclass=ABCMeta):
    @abstractmethod
    def execute(self, cmd: str, /, from_tty: bool = False, to_string: bool = False) -> Optional[str]:
        pass
