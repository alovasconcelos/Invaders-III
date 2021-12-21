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

    def move(self):
        if self.y == 4:
            self.fired = False
            self.visible = False

    def update(self, keyPressed): 
        super().update(keyPressed)
        self.move()

