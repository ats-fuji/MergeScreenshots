# -*- coding: Shift_JIS -*-

import subprocess
from gui_utils import show_message, select_folder
from folder_utils import clear_folder
from image_utils import combine_images_from_folder, copy_image_to_clipboard

def start_snipping_tool():
    """スニッピングツールを起動し、終了を待つ関数（ウィンドウを非表示）"""
    print("スニッピングツールを起動しています。スクリーンショットを保存してください...")
    # スニッピングツールを非表示で起動
    SW_HIDE = 0  # ウィンドウを非表示にするフラグ
    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    startupinfo.wShowWindow = SW_HIDE

    process = subprocess.Popen("snippingtool", shell=True, startupinfo=startupinfo)
    process.wait()  # スニッピングツールのプロセスが終了するまで待機
    print("スニッピングツールが終了しました。次の処理に進みます。")

def main():
    # フォルダ選択ダイアログを表示
    folder_path = select_folder()

    if not folder_path:
        show_message("エラー", "フォルダが選択されませんでした。処理を終了します。")
        return

    clear_folder(folder_path)  # フォルダをクリア

    # スニッピングツールを起動
    start_snipping_tool()

    # フォルダ内の画像を結合
    combined_image = combine_images_from_folder(folder_path)
    if combined_image:
        # クリップボードにコピー
        copy_image_to_clipboard(combined_image)
        show_message("成功", "結合された画像がクリップボードにコピーされました！")

if __name__ == "__main__":
    main() 