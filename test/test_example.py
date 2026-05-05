"""简单的测试用例"""

import pytest


def test_add():
    """测试加法"""
    assert 1 + 1 == 2


def test_string_upper():
    """测试字符串大写"""
    assert "hello".upper() == "HELLO"


@pytest.mark.parametrize("a, b, expected", [
    (1, 1, 2),
    (0, 0, 0),
    (-1, 1, 0),
    (100, 200, 300),
])
def test_add_parametrized(a, b, expected):
    """参数化测试加法"""
    assert a + b == expected


@pytest.mark.parametrize("text, expected", [
    ("hello", "HELLO"),
    ("python", "PYTHON"),
    ("123abc", "123ABC"),
    ("", ""),
])
def test_upper_parametrized(text, expected):
    """参数化测试字符串大写"""
    assert text.upper() == expected


class TestExample:
    """示例测试类"""

    def test_sum(self):
        assert sum([1, 2, 3]) == 6

    def test_string_join(self):
        assert "-".join(["a", "b", "c"]) == "a-b-c"


# ---------- fixture 示例（conftest.py 共享） ----------

def test_fixture_list_sum(sample_list):
    """使用 fixture 测试列表求和"""
    assert sum(sample_list) == 15


def test_fixture_dict_access(sample_dict):
    """使用 fixture 测试字典访问"""
    assert sample_dict["name"] == "Alice"
    assert sample_dict["age"] == 30


class TestWithFixtures:
    """在类中使用 fixture"""

    @pytest.fixture
    def greeting(self):
        return "Hello, pytest!"

    def test_greeting(self, greeting):
        assert greeting == "Hello, pytest!"
        assert len(greeting) > 0

    def test_greeting_upper(self, greeting):
        assert greeting.upper() == "HELLO, PYTEST!"
