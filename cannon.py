import emoji
from gameObject import GameObject

class Cannon(GameObject):
    sprite = emoji.emojize(':robot:')

    def moveLeft(self):
        if self.x > 2:
            self.x -= 1

    def moveRight(self):
        if self.x < 98:
            self.x += 1

    def update(self, keyPressed):
        if keyPressed == "s" or keyPressed == "S":
            self.moveLeft()
        
        if keyPressed == "d" or keyPressed == "D":
            self.moveRight()
                
        super().update(keyPressed)