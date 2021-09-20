from typing import Optional

from pwndbg.bridge.interface import IDbg


def bridge_lldb() -> Optional[IDbg]:
    try:
        import lldb
        if lldb.debugger:
            return LldbImpl()
        else:
            return None
    except ImportError:
        return None


class LldbImpl(IDbg):
    pass
