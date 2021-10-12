from config import relativeToAssets
from tkinter import Button, PhotoImage

"""
Clase menu para mostrar un menu aparte cuando se decida recrear una jugada, se puede borrar, seleccionar,
cerrar el modo de recrear jugada 
"""

class MenuRecreate:

    """
    Constructor de la clse menu
    """    
    def __init__(self, canvas, board) -> None:
        self.canvas = canvas
        self.board = board
        self.pieces = ["R","D","T","A","C","p"]
        self.isSelect = True

        #Primeros 0-5 negras, 6 - 11 blancas
        # Botones para la fichas

        self.buttons= [] 

        #Imágenes de los botones

        self.imgButtons= [] 

        #Img para seleccionar una pieza

        self.selectPiece =PhotoImage(file=relativeToAssets("images/selection.png"))

        #Img para borrar una pieza

        self.deletePiece  =PhotoImage(file=relativeToAssets("images/eraser.png"))

        #Img para cerrar el menú

        self.close  =PhotoImage(file=relativeToAssets("images/close.png"))
        
    """
    Función para saber si se hizo click 
    """
    def doClick(self, id):
        if self.isSelect:
            self.board.setPiece(id)
        else:
            self.board.setPiece("")

    """
    Configurar las piezas del talbero
    """
    def setPieces(self, y, color):
        p = 0 if color == "N" else 6
        for i in range(6):
            name = self.pieces[i] + color
            self.imgButtons.append(PhotoImage(file=relativeToAssets("images/" + name + "0.png")))
            self.buttons.append(Button(image=self.imgButtons[p+i],borderwidth=0,highlightthickness=0,command= lambda x = name: self.doClick(x),
                relief="flat"
            ))
            self.buttons[p+i].place(x=234.0 + (43 * i), y= y, width=43.0,height=43.0)

    """
    Quita el menu
    """
    def deleteMenu(self):
        for i in self.buttons:
            i.destroy()
        self.buttons= [] 
        self.imgButtons= []


    """
    Nos dice si se va a poner una pieza o quitar
    """
    def switchVar(self, val):
        self.isSelect = val
        if not self.isSelect:
            self.doClick(0)
    
    """
    Muestra las piezas para poder seleccionarlas
    """
    def setMenu(self):
        self.setPieces(43.0, "N") 
        self.setPieces(479.0, "B")
        aux = False
        for i in range(2):
            aux = not aux
            self.buttons.append(Button(image=self.selectPiece if i == 0 else self.deletePiece,
                borderwidth=0,
                highlightthickness=0,
                command=lambda x = aux: self.switchVar(x),
                relief="flat"
            ))
            self.buttons[12 + i].place(x=580.0 + (i * 55),y=43.0 + (i*2),width=50.0 - (i*10),height=50.0 - (i*10))
        self.buttons.append(Button(image=self.close,borderwidth=0,highlightthickness=0,command= self.deleteMenu,relief="flat"))

        self.buttons[14].place(x=685.0, y=45,width=40.0,height=40.0)