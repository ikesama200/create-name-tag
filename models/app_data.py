from dataclasses import dataclass
from typing import Optional

@dataclass
class AppData:
    # 入力画面
    value: str = ""

    # 取込画面
    template_path: Optional[str] = None

    # 出力関連
    output_path: Optional[str] = None