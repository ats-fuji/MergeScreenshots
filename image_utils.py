# -*- coding: Shift_JIS -*-

import os
from PIL import Image
import win32clipboard
from io import BytesIO
from gui_utils import show_message

def combine_images_from_folder(folder_path):
    """フォルダ内の画像を結合する関数"""
    image_files = [f for f in os.listdir(folder_path) if f.lower().endswith(('png', 'jpg', 'jpeg'))]
    if not image_files:
        show_message("エラー", "フォルダ内に画像が見つかりませんでした。")
        return None

    image_files.sort()  # ファイル名順に並べる
    images = [Image.open(os.path.join(folder_path, file)) for file in image_files]

    max_width = max(img.width for img in images)
    total_height = sum(img.height for img in images)

    combined_image = Image.new("RGB", (max_width, total_height))
    y_offset = 0
    for img in images:
        combined_image.paste(img, (0, y_offset))
        y_offset += img.height
    
    return combined_image

def copy_image_to_clipboard(image):
    """画像をクリップボードにコピーする関数"""
    output = BytesIO()
    image.convert("RGB").save(output, "BMP")
    data = output.getvalue()[14:]  # BMPヘッダーをスキップ
    output.close()

    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
    win32clipboard.CloseClipboard() 