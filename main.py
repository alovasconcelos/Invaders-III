import curses
import random
import time
from alien_squad import AlienSquad
import util
from curses import wrapper
from cannon import Cannon
import locale
locale.setlocale(locale.LC_ALL, '')

# Curses initialization
sc = curses.initscr()

# Screen size
height = 28
width = 100

win = curses.newwin(height, width, 0, 0)
curses.noecho()  
win.keypad(1)
curses.curs_set(0)

# Cannon
cannon = Cannon(win, 24, (width // 2) - 1)

# Initial x squad position - random from 2 to 54
squadX = random.randrange(2, AlienSquad.x_limit)

# Alien squad
alienSquad = AlienSquad(win, 4, squadX)

# Confirm to quit game
def confirmQuit():    
    return util.confirm(win, 26 , 2,  "Do you want to quit game? Press Y to exit or N other key to keep playing.")    
        
# Game loop
while True:
    win.border(0)
    
    win.timeout(100)
    keyPressed = win.getch()

    if keyPressed == ord('q'):
        if confirmQuit():
            break
    
    cannon.draw()
    alienSquad.draw()
    alienSquad.move() 

sc.refresh()
curses.endwin()
