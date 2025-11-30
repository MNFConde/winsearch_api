from typing import Any, Callable
from .singleton_pattern import singleton_args
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

    def __getitem__(self, name: str) -> Callable[..., Any]:
        return self.__registry[name]

    def __setitem__(self, name: str, value: Callable[..., Any]) -> None:
        self.__registry[name] = value
    

    @property
    def registry(self) -> dict[str, Callable[..., Any]]:
        return self.__registry

    def __getattr__(self, name: str) -> Any:
        '''
        为了兼容 hasatttr 
        '''
        try:
            return self.__registry[name]
        except Exception as e:
            raise AttributeError(e)

@singleton_args
class RegistryClass:
    def __init__(self, name: str = ""):
        self._name = name
        self.verion = Version()

    def __call__(self, name: str) -> Callable:
        def decorator(fn: Callable[..., Any]) -> Callable[..., Any]:
            # 这里并不需要额外在调用函数时增加行为，所以就不创建子函数来调用 fn
            setattr(self, name, fn)
            return fn

        return decorator
    
    def __getattr__(self, name: str) -> Any:
        '''
        当访问不存在的属性时，抛出 AttributeError。
        这使得 hasattr() 能够正确地工作。
        '''
        raise AttributeError(f"'{type(self).__name__}' object has no attribute '{name}'")