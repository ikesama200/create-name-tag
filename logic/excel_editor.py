import shutil
from openpyxl import load_workbook
from datetime import datetime
import os

def run_export(data):
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
