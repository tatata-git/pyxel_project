from typing import override
import pyxel
import const
from input import Input
from vec2 import Vec2
from animation import CAnimation

from color_ball import CColorBall

from stage import CStage

from entity import CEntity

class CPlayer(CEntity):

    # 初期化
    def __init__(self, InputGlobalPos: Vec2, InputLocalPos: Vec2):
        super().__init__(InputGlobalPos, InputLocalPos)
        self.cStage = None
        self.eWalkState = const.eWALKSTATE_ID.FRONT
        self.WalkAnimation = CAnimation(const.PLAYER_WALKANIMATION_FRAMES, 7, True)

    # ステージへの参照をセットする
    def InitStage(self, InputStage: CStage):
        self.cStage = InputStage

    # 更新
    @override
    def update(self):
        if Input.IsPress(Input.RIGHT):
            self.GlobalPos.x += const.PLAYER_VEL
            self.eWalkState = const.eWALKSTATE_ID.RIGHT
        
        if Input.IsPress(Input.LEFT):
            self.GlobalPos.x -= const.PLAYER_VEL
            self.eWalkState = const.eWALKSTATE_ID.LEFT

        if Input.IsPress(Input.UP):
            self.GlobalPos.y -= const.PLAYER_VEL
            self.eWalkState = const.eWALKSTATE_ID.BACK

        if Input.IsPress(Input.DOWN):
            self.GlobalPos.y += const.PLAYER_VEL 
            self.eWalkState = const.eWALKSTATE_ID.FRONT

        # カメラ位置の更新を要求
        self.cStage.SetCameraPos(self.GlobalPos)

        # ローカル座標を更新
        self.UpdateLocalPos(self.cStage.CameraPos)

        self.WalkAnimation.update()
    
    # 描画
    @override
    def draw(self):
        #CColorBall.Draw(self.LocalPos, const.COLOR_ID.RED)

        NowWalkAnimationFrame = self.WalkAnimation.current_frame()
        pyxel.blt(self.LocalPos.x, self.LocalPos.y,
                  1,
                  const.PLAYER_WIDTH * NowWalkAnimationFrame, const.PLAYER_HEIGHT * self.eWalkState,
                  const.PLAYER_WIDTH, const.PLAYER_HEIGHT,
                  const.TRANSPARENT_COLLORKEY)

    