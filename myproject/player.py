import pyxel
import const
import os
from typing import override
from input import Input
from vec2 import Vec2
from animation import CAnimation
from color_ball import CColorBall

from automade.img_enum import Img
from imagemanager import CImageManager
from stage import CStage

from entity import CEntity

class CPlayer(CEntity):

    # 初期化
    def __init__(self, InputGlobalPos: Vec2, InputLocalPos: Vec2):
        super().__init__(InputGlobalPos, InputLocalPos)
        self.cStage = None
        self.eWalkState = const.eWALKSTATE_ID.FRONT
        self.WalkAnimation = CAnimation(const.PLAYER_WALKANIMATION_FRAMES, const.PLAYER_WALKANIMATION_SPEED, True)
        self.DamageAnimation = CAnimation(2,3,True)
        self.Img = CImageManager.Instance().images[Img.eIMG_SLIME_BLUE.value]
        self.Opacity = 1.0 # 不透明度
        self.fade_speed = 0.07 # 1フレーム当たりの不透明度の減少量

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

        self.DamageAnimation.update()

        if self.Opacity > 0.0:
            self.Opacity = max(self.Opacity - self.fade_speed, 0.0)
        if self.Opacity == 0.0:
            self.Opacity = 1.0

    # 描画
    @override
    def draw(self):
        #CColorBall.Draw(self.LocalPos, const.COLOR_ID.RED)

        # # 点滅処理
        # if self.DamageAnimation.CurrentFrame() == 0:
        #     for c in range(const.COLOR_NUM):
        #         if c != const.TRANSPARENT_COLLORKEY:
        #             pyxel.pal(c, const.COLOR_WHITE)

        pyxel.dither(self.Opacity)

        NowWalkAnimationFrame = self.WalkAnimation.CurrentFrame()
        pyxel.blt(self.LocalPos.x, self.LocalPos.y,
                  self.Img,
                  const.PLAYER_WIDTH * NowWalkAnimationFrame, const.PLAYER_HEIGHT * self.eWalkState,
                  const.PLAYER_WIDTH, const.PLAYER_HEIGHT,
                  const.TRANSPARENT_COLLORKEY)

        pyxel.dither(1.0)
        #pyxel.pal()