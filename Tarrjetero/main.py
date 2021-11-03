from tkinter import *
from typing import Collection
import pymysql
from tkinter import font as tkFont  # for convenience
from chess.interface import Interface


"""--------------------------------------------------------------------------------"""
"""Hacemos la consulta inicial para mostrar los datos cuando se compila el programa"""

con = pymysql.connect(host='localhost',
        user='root',
        password='pruebatest',
        db='mydb',
        charset='utf8mb4')

diccionario = {}
listaAtributos = []

try:

    with con.cursor() as cur:

        cur.execute('SELECT * FROM Tarjeta')

        rows = cur.fetchall()

        for row in rows:
            diccionario[row[0]] = [row[1], row[2], row[3]]
            
finally:

    con.close()

"""--------------------------------------------------------------------------------"""


ventana = Tk()

ventana.geometry('1200x1000')


"""Frame de la ventana para poner el titulo de la aplicación"""

tituloFrame = Frame(ventana, width=1000, height=100)
tituloFrame.grid(row=0,column=0)
tituloFrame.grid_propagate(0)

"""El logo de la aplicación"""

logoImg = PhotoImage(file='logo.png')
logo = Label(tituloFrame, image=logoImg)
logo.grid(row=0,column=0)

"""El titulo de la aplicación"""

titulo = Label(tituloFrame, text='Tarjetero',width=50,bg="#BABABA", font=("Arial", 25))
titulo.grid(row=0, column=1)

"""Frame para poner todos los datos de la tarjeta"""

frameTarjeta = Frame(ventana, width=1000, height=430)
frameTarjeta.grid(row=1, column=0)
frameTarjeta.grid_propagate(0)


"""El label del tema"""


tituloTema = Label(frameTarjeta, text='Tema:', width=50,font=("Arial", 15))
tituloTema.grid(row=0, column=0, sticky="news", pady=10, padx=10)

"""el margen donde va ir el tema"""

Tema = ''
bordeTema = Frame(frameTarjeta, bg="black")
bordeTema.grid(row=0, column=1, sticky="news")

"""Aqui va el tema que se seleccione"""
salidaTema = Label(frameTarjeta, text=Tema, bg="white") 
salidaTema.grid(row=0, column=1, sticky="news", padx=0.5, pady=0.5)

"""El frame para poner la descripción de la consulta"""

frameTexto = Frame(frameTarjeta, width=100)
frameTexto.grid(row=1, column=0, sticky="news")

"""Esta es la fuente que ocupamos para el diagrama, se escogio la de Chess Merida"""

chessMerida = tkFont.Font(family='Chess Merida', size=25, weight='bold')

"""El Label del diagrama"""

textoDoagrama = Label(frameTarjeta, text="Diagrama",font=("Arial", 15))
textoDoagrama.grid(row=1, column=1, sticky="news", pady=10)

"""El texto del diagrama con la fuente Merida"""

diagrama = ''
salidaDiagrama = Label(frameTarjeta, text=Tema, bg="white", justify="left", anchor='w')
salidaDiagrama['font'] = chessMerida
salidaDiagrama.grid(row=2, column=1, sticky=E)

"""El frame donde van a ir las consultas"""

frameConsultaHeader = Frame(ventana)
frameConsultaHeader.grid(row=3, column=0)

"""El frame para la cunsulta de los datos"""

frameConsultaDatos = Frame(ventana)
frameConsultaDatos.grid(row=4, column=0)

"""En esta seccion se crea el Scrollable para que se puedan ver los datos hacindo Scroll"""


miFrame= Frame(frameConsultaDatos, bg = "black")
miFrame.grid(row=0, column=0, sticky="news", padx=10, pady=10)
miFrame.grid_propagate(True)

miFrameTxt = Frame(frameConsultaDatos)
miFrameTxt.grid(padx=10, pady=10)

canvas = Canvas(miFrameTxt, height=150, width=600, bg="white")
scrollBar = Scrollbar(miFrameTxt, orient="vertical", command=canvas.yview)
scrollable_frame = Frame(canvas)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.config(
        scrollregion = canvas.bbox("all")
    )

)

canvas.create_window((0,0), window=scrollable_frame)
canvas.configure(yscrollcommand=scrollBar.set)

canvas.grid(row=0, column=0)
scrollBar.grid(row=0, column=1, sticky="ns")

"""Al principio dejamos los espacios en blanco hasta que se hace la consulta"""


descripcionTarjeta = ""
textoTarjeta = ''
textoTema = ''

"""Aqui ponemos el texto de la descripción de la tarjeta"""

salidaTexto = Text(frameTarjeta,width=20, bg="white",padx=15, pady=15, height=20)
salidaTexto.insert("1.0", textoTarjeta)
salidaTexto.grid(row=2, column=0, sticky="news")

"""
Funcion para hacer la consulta primero actualiza los datos y el diccionario por que si agragamos
una tarjeta tenemos que actualizar los datos antes de hacer la consulta
"""

def clickConsultaButton(id):

    global idConsulta
    idConsulta = id

    con = pymysql.connect(host='localhost',
        user='root',
        password='pruebatest',
        db='mydb',
        charset='utf8mb4')

    diccionario = {}

    try:

        with con.cursor() as cur:

            cur.execute('SELECT * FROM Tarjeta')
            rows = cur.fetchall()

            for row in rows:
                 diccionario[row[0]] = [row[1], row[2], row[3]]

    finally:

        con.close()

    global listaBotonesid
    global listaBotonesTemas

    for i in listaBotonesid:
        i.destroy()
    for i in listaBotonesTemas:
        i.destroy()
   
    listaBotonesid= []
    contador = 0
    for key  in diccionario:
        botonaux = Button(scrollable_frame, text=key, command=lambda i=key: clickConsultaButton(i))
        listaBotonesid.append(botonaux)
        listaBotonesid[contador].grid(row=contador, column=0, sticky="news")
        contador = contador + 1
        
    listaBotonesTemas =[]
    contador = 0
    for key in diccionario:
        buttontarjetaaxu = Button(scrollable_frame, text=diccionario[key][2] , command=lambda i=key: clickConsultaButton(i))
        listaBotonesTemas.append(buttontarjetaaxu)
        listaBotonesTemas[contador].grid(row=contador, column=1, sticky="news" )
        contador = contador + 1
    salidaTexto.delete("1.0", END)
    salidaTexto.insert("1.0",diccionario[id][0])
    salidaTema.config(text=diccionario[id][2])
    salidaDiagrama.config(text=diccionario[id][1])

"""
Función para la consulta pero de las busquedas ya que busca en el diccionario que corresponde
"""
def clickConsultaButtonB(id):

    global idConsulta
    idConsulta = id

    

    global listaBotonesid
    global listaBotonesTemas

    for i in listaBotonesid:
        i.destroy()
    for i in listaBotonesTemas:
        i.destroy()
   
    listaBotonesid= []
    contador = 0
    for key  in diccionario:
        botonaux = Button(scrollable_frame, text=key, command=lambda i=key: clickConsultaButton(i))
        listaBotonesid.append(botonaux)
        listaBotonesid[contador].grid(row=contador, column=0, sticky="news")
        contador = contador + 1
        
    listaBotonesTemas =[]
    contador = 0
    for key in diccionario:
        buttontarjetaaxu = Button(scrollable_frame, text=diccionario[key][2] , command=lambda i=key: clickConsultaButton(i))
        listaBotonesTemas.append(buttontarjetaaxu)
        listaBotonesTemas[contador].grid(row=contador, column=1, sticky="news" )
        contador = contador + 1
    
    salidaTexto.delete("1.0", END)
    salidaTexto.insert("1.0", diccionario[id][0])

    salidaTema.config(text=diccionario[id][2])
    salidaDiagrama.config(text=diccionario[id][1])

"""
Aqui se actulizan por primera vez los botoner para que los podamos ver en pantalla y de ahi ya no se vulven
a actulizart los datos ya que se llama la funcion refresh para actulizar los datos
"""

listaBotonesid= []
contador = 0
for key  in diccionario:
    botonaux = Button(scrollable_frame, text=key, command=lambda i=key: clickConsultaButton(i))
    listaBotonesid.append(botonaux)
    listaBotonesid[contador].grid(row=contador, column=0, sticky="news")
    contador = contador + 1
    
listaBotonesTemas =[]
contador = 0
for key in diccionario:
    buttontarjetaaxu = Button(scrollable_frame, text=diccionario[key][2] , command=lambda i=key: clickConsultaButton(i))
    listaBotonesTemas.append(buttontarjetaaxu)
    listaBotonesTemas[contador].grid(row=contador, column=1, sticky="news" )
    contador = contador + 1


"""Frame para las opciones"""

frameOpciones = Frame(ventana)
frameOpciones.grid(row=1, column=1)

"""El botón de las opciones para poder buscar"""

buscar = Button(frameOpciones, text='Buscar Tarjeta',font=("Arial",15), command=lambda: buscarTar())
buscar.grid(row=4, column=0, sticky="news", pady=10, padx=10)

"""
función para hacer una busqueda
"""

def buscarTar():
      

    top = Toplevel()

    labelBusqueda = Label(top, text="Ingrese el tema que quiera buscar")

    labelBusqueda.place(x=10, y=10)

    entradaBusqueda = Entry(top)

    entradaBusqueda.place(x=10, y=50)

    botonBuscar = Button(top, text="Buscar", command=lambda: buscarT(entradaBusqueda.get()))
    botonBuscar.place(x=10, y=90)
    top.mainloop()

"""
Fucnión auxiliar que hace las busqueda de acuerdo al tema que se selecciono
La función logra sacar los resultados si estan en mayusculas o minusculas, lo que si es necesario
son los acentos
"""

def buscarT(temaB):
    con = pymysql.connect(host='localhost',
        user='root',
        password='pruebatest',
        db='mydb',
        charset='utf8mb4')
    comillas = "'"
    print("este es el tema"+temaB)
    try:

        with con.cursor() as cur:

            cur.execute('select * from tarjeta where tema like '+comillas+'%'+temaB+'%'+comillas)

            rows = cur.fetchall()

            diccB = {}
            for row in rows:
                diccB[row[0]] = [row[1], row[2], row[3]]

    
    finally:

        con.close()

    global listaBotonesTemas
    global listaBotonesid
    for i in listaBotonesid:
            i.destroy()
    for i in listaBotonesTemas:
            i.destroy()


    del listaBotonesid[:] 
    del listaBotonesTemas[:]
    
    
    listaBotonesid= []
    contador = 0
    for key  in diccB:
        botonaux = Button(scrollable_frame, text=key, command=lambda i=key: clickConsultaButtonB(i))
        listaBotonesid.append(botonaux)
        listaBotonesid[contador].grid(row=contador, column=0, sticky="news")
        contador = contador + 1
        
    listaBotonesTemas =[]
    contador = 0
    for key in diccB:
        buttontarjetaaxu = Button(scrollable_frame, text=diccB[key][2] , command=lambda i=key: clickConsultaButtonB(i))
        listaBotonesTemas.append(buttontarjetaaxu)
        listaBotonesTemas[contador].grid(row=contador, column=1, sticky="news" )
        contador = contador + 1

"""El label de la terjeta"""

tituloTexto = Label(frameTarjeta, text='Tarjeta',font=("Arial", 15))
tituloTexto.grid(row=1, column=0, sticky="news")

"""boton dentro de las opciones para agregar las tarjetas"""

agregarBoton = Button(frameOpciones, text='Agregar Tarjeta', font=("Arial",15),command= lambda : agregarTarjeta())
agregarBoton.grid(row=0, column=0, sticky="news", pady=10, padx=10)

"""Frame auxiliar"""

frameChess = Frame(ventana)
frameChess.grid(row=4, column=0)

"""Función para refrescar la pantalla y los botones cada vez que se agrega, quita , o edita una tarjeta """

def refresh():
    con = pymysql.connect(host='localhost',
        user='root',
        password='pruebatest',
        db='mydb',
        charset='utf8mb4')

    diccionario = {}

    try:

        with con.cursor() as cur:

            cur.execute('SELECT * FROM Tarjeta')

            rows = cur.fetchall()

            for row in rows:
                 diccionario[row[0]] = [row[1], row[2], row[3]]
            
        

    finally:

        con.close()

    global listaBotonesid
    global listaBotonesTemas

    for i in listaBotonesid:
        i.destroy()
    for i in listaBotonesTemas:
        i.destroy()
      
    listaBotonesid= []
    contador = 0
    for key  in diccionario:
        botonaux = Button(scrollable_frame, text=key, command=lambda i=key: clickConsultaButton(i))
        listaBotonesid.append(botonaux)
        listaBotonesid[contador].grid(row=contador, column=0, sticky="news")
        contador = contador + 1
        
    listaBotonesTemas =[]
    contador = 0
    for key in diccionario:
        buttontarjetaaxu = Button(scrollable_frame, text=diccionario[key][2] , command=lambda i=key: clickConsultaButton(i))
        listaBotonesTemas.append(buttontarjetaaxu)
        listaBotonesTemas[contador].grid(row=contador, column=1, sticky="news" )
        contador = contador + 1
    

"""
Función para agregar una nueva tarjeta
"""
def agregarTarjeta():
    
    top = Toplevel()
    frameLevel = Frame(top, bg="white")
    frameLevel.grid(row=0, column=0)
    canvas1 = Canvas(frameLevel,width=1000,height=1000)
    canvas1.grid(row=0, column=0)
    interfaceI = Interface(canvas1)
    interfaceI.setLogo()
    interfaceI.setBoard()
    interfaceI.createButtons()
    interfaceI.createDescripcion()    
    salir = Button(top, text="Salir",padx=7, pady=7, font=("Arail",15), command= lambda : [top.destroy(),refresh(),Tk.update(ventana)])
    salir.place(x=870, y=30)
    top.mainloop()


"""Boton para editar las tarjetas"""

editarTarjeta = Button(frameOpciones, text='Editar Tarjeta',font=("Arial",15) ,command= lambda : editarTar())
editarTarjeta.grid(row=1, column=0, sticky="news", pady=10, padx=10)

"""
Función para editar las tarjetas
"""

def editarTar():
    
    if idConsulta  != None :
        
        top = Toplevel()
        frameLevel = Frame(top, bg="white")
        frameLevel.grid(row=0, column=0)
        canvas1 = Canvas(frameLevel,width=1000,height=1000)
        canvas1.grid(row=0, column=0)
        interfaceI = Interface(canvas1)
        interfaceI.setLogo()
        interfaceI.setBoard1(idConsulta)
        interfaceI.createButtons()
        interfaceI.editar(idConsulta)    
        salir = Button(top, text="Salir",padx=7, pady=7, font=("Arail",15), command= lambda : [top.destroy(), refresh(),Tk.update(ventana)] )
        salir.place(x=870, y=30)
    else:
        print("primero selecciona un id")
    
    top.mainloop()

"""Boton para borraar una tarjeta"""
borrarTarjeta = Button(frameOpciones, text='Borrar Tarjeta',font=("Arial", 15), command= lambda: delete())
borrarTarjeta.grid(row=2, column=0, sticky="news", pady=10, padx=10)

"""
Función para borrar una tarjeta
"""

def delete():
    con = pymysql.connect(host='localhost',
    user='root',
    password='pruebatest',
    db='mydb',
    charset='utf8mb4')
    
    try:

            with con.cursor() as cur:
                consulta = 'DELETE FROM tarjeta WHERE idTarjeta ='+ str(idConsulta)
                cur.execute(consulta)
            con.commit()
    finally:

            con.close()
    top = Toplevel()
    aviso = Label(top, text=  "El borrado se ha llevado con exito")
    aviso.place(x=20, y=20)
    refresh()


"""Frame para los derechos de autor"""

frameFooter = Frame(ventana)
frameFooter.grid(row=5, column=0)

derechos = Label(frameFooter, text="Creado por Marco Antonio Orduña Avila, todos los derechos reservaoos")
derechos.place(x=10, y=955 )

"""Frame para salir del programa"""

salir= Button(frameFooter,text='Salir')
salir.grid(row=0,column=0)

ventana.mainloop()