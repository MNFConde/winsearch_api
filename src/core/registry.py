from functools import wraps # wraps 将被装饰器修饰的函数签名复制给装饰器返回的函数
from typing import Any, Callable

class Registry:
    def __init__(self):
        self.__registry: dict[str, Callable[..., Any]] = dict()
