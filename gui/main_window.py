import tkinter as tk
from gui.input_frame import InputFrame
from gui.import_frame import ImportFrame
from logic.excel_editor import run_export
from models.app_data import AppData
from tkinter import messagebox
import logging

class MainWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Excel自動編集ツール")
        self.root.geometry("600x400")

        # 入力値保持用
        self.data = AppData()

        self.frame_area = tk.Frame(self.root)
        self.frame_area.pack(expand=True, fill="both")

        self.frames = {
            "input": InputFrame(self.frame_area, self.data),
            "import": ImportFrame(self.frame_area, self.data),
        }

        self.current_frame = None
        self.show_frame("input")

        self.create_buttons()

    def create_buttons(self):
        bar = tk.Frame(self.root)
        bar.pack(fill="x")

        tk.Button(bar, text="入力画面", command=lambda: self.show_frame("input")).pack(side="left")
        tk.Button(bar, text="取込画面", command=lambda: self.show_frame("import")).pack(side="left")
        tk.Button(bar, text="出力実行", command=self.export).pack(side="left")
        tk.Button(bar, text="終了", command=self.root.quit).pack(side="right")

    def show_frame(self, name):
        if self.current_frame:
            self.current_frame.pack_forget()
        self.current_frame = self.frames[name]
        self.current_frame.pack(expand=True, fill="both")

    def export(self):
        try:
            run_export(self.data)
            messagebox.showinfo("完了", "出力が完了しました")
            logging.info("出力成功")
        except ValueError as e:
            logging.exception("出力失敗")
            messagebox.showerror("エラー", f"エラーが発生しました\n{e}")

    def run(self):
        self.root.mainloop()
