from functools import wraps # wraps 将被装饰器修饰的函数签名复制给装饰器返回的函数
from typing import Any, Callable
from singleton_pattern import singleton

@singleton
class Registry:
    def __init__(self):
        self.__registry: dict[str, Callable[..., Any]] = dict()
    
    def __call__(self, name: str) -> Callable:
        def decorator(fn: Callable[..., Any]) -> Callable[..., Any]:
            # 这里并不需要额外在调用函数时增加行为，所以就不创建子函数来调用 fn
            self.__registry[name] = fn
            return fn
        return decorator
    
    @property
    def registry(self) -> dict[str, Callable[..., Any]]:
        return self.__registry

if __name__ == "__main__":
    registry = Registry()
    
    @registry("func1")
    def test():
        return 1
    
    r2 = Registry()
    
    @r2("func2")
    def test2():
        return 2
    
    r3 = Registry()
    
    print(r3.registry['func1']())
    print(r3.registry['func2']())