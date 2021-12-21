import emoji
from gameObject import GameObject

class Bullet(GameObject):
    sprite = emoji.emojize(':fire:')
    fired = False

    def fire(self, cannon):
        self.fired = True
        self.x = cannon.x
        for yAxis in range(cannon.y, 4, -1):
            self.y = yAxis
