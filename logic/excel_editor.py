import shutil
import os
import sys
from openpyxl import load_workbook
from datetime import datetime
import logging

def run_export(data):
  logging.info("出力処理開始")
  if not data.template_path:
    raise ValueError("テンプレートが選択されていません")

  template = data.template_path
  value = data.value

  if not template:
      return

  os.makedirs("output", exist_ok=True)
  out_file = f"output/result_{datetime.now():%Y%m%d_%H%M%S}.xlsx"

  shutil.copy(template, out_file)

  wb = load_workbook(out_file)
  ws = wb.active
  ws["A1"] = value
  wb.save(out_file)
  logging.info("出力処理終了")

# -------------------------
# Excelテンプレートパス取得
# -------------------------
def resource_path(relative_path):
  if hasattr(sys, "_MEIPASS"):
      return os.path.join(sys._MEIPASS, relative_path)
  return os.path.join(os.path.abspath("."), relative_path)

# -------------------------
# Excel書き込み処理の実行
# -------------------------
def load_excel_file(name_tag):
  template_path = resource_path("templates/template.xlsx")

  os.makedirs("output", exist_ok=True)
  output_path = f"output/result_{datetime.now():%Y%m%d_%H%M%S}.xlsx"

  write_to_excel(name_tag, template_path, output_path) 

# -------------------------
# Excelへの書き込み処理
# -------------------------
def write_to_excel(name_tag, template_path, output_path):
  # テンプレートを呼び出し
  wb = load_workbook(template_path)
  # ワークシートを選択
  ws = wb.active
  # データ書き込み
  for i, row in name_tag.items():
      # 配列の中身を展開して変数に格納
      name = row.name
      kana = row.nameKana
      itemA = row.itemA
      itemB = row.itemB
      # 列オフセットと行ベースを計算
      col_offset = (i % 2) * 2
      # 
      row_base = (i // 2) * 2

      base_row = 2 + row_base
      base_col = 1 + col_offset  # A=1

      # 上段左
      ws.cell(row=base_row, column=base_col).value = itemA
      # 上段右
      ws.cell(row=base_row + 1, column=base_col).value = itemB
      # 中段
      ws.cell(row=base_row, column=base_col + 1).value = kana
      # 最下段
      ws.cell(row=base_row, column=base_col + 2).value = name

  wb.save(output_path)