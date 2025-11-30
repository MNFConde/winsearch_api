from ..core.function_interface import interface

@interface
def get_result_date_created():
    pass

@interface
def get_result_date_modified():
    pass

@interface
def get_result_date_accessed():
    pass

@interface
def get_result_date_run():
    pass

@interface
def get_result_date_recently_changed():
    pass

@interface
def get_result_size():
    pass

@interface
def is_query_reply():
    pass

@interface
def get_result_file_name_w():
    pass

@interface
def get_result_path_w():
    pass

@interface
def get_result_extension_w():
    pass

@interface
def get_result_highlighted_file_name_w():
    pass

@interface
def get_result_highlighted_path_w():
    pass

@interface
def get_result_highlighted_full_path_and_file_name_w():
    pass

@interface
def get_search_w():
    pass

@interface
def get_result_full_path_name_w():
    pass

@interface
def get_result_file_list_file_name_w():
    pass

@interface
def get_run_count_from_file_name_w():
    pass

@interface
def set_run_count_from_file_name_w():
    pass

@interface
def inc_run_count_from_file_name_w():
    pass

@interface
def set_reply_window():
    pass

@interface
def set_reply_id():
    pass

@interface
def get_reply_window():
    pass

@interface
def get_reply_id():
    pass
