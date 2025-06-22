#####定数系まとめ#####

from enum import IntEnum, auto

TRANSPARENT_COLLORKEY = 0   # 透明色の指定

DEFAULT_WIDTH = 16          # 絵の幅
DEFAULT_HEIGHT = 16         # 絵の高さ

COLOR_BALL_IMGPLT = 0       # ColorBallが書かれているimgパレットの番号
COLOR_BALL_WIDTH = 16       # ColorBallの幅
COLOR_BALL_HEIGHT = 16      # ColorBallの高さ
COLOR_BALL_OFFSET_U = 0     # ColorBallが格納されている最初のu座標
COLOR_BALL_OFFSET_V = 0     # ColorBallが格納されている最初のv座標

class COLOR_ID(IntEnum):
    RED     =   0       
    GREEN   =   auto()  
    BLUE    =   auto()