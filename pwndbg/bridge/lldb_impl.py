from typing import Optional, Union

import lldb

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
    CMD_REDIRECT_MAPPING = {
        "set python print-stack full": "",
        "set python print-stack message": "",
    }

    def execute(self, cmd: str, /, from_tty: bool = False, to_string: bool = False) -> Optional[str]:
        if cmd not in self.CMD_REDIRECT_MAPPING or not self.CMD_REDIRECT_MAPPING[cmd]:
            raise NotImplementedError(f"{cmd} is not implement in lldb version")
        interp: lldb.SBCommandInterpreter = lldb.debugger.GetCommandInterpreter()
        result: lldb.SBCommandReturnObject = lldb.SBCommandReturnObject()
        interp.HandleCommand(cmd, result)
        if result.Succeeded():
            return result.GetOutput()
        else:
            raise RuntimeError(f"FAIL: {cmd}. Error msg: {result.GetError()}")

    def read(self, addr: int, count: int, partial: bool = False) -> bytearray:
        pass

    def write(self, addr: int, data: Union[str, bytes, bytearray]):
        pass
