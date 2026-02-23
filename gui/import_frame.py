import tkinter as tk
from tkinter import filedialog

class ImportFrame(tk.Frame):
    def __init__(self, master, data):
        super().__init__(master)
        self.data = data

        tk.Button(self, text="テンプレ選択", command=self.select).pack()
        self.label = tk.Label(self, text="")
        self.label.pack()

    def select(self):
        path = filedialog.askopenfilename(filetypes=[("Excel", "*.xlsx")])
        self.data.template_path = path
        self.label.config(text=path)
