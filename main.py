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
game_objects = [0,0,0,0,0]

CANNON_INDEX = 0
SQUAD_INDEX = 1
BULLET_1_INDEX = 2
BULLET_2_INDEX = 3
BULLET_3_INDEX = 4

# Initial x cannon position
cannonX = (width // 2) - 1

# Cannon
game_objects[CANNON_INDEX] = Cannon(win, 24, cannonX)

# Initial x squad position - random from 3 to 54
squadX = random.randrange(3, AlienSquad.x_limit)

# Alien squad
game_objects[SQUAD_INDEX] = AlienSquad(win, 4, squadX)

# Bullets
game_objects[BULLET_1_INDEX] = Bullet(win, 23, cannonX)
game_objects[BULLET_2_INDEX] = Bullet(win, 23, cannonX)
game_objects[BULLET_3_INDEX] = Bullet(win, 23, cannonX)

def fire():
    if game_objects[BULLET_1_INDEX].fired == False:
        game_objects[BULLET_1_INDEX].fire(game_objects[CANNON_INDEX])
        return
    
    if game_objects[BULLET_2_INDEX].fired == False:
        game_objects[BULLET_2_INDEX].fire(game_objects[CANNON_INDEX])
        return
    
    if game_objects[BULLET_3_INDEX].fired == False:
        game_objects[BULLET_3_INDEX].fire(game_objects[CANNON_INDEX])
        return
    

# Game loop
while True:    
    win.timeout(100)
    keyPressed = win.getch()

    # Quit
    if keyPressed == ord('q') and util.confirmQuit(win):
        break
    
    # Update  game objects
    for obj in game_objects:
        obj.update(keyPressed)

    # Fire
    if keyPressed == ord(' '):
        fire()
    
sc.refresh()
curses.endwin()
