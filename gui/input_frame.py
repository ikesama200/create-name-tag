import tkinter as tk

class InputFrame(tk.Frame):
    def __init__(self, master, data, name_tag):
        super().__init__(master)
        self.data = data
        self.name_tag = name_tag

        self.labels = ["名前", "仮名名", "項目A", "項目B"]
        self.input_row_count = 5  # ← 行数
        self.button_row = self.input_row_count + 2  # ← ボタン行数
        self.entries = []  # 2次元リスト

        self.create_input_table()
    def create_input_table(self):
        # サンプル入力欄の作成
        # tk.Label(self, text="入力値").pack()
        # #self.entry = tk.Entry(self)
        # self.entry.pack()

        # 仮名表示のチェックボックス
        self.kana_var = tk.BooleanVar()
        tk.Checkbutton(self, text="仮名表示", variable=self.kana_var).grid(row=0, column=0, columnspan=len(self.labels))
        
        # ヘッダーのラベルを作成
        for col, name in enumerate(self.labels):
            label = tk.Label(self, text=name, borderwidth=1, relief="solid")
            label.grid(row=1, column=col, sticky="nsew")

        # 入力欄を作成
        for r in range(self.input_row_count):
            self.add_row()

        tk.Button(self, text="行追加", command=self.add_row).grid(row=self.button_row, column=0, columnspan=len(self.labels), pady=10)
        tk.Button(self, text="保存", command=self.save).grid(row=self.button_row, column=1, columnspan=len(self.labels), pady=10)

        # カラムを伸ばす設定
        for col in range(len(self.labels)):
            self.grid_columnconfigure(col, weight=1)

    def add_row(self):
        r = len(self.entries) + 2
        row_entries = []
        for c in range(len(self.labels)):
            entry = tk.Entry(self)
            entry.grid(row=r, column=c, padx=2, pady=2, sticky="nsew")
            row_entries.append(entry)
        self.entries.append(row_entries)
        self.button_row += 2

    def save(self):
        self.data.value = self.entry.get()
        self.name_tag[0].name = self.name.get()
        self.name_tag[0].nameKana = self.nameKana.get()
        self.name_tag[0].itemA = self.itemA.get()
        self.name_tag[0].itemB = self.itemB.get()