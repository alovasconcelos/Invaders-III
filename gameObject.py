class GameObject:
    win = None
    x = 0
    y = 0
    visible = True
    sprite = ""

    def __init__(self, win, y, x):
        self.win =  win
        self.y = y
        self.x = x

    def draw(self):
        self.win.addstr(self.y, self.x, self.sprite)    

    def clear(self):
        self.win.addstr(self.y, self. x -1, " ") 
        self.win.addstr(self.y, self. x +1, " ") 
