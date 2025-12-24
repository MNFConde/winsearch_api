from ctypes.wintypes import FILETIME, DWORD, LPCWSTR
from datetime import datetime, timedelta

LPCTSTR = LPCWSTR  # 指定 Unicode 字符集，不使用 ANSI


class TransTypeError(Exception): ...


class WinDWORD:
    def __init__(self, input_num: int) -> None:
        if input_num > (pow(2, 32) - 1) or input_num < 0:
            raise ValueError(f"给定数字: {input_num} 不在 [0, {pow(2, 32) - 1}] 中")
        self.dword = DWORD()
        self.dword.value = input_num


def filetime_to_datetime(time: FILETIME) -> datetime:
    try:
        filetime_seconds: int = (time.dwHighDateTime << 32) | time.dwLowDateTime
        if filetime_seconds == 0:
            raise ValueError(f"{time.dwHighDateTime}, {time.dwLowDateTime} 为无效值！")

        filetime_seconds = filetime_seconds // 10_000_000

        epoch = datetime(1601, 1, 1)

        return epoch + timedelta(seconds=filetime_seconds)

    except Exception as e:
        raise TransTypeError(e)
