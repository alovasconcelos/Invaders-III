from alien import Alien
from gameObject import GameObject
import alien

class AlienSquad(GameObject):
    x_limit = 54
    direction = 1

    aliens = [[0 for i in range(8)] for j in range(5)]
 
    def __init__(self, win, y, x):
        super().__init__(win, y, x)
        self.win = win
        for yaxis in range(5):
            for xaxis in range(8) :                  
                self.aliens[yaxis][xaxis] = Alien(self.win, self.y + yaxis, self.x + (5 * xaxis))

    def draw(self):
#        for i in range(75):
        for yaxis in range(5):
            for xaxis in range(8) :                  
                self.aliens[yaxis][xaxis].draw()

    def move(self):
        if self.x == self.x_limit or self.x == 2:
            self.direction = self.direction * (-1)
            
        self.x += self.direction
        for yaxis in range(5):
            for xaxis in range(8) :                  
                self.aliens[yaxis][xaxis].clear();
                self.aliens[yaxis][xaxis].x = self.x + (5 * xaxis)

                