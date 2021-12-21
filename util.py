
# Confirm to quit game
def confirm(win, y, x, message):
    win.addstr(y, x, message)    
    keyPressed = 0
    while keyPressed != ord('y') and keyPressed != ord('Y') and keyPressed != ord('n') and keyPressed != ord('N'):
        win.timeout(100)
        keyPressed = win.getch()

    win.addstr(y, x, len(message) * " ")    

    if keyPressed == ord('y') or keyPressed == ord('Y'):
        return True
    else:
        return False

# Confirm to quit game
def confirmQuit(win):    
    return confirm(win, 26 , 2,  "Do you want to quit game? Press Y to exit or N other key to keep playing.")    
