from tkinter import *

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

        #self.menubar = Menu(self.master) #Se crea la barra del menú.
        #self.menubar.add_command(label="PRESENTACIÓN",command= print("Ola")) #Se crea el comando para que.
        #self.master.config(menu=self.menubar) #Se posiciona la barra del menú.

        def colision (self):
            pos1 = self.canvas.bbox(self.robot)
            pos2 = self.canvas.bbox(self.cono)
            if pos2[0] < pos1[2] < pos2[2] and pos2[1] < pos1[1] < pos2[3]:
                print ("¡Colisión!")

        #Movimientos del robot

        def move_left(temp):
            x1, y1, x2, y2 = self.canvas.bbox("self.robot")
            if(x1 <= 0):
                return
            else:
                self.canvas.move(self.robot, -5, 0)
                colision(self)
                #print("Left")


        def move_right(temp):
            x1, y1, x2, y2 = self.canvas.bbox("self.robot")
            if(x2 >= self.canvas.winfo_width() -5):
                return
            else:
                self.canvas.move(self.robot, 5, 0)
                colision(self)
                #print("Right")

        def move_up(temp):
            b_move_down = True
            b_speed = 5
            x1, y1, x2, y2 = self.canvas.bbox("self.robot")
            if(y1 <= 0):
                return
            else:
                b_move_down = not b_move_down
                b_speed = -b_speed
                self.canvas.move(self.robot, 0, -5)
                colision(self) 
                #print("Up") 

        def move_down(temp):
            b_move_down = True
            b_speed = 5
            self.canvas.move(self.robot, 0, b_speed)
            x1, y1, x2, y2 = self.canvas.bbox("self.robot")
            if b_move_down:
                if(y2 >= self.canvas.winfo_height() -5):
                    b_move_down = not b_move_down
                    b_speed = -b_speed
            else:
                return
                #else:
                    #b_move_down = not b_move_down
                    #b_speed = -b_speed
                    #self.canvas.move(self.robot, 0, b_speed)
                    #colision(self)  
                    #print("Down")
        
        self.master.bind('d', move_right)
        self.master.bind('a', move_left)
        self.master.bind('w', move_up)
        self.master.bind('s', move_down)
        self.master.after(25,move_down)
        #print(self.canvas.bbox(self.cono))

        self.master.mainloop()

escenario2()