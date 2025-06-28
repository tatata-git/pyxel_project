from vec2 import Vec2

class Entity:
    # GlobalPosだけを受け取って初期化
    def __init__(self, InputGlobalPos: Vec2):
        self.GlobalPos = InputGlobalPos
        self.LocalPos = InputGlobalPos

    # GlobalPosとLocalPosを両方受け取って初期化
    def __init__(self, InputGlobalPos: Vec2, InputLocalPos: Vec2):
        self.GlobalPos = InputGlobalPos
        self.LocalPos = InputLocalPos