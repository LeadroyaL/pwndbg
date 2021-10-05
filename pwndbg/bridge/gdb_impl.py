from typing import Optional, Union

import gdb

from pwndbg.bridge.interface import IDbg
from pwndbg.bridge.common import *


def bridge_gdb() -> Optional[IDbg]:
    try:
        if gdb:
            return GdbImpl()
    except NameError:
        return None


class GdbImpl(IDbg):
    def execute(self, cmd: str, /, from_tty: bool = False, to_string: bool = False) -> Optional[str]:
        return gdb.execute(cmd, from_tty=from_tty, to_string=to_string)

    def read(self, addr: int, count: int, partial: bool = False) -> bytearray:
        """read(addr, count, partial=False) -> bytearray

        Read memory from the program being debugged.

        Arguments:
            addr(int): Address to read
            count(int): Number of bytes to read
            partial(bool): Whether less than ``count`` bytes can be returned

        Returns:
            :class:`bytearray`: The memory at the specified address,
            or ``None``.
        """
        result = b''
        count = max(int(count), 0)

        try:
            result = gdb.selected_inferior().read_memory(addr, count)
        except gdb.MemoryError as e:
            if not partial:
                raise DbgMemoryException(e)

            if not hasattr(e, 'message'):
                e.message = str(e)

            stop_addr = int(e.message.rsplit(maxsplit=1)[-1], 0)
            if stop_addr != addr:
                return self.read(addr, stop_addr - addr)

            # QEMU will return the start address as the failed
            # read address.  Try moving back a few pages at a time.
            stop_addr = addr + count

            # Move the stop address down to the previous page boundary
            stop_addr &= PAGE_MASK
            while stop_addr > addr:
                result = self.read(addr, stop_addr - addr)

                if result:
                    return result

                # Move down by another page
                stop_addr -= PAGE_SIZE
        except gdb.error as e:
            raise DbgException(e)
        return bytearray(result)

    def write(self, addr: int, data: Union[str, bytes, bytearray]):
        """write(addr, data)

        Writes data into the memory of the process being debugged.

        Arguments:
            addr(int): Address to write
            data(str,bytes,bytearray): Data to write
        """
        gdb.selected_inferior().write_memory(addr, data)
