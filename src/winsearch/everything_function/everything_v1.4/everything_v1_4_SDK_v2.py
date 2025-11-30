from ...core.registry import Registry
from ..everything_base_interface import (
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

registry_name: str = 'everything_v1.4'

everything = Registry(registry_name)
everything.verion.version = "1.4"

@everything('get_result_date_created')
@get_result_date_created.impl
def func():
    return 1