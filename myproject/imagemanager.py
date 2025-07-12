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
        BaseDir = os.path.dirname(os.path.abspath(__file__))
        CSVPath = os.path.join(BaseDir, "asset", "image_info.csv")
        with open(CSVPath, newline='', encoding='utf-8-sig') as csvfile:
            Render = csv.DictReader(csvfile)
            for row in Render:
                width = int(row['width'])
                height = int(row['height'])
                path = row['pass']
                img = pyxel.Image(width,height)
                img.load(0, 0, path)
                self.images.append(img)
