#####定数系まとめ#####

from enum import IntEnum, auto

TRANSPARENT_COLLORKEY = 1   # 透明色の指定
COLOR_NUM = 217             # 色の総数. myproject_editor.pyxpalで指定している個数.
COLOR_WHITE = 7             # 白色を示すパレット番号

GAMEWINDOW_WIDTH = 600      # ウィンドウの幅
GAMEWINDOW_HEIGHT = 400     # ウィンドウの高さ
DIPLAY_SCALE = 2            # 拡大

# グローバル座標の範囲を定義. 0~GLOBAL_MAXまでの範囲を描画する
GLOBAL_MAX_X = 1000
GLOBAL_MAX_Y = 1000

DEFAULT_WIDTH = 16          # 絵の幅
DEFAULT_HEIGHT = 16         # 絵の高さ

COLOR_BALL_IMGPLT = 0       # ColorBallが書かれているimgパレットの番号
COLOR_BALL_WIDTH = 32       # ColorBallの幅
COLOR_BALL_HEIGHT = 32      # ColorBallの高さ
COLOR_BALL_OFFSET_U = 0     # ColorBallが格納されている最初のu座標
COLOR_BALL_OFFSET_V = 0     # ColorBallが格納されている最初のv座標

PLAYER_WIDTH = 32                                           # プレイヤーの幅
PLAYER_HEIGHT =32                                           # プレイヤーの高さ
PLAYER_INIT_POS_X = GLOBAL_MAX_X  / 2 - PLAYER_WIDTH / 2    # プレイヤーの初期x座標
PLAYER_INIT_POS_Y = GLOBAL_MAX_Y / 2 - PLAYER_HEIGHT / 2    # プレイヤーの初期y座標
PLAYER_VEL = 2                                              # プレイヤーの移動速度
PLAYER_WALKANIMATION_FRAMES = 3                             # 歩行アニメの総コマ数
PLAYER_WALKANIMATION_SPEED = 7                              # 歩行アニメのスピード              

# マップの一単位の高さを定義. マップはこの(MAP_UNIT_WIDTH*MAP_UNIT_HEIGHT)を一単位としてループして表示される
MAP_UNIT_WIDTH = 8 * 16      # マップ一単位の幅
MAP_UNIT_HEIGHT = 8 * 16     # マップ一単位の高さ



# colorball用のID
class eCOLOR_ID(IntEnum):
    RED     =   0       
    GREEN   =   auto()  
    BLUE    =   auto()

# 歩行アニメの状態
class eWALKSTATE_ID(IntEnum):
    FRONT   =   0
    LEFT    =   auto()
    RIGHT   =   auto()
    BACK    =   auto()
    