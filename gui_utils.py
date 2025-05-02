# -*- coding: Shift_JIS -*-

import tkinter as tk
from tkinter import messagebox, filedialog

def show_message(title, message):
    """エラーまたは成功時のみメッセージを表示"""
    root = tk.Tk()
    root.attributes('-topmost', True)  # ウィンドウを最前面に表示
    root.withdraw()  # メインウィンドウを隠す
    messagebox.showinfo(title, message)  # メッセージボックスを表示し、ユーザーの操作を待つ
    root.destroy()  # ユーザーがOKを押した後にウィンドウを破棄

def select_folder():
    """フォルダを選択するダイアログを表示する関数"""
    root = tk.Tk()
    root.withdraw()  # メインウィンドウを隠す
    folder_selected = filedialog.askdirectory(title="スクリーンショットが保存されるフォルダを選択してください")
    root.destroy()
    return folder_selected 