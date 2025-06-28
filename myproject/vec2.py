class Vec2:
    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector2({self.x}, {self.y})"

    # 加算: v1 + v2
    def __add__(self, other):
        if not isinstance(other, Vec2):
            return NotImplemented
        return Vec2(self.x + other.x, self.y + other.y)

    # 減算: v1 - v2
    def __sub__(self, other):
        if not isinstance(other, Vec2):
            return NotImplemented
        return Vec2(self.x - other.x, self.y - other.y)

    # 乗算（スカラー倍）: v * scalar
    def __mul__(self, scalar):
        if not isinstance(scalar, (int, float)):
            return NotImplemented
        return Vec2(self.x * scalar, self.y * scalar)

    # 乗算（反転対応）: scalar * v
    __rmul__ = __mul__

    # 除算（スカラーで割る）: v / scalar
    def __truediv__(self, scalar):
        if not isinstance(scalar, (int, float)):
            return NotImplemented
        return Vec2(self.x / scalar, self.y / scalar)