from tkinter import *

#circles 1st set of quads - c for circle x/y for x or y 1 for 1st set
global cx1
cx1 = 10
global cy1
cy1 = 10


# circles second set of quads
global cx2
cx2 = 90
global cy2
cy2 = 90


root = Tk()
root.title("jump")

game = Canvas(root, width = 1000, height = 1000)
game.pack()

ship11 = game.create_oval(cx1, cy1, cx2, cy2, fill = "black")
#ship12 = game.create_polygon((50, 10, 15, 70, 85, 70), fill="red")

def down(zero) :
    dx = 0
    dy = 100
    game.move(ship11, dx, dy)
    print("down")

def up (zero) :
    dx = 0
    dy = -100
    game.move(ship11, dx, dy)
    print("up")

def left (zero) :
    dx = -100
    dy = 0
    game.move(ship11, dx, dy)
    print("left")

def right (zero) :
    dx = 100
    dy = 0
    game.move(ship11, dx, dy)
    print("right")

root.bind("s", down)
root.bind("w", up)
root.bind("a", left)
root.bind("d", right)

root.mainloop()