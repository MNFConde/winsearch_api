from winsearch.everything_function.everything_dll import make_get_name, DllError, EverythingDll, dll_filter
from winsearch.everything_function.everything_error import ERROR_CODE_TO_EXCEPTION
from winsearch.utils.version import Version
from winsearch.utils.file_operation import file_rename
from winsearch.everything_function.constants import ErrorCode
import pytest
from typing import Callable
from tests.test_dependence.test_file import test_file_dir
from pathlib import Path

dir_path = test_file_dir / 'test_everything'
a = Version()
a.version = '1.4.3'

@pytest.mark.parametrize('version_str', [
    '1.1',
    '1.2',
    '1.3.1',
    '1.5.4',
])
def test_make_name(version_str: str):
    a = Version()
    a.version = version_str
    name_fn: Callable[[str], str] = make_get_name(a)
    
    assert name_fn('1') == f"everything_sdk_{str(a)}_32.dll"
    assert name_fn('64') == f"everything_sdk_{str(a)}_64.dll"

# 单例模式删除
@pytest.fixture(autouse=True, scope='function')
def reset_singleton():
    ...
    yield
    EverythingDll.clear() # 调用在 EverythingDll 上的装饰器赋予的 clear 清除单例
    dll_32: Path = dir_path / f"everything_sdk_{str(a)}_32.dll"
    dll_64: Path = dir_path / f"everything_sdk_{str(a)}_64.dll"
    
    assert dll_32.exists()
    assert dll_64.exists()
    
    file_rename(dll_32, '32.dll')
    file_rename(dll_64, '64.dll')

class TestClass:
    def __init__(self, res = 0) -> None:
        self.a = 1
        self.b = 2
        self.c_func = lambda i : i + 1
        self.res = res
    
    def Everything_GetLastError(self):
        return self.res
    
    def Everything_IsDBLoaded(self) -> bool:
        return False
    
    def Everything_IsAdmin(self) -> bool:
        return False
    

def test_everything_dll(mocker):
    # 这里 mock 需要 mock 使用的地方
    mocker.patch('winsearch.everything_function.everything_dll.download_dll', return_value=None)
    mocker.patch('winsearch.everything_function.everything_dll.unzip_dll', return_value=None)
    mocker.patch('winsearch.everything_function.everything_dll.WinDLL', return_value=TestClass())
    
    
    assert (dir_path / '32.dll').exists()
    assert (dir_path / '64.dll').exists()
    
    
    dll = EverythingDll(a, dir_path)
    
    dll_32: Path = dir_path / f"everything_sdk_{str(a)}_32.dll"
    dll_64: Path = dir_path / f"everything_sdk_{str(a)}_64.dll"
    
    assert dll_32.exists()
    assert dll_64.exists()
    assert dll['a'] == 1
    assert dll['c_func'](1) == 2
    assert dll.a == 1
    assert dll.c_func(1) == 2
    
    file_rename(dll_32, '32.dll')
    file_rename(dll_64, '64.dll')

def test_except(mocker):
    mocker.patch('winsearch.everything_function.everything_dll.download_dll', return_value=None)
    mocker.patch('winsearch.everything_function.everything_dll.unzip_dll', return_value=None)
    mock_windll = mocker.patch('winsearch.everything_function.everything_dll.WinDLL')
    mock_windll.side_effect = Exception('123')
    dir_path = test_file_dir / 'test_everything'
    
    a = Version()
    a.version = '1.4.3'
    with pytest.raises(DllError, match=f"无法加载 dll: {'123'}"):
        EverythingDll(a, dir_path)


@pytest.mark.parametrize('res', [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
])
def test_mini_fn_method(mocker, res: int):
    mocker.patch('winsearch.everything_function.everything_dll.download_dll', return_value=None)
    mocker.patch('winsearch.everything_function.everything_dll.unzip_dll', return_value=None)
    mocker.patch('winsearch.everything_function.everything_dll.WinDLL', return_value=TestClass(res))
    dir_path = test_file_dir / 'test_everything'
    
    a = Version()
    a.version = '1.4.3'
    dll = EverythingDll(a, dir_path)
    
    assert not dll.is_admin()
    assert not dll.is_db_loaded()
    
    # dll_filter 测试
    assert not dll_filter('awdw.dkk')
    assert dll_filter('awdw.dll')
    
    # 测试 check_dll 方法
    with pytest.raises(ERROR_CODE_TO_EXCEPTION[ErrorCode(res)]):
        dll.check_error()