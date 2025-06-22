import pyxel
import const

#####カラーボールの描画のためのクラス
class CColorBall:
    # 指定されたカラーボールのu座標を返す
    @staticmethod
    def U(InputColorId):
        return InputColorId * const.DEFAULT_WIDTH + const.COLOR_BALL_OFFSET_U

    # 指定されたカラーボールのv座標を返す
    @staticmethod
    def V(InputColorId):
        return const.COLOR_BALL_OFFSET_V
    
    # (DrawX, DrawY)の位置にInputColorIdで指定されたいろのColorBallを描画する
    @staticmethod
    def Draw(DrawX, DrawY, InputColorId, TransParentCol = const.TRANSPARENT_COLLORKEY):
        pyxel.blt(DrawX, DrawY, const.COLOR_BALL_IMGPLT, CColorBall.U(InputColorId), CColorBall.V(InputColorId), const.COLOR_BALL_WIDTH, const.COLOR_BALL_HEIGHT, TransParentCol)