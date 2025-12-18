from winsearch.core.registry import Registry
from winsearch.everything_function.everything_base_interface import (
    get_result_date_created,
    get_result_date_modified,
    get_result_date_accessed,
    get_result_date_run,
    get_result_date_recently_changed,
    get_result_size,
    is_query_reply,
    get_result_file_name_w,
    get_result_path_w,
    get_result_extension_w,
    get_result_highlighted_file_name_w,
    get_result_highlighted_path_w,
    get_result_highlighted_full_path_and_file_name_w,
    get_search_w,
    get_result_full_path_name_w,
    get_result_file_list_file_name_w,
    get_run_count_from_file_name_w,
    set_run_count_from_file_name_w,
    inc_run_count_from_file_name_w,
    set_reply_window,
    set_reply_id,
    get_reply_window,
    get_reply_id,
)
from winsearch.everything_function.everything_dll import EverythingDll
from pathlib import Path
import ctypes
from typing import Optional

registry_name: str = 'everything_v1.4'

everything = Registry(registry_name)
everything.verion.version = "1.4"
everything_dll_dir_path = Path(__file__).parent.parent / 'dll'
everything_dll = EverythingDll(everything.verion, everything_dll_dir_path)

@everything('get_result_date_created')
@get_result_date_created.impl
def func(index: int) -> Optional[int]:
    """获取结果创建时间（Windows FILETIME格式）"""
    everything_dll.Everything_GetResultDateCreated.argtypes = [
        ctypes.c_int,
        ctypes.POINTER(ctypes.c_ulonglong),
    ]
    everything_dll.Everything_GetResultDateCreated.restype = []
    
    filetime = ctypes.c_ulonglong()
    everything_dll.Everything_GetResultDateCreated(index, ctypes.byref(filetime))
    return filetime.value if filetime.value != 0 else None