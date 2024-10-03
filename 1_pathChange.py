import os
from pathlib import Path

def create_text_file(text, base_filename="babel"):
  """
  テキストファイルをに作成する関数

  Args:
    text (str): ファイルに書き込むテキスト
    base_filename (str, optional): ファイル名のベース。デフォルトは"babel"

  Returns:
    str: 作成されたファイルのパス
  """

  # ファイル名のベースからパスを作成
  base_path = Path(base_filename+".txt")

  # ファイルが存在しない場合は、そのまま作成
  if not base_path.exists():
    base_path = Path(base_filename+".txt")
    with open(base_path, "w") as f:
      f.write(text)
    return str(base_path)

  # ファイルが存在する場合、番号を付けて新しいファイルを作成
  i = 1
  while True:
    new_filename = f"{base_filename}_{i}"
    new_path = Path(new_filename+".txt")
    if not new_path.exists():
      new_path = Path(new_filename+".txt")
      with open(new_path, "w") as f:
        f.write(text)
      return str(new_path)
    i += 1

# テスト実行
text_to_write = "Hello, world!"
created_file = create_text_file(text_to_write)
print(f"ファイルが作成されました: {created_file}")