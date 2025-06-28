from typing import override
import pyxel
import const
from input import Input
from vec2 import Vec2

from color_ball import CColorBall

from entity import CEntity
class CPlayer(CEntity):

    # 初期化
    def __init__(self, InputGlobalPos: Vec2, InputLocalPos: Vec2):
        super().__init__(InputGlobalPos, InputLocalPos)

    # 更新
    @override
    def update(self):
        if Input.IsPress(Input.RIGHT):
            self.GlobalPos.x += const.PLAYER_VEL
        
        if Input.IsPress(Input.LEFT):
            self.GlobalPos.x -= const.PLAYER_VEL

        if Input.IsPress(Input.UP):
            self.GlobalPos.y -= const.PLAYER_VEL

        if Input.IsPress(Input.DOWN):
            self.GlobalPos.y += const.PLAYER_VEL 
    
    # 描画
    @override
    def draw(self):
        CColorBall.Draw(self.GlobalPos, const.COLOR_ID.RED)