from typing import Any, Callable
from singleton_pattern import singleton_args
from ..utils.version import Version


@singleton_args
class Registry:
    def __init__(self, name: str = ""):
        self.__registry: dict[str, Callable[..., Any]] = dict()
        self._name = name
        self.verion = Version()

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

    print(r3.registry["func1"]())
    print(r3.registry["func2"]())
    print("func1" in r3.registry.keys())

    r4 = Registry("1")
    print("func1" in r4.registry.keys())
