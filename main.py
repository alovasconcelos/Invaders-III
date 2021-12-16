import curses
import random
import time
from curses import wrapper
from cannon import Cannon

# Emojis used as sprites
enemy = "\U0001F47E"
explosion = "\U0001F4A5"
fire = "\U0001F525"

# Curses initialization
sc = curses.initscr()
h, w = sc.getmaxyx()
win = curses.newwin(h, w, 0, 0)
curses.noecho()  
win.keypad(1)
curses.curs_set(0)

# Cannon
cannon = Cannon(h - 4, w / 2 -1)


# Confirm to quit game
def confirmQuit():
    win.addstr(h - 2, 2, "Do you want to quit game? Press Y to exit or N other key to keep playing.")    
    keyPressed = 0
    while keyPressed != ord('y') and keyPressed != ord('Y') and keyPressed != ord('n') and keyPressed != ord('N'):
        win.timeout(100)
        keyPressed = win.getch()

    win.addstr(h - 2, 2, "                                                                                                                             ")    
    if keyPressed == ord('y') or keyPressed == ord('Y'):
        return True
    else:
        return False

def drawCannon():
    win.addstr(cannon.x, cannon.y, "Do you want to quit game? Press Y to exit or N other key to keep playing.")    
        
# Game loop
while True:
    win.border(0)
    win.timeout(100)

    keyPressed = win.getch()

    if keyPressed == ord('q'):
        if confirmQuit():
            break

    

sc.refresh()
curses.endwin()


