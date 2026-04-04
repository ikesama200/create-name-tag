import csv
import tkinter as tk
from tkinter import filedialog, ttk, messagebox

def open_csv_mapping_dialog(parent, data, columns, input_frame):
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if not file_path:
        return
    try:
        with open(file_path, newline="", encoding="utf-8-sig") as f:
            reader = list(csv.reader(f))
    except Exception:
        messagebox.showerror("エラー", "CSVの読み込みに失敗しました")
        return
    if not reader:
        messagebox.showerror("エラー", "CSVが空です")
        return

    first_row = reader[0]
    if len(first_row) > 20:
        messagebox.showerror("エラー", "CSVの列数が多すぎます（20列まで）")
        return
    
    rows = reader[1:] if len(reader) > 1 else []

    dialog = tk.Toplevel(parent)
    dialog.title("CSV取込設定")
    dialog.geometry("800x200")

    combo_vars = []
    combos = []
    # -------------------------
    # CSV列（上段）
    # -------------------------
    for col, value in enumerate(first_row):
        e = tk.Entry(dialog, width=15)
        e.grid(row=0, column=col, padx=3, pady=5)
        e.insert(0, value)
        e.configure(state="readonly")

    # -------------------------
    # コンボ（下段）
    # -------------------------
    def on_focus_out(current_index):
        selected = combo_vars[current_index].get()
        if not selected:
            return

        for i, var in enumerate(combo_vars):
            if i != current_index and var.get() == selected:
                var.set("")

    for col in range(len(first_row)):
        var = tk.StringVar()

        combo = ttk.Combobox(dialog, textvariable=var, state="readonly")
        combo["values"] = [""] + columns
        combo.current(0)

        combo.grid(row=1, column=col, padx=3, pady=5)

        # フォーカスアウト時に重複チェック
        combo.bind("<FocusOut>", lambda e, i=col: on_focus_out(i))

        combo_vars.append(var)
        combos.append(combo)

    # -------------------------
    # プレビュー処理
    # -------------------------
    def preview_import():
        mapping = [var.get() for var in combo_vars]
        col_index_map = {name: i for i, name in enumerate(columns)}

        preview_data = []

        for row in rows[:3]:
            new_row = [""] * len(columns)

            for csv_col, target_name in enumerate(mapping):
                if not target_name:
                    continue

                if csv_col >= len(row):
                    continue

                target_idx = col_index_map[target_name]
                new_row[target_idx] = row[csv_col]

            preview_data.append(new_row)

        show_preview_dialog(preview_data, mapping, rows)

    # -------------------------
    # プレビュー画面
    # -------------------------
    def show_preview_dialog(preview_data, mapping, all_rows):
        preview = tk.Toplevel(dialog)
        preview.title("プレビュー")
        preview.geometry("600x200")

        # ヘッダー
        for col, name in enumerate(columns):
            tk.Label(preview, text=name, borderwidth=1, relief="solid").grid(
                row=0, column=col, sticky="nsew"
            )

        # データ表示
        for r, row in enumerate(preview_data, start=1):
            for c, val in enumerate(row):
                tk.Label(preview, text=val, borderwidth=1).grid(
                    row=r, column=c, sticky="nsew"
                )

        # -------------------------
        # OK（本取込）
        # -------------------------
        def do_import():
            col_index_map = {name: i for i, name in enumerate(columns)}

            input_frame.clear_all_rows()

            for row in all_rows:
                new_row = [""] * len(columns)

                for csv_col, target_name in enumerate(mapping):
                    if not target_name:
                        continue

                    if csv_col >= len(row):
                        continue

                    target_idx = col_index_map[target_name]
                    new_row[target_idx] = row[csv_col]

                input_frame.add_row_insert_values(new_row)

            input_frame.save()

            preview.destroy()
            dialog.destroy()

        # ボタン
        btn_frame = tk.Frame(preview)
        btn_frame.grid(row=10, column=0, columnspan=len(columns), pady=10)

        tk.Button(btn_frame, text="OK", command=do_import).pack(side="left", padx=10)
        tk.Button(btn_frame, text="キャンセル", command=preview.destroy).pack(side="left", padx=10)

    # -------------------------
    # ボタン
    # -------------------------
    btn_frame = tk.Frame(dialog)
    btn_frame.grid(row=2, column=0, columnspan=20, pady=10)

    tk.Button(btn_frame, text="取込", command=preview_import).pack(side="left", padx=10)
    tk.Button(btn_frame, text="閉じる", command=dialog.destroy).pack(side="left", padx=10)
