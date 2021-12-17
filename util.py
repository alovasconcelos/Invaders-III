
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
