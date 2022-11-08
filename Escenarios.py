from tkinter import *
from tkinter.ttk import *
 
class escenario1:

    def __init__(self): #El constructor de la clase
        """
                Instituto Tecnológico de Costa Rica
                    Ingeniería en Computadores


        Lenguaje: Python
        Versión: 10.6
        Autores: Joseph Herra y Evan Salas
        Versión del programa: Windows 11 
        Última modificación: 7/11/2022

        """

        self.create () #Se llama a la función
 
    def create(self):
        """
                Instituto Tecnológico de Costa Rica
                    Ingeniería en Computadores


        Lenguaje: Python
        Versión: 10.6
        Autores: Joseph Herra y Evan Salas
        Versión del programa: Windows 11 
        Última modificación: 7/11/2022

        """
 
        self.master = Tk() #Se inicia Tkinter

        #Imágenes

        self.imagen_robot = PhotoImage (file = 'Images/robot.png')
        self.imagen_cono = PhotoImage (file = 'Images/cono.png')
        self.imagen_arbol = PhotoImage (file = 'Images/arbol.png')
    
        self.master.title("ESCENARIO 1") #Título de la pantalla
 
    
        self.master.minsize(502,502) #Dimensiones de la pantalla
        self.master.resizable(False,False) #Que no se puedan modificar
    
    
        self.canvas = Canvas(self.master) #Se crea el canvas

        #Líneas Horizontales
        
        self.canvas.create_line(700, 100, 0, 100)

        self.canvas.create_line(700, 200, 0, 200)

        self.canvas.create_line(700, 300, 0, 300)

        self.canvas.create_line(700, 400, 0, 400)

        self.canvas.create_line(700, 500, 0, 500)

        self.canvas.create_line(700, 600, 0, 600)
 
        #Líneas Verticales

        self.canvas.create_line(500, 0, 500, 700)
         
        self.canvas.create_line(400, 0, 400, 700)

        self.canvas.create_line(300, 0, 300, 700)
        
        self.canvas.create_line(200, 0, 200, 700)
        
        self.canvas.create_line(100, 0, 100, 700)

        #Poner las imágenes

        self.robot = self.canvas.create_image(50,50,image = self.imagen_robot,tags ="self.robot")

        self.cono = self.canvas.create_image(250,250,image = self.imagen_cono)

        self.canvas.pack(fill = BOTH, expand = True)

        #Variables globales

        global temperatura1
        global temperatura2
        temperatura1 = 20
        temperatura2 = 10

        def medidor_cono (self): #Función que mide la temperatura en el sitio del cono
            file = open(r"mediciones.txt", 'a') #Abre el archivo
            file.write(str(temperatura1)+"\n") #Escribe en el archivo
            file.close #Cierra el archivo
            promedio(self) #Llama a la función promedio

        def medidor_abajo (self): #Función que mide la temperatura en el sitio de abajo
            file = open(r"mediciones.txt", 'a') #Abre el archivo
            file.write(str(temperatura2)+"\n") #Escribe en el archivo
            file.close #Cierra el archivo
            promedio(self) #Llama a la función promedio

        def promedio (self): #Función que saca el promedio
           promedio = (temperatura1 + temperatura2) // 10
           print(promedio)

        def colision_cono (self): #Función que crea la colisión entre el robot y el cono
            pos1 = self.canvas.bbox(self.robot) #Posición del robot
            pos2 = self.canvas.bbox(self.cono) #Posición del cono
            if pos2[0] < pos1[2] < pos2[2] and pos2[1] < pos1[1] < pos2[3]: #Para ver las posiciones y ver si chocan
                medidor_cono(self) #Llama a la función medidor_cono
                print ("¡Colisión Cono!") #Manda un print de que hubo una colisión

        def move_left(temp): #Función que hace que el robot se mueva hacia la izquierda
            x1,y1,x2,y2=self.canvas.bbox("self.robot") #Posiciones del robot
            if(x1<=0): #Si x1 es igual o menor a 0 entonces llegó al límite de la pantalla
                print("Chocó a la izquierda") #Pone uun print de que chocó abajo
            else:
                self.canvas.move(self.robot,-5,0) #Hace que el robot se mueva hacia la izquierda
                colision_cono(self) #Llama a colisión cono
                #print("Left")

        def move_right(temp): #Función que hace que el robot se mueva hacia la derecha
            x1,y1,x2,y2=self.canvas.bbox("self.robot") #Posiciones del robot
            if(x2>=self.canvas.winfo_width()-5):#Si x2 es igual o mayor al largo de la ventana entonces llegó al límite de la pantalla
                print("Chocó a la derecha") #Pone uun print de que chocó abajo
            else:
                self.canvas.move(self.robot,5,0) #Hace que el robot se mueva hacia la derecha
                colision_cono(self) #Llama a colisión cono
                #print("Right")  

        def move_up(temp): #Función que hace que el robot se mueva hacia arriba
            x1,y1,x2,y2=self.canvas.bbox("self.robot") #Posiciones del robot
            if(y1<=0): #Si y1 es igual o menor a 0 entonces llegó al límite de la pantalla
                print("Chocó arriba") #Pone uun print de que chocó abajo
            else:
                self.canvas.move(self.robot,0,-5) #Hace que el robot se mueva hacia arriba
                colision_cono(self) #Llama a colisión cono
                #print("Up")  

        def move_down(temp): #Función que hace que el robot se mueva hacia arriba
            x1,y1,x2,y2=self.canvas.bbox("self.robot") #Posiciones del robot
            if(y2>=self.canvas.winfo_height()-5): #Si y2 es igual o mayor al largo de la ventana entonces llegó al límite de la pantalla
                medidor_abajo(self) #Llama a medidor abajo
                print("Chocó abajo") #Pone uun print de que chocó abajo
            else:
                self.canvas.move(self.robot,0,5)   #Hace que el robot se mueva hacia abajo
                colision_cono(self) #Llama a colision cono
                #print("Down")  
        
        self.master.bind('d', move_right) #Para que se mueva hacia la derecha con la letra d
        self.master.bind('a', move_left) #Para que se mueva hacia la izquierda con la letra a
        self.master.bind('w', move_up) #Para que se mueva hacia arriba con la letra w
        self.master.bind('s', move_down) #Para que se mueva hacia abajo con la letra s

        self.master.mainloop() #Mainloop de la pantalla

class escenario2:
    """
                Instituto Tecnológico de Costa Rica
                    Ingeniería en Computadores


        Lenguaje: Python
        Versión: 10.6
        Autores: Joseph Herra y Evan Salas
        Versión del programa: Windows 11 
        Última modificación: 7/11/2022

    """

    def __init__(self, master = None): #Constructor de la clase
        """
                Instituto Tecnológico de Costa Rica
                    Ingeniería en Computadores


        Lenguaje: Python
        Versión: 10.6
        Autores: Joseph Herra y Evan Salas
        Versión del programa: Windows 11 
        Última modificación: 7/11/2022

        """

        self.master = master #Se establece el self.master
        self.create() #Se manda a crear la función create
        self.imprimir()


    def create(self):
        """
                Instituto Tecnológico de Costa Rica
                    Ingeniería en Computadores


        Lenguaje: Python
        Versión: 10.6
        Autores: Joseph Herra y Evan Salas
        Versión del programa: Windows 11 
        Última modificación: 7/11/2022

        """
 
        self.master = Tk() #Se inicializa Tkinter

        #Imágenes

        self.imagen_robot = PhotoImage (file = 'Images/robot.png')
        self.imagen_cono = PhotoImage (file = 'Images/cono.png')
        self.imagen_arbol = PhotoImage (file = 'Images/arbol.png')
    
        self.master.title("ESCENARIO 2") #Título de la pantalla
 
    
        self.master.minsize(502,502) #Dimensiones de la pantalla
        self.master.resizable(False,False) #No se puede modificar
    
    
        self.canvas = Canvas(self.master) #Se crea el canvas

        #Líneas Horizontales
        
        self.canvas.create_line(700, 100, 0, 100)

        self.canvas.create_line(700, 200, 0, 200)

        self.canvas.create_line(700, 300, 0, 300)

        self.canvas.create_line(700, 400, 0, 400)

        self.canvas.create_line(700, 500, 0, 500)

        self.canvas.create_line(700, 600, 0, 600)
 
        #Líneas Verticales

        self.canvas.create_line(500, 0, 500, 700)
         
        self.canvas.create_line(400, 0, 400, 700)

        self.canvas.create_line(300, 0, 300, 700)
        
        self.canvas.create_line(200, 0, 200, 700)
        
        self.canvas.create_line(100, 0, 100, 700) 
        
        #Se ponen las imágenes

        self.robot = self.canvas.create_image(250,250,image = self.imagen_robot, tags=("self.robot"))

        self.cono = self.canvas.create_image(250,50,image = self.imagen_cono)

        self.arbol = self.canvas.create_image(150,400,image = self.imagen_arbol)

        self.canvas.pack(fill = BOTH, expand = True) #Se crea el canvas

        #Variables globales

        global temperatura1
        global temperatura2
        temperatura1 = 20
        temperatura2 = 10

        def medidor_cono (self): #Medidor de la temperatura
            file = open(r"mediciones.txt", 'a') #Se abre el archivo
            file.write(str(temperatura1)+"\n") #Se escribe en el archivo
            file.close #Se cierra el archivo
            promedio(self) #LLama a la función promedio

        def medidor_borde_derecho (self): #Medidor de la temperatura
            file = open(r"mediciones.txt", 'a') #Se abre el archivo
            file.write(str(temperatura2)+"\n") #Se escribe en el archivo
            file.close #Se cierra el archivo
            promedio(self) #LLama a la función promedio

        def promedio (self): #Función que saca el promedio
           promedio = (temperatura1 + temperatura2) // 5
           print(promedio)

        #self.menubar = Menu(self.master) #Se crea la barra del menú.
        #self.menubar.add_command(label="PRESENTACIÓN",command= print("Ola")) #Se crea el comando para que.
        #self.master.config(menu=self.menubar) #Se posiciona la barra del menú.

        def colision_cono (self): #Función que saca la colisión con el cono
            pos1 = self.canvas.bbox(self.robot) #Posición del robot
            pos2 = self.canvas.bbox(self.cono) #Posici+on del cono
            if pos2[0] < pos1[2] < pos2[2] and pos2[1] < pos1[1] < pos2[3]: #Se ve si pegan
                medidor_cono(self) #Llama medidor cono
                print ("¡Colisión Cono!") #Pone un print de que colisionó

        def colision_arbol (self): #Función que saca la colisión con el árbol
            pos1 = self.canvas.bbox(self.robot) #Posición del robot
            pos2 = self.canvas.bbox(self.arbol) #Posici+on del árbol
            if pos2[0] < pos1[2] < pos2[2] and pos2[1] < pos1[1] < pos2[3]: #Se ve si pegan
                print ("¡Colisión Árbol!") #Pone un print de que colisionó

        #Movimientos del robot

        def move_left(temp): #Función para que se mueva hacia la izquierda
            x1, y1, x2, y2 = self.canvas.bbox("self.robot") #Posiciones del canvas
            if(x1 <= 0): #Si x1 es menor o igual a 0 entonces llegó al límite de la pantalla
                print("Chocó a la izquierda") #Pone un print de que chocó a la izquierda
            else:
                self.canvas.move(self.robot, -5, 0) #El robot se mueve
                colision_cono(self) #Llama a colisión cono
                colision_arbol(self) #LLama a colisión árbol
                #print("Left")

        def move_right(temp): #Función para que se mueva hacia la derecha
            x1, y1, x2, y2 = self.canvas.bbox("self.robot") #Posiciones del canvas
            if(x2 >= self.canvas.winfo_width() -5): #Si x2 es mayor o igual al largo de la pantalla entonces llegó al límite de la pantalla
                medidor_borde_derecho(self) #Llama al medidor
                print("Chocó a la derecha") #Print de que chocó
            else:
                self.canvas.move(self.robot, 5, 0) #El robot se mueve
                colision_cono(self) #Llama a colisión cono
                colision_arbol(self) #LLama a colisión árbol
                #print("Right")

        def move_up(temp): #Función para que se mueva hacia arriba
            x1, y1, x2, y2 = self.canvas.bbox("self.robot") #Posiciones del canvas
            if(y1 <= 0): #Si y1 es menor o igual a 0 entonces llegó al límite de la pantalla
                print("Chocó arriba") #Pone uun print de que chocó arriba
            else:
                self.canvas.move(self.robot, 0, -5) #El robot se mueve
                colision_cono(self) #Llama a colisión cono
                colision_arbol(self) #LLama a colisión árbol
                #print("Up") 

        def move_down(temp): #Función para que se mueva hacia arriba
            x1, y1, x2, y2 = self.canvas.bbox("self.robot") #Posiciones del canvas
            if(y2 >= self.canvas.winfo_height() -5): #Si y2 es mayor o igual al largo de la pantalla entonces llegó al límite de la pantalla
                print("Chocó abajo") #Pone uun print de que chocó abajo
            else:
                self.canvas.move(self.robot, 0, 5) #El robot se mueve
                colision_cono(self) #Llama a colisión cono
                colision_arbol(self) #LLama a colisión árbol
                #print("Down")
        
        self.master.bind('d', move_right) #Hace que se mueva hacia la derecha con la letra d
        self.master.bind('a', move_left) #Hace que se mueva hacia la izquierda con la letra a
        self.master.bind('w', move_up) #Hace que se mueva hacia arriba con la letra w
        self.master.bind('s', move_down) #Hace que se mueva hacia abajo con la letra s
        self.master.mainloop() #El mainloop de la pantalla
    
    def imprimir (self):
        print (escenario2.__doc__())
        
        
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
