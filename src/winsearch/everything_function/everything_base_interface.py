from winsearch.core.function_interface import interface
from winsearch.everything_function.constants import (
    SortType,
    RequestFlag,
)
from winsearch.utils.wintype_operation import (
    LPCTSTR,
    WinDWORD,
)
from ctypes import wintypes


# --------- 操作搜索状态 ---------
@interface
def set_search(search_str: str) -> None:
    ...

@interface
def set_match_path(enable_fullpath_matching: bool) -> None:
    ...

@interface
def set_match_case(enable_matchcase_sensitive: bool) -> None:
    ...

@interface
def set_match_whole_word(enable_match_whole_word: bool) -> None:
    ...

@interface
def set_regex(enable_regex: bool) -> None:
    ...

@interface
def set_max(max_result_num: WinDWORD) -> None:
    ...

@interface
def set_offset(available_offset: WinDWORD) -> None:
    ...

@interface
def set_sort(sort_type: SortType) -> None:
    ...

@interface
def set_request_flags(request_flag: RequestFlag) -> None:
    ...

# --------- 读取搜索状态 ---------
@interface
def get_search() -> LPCTSTR:
    ...

@interface
def get_match_path() -> bool:
    ...

@interface
def get_match_case() -> bool:
    ...

@interface
def get_match_whole_word() -> bool:
    ...

@interface
def get_regex() -> bool:
    ...

@interface
def get_max() -> bool:
    ...

@interface
def get_offset() -> WinDWORD:
    ...

@interface
def get_last_error() -> WinDWORD:
    ...

@interface
def get_sort() -> WinDWORD:
    ...

@interface
def get_request_flags() -> WinDWORD:
    ...

# --------- 执行查询 ---------
@interface
def query(wait_result: bool) -> None:
    ...

# --------- 操作结果 ---------
@interface
def sort_results_by_path() -> None:
    ...


@interface
def reset() -> None:
    ...

# --------- 读取结果 ---------
@interface
def get_num_file_results() -> WinDWORD:
    ...

@interface
def get_num_folder_results() -> WinDWORD:
    ...

@interface
def get_num_results() -> WinDWORD:
    ...

@interface
def get_tot_file_results() -> WinDWORD:
    ...

@interface
def get_tot_folder_results() -> WinDWORD:
    ...

@interface
def get_tot_results() -> WinDWORD:
    ...

@interface
def is_volume_result(index: WinDWORD) -> bool:
    '''
    判断第 index(从 0 开始) 个返回结果是否是盘符根目录
    '''
    ...

@interface
def is_folder_result(index: WinDWORD) -> bool:
    '''
    判断第 index(从 0 开始) 个返回结果是否是文件夹
    '''
    ...

@interface
def is_file_result(index: WinDWORD) -> bool:
    '''
    判断第 index(从 0 开始) 个返回结果是否是文件
    '''
    ...

@interface
def get_result_file_name(index: WinDWORD) -> LPCTSTR:
    '''
    获取第 index(从 0 开始) 个返回结果的文件名部分
    '''
    ...

@interface
def get_result_path(index: WinDWORD) -> LPCTSTR:
    '''
    获取第 index(从 0 开始) 个返回结果的文件名部分
    '''
    ...

@interface
def get_result_extension(index: WinDWORD) -> LPCTSTR:
    '''
    获取第 index(从 0 开始) 个返回结果的文件扩展名部分
    '''
    ...

@interface
def get_result_size(index: WinDWORD, size: wintypes.LARGE_INTEGER) -> bool:
    '''
    获取第 index(从 0 开始) 个返回结果的文件大小
    '''
    ...

@interface
def get_result_date_created(index: WinDWORD, date_created: wintypes.FILETIME) -> bool:
    '''
    获取第 index(从 0 开始) 个返回结果的文件创建时间
    '''
    ...

@interface
def get_result_date_modified(index: WinDWORD, date_created: wintypes.FILETIME) -> bool:
    '''
    获取第 index(从 0 开始) 个返回结果的文件修改时间
    '''
    ...

@interface
def get_result_date_accessed(index: WinDWORD, date_created: wintypes.FILETIME) -> bool:
    '''
    获取第 index(从 0 开始) 个返回结果的文件访问时间
    '''
    ...

@interface
def get_result_attributes(index: WinDWORD) -> WinDWORD:
    '''
    获取第 index(从 0 开始) 个返回结果的文件属性（可叠加）
    '''
    ...

@interface
def get_result_full_path_name(index: WinDWORD, string: LPCTSTR, max_char_number: WinDWORD) -> WinDWORD:
    '''
    获取第 index(从 0 开始) 个返回结果的文件完整路径
        
        string: 存储结果的缓冲区
        max_char_number: 指定最多存储的字符数
    '''
    ...

@interface
def get_result_run_count(index: WinDWORD) -> WinDWORD:
    '''
    获取第 index(从 0 开始) 个返回结果的文件通过 everything 运行了多少次
    '''
    ...

@interface
def get_result_date_run(index: WinDWORD, date_run: wintypes.FILETIME) -> bool:
    '''
    获取第 index(从 0 开始) 个返回结果的文件上一次 运行 的日期
    '''
    ...

@interface
def get_result_date_recently_changed(index: WinDWORD, date_run: wintypes.FILETIME) -> bool:
    '''
    获取第 index(从 0 开始) 个返回结果的文件上一次 修改 的日期
    '''
    ...

@interface
def get_result_highlighted_file_name(index: WinDWORD) -> LPCTSTR:
    '''
    获取第 index(从 0 开始) 个返回结果的文件的 文件名 中被匹配到的部分（高亮部分）
    '''
    ...

@interface
def get_result_highlighted_path(index: WinDWORD) -> LPCTSTR:
    '''
    获取第 index(从 0 开始) 个返回结果的文件的 文件路径 中被匹配到的部分（高亮部分）
    '''
    ...

@interface
def get_result_highlighted_full_path_and_file_name(index: WinDWORD) -> LPCTSTR:
    '''
    获取第 index(从 0 开始) 个返回结果的文件的 文件路径与文件名 中被匹配到的部分（高亮部分）
    '''
    ...

@interface
def get_result_list_sort() -> WinDWORD:
    '''
    获取返回结果实际的排序顺序 SortType
    '''
    ...

@interface
def get_result_list_request_flags() -> WinDWORD:
    '''
    返回当前查询结果中实际可用的数据类型的标志 RequestFlag
    '''
    ...

@interface
def get_result_file_list_file_name(index: WinDWORD) -> LPCTSTR:
    '''
    获取第 index(从 0 开始) 个返回结果的文件是 来源于哪个索引列表（例如，区分文件是来自本地NTFS卷，还是从一个自定义的.efu列表文件中导入）
    '''
    ...

# --------- 检查查询应答 ---------
@interface
def is_query_reply(message: wintypes.UINT, w_param: wintypes.WPARAM, l_param: wintypes.LPARAM, id: WinDWORD) -> bool:
    '''
    在 Windows 消息循环中检查接收到的消息是否为 Everything 通过异步方式发回的查询结果回复
    '''
    ...

# --------- 设置回调窗口和ID ---------
@interface
def set_reply_window(id: WinDWORD) -> None:
    
    ...

@interface
def set_reply_id(id: WinDWORD) -> None:
    '''
    设置用来标识下一次查询的 id
    '''
    ...

@interface
def get_reply_window():
    ...

@interface
def get_reply_id():
    ...

# --------- 运行历史 ---------
@interface
def get_run_count_from_file_name():
    ...

@interface
def set_run_count_from_file_name():
    ...

@interface
def inc_run_count_from_file_name():
    ...


# --------- 常规功能 ---------
@interface
def cleanup():
    ...

@interface
def get_major_version():
    ...

@interface
def get_minor_version():
    ...

@interface
def get_revision():
    ...

@interface
def get_build_number():
    ...

@interface
def exit():
    ...

@interface
def is_db_loaded():
    ...

@interface
def is_admin():
    ...

@interface
def is_app_data():
    ...

@interface
def rebuild_db():
    ...

@interface
def update_all_folder_indexes():
    ...

@interface
def save_db():
    ...

@interface
def save_run_history():
    ...

@interface
def delete_run_history():
    ...

@interface
def get_target_machine():
    ...
