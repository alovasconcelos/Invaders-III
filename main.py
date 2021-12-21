import curses
import random
import time
from alien_squad import AlienSquad
from bullet import Bullet
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

# Game objects
game_objects = []

# Initial x cannon position
cannonX = (width // 2) - 1

# Cannon
game_objects.append(Cannon(win, 24, cannonX))

# Initial x squad position - random from 2 to 54
squadX = random.randrange(2, AlienSquad.x_limit)

# Alien squad
game_objects.append(AlienSquad(win, 4, squadX))

# Bullets
game_objects.append(Bullet(win, 23, cannonX))
game_objects.append(Bullet(win, 23, cannonX))
game_objects.append(Bullet(win, 23, cannonX))


# def fire():
#     if bullet_1.fired == False:
#         bullet_1.fire(cannon)
#         return
    
#     if bullet_2.fired == False:
#         bullet_2.fire(cannon)
#         return

#     if bullet_3.fired == False:
#         bullet_3.fire(cannon)
#         return

#     pass

# Game loop
while True:    
    win.timeout(100)
    keyPressed = win.getch()

    # Quit
    if keyPressed == ord('q'):
        if util.confirmQuit(win):
            break
    
    # Update  game objects
    for obj in range(len(game_objects)):
        game_objects[obj].update(win)

    # Fire
    if keyPressed == ord(' '):
        pass
        #fire()
    

sc.refresh()
curses.endwin()
