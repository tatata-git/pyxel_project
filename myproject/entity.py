import pyxel
from abc import ABC, abstractmethod
from contextlib import contextmanager

import const
from animation import CAnimation
from vec2 import Vec2

from automade.img_enum import Img
from imagemanager import CImageManager

from stage import CStage

class CEntity(ABC):

    # GlobalPosとLocalPosを両方受け取って初期化
    def __init__(self, InputGlobalPos: Vec2, InputLocalPos: Vec2):
        self.GlobalPos: Vec2 = InputGlobalPos
        self.LocalPos: Vec2 = InputLocalPos

        self.Vel = 0    # 速度

        self.eWalkState = const.eWALKSTATE_ID.FRONT
        self.WalkAnimation = CAnimation(const.CHARA_WALKANIMATION_FRAMES, const.PLAYER_WALKANIMATION_SPEED, True)
        self.DamageAnimation = CAnimation(2, const.DAMAGEANIMATION_SPEED, True)
        self.Img = CImageManager.Instance().images[Img.eIMG_APPLE.value] # enumだけを保持して、ImageManagerの描画を都度呼び出す方がいいかも

        self.cStage = None  # 現在のステージを格納

        self.Opacity = 1.0              # 不透過度
        
        self.IsDamageAnime = False      # ダメージアニメ再生フラグ
        self.IsDither = False           # つぶつぶアニメ再生フラグ

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def draw(self):
        pass

    # ステージへの参照をセットする
    def SetStage(self, InputStage: CStage):
        self.cStage = InputStage

    # 画像の更新
    def SetImg(self, InputeImgValue: int):
        self.Img = CImageManager.Instance().images[InputeImgValue]

    # ローカル座標の更新
    def UpdateLocalPos(self, InputCameraPos: Vec2):
        self.LocalPos = self.GlobalPos - InputCameraPos

    # 現在のローカル座標に歩行アニメを描画
    def DrawWalking(self):
        NowWalkAnimationFrame = self.WalkAnimation.CurrentFrame()
        pyxel.blt(self.LocalPos.x, self.LocalPos.y,
                  self.Img,
                  const.CHARA_WIDTH * NowWalkAnimationFrame, const.CHARA_HEIGHT * self.eWalkState,
                  const.CHARA_WIDTH, const.CHARA_HEIGHT,
                  const.TRANSPARENT_COLLORKEY)
        
    def UpdateOpacity(self):
        if self.Opacity > 0.0:
            self.Opacity = max(self.Opacity - const.DITHER_SPEED, 0.0)
        if self.Opacity == 0.0:
            self.Opacity = 1.0
        
    # ダメージ時のエフェクト描画
    @contextmanager
    def DamageAnime(self):
        if self.IsDamageAnime:
            # 点滅処理開始
            if self.DamageAnimation.CurrentFrame() == 0:
                for c in range(const.COLOR_NUM):
                    if c != const.TRANSPARENT_COLLORKEY:
                        pyxel.pal(c, const.COLOR_WHITE)
        try:
            yield
        finally:
            pyxel.pal() # 点滅処理で使用したパレットのリセット

    # つぶつぶ処理
    @contextmanager
    def DitherAnime(self):
        if self.IsDither:
            # つぶつぶ処理開始
            pyxel.dither(self.Opacity)
        try:
            yield
        finally:
            pyxel.dither(1.0) # ditherのリセット
