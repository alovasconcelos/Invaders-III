class GameObject:
    x = 0
    y = 0
    visible = True
    sprite = ""

    def __init__(self, y, x):
        self.y = y
        self.x = x

    def draw(self, win):
        win.addstr(self.y, self.x, self.sprite)    

    def clear(self, win):
        win.addstr(self.y, self.x, " ") 
