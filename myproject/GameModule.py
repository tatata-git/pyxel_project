import pyxel
import PyxelUniversalFont as puf

import const
from color_ball import CColorBall
from vec2 import Vec2

from imagemanager import CImageManager

from player import CPlayer
from stage import CStage

class App:
    def __init__(self):
        pyxel.init(const.GAMEWINDOW_WIDTH, const.GAMEWINDOW_HEIGHT, title="myproject", display_scale = const.DIPLAY_SCALE)
        pyxel.load("myproject_editor.pyxres")

        # # テスト用
        # pyxel.images[1].load(100,100,"asset/palette.png")
        pyxel.images[1].load(0, 0, "asset/Monster/Slime_Blue.png")
        # pyxel.images[1].load(0,50, "asset/black.png")

        # イメージマネージャの初期化
        pI = CImageManager.Instance()
        pI.LoadAll()
        

        ## オブジェクトの生成
        # プレイヤー
        self.cPlayer = CPlayer(Vec2(const.PLAYER_INIT_POS_X, const.PLAYER_INIT_POS_Y), Vec2(const.PLAYER_INIT_POS_X, const.PLAYER_INIT_POS_Y))

        # ステージ
        self.cStage  = CStage()

        ## 依存性の注入
        # プレイヤー
        self.cPlayer.InitStage(self.cStage)

        pyxel.run(self.update, self.draw)

    def update(self):
        self.cPlayer.update()
        self.cStage.update()

        # アプリの終了
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(0)

        self.cStage.draw()
        self.cPlayer.draw()

        writer = puf.Writer("misaki_gothic.ttf")
        writer.draw(0, 0, "PlayerGloBalPosX : " + str(int(self.cPlayer.GlobalPos.x)), 16, 7)

        # # テスト用
        #pyxel.blt(0, 0, 1, 0, 0, 32, 32,1)
        # pyxel.blt(25, 0, 1, 100, 100, 256, 16)
        # pyxel.blt(0,50,1,0,50,25,25)

        
        self.img = pyxel.Image(1024, 1024)
        self.img.load(x=0, y=0, filename="asset/Monster/Slime_Blue.png")
        pyxel.blt(0, 0, self.img, 0, 0, 96, 128,1)

App()
