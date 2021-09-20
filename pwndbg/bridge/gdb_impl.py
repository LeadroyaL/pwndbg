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
    pass
