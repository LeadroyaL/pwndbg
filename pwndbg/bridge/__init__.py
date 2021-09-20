"""
For gdb, variable named `gdb` is always globally.
For lldb, load `lldb` module then check `lldb.debugger`.
This module provides `dbg` instance to resolve the compatibility.
"""

from pwndbg.bridge.interface import IDbg
from pwndbg.bridge.gdb_impl import bridge_gdb
from pwndbg.bridge.lldb_impl import bridge_lldb

__all__ = ['dbg']

dbg: IDbg = bridge_gdb()
if not dbg:
    dbg = bridge_lldb()
if not dbg:
    raise RuntimeError("Cannot detect gdb or lldb")
