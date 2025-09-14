import pyxel
import PyxelUniversalFont as puf
import time
from collections import deque

import myproject.game.system.const as const
from myproject.game.system.color_ball import CColorBall
from myproject.game.system.vec2 import Vec2

from myproject.game.asset.imagemanager import CImageManager

from myproject.game.entity.player import CPlayer
from myproject.game.stage.stage import CStage

class App:
    def __init__(self):
        # タイマーの初期化
        self._last_time = time.perf_counter()
        self._frame_times = deque(maxlen=30)  # 直近30フレームの dt を保持
        self.fps_avg = 0.0   

        pyxel.init(const.GAMEWINDOW_WIDTH, const.GAMEWINDOW_HEIGHT, title="myproject", display_scale = const.DIPLAY_SCALE)
        pyxel.load("myproject_editor.pyxres")

        # # テスト用
        # pyxel.images[1].load(100,100,"asset/palette.png")
        # pyxel.images[1].load(0, 0, "asset/Monster/Slime_Blue.png")
        # pyxel.images[1].load(0,50, "asset/black.png")

        # イメージマネージャの初期化
        pI = CImageManager.Instance()
        pI.LoadAll()
        
        ## オブジェクトの生成
        # プレイヤー
        self.cPlayer = CPlayer(Vec2(const.CHARA_INIT_POS_X, const.CHARA_INIT_POS_Y), Vec2(const.CHARA_INIT_POS_X, const.CHARA_INIT_POS_Y))

        # ステージ
        self.cStage  = CStage()

        ## 依存性の注入
        # プレイヤー
        self.cPlayer.SetStage(self.cStage)

        pyxel.run(self.update, self.draw)

    def update(self):
        # --- delta time 計測 ---
        now = time.perf_counter()
        dt = now - self._last_time
        self._last_time = now

        # --- 移動平均のために dt を保存 ---
        # （極端なスパイクを弾きたい場合は、0<dt<0.5 などの簡単な範囲チェックを入れても良い）
        if dt > 0:
            self._frame_times.append(dt)

        # --- 平均 dt から平均 FPS を計算 ---
        if self._frame_times:
            avg_dt = sum(self._frame_times) / len(self._frame_times)
            if avg_dt > 0:
                self.fps_avg = 1.0 / avg_dt

        self.cPlayer.update()
        self.cStage.update()

        # アプリの終了
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(0)

        self.cStage.draw()
        self.cPlayer.draw()

        #writer = puf.Writer("misaki_mincho.ttf")
        #writer.draw(0, 0, "FPS : " + str(int(self.fps_avg)), 16, 7)

        pyxel.text(5, 5, f"FPS(avg30): {self.fps_avg:4.1f}", 7)

        # # テスト用
        #pyxel.blt(0, 0, 1, 0, 0, 32, 32,1)
        # pyxel.blt(25, 0, 1, 100, 100, 256, 16)
        # pyxel.blt(0,50,1,0,50,25,25)

        # self.img = pyxel.Image(1024, 1024)
        # self.img.load(x=0, y=0, filename="asset/Monster/Slime_Blue.png")
        # pyxel.blt(0, 0, self.img, 0, 0, 96, 128,1)

App()
