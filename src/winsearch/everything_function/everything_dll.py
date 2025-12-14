from ..utils.file_operation import download_dll, unzip_dll, file_rename
from ..utils.version import Version
from ..core.singleton_pattern import singleton
from ..utils.mini_fn import get_arch
from .everything_error import raise_for_error_code
from pathlib import Path
from ctypes import WinDLL
from typing import Any, Callable

sdk_url = {
    '1.4': 'https://www.voidtools.com/Everything-SDK.zip',
}

sdk_dir = Path('./dll').resolve()
sdk_zip_path = sdk_dir / 'Everything_SDK_Zip.zip'

def make_get_name(version: Version) -> Callable[..., Any]:
    def get_dll_name(file_name: str) -> str:
        arch = 64 if '64' in file_name else 32
        
        return "everything_sdk_{}_{}.dll".format(
            str(version),
            arch,
        )
    
    return get_dll_name

def dll_filter(file_name: str) -> bool:
    return file_name.endswith('.dll')

class DllError(Exception):
    pass

@singleton
class EverythingDll:
    def __init__(self, version: Version, dir_path: Path = Path.cwd() / 'dll') -> None:
        self.ver = version
        self.arch = get_arch()
        self.name_fn = make_get_name(self.ver)
        self.dir_path = dir_path
        self.dll = self._load_dll()
    
    def __getitem__(self, fn_name: str) -> Any:
        return getattr(self.dll, fn_name)
    
    def __getattr__(self, fn_name: str) -> Any:
        return getattr(self.dll, fn_name)
    
    def _load_dll(self) -> WinDLL:
        dll_name: str = self.name_fn(str(self.arch))
        dll_path: Path = self.dir_path / dll_name
        
        if not dll_path.exists():
            download_dll(
                self.dir_path,
                sdk_url[str(self.ver)],
                'Everything_SDK_Zip.zip',
            )
            
            unzip_dll(
                sdk_zip_path,
                sdk_dir,
                dll_filter,
            )
            
            for file in self.dir_path.rglob('*.dll'):
                if file.is_file():
                    file_rename(file, self.name_fn(file.name))
        
        try:
            return WinDLL(str(dll_path))
        except Exception as e:
            raise DllError(f"无法加载 dll: {str(e)}")
    
    def check_error(self) -> None:
        error_code = self.dll.Everything_GetLastError()
        raise_for_error_code(error_code)
    
    def is_db_loaded(self) -> bool:
        """检查Everything数据库是否已加载

        Returns:
            布尔值表示数据库是否已加载
        """
        return bool(self.dll.Everything_IsDBLoaded())

    def is_admin(self) -> bool:
        """检查Everything是否以管理员身份运行

        Returns:
            布尔值表示是否为管理员
        """
        return bool(self.dll.Everything_IsAdmin())