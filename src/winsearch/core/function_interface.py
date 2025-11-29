from typing import Any, Callable, TypeVar, Generic

T = TypeVar('T')

class interface(Generic[T]):
    def __init__(self, func: Callable[..., Any]) -> None:
        self._impl = None
    
    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        if self._impl is None:
            raise NotImplementedError("Interface method not implemented")
        return self._impl(*args, **kwargs)
    
    def impl(self, func: Callable[..., T]) -> Callable[..., T]:
        self._impl = func
        return self