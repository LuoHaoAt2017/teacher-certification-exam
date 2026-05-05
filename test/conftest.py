"""共享 fixture：conftest.py 中的 fixture 可被同目录下所有测试文件使用"""

from pathlib import Path

import pytest


@pytest.fixture
def sample_list():
    """提供一个示例列表（共享）"""
    return [1, 2, 3, 4, 5]


@pytest.fixture
def sample_dict():
    """提供一个示例字典（共享）"""
    return {"name": "Alice", "age": 30}


@pytest.fixture
def db_connection():
    """模拟数据库连接"""
    return {"host": "localhost", "port": 5432, "connected": True}


@pytest.fixture
def user_data():
    """模拟用户数据"""
    return [
        {"id": 1, "name": "Alice", "role": "admin"},
        {"id": 2, "name": "Bob", "role": "user"},
        {"id": 3, "name": "Charlie", "role": "user"},
    ]


# ---------- scope="session" fixture ----------

@pytest.fixture(scope="session")
def session_id():
    """session 级别的 fixture：整个测试会话只创建一次"""
    import random
    sid = random.randint(1000, 9999)
    print(f"\n[session fixture] 创建 session_id={sid}")
    return sid


@pytest.fixture(scope="session")
def temp_dir(tmp_path_factory):
    """session 级别：创建一个供整个会话使用的临时目录"""
    path = tmp_path_factory.mktemp("session_data")
    print(f"\n[session fixture] 创建临时目录: {path}")
    # 写入一个文件供所有测试共享
    (path / "config.txt").write_text("shared_config")
    return path
