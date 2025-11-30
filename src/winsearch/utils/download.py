import os
import zipfile
import requests
from pathlib import Path


class DownloadError(Exception):
    pass


def download_dll(dir_path: Path, file_url: str, zip_name: str, file_name: str) -> None:
    os.makedirs(dir_path, exist_ok=True)
    zip_path: Path = dir_path / zip_name

    try:
        # 下载
        res = requests.get(file_url, stream=True, timeout=30)
        res.raise_for_status()

        with open(zip_path, "wb") as f:
            for chunk in res.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)

        # 解压
        with zipfile.ZipFile(zip_path, "r") as z:
            for file in z.namelist():
                if not file.endswith(".dll"):
                    continue

                z.extract(file, dir_path / file_name)

        os.remove(zip_path)

    except requests.RequestException as e:
        raise DownloadError(f"下载SDK失败: {str(e)}")
    except zipfile.BadZipFile:
        if os.path.exists(zip_path):
            os.remove(zip_path)
        raise DownloadError("无效的ZIP文件")
    except Exception as e:
        raise DownloadError(f"处理SDK过程中出错: {str(e)}")
