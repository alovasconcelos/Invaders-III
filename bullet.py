import emoji
from gameObject import GameObject

class Bullet(GameObject):
    sprite = emoji.emojize(':fire:')
    fired = False

    def __init__(self, win, y, x):
        self.visible = False
        super().__init__(win, y, x)

    def fire(self, cannon):
        self.fired = True
        self.visible = True
        self.x = cannon.x
        self.y = cannon.y            

    def clearBulletTrail(self):
        self.win.addstr(self.y + 1, self.x, " ") 

    def clear(self):
        self.win.addstr(self.y, self. x, " ") 

    def move(self):
        if self.y == 5:
            self.fired = False
            self.visible = False
            self.clear()
        else:
            self.y -= 1

    def update(self, keyPressed):         
        super().update(keyPressed)
        self.clearBulletTrail()
        self.move()

