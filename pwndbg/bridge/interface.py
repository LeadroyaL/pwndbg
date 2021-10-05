from abc import ABCMeta, abstractmethod
from typing import Optional, Union


class IDbg(metaclass=ABCMeta):
    @abstractmethod
    def execute(self, cmd: str, /, from_tty: bool = False, to_string: bool = False) -> Optional[str]:
        pass

    @abstractmethod
    def read(self, addr: int, count: int, partial: bool = False) -> bytearray:
        pass

    @abstractmethod
    def write(self, addr: int, data: Union[str, bytes, bytearray]):
        pass
