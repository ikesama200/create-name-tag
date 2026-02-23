import tkinter as tk

class InputFrame(tk.Frame):
    def __init__(self, master, data):
        super().__init__(master)
        self.data = data

        tk.Label(self, text="入力値").pack()
        self.entry = tk.Entry(self)
        self.entry.pack()
        # 仮名表示のチェックボックス
        self.kana_var = tk.BooleanVar()
        tk.Checkbutton(self, text="仮名表示", variable=self.kana_var).pack()
        # 名前項目
        tk.Label(self, text="名前").pack()
        self.name = tk.Entry(self)
        self.name.pack()
        # 仮名名の項目
        tk.Label(self, text="仮名名").pack()
        self.nameKana = tk.Entry(self)
        self.nameKana.pack()
        # 項目A
        tk.Label(self, text="項目A").pack()
        self.itemA = tk.Entry(self)
        self.itemA.pack()
        # 項目B
        tk.Label(self, text="項目B").pack()
        self.itemB = tk.Entry(self)
        self.itemB.pack()

        tk.Button(self, text="保存", command=self.save).pack()

    def save(self):
        self.data.value = self.entry.get()
