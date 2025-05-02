# -*- coding: Shift_JIS -*-

import os
import shutil
from gui_utils import show_message

def clear_folder(folder_path):
    """フォルダ内のすべてのファイルとサブフォルダを削除する関数"""
    if not os.path.exists(folder_path):
        show_message("エラー", "指定されたフォルダが存在しません。")
        return

    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        try:
            if os.path.isfile(item_path) or os.path.islink(item_path):
                os.unlink(item_path)  # ファイルまたはシンボリックリンクを削除
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)  # サブフォルダを削除
        except Exception as e:
            show_message("エラー", f"'{item}' の削除中にエラーが発生しました: {e}") 