import logging
import sys

def setup_logger():
    if getattr(sys, "frozen", False):
        # EXE実行時なのでログ出力を止める
        logging.disable(logging.CRITICAL)
    else:
        # コンソール実行なのでログ出力を有効にする
        logging.basicConfig(
            filename="app.log",
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s"
        )