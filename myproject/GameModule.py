import pyxel
import Const

# カラーボールの描画のためのクラス
class COLOR_BALL:
    # 指定されたカラーボールのu座標を返す
    @staticmethod
    def U(InputColorId):
        return InputColorId * Const.DEFAULT_WIDTH + Const.COLOR_BALL_OFFSET_U

    # 指定されたカラーボールのv座標を返す
    @staticmethod
    def V(InputColorId):
        return Const.COLOR_BALL_OFFSET_V
    
    # (DrawX, DrawY)の位置にInputColorIdで指定されたいろのColorBallを描画する
    @staticmethod
    def Draw(DrawX, DrawY, InputColorId, TransParentCol = Const.TRANSPARENT_COLLORKEY):
        pyxel.blt(DrawX, DrawY, Const.COLOR_BALL_IMGPLT, COLOR_BALL.U(InputColorId), COLOR_BALL.V(InputColorId), Const.COLOR_BALL_WIDTH, Const.COLOR_BALL_HEIGHT, TransParentCol)
    
# プレイヤークラス
class CPlayer:
    # 初期化
    def __init__(self, Inputm_XPos, Inputm_YPos):
        self.XPos = Inputm_XPos
        self.YPos = Inputm_YPos

    # 更新
    def update(self):
        if pyxel.btn(pyxel.KEY_D):
            self.XPos += 1
        
        if pyxel.btn(pyxel.KEY_A):
            self.XPos -= 1

        if pyxel.btn(pyxel.KEY_W):
            self.YPos -= 1

        if pyxel.btn(pyxel.KEY_S):
            self.YPos += 1    

    # 描画
    def draw(self):
        COLOR_BALL.Draw(self.XPos, self.YPos, Const.COLOR_ID.GREEN)


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
