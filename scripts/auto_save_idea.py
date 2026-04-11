import os
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Optional, Tuple

# ===================== 固定配置 =====================
SAVE_DIR = "src/idea"
SKILL_TRIGGER_KEYWORDS = [
    "人类学家视角",
    "哲学家视角",
    "政治家视角",
    "三维视角问题解析",
]
MIN_TRIGGER_COUNT = 2
# ====================================================


def ensure_save_dir(save_dir: str = SAVE_DIR) -> None:
    Path(save_dir).mkdir(parents=True, exist_ok=True)


def get_clipboard_text() -> str:
    """读取当前系统剪贴板文本内容。"""
    if sys.platform.startswith("darwin"):
        try:
            result = subprocess.run(
                ["pbpaste"], capture_output=True, text=True, check=True
            )
            return result.stdout
        except (subprocess.SubprocessError, FileNotFoundError):
            pass

    try:
        import pyperclip

        return pyperclip.paste() or ""
    except ImportError:
        return ""


def count_trigger_keywords(content: str) -> int:
    return sum(1 for keyword in SKILL_TRIGGER_KEYWORDS if keyword in content)


def is_skill_used(content: str) -> bool:
    """判断内容是否包含至少 MIN_TRIGGER_COUNT 个触发关键词。"""
    if not content:
        return False
    return count_trigger_keywords(content) >= MIN_TRIGGER_COUNT


def save_to_markdown(content: str, save_dir: str = SAVE_DIR) -> str:
    ensure_save_dir(save_dir)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"skill_analysis_{timestamp}.md"
    filepath = os.path.join(save_dir, filename)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    return filepath


def process_content(
    content: str,
    skill_name: Optional[str] = None,
    save_dir: str = SAVE_DIR,
) -> Tuple[bool, str]:
    content = content.strip()
    if not content:
        return False, "无内容"

    if skill_name or is_skill_used(content):
        filepath = save_to_markdown(content, save_dir)
        return True, filepath

    count = count_trigger_keywords(content)
    return (
        False,
        f"未检测到触发关键词，匹配 {count}/{MIN_TRIGGER_COUNT} 个。",
    )


def watch_clipboard(interval: float = 0.5, save_dir: str = SAVE_DIR) -> None:
    """监听剪贴板变化，复制文本符合触发条件时保存到文件。"""
    ensure_save_dir(save_dir)
    last_text = get_clipboard_text()

    print("📝 剪贴板监听已启动。复制新文本后自动保存符合条件的内容。按 Ctrl+C 退出。")

    try:
        while True:
            time.sleep(interval)
            current = get_clipboard_text()
            if not current:
                continue
            if current == last_text:
                continue

            last_text = current
            success, result = process_content(current, save_dir=save_dir)
            if success:
                print(f"✅ 已保存：{result}")
            else:
                print(f"⚠️ {result}")
    except KeyboardInterrupt:
        print("\n🛑 剪贴板监听已停止。")


if __name__ == "__main__":
    watch_clipboard()
