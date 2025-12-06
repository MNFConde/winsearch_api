from test_file.test_file import everything_path, current_dir
from winsearch.everything_function.everything_dll import sdk_url
from winsearch.utils.file_operation import download_dll, unzip_dll
import os
from pathlib import Path

def test_download_unzip_base():
    
    for path in (everything_path, current_dir):
        dir_path: Path = path
        file_url = list(sdk_url.values())[0]
        # file_url = r'https://127.0.0.1/book/book.zip'
        file_name = 'test.zip'
        file_path = dir_path / file_name
        
        download_dll(
            dir_path,
            file_url,
            file_name
        )
        
        assert file_path.exists()
        
        unzip_dll(
            file_path,
            dir_path,
        )
        
        file1_path = dir_path / r'1.txt'
        file2_path = dir_path / r'2.txt'
        
        assert file1_path.exists()
        assert file2_path.exists()
        
        os.remove(file1_path)
        os.remove(file2_path)