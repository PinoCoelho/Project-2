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
        self.imagen_arbol = PhotoImage (file = 'Images/arbol.png')
    
        self.master.title("ESCENARIO 1")
 
    
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
        #Imagenes

        self.robot = self.canvas.create_image(50,50,image = self.imagen_robot,tags ="self.robot")

        self.cono = self.canvas.create_image(250,250,image = self.imagen_cono)

        self.canvas.pack(fill = BOTH, expand = True)

        def colision_cono (self):
            pos1 = self.canvas.bbox(self.robot)
            pos2 = self.canvas.bbox(self.cono)
            if pos2[0] < pos1[2] < pos2[2] and pos2[1] < pos1[1] < pos2[3]:
                self.canvas.move(self.robot, 0, 0)
                print ("¡Colisión Cono!")

        def move_left(temp):
            x1,y1,x2,y2=self.canvas.bbox("self.robot")
            if(x1<=0):
                return
            else:
                self.canvas.move(self.robot,-5,0)
                colision_cono(self)
                #print("Left")
        def move_right(temp):
            x1,y1,x2,y2=self.canvas.bbox("self.robot")
            if(x2>=self.canvas.winfo_width()-5):
                return
            else:
                self.canvas.move(self.robot,5,0)
                colision_cono(self)
                #print("Right")  
        def move_up(temp):
            x1,y1,x2,y2=self.canvas.bbox("self.robot")
            if(y1<=0):
                return
            else:
                self.canvas.move(self.robot,0,-5) 
                colision_cono(self)
                #print("Up")  
        def move_down(temp):
            x1,y1,x2,y2=self.canvas.bbox("self.robot")
            if(y2>=self.canvas.winfo_height()-5):
                return
            else:
                self.canvas.move(self.robot,0,5)  
                colision_cono(self)
                #print("Down")  
        
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

        self.arbol = self.canvas.create_image(150,400,image = self.imagen_arbol)

        self.canvas.pack(fill = BOTH, expand = True)

        #self.menubar = Menu(self.master) #Se crea la barra del menú.
        #self.menubar.add_command(label="PRESENTACIÓN",command= print("Ola")) #Se crea el comando para que.
        #self.master.config(menu=self.menubar) #Se posiciona la barra del menú.

        def colision_cono (self):
            pos1 = self.canvas.bbox(self.robot)
            pos2 = self.canvas.bbox(self.cono)
            if pos2[0] < pos1[2] < pos2[2] and pos2[1] < pos1[1] < pos2[3]:
                self.canvas.move(self.robot, 0, 0)
                print ("¡Colisión Cono!")

        def colision_arbol (self):
            pos1 = self.canvas.bbox(self.robot)
            pos2 = self.canvas.bbox(self.arbol)
            if pos2[0] < pos1[2] < pos2[2] and pos2[1] < pos1[1] < pos2[3]:
                self.canvas.move(self.robot, 0, 0)
                print ("¡Colisión Árbol!")

        def medicion (self,temp):
            #temp = 0
            if temp == 120:
                return temp
            else: 
                #temp += 20
                return medicion(self,temp +20)

        #Movimientos del robot

        def move_left(temp):
            x1, y1, x2, y2 = self.canvas.bbox("self.robot")
            if(x1 <= 0):
                return
            else:
                self.canvas.move(self.robot, -5, 0)
                colision_cono(self)
                colision_arbol(self)
                medicion(self,0)
                #print("Left")


        def move_right(temp):
            x1, y1, x2, y2 = self.canvas.bbox("self.robot")
            if(x2 >= self.canvas.winfo_width() -5):
                return
            else:
                self.canvas.move(self.robot, 5, 0)
                colision_cono(self)
                colision_arbol(self)
                medicion(self,0)
                #print("Right")

        def move_up(temp):
            x1, y1, x2, y2 = self.canvas.bbox("self.robot")
            if(y1 <= 0):
                return
            else:
                self.canvas.move(self.robot, 0, -5)
                colision_cono(self)
                colision_arbol(self)
                medicion(self,0) 
                #print("Up") 

        def move_down(temp):
            x1, y1, x2, y2 = self.canvas.bbox("self.robot")
            if(y2 >= self.canvas.winfo_height() -5):
                return
            else:
                self.canvas.move(self.robot, 0, 5)
                colision_cono(self)
                colision_arbol(self)
                medicion(self,0)  
                #print("Down")
        
        self.master.bind('d', move_right)
        self.master.bind('a', move_left)
        self.master.bind('w', move_up)
        self.master.bind('s', move_down)

        print(self.canvas.bbox(self.cono))

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
