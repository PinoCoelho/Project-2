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
        self.canvas.resizable(False,False)
    

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

        self.robot = self.canvas.create_image(50,50,image = self.imagen_robot,tags ="self.robot")

        self.canvas.create_image(250,250,image = self.imagen_cono)

        self.canvas.pack(fill = BOTH, expand = True)

        def move_left(temp):
            x1,y1,x2,y2=self.canvas.bbox("self.robot")
            if(x1<=0):
                return
            else:
                self.canvas.move(self.robot,-5,0)
                print("Left") #Only for test purpose.Remove if not needed.
        def move_right(temp):
            x1,y1,x2,y2=self.canvas.bbox("self.robot")
            if(x2>=self.canvas.winfo_width()-5):
                return
            else:
                self.canvas.move(self.robot,5,0)
                print("Right")  #Only for test purpose.Remove if not needed.
        def move_up(temp):
            x1,y1,x2,y2=self.canvas.bbox("self.robot")
            if(y1<=0):
                return
            else:
                self.canvas.move(self.robot,0,-5) 
                print("Up")    #Only for test purpose.Remove if not needed. 
        def move_down(temp):
            x1,y1,x2,y2=self.canvas.bbox("self.robot")
            if(y2>=self.canvas.winfo_height()-5):
                return
            else:
                self.canvas.move(self.robot,0,5)  
                print("Down")  #Only for test purpose.Remove if not needed.
        
        self.master.bind('d', move_right)
        self.master.bind('a', move_left)
        self.master.bind('w', move_up)
        self.master.bind('s', move_down)

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
        self.master.resizable(False,False)
    
    
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
        
        #Imágenes

        self.robot = self.canvas.create_image(250,250,image = self.imagen_robot, tags=("self.robot"))

        self.cono = self.canvas.create_image(250,50,image = self.imagen_cono)

        self.canvas.pack(fill = BOTH, expand = True)

        self.canvas.create_image(150,400,image = self.imagen_arbol)

        self.menubar = Menu(self.master) #Se crea la barra del menú.
        self.menubar.add_command(label="PRESENTACIÓN",command= print("Ola")) #Se crea el comando para que.
        self.master.config(menu=self.menubar) #Se posiciona la barra del menú.


        #Movimientos del robot

        def move_left(temp):
            x1, y1, x2, y2 = self.canvas.bbox("self.robot")
            p = self.master.coords.self.robot
            c = self.cono
            if(x1 <= 0):
                return
            else:
                self.canvas.move(self.robot, -5, 0)
                print("Left")


        def move_right(temp):
            x1, y1, x2, y2 = self.canvas.bbox("self.robot")
            if(x2 >= self.canvas.winfo_width() -5):
                return
            else:
                self.canvas.move(self.robot, 5, 0)
                print("Right")

        def move_up(temp):
            x1, y1, x2, y2 = self.canvas.bbox("self.robot")
            if(y1 <= 0):
                return
            else:
                self.canvas.move(self.robot, 0, -5) 
                print("Up") 

        def move_down(temp):
            x1, y1, x2, y2 = self.canvas.bbox("self.robot")
            if(y2 >= self.canvas.winfo_height() -5):
                return
            else:
                self.canvas.move(self.robot, 0, 5)  
                print("Down")
        
        self.master.bind('d', move_right)
        self.master.bind('a', move_left)
        self.master.bind('w', move_up)
        self.master.bind('s', move_down)

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
