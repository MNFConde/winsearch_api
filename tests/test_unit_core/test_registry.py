import pytest
from winsearch.core.registry import Registry, RegistryClass


# 单例模式删除
@pytest.fixture(autouse=True, scope='function')
def reset_singleton():
    Registry.clear()
    RegistryClass.clear()

def test_basic():
    a = Registry()
    
    @a("f1")
    def func1():
        return 1
    
    @a("f2")
    def func2():
        return 2
        
    assert a['f1']() == func1()
    assert a['f2']() == func2()

def test_name_registry():
    a = Registry('a')
    b = Registry('b')
    
    @a('f1')
    def func_a1():
        return 1
    
    @b('f1')
    def func_b1():
        return 2
    
    @b('f2')
    def func2():
        return 3
    
    assert a['f1']() == func_a1()
    assert b['f1']() == func_b1()
    assert b['f2']() == func2()
    
    assert not hasattr(a, 'f2')
    assert hasattr(a, 'f1')

def test_setitem():
    c = Registry('c')
    c['a'] = lambda i: i+1
    
    assert c['a'](1) == 2

def test_singleton():
    a = Registry('test')
    @a('f1')
    def func1():
        return 1
    b = Registry('test')
    
    assert b['f1']() == func1()

def test_property():
    a = Registry('test')
    assert not hasattr(a.registry, 'f1')
    
    @a('f1')
    def func1():
        return 1
    
    assert a.registry['f1']() == func1()

def test_getattr():
    a = Registry('test')
    assert not hasattr(a.registry, 'f1')
    
    @a('f1')
    def func1():
        return 1
    
    assert a.f1() == func1()

def test_registry_class():
    a = RegistryClass('a')
    
    @a('f1')
    def func():
        return 1
    
    assert a.f1() == 1

def test_name_registry_2():
    a = RegistryClass('a')
    b = RegistryClass('b')
    
    @a('f1')
    def func_a1():
        return 1
    
    @b('f1')
    def func_b1():
        return 2
    
    @b('f2')
    def func2():
        return 3
    
    assert a.f1() == func_a1()
    assert b.f1() == func_b1()
    assert b.f2() == func2()
    
    assert not hasattr(a, 'f2')
    assert hasattr(a, 'f1')