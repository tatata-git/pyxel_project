import pyxel
import const
from color_ball import CColorBall
from input import Input

import colorsys
# test用
# プレイヤークラス
class CPlayer:
    # 初期化
    def __init__(self, Inputm_XPos, Inputm_YPos):
        self.XPos = Inputm_XPos
        self.YPos = Inputm_YPos

    # 更新
    def update(self):
        if Input.IsPress(Input.RIGHT):
            self.XPos += const.PLAYER_VEL
        
        if Input.IsPress(Input.LEFT):
            self.XPos -= const.PLAYER_VEL

        if Input.IsPress(Input.UP):
            self.YPos -= const.PLAYER_VEL

        if Input.IsPress(Input.DOWN):
            self.YPos += const.PLAYER_VEL 

    # 描画
    def draw(self):
        CColorBall.Draw(self.XPos, self.YPos, const.COLOR_ID.RED)


class App:
    def __init__(self):
        pyxel.init(const.GAMEWINDOW_WIDTH, const.GAMEWINDOW_HEIGHT, title="myproject")
        pyxel.load("myproject_editor.pyxres")

        # # テスト用
        # pyxel.images[1].load(100,100,"asset/palette.png")
        # pyxel.images[1].load(0, 0, "asset/wizard2550.png")
        # pyxel.images[1].load(0,50, "asset/black.png")

        self.m_cPlayer = CPlayer(const.PLAYER_INIT_POS_X, const.PLAYER_INIT_POS_Y) # プレイヤーインスタンスの作成

        pyxel.run(self.update, self.draw)

    def update(self):
        self.m_cPlayer.update()

        # アプリの終了
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(0)

        # # テスト用
        # pyxel.blt(0, 0, 1, 0, 0, 25, 50,1)
        # pyxel.blt(25, 0, 1, 100, 100, 256, 16)
        # pyxel.blt(0,50,1,0,50,25,25)

        pyxel.bltm(0, 0, 0, 0, 0, 256, 256)
        self.m_cPlayer.draw()

App()
