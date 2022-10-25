from tkinter import *
import os

class iniciador():

    def __init__(self) -> None:
        self.inicio()

    def cargarImagen(self,nombre): #Funcion para cargar la imagen. 
        """
        Funcion simple que permite cargar las imagenes para poder usarse.

        """
        self.ruta = os.path.join('Images',nombre) #Se define la ubicación de la imagen.
        imagen = PhotoImage(file=self.ruta)
        return imagen

    def inicio (self):
        self.ventana = Tk() #Se crea la ventana principal.
        self.ventana.title("VENDING MACHINE") #Titulo de la pantalla principal. 
        self.ventana.minsize(600,700) #Dimensiones de la pantalla.
        self.ventana.resizable(width=NO,height=NO) #Que no se puede modificar. 
        self.fondo = iniciador.cargarImagen(self,"fondo.gif") #Pone la imagen de fondo. 
        self.LabelFondo=Label(self.ventana, image=self.fondo) #Etiqueta que va a contener la imagen.
        self.LabelFondo.place (x=0, y=0) #Posición de la imagen.
        self.Boton_iniciar = Button(self.ventana,text="INICIAR",bg="red",fg="yellow",height= 2,width=7) #Botón para entrar a la pantalla secundaria llamada game.
        self.Boton_iniciar.place(x=308,y=450, anchor = "center")
        self.Boton_salir = Button (self.ventana,text="APAGAR", bg="red",fg="yellow",height= 2,width=7,command= self.ventana.destroy)
        self.Boton_salir.place (x= 510,y= 20)
        self.Label_text_nombre = Label (self.ventana, text="Por favor introduce un nombre al robot:", bg = "yellow", fg = "black")
        self.Label_text_nombre.place (x= 310,y=200,anchor="center")
        self.Entry_nombre = Entry(self.ventana, width=25, bg="light green")
        self.Entry_nombre.place (x= 310,y= 230,anchor="center")
        self.Label_text_creacion = Label (self.ventana, text="Por favor introduce la fecha de creación del robot:", bg = "yellow", fg = "black")
        self.Label_text_creacion.place (x= 310,y=260,anchor="center")
        self.Entry_creacion = Entry(self.ventana, width=25, bg="light green")
        self.Entry_creacion.place (x= 310,y= 290,anchor="center")
        self.Label_text_modelo = Label (self.ventana, text="Por favor introduce un modelo al robot:", bg = "yellow", fg = "black")
        self.Label_text_modelo.place (x= 310,y=320,anchor="center")
        self.Entry_modelo = Entry(self.ventana, width=25, bg="light green")
        self.Entry_modelo.place (x= 310,y= 350,anchor="center")
        self.Label_text_fabricante = Label (self.ventana, text="Por favor introduce el nombre del fabricante:", bg = "yellow", fg = "black")
        self.Label_text_fabricante.place (x= 310,y=380,anchor="center")
        self.Entry_fabricante = Entry(self.ventana, width=25, bg="light green")
        self.Entry_fabricante.place (x= 310,y= 410,anchor="center")

        self.ventana.mainloop() #El loop principal de toda la pantalla principa





iniciador()