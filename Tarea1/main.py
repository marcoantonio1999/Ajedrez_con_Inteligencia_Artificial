from chess.interface import Interface
from tkinter import Canvas
import tkinter as tk

"""
    Autor: Marco Antonio Orduña Avila
   Programa que por ahora solo permite poner piezas de ajedréz en el tablero y guardar las
   jugadas en un archivo txt con la fuente chess merida.
"""

if __name__ == "__main__":
    window = tk.Tk()
    #Define el tamaño de la ventana

    window.geometry("770x562")

    window.configure(bg = "#FFFFFF")

    canvas = Canvas(
        window,
        bg = "#FFFFFF",
        height = 562,
        width = 770,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    # Una instancia de la clase Interface pues debe eredar kis atributos de la raiz, la interfaz
    # es la que tendra todos los elementos visibles del ajedrez
    interface = Interface(canvas)

    # Solo para poner el logo personal de mi aplicación
        
    interface.setLogo()
    
    # Agregra los botones para las funcionalidades que tendra la aplicación
    # (Esto posiblemente cambie por un dropdown si después tienen mas funcionalidades)

    interface.createButtons()

    #configuracion del tablero inicial

    interface.setBoard()

    window.resizable(False, False)
    window.mainloop()