from typing import Callable, List


def default_zero(index: int):
    return 0


class Version:
    def __init__(
        self, len: int = 3, fill_func: Callable = default_zero, split_alpha: str = "."
    ) -> None:
        self._split_num = len
        self._fill_func = fill_func
        self._split_alpha = split_alpha
        self._ver = [self._fill_func(index) for index in range(self._split_num)]
        self.version_str = ""

    def __str__(self) -> str:
        return self.version

    @property
    def version(self) -> str:
        if not self.is_valid():
            raise ValueError("未初始化版本号")
        return ".".join((str(i) for i in self._ver))

    @version.setter
    def version(self, version: str = "") -> None:
        if version == "":
            return  # 符合给定默认值

        tmp_version: List[int] = list(map(int, version.split(self._split_alpha)))

        if len(tmp_version) <= self._split_num:
            self.version_str = version
            for index in range(self._split_num):
                self._ver[index] = (
                    self._fill_func(index)
                    if index >= len(tmp_version)
                    else tmp_version[index]
                )

        else:
            raise ValueError(
                "给定字符串分割后的长度 {} 大于设定的长度 len：{}".format(
                    len(tmp_version),
                    self._split_num,
                )
            )

    def is_valid(self) -> bool:
        if len(self._ver) != self._split_num or self.version_str == "":
            return False
        return True


if __name__ == "__main__":
    a = Version()
    print(a.is_valid())
    a.version = "1.2.3"
    print(a.is_valid())
    print(a)
    print(a.version)
    a.version = "1.2.34"
    print(a.version)
