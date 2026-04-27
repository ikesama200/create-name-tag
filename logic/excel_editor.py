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
  # Excelテンプレートのパスを取得
  template_path = resource_path("templates/template.xlsx")
  # 出力先のパスを生成
  os.makedirs("output", exist_ok=True)
  output_path = f"output/result_{datetime.now():%Y%m%d_%H%M%S}.xlsx"
  # Excelへの書き込み処理を実行
  write_to_excel(name_tag, template_path, output_path) 

# -------------------------
# Excelへの書き込み処理
# -------------------------
def write_to_excel(name_tag, template_path, output_path):
  # テンプレートを呼び出し
  wb = load_workbook(template_path)
  # データ書き込み用のシートを選択
  ws = wb["List"]
  # データ書き込み
  for i, row in name_tag.items():
    # 書き込み行をセット(2行目からスタート)
    execl_row = i + 2
    # A列 空行
    # B列 行番号
    ws.cell(row=execl_row, column=2).value = row.value + 1
    # C列 名前
    ws.cell(row=execl_row, column=3).value = row.name
    # D列 仮名
    ws.cell(row=execl_row, column=4).value = row.nameKana
    # E列 項目A
    ws.cell(row=execl_row, column=5).value = row.itemA
    # F列 項目B
    ws.cell(row=execl_row, column=6).value = row.itemB

  wb.save(output_path)