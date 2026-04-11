# Python 环境说明
本项目已配置本地 Python 虚拟环境，建议运行时使用该环境以隔离依赖和避免系统 Python 冲突。

1. 进入项目目录：
   ```bash
   cd /Users/luohao/github/teacher-certification-exam
   ```
2. 激活虚拟环境：
   ```bash
   source .venv/bin/activate
   ```
3. 安装依赖（如果尚未安装）：
   ```bash
   pip install -r requirements.txt
   ```
4. 运行脚本：
   ```bash
   python main.py --text '测试内容'
   ```

已创建文件：`.venv/`, `requirements.txt`, `.gitignore`。