import os
import zipfile
import requests
from pathlib import Path
from typing import Callable, Any


class DownloadError(Exception):
    pass


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


def unzip_dll(zip_path: Path, dir_path: Path, name_fn: Callable[[str], str]):
    with zipfile.ZipFile(zip_path, "r") as z:
        for file in z.namelist():
            if not file.endswith(".dll"):
                continue
            
            dll_path = dir_path / name_fn(file)
            
            z.extract(file, dll_path)

    os.remove(zip_path)