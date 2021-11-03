from .box import Box
from tkinter import Label, Place, Toplevel, messagebox
import pymysql

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

    def set_piece(self, piece):
        """
            Guarda una pieza seleccionada para ser puesta/movida
            en el tablero
            piece - nombre y pieza
        """
        self.piece = piece
    """
    Cambia la casilla por otro imagen ya sea con pieza o con casilla vacía
    """
    def putPiece(self, id):
        if self.piece != "":
            self.board[id].setPiece(self.piece[0], self.piece[1])
        else:   
            self.board[id].setPiece("", "")
    def put_piece(self, id):
        """
            Modifica una casilla para poner o quitar una pieza
            id - número de la pieza
        """
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

    def doListFichasConString(self,cadena):
        listaPieces = []
        pieces_font = {      " ":"0" ,
                             "+":"1" ,
                            "k":"RB0",
                            "K":"RB1",
                            "l":"RN0",
                            "L":"RN1",
                            "p":"pB0",
                            "P":"pB1",
                            "o":"pN0",
                            "O":"pN1",
                            "n":"CB0",
                            "N":"CB1",
                            "m":"CN0",
                            "M":"CN1",
                            "b":"AB0",
                            "B":"AB1",
                            "v":"AN0",
                            "V":"AN1",
                            "r":"TB0",
                            "R":"TB1",
                            "t":"TN0",
                            "T":"TN1",
                            "q":"DB0",
                            "Q":"DB1",
                            "w":"DN0",
                            "W":"DN1"          
        }
        for i in cadena:
            if i in pieces_font:
                listaPieces.append(pieces_font[i])

        return listaPieces


    def setBoardSQLid(self,id):
        con = pymysql.connect(host='localhost',
        user='root',
        password='pruebatest',
        db='mydb',
        charset='utf8mb4')
        tableroVirgen = ""
        try:

            with con.cursor() as cur:
                consulta = 'select diagrama from tarjeta where idTarjeta ='+str(id)
                cur.execute(consulta)

            row = cur.fetchone()
            for i in row:
                tableroVirgen = i

            

        finally:

            con.close()

        listaFichas = self.doListFichasConString(tableroVirgen)
        self.set_board(listaFichas)    

    def set_board(self, pieces):
        """Muestra un tablero con ciertas piezas
        pieces - arreglo que contiene el nombre de las img 
            para mostrar el tablero con las piezas"""
        for x in range(8):
            for y in range(8):
                piece = pieces[(8*x)+y]
                color = piece[-1]
                if len(self.board) < 64:
                    #Si el tablero no contiene todas las casillas
                    box = Box(self.canvas, x, y, color, self.put_piece)
                    box.setImage()
                    box.showOnScreen()
                    self.board.append(box)
                #Modificamos su imagen
                if len(piece) == 1:
                    self.board[(8*x)+y].setPiece("","")
                else:
                    name = piece[:-1]
                    self.board[(8*x)+y].setPiece(name[0],name[1])

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

    def save1(self, descripcion, tema):
         
          
        con = pymysql.connect(host='localhost',
        user='root',
        password='pruebatest',
        db='mydb',
        charset='utf8mb4')
        tablero = self.to_string()

        try:

            with con.cursor() as cur:
                cadenaComilla = "'"
                consulta = 'INSERT INTO tarjeta (descripcion, diagrama, tema) values('+cadenaComilla+descripcion+cadenaComilla+','+cadenaComilla+tablero+cadenaComilla +',' +cadenaComilla+tema+cadenaComilla+ ')'
                cur.execute(consulta)

                
            con.commit()
            
            ventanaExito = Toplevel()
            exitol = Label(ventanaExito, text="La tarjeta se creo con exito")
            exitol.place(x=10, y=10)

        finally:

            con.close()

        

        
        return

    
    """Funcion para guardar la jugada en formato txt"""

    def save(self):
        tablero = self.to_string()
        archivo = open("chess.txt", "w+")
        for i in tablero:
            archivo.write(i)
        messagebox.showinfo("Information","Tablero guardado en chess.txt")

    """
    Función para guardar los nuevos datos en editar
    """
    
    def save2(self, descripcion, tema, id):
        con = pymysql.connect(host='localhost',
        user='root',
        password='pruebatest',
        db='mydb',
        charset='utf8mb4')

        tablero = self.to_string()
       
        try:

            with con.cursor() as cur:
                cadenaComilla = "'"
                consulta = 'UPDATE tarjeta SET descripcion =' + cadenaComilla+  descripcion + cadenaComilla + ', diagrama = ' + cadenaComilla + tablero+ cadenaComilla+  ', tema = '+cadenaComilla+ tema+cadenaComilla+ ' WHERE idTarjeta = '+ str(id)+';'
                cur.execute(consulta)

                
            con.commit()
            
            ventanaExito = Toplevel()
            exitol = Label(ventanaExito, text="La tarjeta se editó con exito")
            exitol.place(x=10, y=10)

        finally:

            con.close()

        
        return
    