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
        # ヘッダー領域の作成
        self.create_header_area()
        # スクロールエリアの作成
        self.create_scroll_area()
        # 入力領域の作成
        self.create_input_table()
    # -------------------------
    # ヘッダー領域の作成
    # -------------------------
    def create_header_area(self):
        header = tk.Frame(self)
        header.pack(fill="x", pady=5)
        
        # 仮名表示のチェックボックス
        self.kana_var = tk.BooleanVar()
        tk.Checkbutton(header, text="仮名表示", variable=self.kana_var).pack(side="left", padx=5)

        # 行追加ボタン
        tk.Button(header, text="行追加", command=self.add_row).pack(side="right", padx=5)
        # 保存ボタン
        tk.Button(header, text="保存", command=self.save).pack(side="right", padx=5)
    # -------------------------
    # スクロールエリア作成
    # -------------------------
    def create_scroll_area(self):
        self.canvas = tk.Canvas(self)

        self.scroll_frame = tk.Frame(self.canvas)
        self.scroll_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )
        self.canvas.create_window((0, 0), window=self.scroll_frame, anchor="nw")
        scrollbar = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        scrollbar.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        # マウスホイール対応
        self.canvas.bind_all("<MouseWheel>", self.on_mousewheel)

    def on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    # -------------------------
    # 入力領域の作成
    # -------------------------
    def create_input_table(self):
        # サンプル入力欄の作成
        # tk.Label(self, text="入力値").pack()
        # #self.entry = tk.Entry(self)
        # self.entry.pack()

        # 仮名表示のチェックボックス
        #self.kana_var = tk.BooleanVar()
        #tk.Checkbutton(self, text="仮名表示", variable=self.kana_var).grid(row=0, column=0, columnspan=len(self.labels))
        # 入力項目のラベルを作成
        for col, name in enumerate(self.labels):
            label = tk.Label(self.scroll_frame, text=name, borderwidth=1, relief="solid")
            label.grid(row=0, column=col, sticky="nsew")

        # 入力欄を作成
        for r in range(self.input_row_count):
            self.add_row()

        #tk.Button(self, text="行追加", command=self.add_row).grid(row=self.button_row, column=0, columnspan=len(self.labels), pady=10)
        #tk.Button(self, text="保存", command=self.save).grid(row=self.button_row, column=1, columnspan=len(self.labels), pady=10)

        # カラムを伸ばす設定
        for col in range(len(self.labels)):
            self.scroll_frame.grid_columnconfigure(col, weight=1)
    # -------------------------
    # 行追加
    # -------------------------
    def add_row(self):
        r = len(self.entries) + 1  # ラベル分を考慮
        row_entries = []
        for c in range(len(self.labels)):
            entry = tk.Entry(self.scroll_frame)
            entry.grid(row=r, column=c, padx=2, pady=2, sticky="nsew")
            row_entries.append(entry)
        # 削除ボタンの追加
        btn = tk.Button(
            self.scroll_frame,
            text="削除",
            command=lambda row=r: self.delete_row(row)
        )
        #削除ボタンの配置
        btn.grid(row=r, column=len(self.labels), padx=2)
        # 入力欄とボタンを配置
        self.entries.append((row_entries, btn))
        self.button_row += 2
    # -------------------------
    # 行削除
    # -------------------------
    def delete_row(self, row_index):
        # インデックス補正（ヘッダー分）
        idx = row_index + 1
        if idx >= len(self.entries):
            return
        row_entries, btn = self.entries[idx]
        # 行項目削除
        for e in row_entries:
            e.destroy()
        btn.destroy()

        # リストから削除
        self.entries.pop(idx)

        # 再配置（これ重要）
        self.refresh_rows()
    # -------------------------
    # 行再配置
    # -------------------------
    def refresh_rows(self):
        for i, (row_entries, btn) in enumerate(self.entries):
            r = i + 1  # ラベル分を考慮

            for c, entry in enumerate(row_entries):
                entry.grid(row=r, column=c)

            btn.configure(command=lambda row=r: self.delete_row(row))
            btn.grid(row=r, column=len(self.labels))

    def save(self):
        self.data.value = self.entry.get()
        self.name_tag[0].name = self.name.get()
        self.name_tag[0].nameKana = self.nameKana.get()
        self.name_tag[0].itemA = self.itemA.get()
        self.name_tag[0].itemB = self.itemB.get()