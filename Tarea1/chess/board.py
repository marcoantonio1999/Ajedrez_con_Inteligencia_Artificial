from .box import Box
from tkinter import messagebox


"""
Clase tablero donde vamos a agregar las piezas al tablero, quitarlas, ademas de guardar
el tablero como archivo de texto txt

En esta clase en el futuro se pueden agregar más funcionalidades como inicializar jugadas guardadas
rotar el tablero, etc...
"""
class Board():
    
    """
    Contructor de la clase
    """
    def __init__(self, canvas) -> None:
        self.canvas = canvas

        # Tablero compuesto de casillas

        self.board = [] 

        #Pieza que será puesta en el tablero

        self.piece = "" 

    """
    Configura la pieza que vamos a mover
    """
    def setPiece(self, piece):
        self.piece = piece

    """
    Cambia la casilla por otro imagen ya sea con pieza o con casilla vacía
    """
    def putPiece(self, id):
        if self.piece != "":
            self.board[id].setPiece(self.piece[0], self.piece[1])
        else:   
            self.board[id].setPiece("", "")

    """
    Agrega los números de las coordenadas del tablero
    """
    def setBoardNum(self):
        for i in range(8):
            self.canvas.create_text(177.0, 421.0 - (43 * i),anchor="nw",text=str(i + 1),fill="#000000",font=("PTSans Bold", 14 * -1))
    
    """
    Agrega las letras de las coordenadas del tablero
    """
    def setBoardLetters(self):
        letters  = list(map(chr, range(97, 105)))
        for i in range(8):
            self.canvas.create_text(205.0 + (43 * i),453.0, anchor="nw",text= letters[i],fill="#000000",font=("PTSans Bold", 14 * -1))
    
    """
    Muestra en pantalla un tablero de ajedrez vacío
    """
    def setEmptyBoard(self):
        num = 0
        for x in range(8):
            for y in range(8):
                if len(self.board) < 64:
                    box = Box(self.canvas, x, y, num * 1, self.putPiece)
                    box.setImage()
                    box.showOnScreen()
                    self.board.append(box)
                else:
                    #Si existen las casillas modificamos su imagen
                    self.board[(8*x)+y].setPiece("","")
                num = not num
            num = not num

    """
    Funcion para rotar el tablero
    """
    def rotate(self):
        print("Por implementar en un futuro")

    """
    Función para darle formato al tablero en forma de chess merida
    """
    def to_string(self) -> str:
        
        # Diccionario poara mapear todas lso nombres de las piezas a la fuente correspondiente

        pieces_font = {"0" : " ", "1" : "+", "RB0":"k","RB1":"K", "RN0":"l","RN1":"L","pB0":"p","pB1":"P",
         "pN0":"o", "pN1":"O", "CB0":"n", "CB1":"N","CN0":"m", "CN1":"M","AB0":"b","AB1":"B","AN0":"v",
            "AN1":"V","TB0":"r", "TB1":"R", "TN0":"t", "TN1":"T","DB0":"q", "DB1":"Q", "DN0":"w","DN1":"W"          
        }

        # Lista para gardar todas las piezas del tablero el la fuente deseada

        listPiece = []

        for i in self.board:
            listPiece.append(pieces_font[i.getName()])    

        # Parte superior del tablero

        superior = "1222222223\n"
        
        # Parte inferior del tablero

        inferior = "7888888889\n"

        # Cada una se las 9 filas del tablero en el formado merida

        medio1 = "4"
        medio2 = "4"
        medio3 = "4"
        medio4 = "4"
        medio5 = "4"
        medio6 = "4"
        medio7 = "4"
        medio8 = "4"
        
        for i in range(8):
            medio1 = medio1 + str(listPiece[i])
        medio1 = medio1+"5"+"\n"

        for i in range(8,16):
            medio2 = medio2 + str(listPiece[i])
        medio2 = medio2+"5"+"\n"

        for i in range(16,24):
            medio3 = medio3 + str(listPiece[i])
        medio3 = medio3+"5"+"\n"
        
        for i in range(24,32):
            medio4 = medio4 + str(listPiece[i])
        medio4 = medio4+"5"+"\n"

        for i in range(32,40):
            medio5 = medio5 + str(listPiece[i])
        medio5 = medio5+"5"+"\n"

        for i in range(40,48):
            medio6 = medio6 + str(listPiece[i])
        medio6 = medio6+"5"+"\n"

        for i in range(48,56):
            medio7 = medio7 + str(listPiece[i])
        medio7 = medio7+"5"+"\n"

        for i in range(56,64):
            medio8 = medio8 + str(listPiece[i])
        medio8 = medio8+"5"+"\n"

        string = superior + medio1 + medio2 + medio3 + medio4 + medio5 + medio6 + medio7 + medio8 + inferior
        
        return string

    """ 
    Funcion para guardar la gugada en un archivo txt con la jugada
    """
    def save(self):
        tablero = self.to_string()
        archivo = open("chess.txt", "w+")
        for i in tablero:
            archivo.write(i)
        messagebox.showinfo("Information","Tablero guardado en chess.txt")