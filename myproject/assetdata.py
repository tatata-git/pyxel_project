import csv
import os

# アセット情報を格納するクラス
class AssetData:
    def __init__(self, enum_name, width, height, path):
        self.EnumName = enum_name
        self.Width = int(width)
        self.Height = int(height)
        self.Path = path


BaseDir = os.path.dirname(os.path.abspath(__file__))
CSVPath = os.path.join(BaseDir, "asset", "image_info.csv")

# CSV を読み込んで AssetData のリストを作る
Assets = []

with open(CSVPath, newline='', encoding='utf-8-sig') as csvfile:
    Render = csv.DictReader(csvfile)
    for row in Render:
        Asset = AssetData(
            row['enum_name'],
            row['width'],
            row['height'],
            row['pass'])
        Assets.append(Asset)

# # テストで表示
# for Asset in Assets:
#     print(f"{Asset.EnumName}: {Asset.Width}x{Asset.Height} -> {Asset.Path}")

# コードを自動生成
# enumの自動生成
AutomadeCode = "from enum import Enum\n"
AutomadeCode += "\n"
AutomadeCode += "class Img(Enum):\n"
for i in range(len(Assets)):
    AutomadeCode += f"    {Assets[i].EnumName} = {i}\n"
AutomadeCode += "\n"

# 生成されるコード内容を出力
print(AutomadeCode)

#.pyファイルに書き込む
WritePath = os.path.join(BaseDir, "automade", "img_enum.py")
with open(WritePath, "w", encoding='utf-8') as f:
    f.write(AutomadeCode)

print("\nimg_enum.pyの出力が完了")

