from pytest import raises
from winsearch.utils.version import Version

def test_init():
    a: Version = Version()
    
    assert a._split_num == 3
    assert a._fill_func(1) == 0
    assert a._split_alpha == '.'
    assert a._ver == [0, 0, 0]
    assert a.version_str == ''
    
def test_version():
    a: Version = Version()
    with raises(ValueError, match='未初始化版本号'):
        a.version
    
    with raises(ValueError, match='给定字符串分割后的长度 4 大于设定的长度 len：3'):
        a.version = '1.2.3.4'
    
    a.version = '1.2.3'
    
    assert a.version == '1.2.3'
    assert str(a) == '1.2'
    
    a.version = ''
    
    assert a.version == '1.2.3'
    assert str(a) == '1.2'

def test_version_match():
    a: Version = Version()
    b: Version = Version()
    c: Version = Version()
    
    a.version = '1.2.1'
    b.version = '1.2.0'
    c.version = '1.3.4'
    
    assert a.match(b)
    assert b.match(a)
    assert not c.match(a)
    assert not c.match(b)
    assert not a.match(c)
    assert not b.match(c)