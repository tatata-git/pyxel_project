import pyxel
import csv
import os

class CImageManager:
    _instance = None  # クラス変数で唯一のインスタンスを保持

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            # 初回だけインスタンスを生成
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, "_initialized"):
            self.images = []
            self._initialized = True

    @classmethod
    def Instance(cls):
        if cls._instance is None:
            cls._instance = CImageManager()
        return cls._instance

    def LoadAll(self):
        # このファイルの場所を基準にリソースパスを解決する
        base_dir = os.path.dirname(os.path.abspath(__file__))              # .../myproject/game/asset
        imageasset_dir = os.path.join(base_dir, "imageasset")             # .../myproject/game/asset/imageasset
        csv_path = os.path.join(imageasset_dir, "image_info.csv")

        with open(csv_path, newline='', encoding='utf-8-sig') as csvfile:
            render = csv.DictReader(csvfile)
            for row in render:
                width = int(row['width'])
                height = int(row['height'])

                rel_path = row['pass'].replace('\\', '/')
                # CSV のパスが "asset/..." で始まるため、imageasset を基準に解決する
                if rel_path.startswith('asset/'):
                    rel_path = rel_path[len('asset/'):]  # 先頭の 'asset/' を除去

                full_path = os.path.join(imageasset_dir, rel_path)

                img = pyxel.Image(width, height)
                img.load(0, 0, full_path)
                self.images.append(img)
