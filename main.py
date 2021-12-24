import util
from game import Game

game = Game()
# Game loop
while True:    
    game.win.timeout(100)
    game.keyPressed = game.win.getch()

    # Quit
    if game.keyPressed == ord('q') and util.confirmQuit(game.win):
        break

    # Update game objects
    game.update()

    # Fire
    if game.keyPressed == ord(' '):
        game.fire()
    
game.sc.refresh()
game.curses.endwin()
