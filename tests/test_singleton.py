from winsearch.core.singleton_pattern import singleton, singleton_args

def test_singleton():
    @singleton
    class A:
        def __init__(self, a):
            self.a = a

    a1 = A(1)
    a2 = A(2)
    a3 = A(1)
    
    assert a1.a == 1
    assert a2.a == 1
    assert a3.a == 1
    assert a1 is a2
    assert a1 is a3
    
    # __isinstancecheck__
    
    assert isinstance(a1, A) # type: ignore 
    assert isinstance(a2, A) # type: ignore 
    assert isinstance(a3, A) # type: ignore 
    
    # clear
    A.clear()
    
    assert not hasattr(a1, '_instance')
    assert not hasattr(a2, '_instance')
    assert not hasattr(a3, '_instance')
    
    A.clear()

def test_singleton_args():
    @singleton_args
    class B:
        def __init__(self, x, y=0):
            self.x = x
            self.y = y
    
    a1 = B(1)  # 创建新实例
    a2 = B(1)  # 返回相同实例
    a3 = B(2)  # 创建新实例
    a4 = B(1, y=0)  # 返回与a1相同的实例
    a5 = B(1, y=1)  # 创建新实例
    
    assert a1.x == 1
    assert a2.x == 1
    assert a3.x == 2
    assert a4.x == 1
    assert a5.x == 1
    
    assert a1.y == 0
    assert a2.y == 0
    assert a3.y == 0
    assert a4.y == 0
    assert a5.y == 1
    
    assert a1 is a2
    assert a1 is not a3
    assert a1 is a4
    assert a1 is not a5
    
    # __isinstancecheck__
    
    assert isinstance(a1, B) # type: ignore 
    assert isinstance(a2, B) # type: ignore 
    assert isinstance(a3, B) # type: ignore 
    
    # clear
    B.clear()
    
    assert not hasattr(a1, '_instance')
    assert not hasattr(a2, '_instance')
    assert not hasattr(a3, '_instance')