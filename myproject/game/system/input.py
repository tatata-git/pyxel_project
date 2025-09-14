import pyxel

class Input:
    UP = [pyxel.KEY_W, pyxel.GAMEPAD1_BUTTON_DPAD_UP]
    DOWN = [pyxel.KEY_S, pyxel.GAMEPAD1_BUTTON_DPAD_DOWN]
    RIGHT = [pyxel.KEY_D, pyxel.GAMEPAD1_BUTTON_DPAD_RIGHT]
    LEFT = [pyxel.KEY_A, pyxel.GAMEPAD1_BUTTON_DPAD_LEFT]

    @staticmethod
    def IsPress(keys):
        return any(pyxel.btn(k) for k in keys)