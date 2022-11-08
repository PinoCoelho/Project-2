from tkinter import *
import os
#import Escenarios

class iniciador:

    def __init__(self):
        """
                Instituto Tecnológico de Costa Rica
                    Ingeniería en Computadores


        Lenguaje: Python
        Versión: 10.6
        Autores: Joseph Herra y Evan Salas
        Versión del programa: Windows 11 
        Última modificación: 7/11/2022

        """

        self.inicio() #llama a la función inicio
        self.scene = iniciador.scene

    def cargarImagen(self,nombre): #Funcion para cargar la imagen. 
        """
                Instituto Tecnológico de Costa Rica
                    Ingeniería en Computadores


        Lenguaje: Python
        Versión: 10.6
        Autores: Joseph Herra y Evan Salas
        Versión del programa: Windows 11 
        Última modificación: 7/11/2022

        """

        self.ruta = os.path.join('Images',nombre) #Se define la ubicación de la imagen.
        imagen = PhotoImage(file=self.ruta)
        return imagen #Retorna la imagen

    
    def inicio (self):
        """
                Instituto Tecnológico de Costa Rica
                    Ingeniería en Computadores


        Lenguaje: Python
        Versión: 10.6
        Autores: Joseph Herra y Evan Salas
        Versión del programa: Windows 11 
        Última modificación: 7/11/2022

        """

        self.ventana = Tk() #Se crea la ventana principal.
        self.ventana.title("ROBOT") #Titulo de la pantalla principal. 
        self.ventana.minsize(600,700) #Dimensiones de la pantalla.
        self.ventana.resizable(width=NO,height=NO) #Que no se puede modificar. 
        self.fondo = iniciador.cargarImagen(self,"robot_fondo2.gif") #Pone la imagen de fondo. 
        self.canvas = Canvas(self.ventana, width=700, height=700, bg="purple")#Crea el canvas
        self.canvas.place(x=0, y=0) #Lo posiciona
        self.canvas.create_image(0, 0, image=self.fondo, anchor="nw") #Crea una imagen en el canvas
        self.Boton_iniciar = Button(self.ventana,text="INICIAR",bg="#33AA5C",fg="black",height= 2,width=7,command= self.scene) #Botón para entrar a la pantalla secundaria llamada game
        self.Boton_iniciar.place(x=308,y=450, anchor = "center")
        self.Boton_salir = Button (self.ventana,text="APAGAR", bg="#33AA5C",fg="black",height= 2,width=7,command= self.ventana.destroy) #Boton para apagar el programa
        self.Boton_salir.place (x= 510,y= 20)
        self.Boton_about = Button (self.ventana,text="ABOUT", bg="#33AA5C",fg="black",height= 2,width=7,command= self.about) #Boton pantalla about
        self.Boton_about.place (x= 50,y= 20)
        self.Boton_presentacion = Button (self.ventana,text="PRESENTACION", bg="#33AA5C",fg="black",height= 2,width=12,command = print ("Hola. Soy Pino, modelo 1.5 y trabajo para el TEC. He efectuado un total de 10 mediciones de temperatura")) #Boton de presentación
        self.Boton_presentacion.place (x= 120,y= 20)
        self.Label_text_nombre = Label (self.ventana, text="Por favor introduce un nombre al robot:", bg = "#67B59C", fg = "black") #Label con un texto
        self.Label_text_nombre.place (x= 310,y=200,anchor="center") #Se posiciona en la ventana
        self.Entry_nombre = Entry(self.ventana, width=25, bg="light green") #Caja de texto para el nombre
        self.Entry_nombre.place (x= 310,y= 230,anchor="center") #Se posiciona en la ventana
        self.Label_text_creacion = Label (self.ventana, text="Por favor introduce la fecha de creación del robot:", bg = "#67B59C", fg = "black") #Label con un texto
        self.Label_text_creacion.place (x= 310,y=260,anchor="center") #Se posiciona en la ventana
        self.Entry_creacion = Entry(self.ventana, width=25, bg="light green") #Caja de texto para la creación
        self.Entry_creacion.place (x= 310,y= 290,anchor="center") #Se posiciona en la ventana
        self.Label_text_modelo = Label (self.ventana, text="Por favor introduce un modelo al robot:", bg = "#67B59C", fg = "black") #Label con un texto
        self.Label_text_modelo.place (x= 310,y=320,anchor="center") #Se posiciona en la ventana
        self.Entry_modelo = Entry(self.ventana, width=25, bg="light green") #Caja de texto para el modelo
        self.Entry_modelo.place (x= 310,y= 350,anchor="center") #Se posiciona en la ventana
        self.Label_text_fabricante = Label (self.ventana, text="Por favor introduce el nombre del fabricante:", bg = "#67B59C", fg = "black") #Label con un texto
        self.Label_text_fabricante.place (x= 310,y=380,anchor="center") #Se posiciona en la ventana
        self.Entry_fabricante = Entry(self.ventana, width=25, bg="light green") #Caja de texto para el nombre del fabricante
        self.Entry_fabricante.place (x= 310,y= 410,anchor="center") #Se posiciona en la ventana
        self.ventana.mainloop() #El loop principal de toda la pantalla principal
    

    def scene (self):
        """
                Instituto Tecnológico de Costa Rica
                    Ingeniería en Computadores


        Lenguaje: Python
        Versión: 10.6
        Autores: Joseph Herra y Evan Salas
        Versión del programa: Windows 11 
        Última modificación: 7/11/2022

        """

        self.root = Toplevel() #Se crea la ventana secundaria
        self.root.title("ROBOT") #Titulo de la pantalla principal. 
        self.root.minsize(600,700) #Dimensiones de la pantalla.
        self.root.resizable(width=NO,height=NO) #Que no se puede modificar. 
        self.fondo = iniciador.cargarImagen(self,"robot_fondo2.gif") #Imagen de fondo
        self.canvas = Canvas(self.root, width=700, height=700, bg="purple") #Se inicia el canvas
        self.canvas.place(x=0, y=0) #Se posiciona
        self.canvas.create_image(0, 0, image=self.fondo, anchor="nw") #Se crea la imagen
        self.Boton_atras = Button(self.root,text="ATRÁS",bg="green",fg="yellow",height= 2,width=7,command= self.root.destroy) #Boton para regresarse
        self.Boton_atras.place(x=308,y=450, anchor = "center") #Se posiciona en la pantalla
        self.Boton_escenario1 = Button(self.root,text="ESCENARIO 1",bg="green",fg="yellow",height= 2,width=10) #Botón para el primer escenario
        self.Boton_escenario1.place(x=210,y=300, anchor = "center") #Se posiciona en la pantalla
        self.Boton_escenario2 = Button(self.root,text="ESCENARIO 2",bg="green",fg="yellow",height= 2,width=10) #Botón para el segundo escenario
        self.Boton_escenario2.place(x=410,y=300, anchor = "center") #Se posiciona en la pantalla
        self.root.mainloop() #Mainloop de la ventana
    
    def about(self):
        """
                Instituto Tecnológico de Costa Rica
                    Ingeniería en Computadores


        Lenguaje: Python
        Versión: 10.6
        Autores: Joseph Herra y Evan Salas
        Versión del programa: Windows 11 
        Última modificación: 7/11/2022

        """

        self.root = Toplevel() #Se crea la vetana secundaria
        self.root.title("ABOUT") #Titulo de la pantalla secundaria. 
        self.root.minsize(600,700) #Dimensiones de la pantalla.
        self.root.resizable(False,False) #Que no se puede modificar. 
        self.fondo = iniciador.cargarImagen(self,"robot_fondo2.gif") #Se pone la imagen
        self.info = iniciador.cargarImagen(self,"info.gif") #Se pone la otra imagen
        self.canvas = Canvas(self.root, width=700, height=700, bg="purple") #Se crea el canvas
        self.canvas.place(x=0, y=0) #Se posiciona el canvas
        self.canvas.create_image(0, 0, image=self.fondo, anchor="nw") #Se crea la imagen
        self.canvas.create_image(80, 180, image=self.info, anchor="nw") #Se crea la imagen
        self.Boton_return = Button(self.root,text="ATRAS",bg="red",fg="yellow",height= 2,width=7, command=self.root.destroy) #Botón para regresar
        self.Boton_return.place(x=308,y=490, anchor = "center") #Se posiciona en la pantalla
        self.root.mainloop() #Mainloop de la pantalla