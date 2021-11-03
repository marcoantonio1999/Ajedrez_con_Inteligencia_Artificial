from tkinter import PhotoImage, Button

"""
Clase box para simular cada una de las casillas del tablero
"""
class Box():
    
    """
    Contructor de la clase box
    """
    def __init__(self, canvas, x, y, back, on_clik) -> None:
        self.canvas = canvas
        self.canvas_box = 0

        #imagen de la casilla que esta es asseets

        self.img_box = 0 

        #Coordenadas
        
        self.x = x 
        self.y = y 

        #nombre de la casilla
        
        self.name = "" 

        # color de la pieza

        self.color = "" 
        
        # color de la casilla

        self.back = back
        
        #función a realizar al dar click en la casilla

        self.onClick = on_clik 
        
    """ 
    Asigna la imagen correspondiente de la casilla que esta en assets
    """
    def setImage(self):
        piece = self.name+self.color+str(self.back)
        self.img_box = PhotoImage(file="assets/images/"+piece+".png")

    """
    Muestra en pantalla la casilla
    """
    def showOnScreen(self):
        self.canvas_box =  Button(self.canvas,image=self.img_box,borderwidth=0,highlightthickness=0,command= lambda id = (8*self.x)+self.y: self.onClick(id),relief="flat")
        self.canvas_box.place(x=192.0 + (43 * self.y), y=105.0 + (43 * self.x), width=43.0, height=43.0)
        #self.canvas_box.grid(row=0, column=0)
    """
    Actualiza la imagen que se agrego al tablero
    """
    def setPiece(self, name, color):
        self.name = name
        self.color = color
        self.setImage()
        self.canvas_box.configure(image=self.img_box)
    
    """
    Obtiene el nombre de la casiila en el tablero
    """
    def getName(self) -> str:
        return self.name+self.color+str(self.back)