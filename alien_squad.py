from alien import Alien
from gameObject import GameObject
import alien

class AlienSquad(GameObject):
    x_limit = 54
    direction = 1

    aliens = [[0 for i in range(15)] for j in range(5)]
 
    def __init__(self, y, x):
        self.y = y
        self.x = x
        for yaxis in range(5):
            for xaxis in range(15) :                  
                #self.aliens.append(Alien(self.y + yaxis, self.x + 3 * xaxis))
                self.aliens[yaxis][xaxis] = Alien(self.y + yaxis, self.x + 3 * xaxis)

    def draw(self, win):
#        for i in range(75):
        for yaxis in range(5):
            for xaxis in range(15) :                  
                self.aliens[yaxis][xaxis].draw(win)

    def clear(self, win):
        for yaxis in range(5):
            win.addstr(self.y + yaxis, 2, 90 * " ")    

    def move(self):
        if self.x == self.x_limit or self.x == 2:
            self.direction = self.direction * -1
            
        self.x += self.direction
        for yaxis in range(5):
            for xaxis in range(15) :                  
                self.aliens[yaxis][xaxis].x = self.x + 3 * xaxis

                