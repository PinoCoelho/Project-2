#import Principal

#Principal.iniciador()

import tkinter as tk

# --- functions ---

def move_a(event):
    canvas.coords(a, event.x-50, event.y-50, event.x+50, event.y+50)

def move_b():
    # inform function to use external/global variable 
    # because we use `=` to change its value
    global b_speed
    global b_move_down

    canvas.move(b, 0, b_speed)

    # get current position        
    x1, y1, x2, y2 = canvas.coords(b)

    # check if you have to change direction
    #if b_speed > 0:
    if b_move_down:
        # if it reachs bottom
        if y2 > 300:
            # change direction
            #b_move_down = False
            b_move_down = not b_move_down
            b_speed = -b_speed
    else:
        # if it reachs top
        if y1 < 0:
            # change direction
            #b_move_down = True
            b_move_down = not b_move_down
            b_speed = -b_speed

    # move again after 25 ms (0.025s)
    root.after(25, move_b)

# --- main ---

# init
root = tk.Tk()

# create canvas
canvas = tk.Canvas(root, width=500, height=300)
canvas.pack()

# create objects
a = canvas.create_rectangle(0, 0, 100, 100, fill='red')
b = canvas.create_rectangle(0, 0, 100, 100, fill='blue')
# create global variables
b_move_down = True
b_speed = 5

# start moving `a` with mouse
canvas.bind("<Motion>", move_a)

# start moving `b` automatically
move_b()

# start program
root.mainloop()