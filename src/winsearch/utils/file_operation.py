import os
import zipfile
import requests
from pathlib import Path
from typing import Callable


class DownloadError(Exception):
    pass


def default_name_filter(file_name: str) -> bool:
    return True

def download_dll(dir_path: Path, file_url: str, file_name: str) -> None:
    os.makedirs(dir_path, exist_ok=True)
    file_path: Path = dir_path / file_name

    try:
        # 下载
        res = requests.get(file_url, stream=True, timeout=30)
        res.raise_for_status()

        with open(file_path, "wb") as f:
            for chunk in res.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)

    except requests.RequestException as e:
        raise DownloadError(f"下载SDK失败: {str(e)}")


def unzip_dll(
    zip_path: Path,
    dir_path: Path,
    name_filter: Callable[[str], bool] = default_name_filter,
):
    with zipfile.ZipFile(zip_path, "r") as z:
        for file in z.infolist():
            if not name_filter(file.filename):
                continue
            
            file_dir = dir_path / Path(file.filename).parent
            file_dir.mkdir(parents=True, exist_ok=True)

            z.extract(file, dir_path)

    os.remove(zip_path)

def file_rename(file_path: Path, new_name: str) -> None:
    if not file_path.exists():
        return
    
    new_file_path: Path = file_path.parent / new_name
    
    if new_file_path.exists():
        raise NameError('指定路径下存在与目标文件名同名的文件')
    
    file_path.rename(new_file_path)