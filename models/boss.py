from views import bossview


class Boss(bossview.BossV):

    def __init__(self):
        bossview.BossV.__init__(self)

        self.health = 200
        self.attack = 15

