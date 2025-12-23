from ctypes.wintypes import FILETIME
from datetime import datetime, timedelta

class TransTypeError(Exception):
    ...

def filetime_to_datetime(time: FILETIME) -> datetime:
    try:
        filetime_seconds: int = (time.dwHighDateTime << 32) | time.dwLowDateTime
        if filetime_seconds == 0:
            raise ValueError(f'{time.dwHighDateTime}, {time.dwLowDateTime} 为无效值！')
        
        filetime_seconds = filetime_seconds // 10_000_000
        
        epoch = datetime(1601, 1, 1)
        
        return epoch + timedelta(seconds=filetime_seconds)
        
    except Exception as e:
        raise TransTypeError(e)