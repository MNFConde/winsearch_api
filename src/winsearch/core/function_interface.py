from typing import Any, Callable, TypeVar, Generic, ParamSpec, cast

P = ParamSpec('P')
T = TypeVar('T')

class interface(Generic[P, T]):
    '''
    用来创建一个函数的接口
    
        @interface
        def fn_name():
            ...
    
    该函数接口名为 fn_name 
    
    如果调用 impl 来实现该函数，如：
    
        @fn_name.impl
        def fn1(a: int) -> int:
            return a + 1
    
    那么在调用时，如：
        fn_name(1)
    就会执行传入的实现函数，返回 2；如果没有调用 impl 实现，那么在调用时会报错
    
    可以使用 @fn_name.init 来为该函数进行一个初始化，结果保存在 self.init_res 中，
    也可以通过 get_init_res 方法来获取；该使用方法可以将初始化的逻辑与函数接口实现的部分放在一起，
    并且将只执行一次的初始化部分和可能会被反复调用的函数逻辑部分分开
    
    '''
    def __init__(self, func: Callable[P, Any]) -> None:
        ...
    
    def __call__(self, *args: P.args, **kwargs: P.kwargs) -> T:
        if not hasattr(self, '_impl'):
            raise NotImplementedError("Interface method not implemented")
        return self._impl(*args, **kwargs)
    
    def impl(self, func: Callable[P, T]) -> T:
        '''
        用来保存传入的函数，并且作为是否实现了该函数接口的依据，返回自身
        '''
        self._impl: Callable[P, T] = func
        # 这里使用 cast 告诉类型检查器将 self 视为 T
        # 既满足 链式调用/装饰器调用 ，又能保持使用时获取正确的返回值提示
        return cast(T, self) 
    
    def init(self, func: Callable[..., Any], *args, **kwargs) -> None:
        '''
        用来执行该函数的 前置逻辑/初始化 等在该函数之前的，只会运行一次的代码，结果保存在 self.init_res 中
        '''
        self.init_res = func(*args, **kwargs)
    
    def get_init_res(self) -> Any:
        return self.init_res