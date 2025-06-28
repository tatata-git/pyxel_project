import pyxel
import const
from color_ball import CColorBall
from input import Input
from vec2 import Vec2

from player import CPlayer


class App:
    def __init__(self):
        pyxel.init(const.GAMEWINDOW_WIDTH, const.GAMEWINDOW_HEIGHT, title="myproject", display_scale = 2)
        pyxel.load("myproject_editor.pyxres")

        # # テスト用
        # pyxel.images[1].load(100,100,"asset/palette.png")
        # pyxel.images[1].load(0, 0, "asset/wizard2550.png")
        # pyxel.images[1].load(0,50, "asset/black.png")

        # プレイヤーインスタンスの作成
        self.cPlayer = CPlayer(Vec2(const.PLAYER_INIT_POS_X, const.PLAYER_INIT_POS_Y), Vec2(const.PLAYER_INIT_POS_X, const.PLAYER_INIT_POS_Y))

        pyxel.run(self.update, self.draw)

    def update(self):
        self.cPlayer.update()

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
        self.cPlayer.draw()

App()
