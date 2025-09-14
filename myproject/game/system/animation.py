class CAnimation:
    def __init__(self, numFrames, speed, loop=True):
        self.NumFrames = numFrames  # アニメーションの総コマ数
        self.Speed = speed      # コマが切り替わるフレーム数
        self.Loop = loop        # ループ再生フラグ
        self.NowFrame = 0       # いまのコマ数
        self.Counter = 0        # 毎フレームごとに増やすカウンタ
        self.IsFinish = False   # アニメ再生終わったかどうか

    def update(self):
        if self.IsFinish: # アニメーション終了済み
            return

        self.Counter += 1

        if self.Counter >= self.Speed:
            self.Counter = 0        # カウンタの初期化
            self.NowFrame += 1
            
            if self.NowFrame >= self.NumFrames: # アニメーションが一周したとき
                if self.Loop:   # ループさせるとき
                    self.NowFrame = 0

                else:           # ループさせないとき
                    self.NowFrame = self.NumFrames
                    self.IsFinish = True # アニメーションを終了済みにする

                
                

    def CurrentFrame(self):
        return self.NowFrame

    def Reset(self):
        self.NowFrame = 0
        self.Counter = 0
        self.IsFinish = False
