import pytest
from winsearch.core.function_interface import interface

def test_not_impl():
    @interface
    def func1():
        pass
    
    assert func1._impl is None
    
    with pytest.raises(NotImplementedError, match='Interface method not implemented'):
        func1()

def test_impl():
    @interface
    def func1():
        pass
    
    @func1.impl
    def f2(a: int) -> int:
        return a + 1
    
    assert func1._impl is not None
    assert func1(1) == 2
    
    @func1.impl
    def f3(a: int, b: int) -> int:
        return a + b
    
    assert func1(1, 2) == 3
    
def test_init():
    @interface
    def func1():
        ...
    
    @func1.init
    def init_fn1():
        return 1
    
    assert func1.init_res == 1
    
    @func1.impl
    def fn1():
        return 1
    
    assert func1() == 1
    