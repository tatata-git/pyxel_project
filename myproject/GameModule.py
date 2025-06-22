import pyxel
from enum import IntEnum, auto

# 変更test

TRANSPARENT_COLLORKEY = 0   # 透明色の指定

DEFAULT_WIDTH = 16          # 絵の幅
DEFAULT_HEIGHT = 16         # 絵の高さ

COLOR_BALL_IMGPLT = 0       # ColorBallが書かれているimgパレットの番号
COLOR_BALL_WIDTH = 16       # ColorBallの幅
COLOR_BALL_HEIGHT = 16      # ColorBallの高さ
COLOR_BALL_OFFSET_U = 0     # ColorBallが格納されている最初のu座標
COLOR_BALL_OFFSET_V = 0     # ColorBallが格納されている最初のv座標

class COLOR_ID(IntEnum):
    RED     =   0       
    GREEN   =   auto()  
    BLUE    =   auto()

#
class COLOR_BALL:
    # 指定されたカラーボールのu座標を返す
    @staticmethod
    def U(InputColorId):
        return InputColorId * DEFAULT_WIDTH + COLOR_BALL_OFFSET_U

    # 指定されたカラーボールのv座標を返す
    @staticmethod
    def V(InputColorId):
        return COLOR_BALL_OFFSET_V
    
    # (DrawX, DrawY)の位置にInputColorIdで指定されたいろのColorBallを描画する
    @staticmethod
    def Draw(DrawX, DrawY, InputColorId, TransParentCol = TRANSPARENT_COLLORKEY):
        pyxel.blt(DrawX, DrawY, COLOR_BALL_IMGPLT, COLOR_BALL.U(InputColorId), COLOR_BALL.V(InputColorId), COLOR_BALL_WIDTH, COLOR_BALL_HEIGHT, TransParentCol)
    
class CPlayer:
    # 初期化
    def __init__(self, Inputm_XPos, Inputm_YPos):
        self.m_XPos = Inputm_XPos
        self.m_YPos = Inputm_YPos

    # 更新
    def update(self):
        if pyxel.btn(pyxel.KEY_D):
            self.m_XPos += 1
        
        if pyxel.btn(pyxel.KEY_A):
            self.m_XPos -= 1

        if pyxel.btn(pyxel.KEY_W):
            self.m_YPos -= 1

        if pyxel.btn(pyxel.KEY_S):
            self.m_YPos += 1    

    # 描画
    def draw(self):
        COLOR_BALL.Draw(self.m_XPos, self.m_YPos, COLOR_ID.GREEN)


class App:
    def __init__(self):
        pyxel.init(240, 240, title="myproject")
        pyxel.load("myproject_editor.pyxres")

        self.m_cPlayer = CPlayer(50, 50) # プレイヤーインスタンスの作成

        pyxel.run(self.update, self.draw)

    def update(self):
        self.m_cPlayer.update()

        # アプリの終了
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(0)
        #pyxel.text(55, 41, "Hello, Pyxel!", pyxel.frame_count % 16)

        self.m_cPlayer.draw()


App()
