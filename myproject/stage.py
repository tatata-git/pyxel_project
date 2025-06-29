from typing import override
import math
import pyxel
import const
from input import Input
from vec2 import Vec2


class CStage:
    def __init__(self):
        self.CameraPos = Vec2(0,0)
        # CameraPosには描画範囲の左上のグローバル座標を格納
        # X座標：(CameraPos.X ~ CameraPos.X + const.GAMEWINDOW_wIDTH)
        # Y座標：(CameraPos.Y ~ CameraPos.Y + const.GAMEWINDOW_HEIGHT)
        # のグローバル座標の範囲が描画される


    def update(self):
        pass

    def draw(self):
        # カメラの右下グローバル座標を計算
        CameraRightDownsidePos = Vec2(
            self.CameraPos.x + const.GAMEWINDOW_WIDTH,
            self.CameraPos.y + const.GAMEWINDOW_HEIGHT
        )

        # x,yそれぞれの方向に何枚のMAPUNITが必要か計算
        NumMapUnit = Vec2(
            math.ceil(CameraRightDownsidePos.x / const.MAP_UNIT_WIDTH) - (self.CameraPos.x // const.MAP_UNIT_WIDTH),
            math.ceil(CameraRightDownsidePos.y / const.MAP_UNIT_HEIGHT) - (self.CameraPos.y // const.MAP_UNIT_HEIGHT),
        )

        # 描画開始位置の計算
        StartDrawPos = Vec2(
            (((self.CameraPos.x // const.MAP_UNIT_WIDTH) * const.MAP_UNIT_WIDTH) - self.CameraPos.x),
            (((self.CameraPos.y // const.MAP_UNIT_HEIGHT) * const.MAP_UNIT_HEIGHT) - self.CameraPos.y)
        )

        # 描画位置の初期化
        NowDrawPos = Vec2(StartDrawPos.x, StartDrawPos.y)
        for i in range(int(NumMapUnit.y)):
            # 描画開始位置(y座標)を計算
            NowDrawPos.y = StartDrawPos.y + i * const.MAP_UNIT_HEIGHT

            for j in range(int(NumMapUnit.x)):
                # 描画開始位置(x座標)を計算
                NowDrawPos.x = StartDrawPos.x + j * const.MAP_UNIT_WIDTH
                pyxel.bltm(NowDrawPos.x , NowDrawPos.y,                     # 描画開始位置
                           0,                                               # タイルマップ番号
                           0, 0,                                            # タイルマップの描画開始位置
                           const.MAP_UNIT_WIDTH, const.MAP_UNIT_HEIGHT)     # タイルマップの描画する範囲
                
            
            
    def SetCameraPos(self, TargetPos: Vec2):
        self.CameraPos.x = TargetPos.x - (const.GAMEWINDOW_WIDTH/2 - const.PLAYER_WIDTH / 2)
        self.CameraPos.y = TargetPos.y - (const.GAMEWINDOW_HEIGHT/2 - const.PLAYER_HEIGHT / 2)