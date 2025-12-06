from test_file.test_file import everything_path, test_file_dir
from winsearch.everything_function.everything_dll import sdk_url
from winsearch.utils.file_operation import download_dll, unzip_dll, DownloadError, file_rename
from pathlib import Path
import shutil
import pytest
from requests import RequestException
from typing import Callable, Iterable
import zipfile

def remove_dir_with_file(dir_path: Path) -> None:
    try:
        shutil.rmtree(dir_path)
    except FileNotFoundError:
        return
    except Exception as e:
        print(f"删除文件夹时发生错误：{e}")

def make_test_zip(file_list: Iterable[Path]):
    zip_path: Path = test_file_dir / 'test_file.zip'
    
    
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for path in file_list:
            path.touch()
            zipf.write(path, path.name)
            path.unlink(missing_ok=True)



def test_download_unzip_base():
    dir_path: Path = everything_path
    file_url = list(sdk_url.values())[0]
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
    
    file1_path = dir_path / r'dll/Everything32.dll'
    file2_path = dir_path / r'dll/Everything64.dll'
    
    assert file1_path.exists()
    assert file2_path.exists()
    
    remove_dir_with_file(dir_path)


def test_download_dll(mocker):
    mock_get = mocker.patch('requests.get')
    mock_get.side_effect = RequestException('123')

    with pytest.raises(DownloadError, match="下载SDK失败: 123"):
        download_dll(
            everything_path,
            '1',
            '1',
        )


@pytest.mark.parametrize('name_filter,true_name,false_name', [
    (
        lambda name: True if '1' in name else False,
        ['1.txt'],
        ['2.txt'],
    ),
    (
        lambda name: True if '2' in name else False,
        ['2.txt'],
        ['1.txt'],
    )
])
def test_unzip_dll(
    name_filter: Callable[[str], bool],
    true_name: Iterable[str],
    false_name: Iterable[str]
):
    test_zip: Path = test_file_dir / 'test_file.zip'
    test_dir: Path = test_file_dir / 'test_dir'
    file_1: Path = test_file_dir / '1.txt'
    file_2: Path = test_file_dir / '2.txt'
    
    make_test_zip((file_1, file_2))
    
    unzip_dll(
        test_zip,
        test_dir,
        name_filter
    )
    
    for file_name in true_name:
        assert (test_dir / file_name).exists()
    
    for file_name in false_name:
        assert not (test_dir / file_name).exists()
    
    remove_dir_with_file(test_dir)

@pytest.mark.parametrize('old_name,new_name', [
    ('test1.txt', 'test2.txt'),
    ('test1.bat', 'test2.bat'),
    ('test1.doc', 'test2.doc'),
])
def test_rename(old_name: str, new_name: str):
    file_path = test_file_dir / old_name
    with pytest.raises(NameError, match='指定文件不存在'):
        file_rename(file_path, '123')
    
    file_path.touch()
    
    file_rename(file_path, new_name)
    
    new_file = test_file_dir / new_name
    
    assert not file_path.exists()
    assert new_file.exists()
    
    with pytest.raises(NameError, match='指定路径下存在与目标文件名同名的文件'):
        file_rename(new_file, new_name)
    
    new_file.unlink(missing_ok=True)
    
    