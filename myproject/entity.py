from abc import ABC, abstractmethod
from vec2 import Vec2

class CEntity(ABC):

    # GlobalPosとLocalPosを両方受け取って初期化
    def __init__(self, InputGlobalPos: Vec2, InputLocalPos: Vec2):
        self.GlobalPos: Vec2 = InputGlobalPos
        self.LocalPos: Vec2 = InputLocalPos

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def draw(self):
        pass

    def UpdateLocalPos(self, InputCameraPos):
        self.LocalPos = self.GlobalPos - InputCameraPos