from winsearch.everything_function.everything_error import ErrorCode, ERROR_CODE_TO_EXCEPTION, raise_for_error_code, EverythingError
import pytest

@pytest.mark.parametrize('error_code,err_expect', [
    (code, ERROR_CODE_TO_EXCEPTION.get(code, EverythingError))
    for code in ErrorCode
])
def test_error_code(error_code: ErrorCode, err_expect: type[EverythingError]):
    if error_code == ErrorCode.EVERYTHING_OK:
        assert not raise_for_error_code(error_code)
    else:
        with pytest.raises(err_expect, match=f"Everything SDK错误: {error_code}"):
            raise_for_error_code(error_code)
    