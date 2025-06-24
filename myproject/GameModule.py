import pyxel
import const
from color_ball import CColorBall
from input import Input

# プレイヤークラス
class CPlayer:
    # 初期化
    def __init__(self, Inputm_XPos, Inputm_YPos):
        self.XPos = Inputm_XPos
        self.YPos = Inputm_YPos

    # 更新
    def update(self):
        if Input.IsPress(Input.RIGHT):
            self.XPos += 1
        
        if Input.IsPress(Input.LEFT):
            self.XPos -= 1

        if Input.IsPress(Input.UP):
            self.YPos -= 1

        if Input.IsPress(Input.DOWN):
            self.YPos += 1    

    # 描画
    def draw(self):
        CColorBall.Draw(self.XPos, self.YPos, const.COLOR_ID.GREEN)


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
