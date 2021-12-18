from alien import Alien
from gameObject import GameObject
import emoji
class AlienSquad(GameObject):
    x_limit = 60
    direction = 1

    rows = 8
    aliens_per_rows = 10

    aliens = [[0 for i in range(10)] for j in range(8)]
 
    def __init__(self, win, y, x):
        super().__init__(win, y, x)
        self.win = win
        for yaxis in range(self.rows):
            for xaxis in range(self.aliens_per_rows) :                  
                self.aliens[yaxis][xaxis] = Alien(self.win, self.y + yaxis, self.x + (3 * xaxis))

    def draw(self):
        for yaxis in range(self.rows):
            for xaxis in range(self.aliens_per_rows) :                  
                self.aliens[yaxis][xaxis].draw()

    def clearPreviousRow(self):
        for x in range(98):
            self.win.addstr(self.y-1, 2 + x,   emoji.emojize("  ") ) 

    def move(self):
        if self.x == self.x_limit or self.x == 2:
            self.direction = self.direction * (-1)            
            self.y += 1
            self.clearPreviousRow()
            
        self.x += self.direction
        for yaxis in range(self.rows):
            for xaxis in range(self.aliens_per_rows) : 
                self.aliens[yaxis][xaxis].clear();
                self.aliens[yaxis][xaxis].x = self.x + (3 * xaxis)
                self.aliens[yaxis][xaxis].y = self.y + yaxis

                