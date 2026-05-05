"""测试 scope="session" fixture"""

import pytest


def test_session_id_1(session_id):
    """多次调用 session_id 但值不变"""
    assert isinstance(session_id, int)
    assert 1000 <= session_id <= 9999


def test_session_id_2(session_id):
    """同一个 session 中 session_id 与上一个测试相同"""
    assert isinstance(session_id, int)


class TestSessionScope:
    """多个测试方法共享同一个 session fixture"""

    def test_session_id_in_class(self, session_id):
        assert isinstance(session_id, int)

    def test_temp_dir_exists(self, temp_dir):
        assert temp_dir.is_dir()
        config_file = temp_dir / "config.txt"
        assert config_file.read_text() == "shared_config"

    def test_temp_dir_same_instance(self, temp_dir, session_id):
        """验证 session fixture 的实例与类中的实例是同一个"""
        # temp_dir 在整个 session 中指向同一个目录
        assert temp_dir.is_dir()
        # config.txt 应该还在（因为是同一个目录）
        config_file = temp_dir / "config.txt"
        assert config_file.exists()
