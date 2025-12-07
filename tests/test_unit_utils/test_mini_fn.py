from winsearch.utils.mini_fn import get_arch

def test_get_arch(mocker):
    # 由于 mini_fn 中将 architecture 直接导入，所以需要 mock mini_fn 下的 architecture
    mock_architecture = mocker.patch('winsearch.utils.mini_fn.architecture')
    mock_architecture.return_value  = ('32bit', '')
    assert get_arch() == 32
    mock_architecture.return_value  = ('64bit', '')
    assert get_arch() == 64
    