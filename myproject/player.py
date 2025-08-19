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

from entity import CEntity

class CPlayer(CEntity):
    # 初期化
    def __init__(self, InputGlobalPos: Vec2, InputLocalPos: Vec2):
        super().__init__(InputGlobalPos, InputLocalPos)

    # 更新
    @override
    def update(self):
        if Input.IsPress(Input.RIGHT):
            self.GlobalPos.x += const.CHARA_VEL
            self.eWalkState = const.eWALKSTATE_ID.RIGHT

        if Input.IsPress(Input.LEFT):
            self.GlobalPos.x -= const.CHARA_VEL
            self.eWalkState = const.eWALKSTATE_ID.LEFT

        if Input.IsPress(Input.UP):
            self.GlobalPos.y -= const.CHARA_VEL
            self.eWalkState = const.eWALKSTATE_ID.BACK

        if Input.IsPress(Input.DOWN):
            self.GlobalPos.y += const.CHARA_VEL
            self.eWalkState = const.eWALKSTATE_ID.FRONT

        # カメラ位置の更新を要求
        self.cStage.SetCameraPos(self.GlobalPos)

        self.UpdateLocalPos(self.cStage.CameraPos)  # ローカル座標を更新
        self.WalkAnimation.update()                 # 歩行アニメの更新 
        self.DamageAnimation.update()               # ダメージアニメの更新

        if self.IsDither:
            self.UpdateOpacity()

    # 描画
    @override
    def draw(self):
        with self.DamageAnime():
            with self.DitherAnime():
                self.DrawWalking()