from typing import Optional

import gdb

from pwndbg.bridge.interface import IDbg


def bridge_gdb() -> Optional[IDbg]:
    try:
        if gdb:
            return GdbImpl()
    except NameError:
        return None


class GdbImpl(IDbg):
    def execute(self, cmd: str, /, from_tty: bool = False, to_string: bool = False) -> Optional[str]:
        return gdb.execute(cmd, from_tty=from_tty, to_string=to_string)
