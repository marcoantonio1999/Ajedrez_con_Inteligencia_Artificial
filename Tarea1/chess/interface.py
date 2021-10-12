from config import relativeToAssets
from chess.board import Board
from chess.menuRecreate import MenuRecreate
from tkinter import Text, Button, PhotoImage


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
        self.canvas.place(x = 0, y = 0)
        self.canvas.create_rectangle(172.13052368164062,93.01907348632812,548.7826538085938,472.9211120605469,fill="#C4C4C4",outline="")

        
        # Pintar los números del tablero

        self.board.setBoardNum()

        # Pintar las letras del tablero

        self.board.setBoardLetters()

        # Empezamos con un tablero vacio

        self.board.setEmptyBoard()

    """
    Función que nos pone los opciones de los botnoes en el tablero en fila vertical
    si se quieren agregar mas botones solo basta con aumentar el rango
    
    """


    def createButtons(self):
        
        for i in range(3):
            self.img_buttons.append(PhotoImage(
            file=relativeToAssets("images/"+self.fun_names[i][0] + ".png")))
            self.buttons.append(Button(image=self.img_buttons[i],borderwidth=0,highlightthickness=0,command=self.fun_names[i][1], relief="flat"))
            if i == 3:
                self.buttons[i].place(x=598.3993530273438,y=479.40289306640625,width=124.44107818603516,height=25.540735244750977)
            else: 
                self.buttons[i].place(x=28.134521484375,y=175.0877685546875 + (55 * i),width=117.407470703125,height=29.888092041015625)


    """
    Función para poner el logo de la aplicación
    """   
    def setLogo(self):
        self.logo_img = PhotoImage(file=relativeToAssets("images/logo.png"))
        self.logo = self.canvas.create_image(91.0,99.0,image=self.logo_img)
        
        