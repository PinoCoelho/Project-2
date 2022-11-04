from tkinter import *
from tkinter.ttk import *
 
class escenario1:

    def __init__(self, master = None):
        self.master = master
 
        
        self.create()
 
    def create(self):
 
        self.master = Tk()

        self.imagen_robot = PhotoImage (file = 'Images/robot.png')
        self.imagen_cono = PhotoImage (file = 'Images/cono.png')
    
        self.master.title("ESCENARIO 1")
 
    
        self.master.minsize(502,502) 
 
    
    
        self.canvas = Canvas(self.master)

        #Horizontales
        
        self.canvas.create_line(700, 100, 0, 100)

        self.canvas.create_line(700, 200, 0, 200)

        self.canvas.create_line(700, 300, 0, 300)

        self.canvas.create_line(700, 400, 0, 400)

        self.canvas.create_line(700, 500, 0, 500)

        self.canvas.create_line(700, 600, 0, 600)
 
        #verticales

        self.canvas.create_line(500, 0, 500, 700)
         
        self.canvas.create_line(400, 0, 400, 700)

        self.canvas.create_line(300, 0, 300, 700)
        
        self.canvas.create_line(200, 0, 200, 700)
        
        self.canvas.create_line(100, 0, 100, 700) 
        
        #Imagenes

        self.canvas.create_image(50,50,image = self.imagen_robot)

        self.canvas.create_image(250,250,image = self.imagen_cono)

        self.canvas.pack(fill = BOTH, expand = True)

        self.master.mainloop()

class escenario2:

    def __init__(self, master = None):
        self.master = master
        
        self.create()
 
    def create(self):
 
        self.master = Tk()

        self.imagen_robot = PhotoImage (file = 'Images/robot.png')
        self.imagen_cono = PhotoImage (file = 'Images/cono.png')
        self.imagen_arbol = PhotoImage (file = 'Images/arbol.png')
    
        self.master.title("ESCENARIO 2")
 
    
        self.master.minsize(502,502) 
 
    
    
        self.canvas = Canvas(self.master)

        #Horizontales
        
        self.canvas.create_line(700, 100, 0, 100)

        self.canvas.create_line(700, 200, 0, 200)

        self.canvas.create_line(700, 300, 0, 300)

        self.canvas.create_line(700, 400, 0, 400)

        self.canvas.create_line(700, 500, 0, 500)

        self.canvas.create_line(700, 600, 0, 600)
 
        #verticales

        self.canvas.create_line(500, 0, 500, 700)
         
        self.canvas.create_line(400, 0, 400, 700)

        self.canvas.create_line(300, 0, 300, 700)
        
        self.canvas.create_line(200, 0, 200, 700)
        
        self.canvas.create_line(100, 0, 100, 700) 
        
        #Imagenes

        robot = self.canvas.create_image(250,250,image = self.imagen_robot)

        self.canvas.create_image(250,50,image = self.imagen_cono)

        self.canvas.pack(fill = BOTH, expand = True)

        self.canvas.create_image(150,400,image = self.imagen_arbol)


        def move_down (self):
            self.dx = 0
            self.dy = 100
            self.canvas.move(robot, self.dx, self.dy)
            print("down")

        self.master.bind("s", move_down)

        self.master.mainloop()
        
"""        
if __name__ == "__main__":
    
    master = Tk()
    geeks = escenario1(master)
 
    
    master.title("ESCENARIO 1")
 
    
    master.minsize(502,502) 
 
    
    master.mainloop()
"""
escenario2()
#escenario1()
