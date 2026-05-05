"""简单的测试用例"""


def test_add():
    """测试加法"""
    assert 1 + 1 == 2


def test_string_upper():
    """测试字符串大写"""
    assert "hello".upper() == "HELLO"


class TestExample:
    """示例测试类"""

    def test_sum(self):
        assert sum([1, 2, 3]) == 6

    def test_string_join(self):
        assert "-".join(["a", "b", "c"]) == "a-b-c"
