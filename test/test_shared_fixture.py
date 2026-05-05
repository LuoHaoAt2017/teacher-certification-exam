"""测试 conftest.py 共享的 fixture"""

import pytest


def test_db_connection(db_connection):
    """使用 conftest.py 中的 db_connection fixture"""
    assert db_connection["connected"] is True
    assert db_connection["host"] == "localhost"


def test_user_data_admin_count(user_data):
    """使用 conftest.py 中的 user_data fixture"""
    admins = [u for u in user_data if u["role"] == "admin"]
    assert len(admins) == 1


class TestSharedFixtures:
    """测试类中使用共享 fixture"""

    def test_user_names(self, user_data):
        names = [u["name"] for u in user_data]
        assert names == ["Alice", "Bob", "Charlie"]

    def test_user_id_types(self, user_data):
        assert all(isinstance(u["id"], int) for u in user_data)

    @pytest.mark.parametrize("uid, expected_name", [
        (1, "Alice"),
        (2, "Bob"),
        (3, "Charlie"),
    ])
    def test_find_user_by_id(self, user_data, uid, expected_name):
        user = next(u for u in user_data if u["id"] == uid)
        assert user["name"] == expected_name
