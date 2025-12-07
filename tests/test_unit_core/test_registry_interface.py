from winsearch.core.function_interface import interface
from winsearch.core.registry import RegistryClass

def test_reigistryclass_interface():
    a = RegistryClass('a')
    
    @interface
    def func1():
        pass
    
    @a('func1')
    @func1.impl
    def f(a: int) -> int:
        return a + 1
    
    assert func1(1) == a.func1(1) 