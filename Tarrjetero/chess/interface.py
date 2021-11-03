from tkinter.constants import END, W
from chess.board import Board
from chess.menuRecreate import MenuRecreate
from tkinter import Entry, Label, Text, Button, PhotoImage
import pymysql

"""
La interfaz de usuario donde se mostrara todos los elementos y futuras actualizaciones
"""

class Interface():
   
    def __init__(self, canvas) -> None:

        #el canvaas de main

        self.canvas = canvas

        # le pasamos el canvas al tablero también

        self.board = Board(canvas)

        # al menu para poner y quitar fichas le pasamos el tabero y el canvas de la raíz

        self.pieces_menu = MenuRecreate(canvas, self.board)
        
        # Lista para poner las opciones del menu

        self.buttons = [] 

        # Lista paraa poner las imagenes de los botones del menu

        self.img_buttons = [] 

        # Duplas de los nombres de los botones y la función que harán al dar click
        # En un futuro se pueden agregar más nombres de funcionalidades desde aquí

        self.fun_names = [("recreatePlay", self.pieces_menu.setMenu), 
                          ("clean", self.board.setEmptyBoard), 
                          ("saveGame", self.board.save)]
                          
        # Variables para la imágenes de adorno
        
        self.logo = 0
        self.logo_img = 0
        
    
    #Funcion para construir un tablero vacio



    def setBoard(self):
        
        #Rectángulo detrás del tablero
        
        self.canvas.create_rectangle(172.13052368164062,93.01907348632812,548.7826538085938,472.9211120605469,fill="#C4C4C4",outline="")

        # Pintar los números del tablero

        self.board.setBoardNum()

        # Pintar las letras del tablero

        self.board.setBoardLetters()

        # Empezamos con un tablero vacio

        self.board.setEmptyBoard()

    def setBoard1(self, id):
        
        #Rectángulo detrás del tablero
        
        self.canvas.create_rectangle(172.13052368164062,93.01907348632812,548.7826538085938,472.9211120605469,fill="#C4C4C4",outline="")

        # Pintar los números del tablero

        self.board.setBoardNum()

        # Pintar las letras del tablero

        self.board.setBoardLetters()

        self.board.setBoardSQLid(id)
    """
    Función que nos pone los opciones de los botnoes en el tablero en fila vertical
    si se quieren agregar mas botones solo basta con aumentar el rango
    """


    def createButtons(self):
        
        for i in range(3):
            self.img_buttons.append(PhotoImage(
            file="assets/images/"+self.fun_names[i][0] + ".png"))
            
            self.buttons.append(Button(self.canvas, image=self.img_buttons[i],borderwidth=0,highlightthickness=0,command=self.fun_names[i][1], relief="flat"))
            
            if i == 3:
                self.buttons[i].place(x=598.3993530273438,y=479.40289306640625,width=124.44107818603516,height=25.540735244750977)
            else: 
                self.buttons[i].place(x=28.134521484375,y=175.0877685546875 + (55 * i),width=117.407470703125,height=29.888092041015625)


    def guardarDescripcion(self):
        return 

    """
    Función para crear los botones y las entradas para poder introducir los datos que
    se requieren para crear una nueva tarjeta
    """

    def createDescripcion(self):

        labelTema = Label(self.canvas, font=("Arial", 20), text="Tema")
        labelTema.place(x=600, y=100)

        entradaTema = Entry(self.canvas , width=50)
        entradaTema.place(x=600, y=150)

        labelCrearDescripcion = Label(self.canvas,font=("Arial", 20), text="descripcion")
        labelCrearDescripcion.place(x=600, y=200)

        entrada = Text(self.canvas , width=40, height=25)
        entrada.place(x=600, y=250)
        
        

        
        boton = Button(self.canvas,padx=6,font=("Arial", 15), pady=6, text="Guardar la tarjeta a la Base de Datos", command= lambda: self.board.save1(entrada.get("1.0",END), entradaTema.get()))
        boton.place(x=600, y=680)
        return
    
    """
    Funcionar para crear los botones necesarios para poder editar una tarjeta
    """

    def editar(self, id):

        descripcionAntigua = ''
        temaAntiguo = ''
        con = pymysql.connect(host='localhost',
        user='root',
        password='pruebatest',
        db='mydb',
        charset='utf8mb4')
        try:

            with con.cursor() as cur:

                cur.execute('SELECT descripcion,tema FROM Tarjeta where idtarjeta ='+str(id))
                rows = cur.fetchone()
                print(rows)
                descripcionAntigua = rows[0]
                temaAntiguo = rows[1]


        finally:

            con.close()

        labelTema = Label(self.canvas, font=("Arial", 20), text="Nuevo Tema")
        labelTema.place(x=600, y=100)

        entradaTema = Entry(self.canvas , width=50)
        entradaTema.place(x=600, y=150)
        entradaTema.insert(0,temaAntiguo)

        labelCrearDescripcion = Label(self.canvas,font=("Arial", 20), text="Nueva descripcion")
        labelCrearDescripcion.place(x=600, y=200)

        entrada = Text(self.canvas , width=40, height=25)
        entrada.place(x=600, y=250)
        entrada.insert('1.0',descripcionAntigua)

        boton = Button(self.canvas,padx=6,font=("Arial", 15), pady=6, text="Guardar la tarjeta a la Base de Datos",command= lambda: self.board.save2(entrada.get('1.0','end'), entradaTema.get(),id))
        boton.place(x=600, y=680)
        return

    
    """
    Función para poner el logo de la aplicación
    """   
    def setLogo(self):
        self.logo_img = PhotoImage(file="assets/images/logo.png")
        self.logo = self.canvas.create_image(91.0,99.0,image=self.logo_img)
        
        