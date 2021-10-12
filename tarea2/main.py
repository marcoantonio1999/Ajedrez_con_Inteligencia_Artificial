from os import terminal_size
from  tkinter import *
from tkinter import font

"""
Autor: Marco Antonio Orduña Avila

Aplicación para sabere el Ratting de ajedrez según el sistema de puntuación Elo

"""


ventana =  Tk()
ventana.geometry('1000x1000') #Tamaño se la ventana

"""
Sección del titulo y el logo de la aplicación
"""



tituloFrame = Frame(ventana)    
tituloFrame.grid(row=0, column=0)


# titulo y logo

titulo =  Label(tituloFrame,text='Calculadora de Ratting', bg='grey',height=1,width=30, font=('Arial',32))
titulo.grid(row=0, column=1, ipadx=100)
logoimg = PhotoImage(file='logo.png')
logo = Label(tituloFrame, image=logoimg)
logo.grid(row=0, column=0)


"""
Sección para los datos del torneo y del raking actual
"""

datosPrimarios= Frame(ventana, pady=15)
datosPrimarios.grid(row=1, column=0, ipadx=100)

# entrada del ranking Actual

labelRatingActual = Label(datosPrimarios,text='Introduce el Ratting Actual')
labelRatingActual.grid(row=0, column=0)
rattingActual = Entry(datosPrimarios)
rattingActual.grid(row=0, column=1)

# entrada para el número de juegos

labelNumJuegos = Label(datosPrimarios,text='Introduce el numero de juegos')
labelNumJuegos.grid(row=1, column=0, pady=10)
numJuegos = Entry(datosPrimarios)
numJuegos.grid(row=1 , column=1)

# Puntuación de Jueos Ganados
# 1 si gano el juego
# 0 si lo perdio
# 0.5 si fue empate

labelGanados = Label(datosPrimarios, text='Introdcuce la puntuación de juegos ganados')
labelGanados.grid(row=2, column=0, pady=10)
ganados = Entry(datosPrimarios)
ganados.grid(row=2, column=1)

# Entrada para el promedio de los niveles solo si ya se calculo anteriormentem
# no importa si este dato es vació

labelPromNiveles = Label(datosPrimarios, text='Promedio de niveles:')
labelPromNiveles.grid(row=3, column=0, pady=10)
promNiveles = Entry(datosPrimarios)
promNiveles.grid(row=3, column=1)

# Entrada para el valor de la constante K

labelK = Label(datosPrimarios, text='Intoduce el valor de K')
labelK.grid(row=4, column=0, pady=10)
constanteK = Entry(datosPrimarios)
constanteK.grid(row=4, column=1)

"""
Sección para poner los datos de la puntuación de los juegadores en el torneo
"""

frameJugadores = Frame(ventana, pady=1, bd=5)
frameJugadores.grid(row=3, column=0)



labe1 = Label(frameJugadores,text='Jugador 1')
labe1.grid(row=0, column=0)
oponente1 = Entry(frameJugadores)
oponente1.insert(0, '0')
oponente1.grid(row=1, column=0)

labe2 = Label(frameJugadores, text='Jugador 2')
labe2.grid(row=2, column=0, pady=10)
oponente2 = Entry(frameJugadores)
oponente2.insert(0, '0')
oponente2.grid(row=3, column=0)


labe3 = Label(frameJugadores, text='Jugador 3')
labe3.grid(row=4, column=0, pady=10)
oponente3 = Entry(frameJugadores)
oponente3.insert(0, '0')
oponente3.grid(row=5, column=0)

labe4 = Label(frameJugadores, text='Jugador 4')
labe4.grid(row=6, column=0, pady=10)
oponente4 = Entry(frameJugadores)
oponente4.insert(0, '0')
oponente4.grid(row=7, column=0)

labe5 = Label(frameJugadores, text='Jugador 5')
labe5.grid(row=8, column=0)
oponente5 = Entry(frameJugadores)
oponente5.insert(0, '0')
oponente5.grid(row=9, column=0)



labe6 = Label(frameJugadores, text='Jugador 6')
labe6.grid(row=0, column=1)
oponente6 = Entry(frameJugadores)
oponente6.insert(0, '0')
oponente6.grid(row=1, column=1,padx=40)




labe7 = Label(frameJugadores, text='Jugador 7')
labe7.grid(row=2, column=1)
oponente7 = Entry(frameJugadores)
oponente7.insert(0, '0')
oponente7.grid(row=3, column=1)


labe8 = Label(frameJugadores, text='Jugador 8')
labe8.grid(row=4, column=1)
oponente8 = Entry(frameJugadores)
oponente8.insert(0, '0')
oponente8.grid(row=5, column=1)


labe9 = Label(frameJugadores, text='Jugador 9')
labe9.grid(row=6, column=1)
oponente9 = Entry(frameJugadores)
oponente9.insert(0, '0')
oponente9.grid(row=7, column=1)


label0 = Label(frameJugadores, text='Jugador 10')
label0.grid(row=8, column=1)
oponente10 = Entry(frameJugadores)
oponente10.insert(0, '0')
oponente10.grid(row=9, column=1,padx=40)

label1 = Label(frameJugadores, text='Jugador 11')
label1.grid(row=0, column=2)
oponente11 = Entry(frameJugadores)
oponente11.insert(0, '0')
oponente11.grid(row=1, column=2)

label2 = Label(frameJugadores, text='Jugador 12')
label2.grid(row=2, column=2)
oponente12 = Entry(frameJugadores)
oponente12.insert(0, '0')
oponente12.grid(row=3, column=2)

label3 = Label(frameJugadores, text='Jugador 13')
label3.grid(row=4, column=2)
oponente13 = Entry(frameJugadores)
oponente13.insert(0, '0')
oponente13.grid(row=5, column=2)

label4 = Label(frameJugadores, text='Jugador 14')
label4.grid(row=6, column=2)
oponente14 = Entry(frameJugadores)
oponente14.insert(0, '0')
oponente14.grid(row=7, column=2)

label5 = Label(frameJugadores, text='Jugador 15')
label5.grid(row=8, column=2)
oponente15 = Entry(frameJugadores)
oponente15.insert(0, '0')
oponente15.grid(row=9, column=2)

label6 = Label(frameJugadores, text='Jugador 16')
label6.grid(row=0, column=3,padx=10)
oponente16 = Entry(frameJugadores)
oponente16.insert(0, '0')
oponente16.grid(row=1, column=3,padx=40)

label7 = Label(frameJugadores, text='Jugador 17')
label7.grid(row=2, column=3)
oponente17 = Entry(frameJugadores)
oponente17.insert(0, '0')
oponente17.grid(row=3, column=3)

label8 = Label(frameJugadores, text='Jugador 18')
label8.grid(row=4, column=3, pady=10)
oponente18 = Entry(frameJugadores)
oponente18.insert(0, '0')
oponente18.grid(row=5, column=3)

label9 = Label(frameJugadores, text='Jugador 19')
label9.grid(row=6, column=3)
oponente19 = Entry(frameJugadores)
oponente19.insert(0, '0')
oponente19.grid(row=7, column=3)


label = Label(frameJugadores, text='Jugador 20')
label.grid(row=8, column=3, pady=10)
oponente20 = Entry(frameJugadores)
oponente20.insert(0, '0')
oponente20.grid(row=9, column=3)



"""
función para calcular el porcentaje segun la puntuación del tablero de puntuación según Elo
recibe la diferencia del promédio de los jugadores entre el ratting actual
returns el porcentaje según la tabla
"""

def tablaElo(difPromedio):
    if 633<difPromedio <2000:
        return 0.99
    if 564<difPromedio <632:
        return 0.98
    if 520<difPromedio <563:
        return 0.97
    if 485<difPromedio <519:
        return 0.96
    if 457<difPromedio <484:
        return 0.95
    if 433<difPromedio <456:
        return 0.94
    if 412<difPromedio <432:
        return 0.93
    if 392<difPromedio <412:
        return 0.92
    if 375<difPromedio <391:
        return 0.91
    if 359<difPromedio <374:
        return 0.90
    if 343<difPromedio <358:
        return 0.89
    if 329<difPromedio <342:
        return 0.88
    if 315<difPromedio <328:
        return 0.87
    if 302<difPromedio <314:
        return 0.86
    if 290<difPromedio <301:
        return 0.85
    if 279<difPromedio <289:
        return 0.84
    if 268<difPromedio <278:
        return 0.83
    if 257<difPromedio <267:
        return 0.82
    if 246<difPromedio <256:
        return 0.81
    if 235<difPromedio <245:
       return 0.80
    if 225<difPromedio <234:
        return 0.79
    if 216<difPromedio <224:
        return 0.78
    if 207<difPromedio <215:
        return 0.77
    if 198<difPromedio <206:
        return 0.76
    if 189<difPromedio <197:
       return 0.75
    if 180<difPromedio <189:
        return 0.74
    if 171<difPromedio <179:
        return 0.73
    if 162<difPromedio <170:
        return 0.72
    if 154<difPromedio <161:
          return 0.71
    if 145<difPromedio <153:
        return 0.70
    if 137<difPromedio <144:
        return 0.69
    if 129<difPromedio <136:
        return 0.68
    if 121<difPromedio <128:
        return 0.67
    if 114<difPromedio <120:
        return 0.66
    if 106<difPromedio <113:
        return 0.65
    if 99<difPromedio <105:
        return 0.64
    if 91<difPromedio <98:
        return 0.63
    if 84<difPromedio <90:
        return 0.62
    if 76<difPromedio <83:
        return 0.61
    if 69<difPromedio <75:
        return 0.60
    if 61<difPromedio <68:
        return 0.59
    if 54<difPromedio <60:
        return 0.58
    if 47<difPromedio <53:
        return 0.57
    if 40<difPromedio <46:
        return 0.56
    if 33<difPromedio <39:
        return 0.55
    if 25<difPromedio <32:
        return 0.54
    if 18<difPromedio <24:
        return 0.53
    if 11<difPromedio <17:
        return 0.52
    if 4<difPromedio <10:
        return 0.51

    if -3<difPromedio <4:
        return 0.50
    
    if -633<difPromedio <-4000:
        return 0.01
    if -632<difPromedio <-564:
        return 0.02
    if -563<difPromedio <-520:
        return 0.03
    if -519<difPromedio <-485:
        return 0.04
    if -484<difPromedio <-457:
        return 0.05
    if -456<difPromedio <-433:
        return 0.06
    if -432<difPromedio <-412:
        return 0.07
    if -412<difPromedio <-392:
        return 0.08
    if -391<difPromedio <-375:
        return 0.09
    if -374<difPromedio <-359:
        return 0.10
    if -358<difPromedio <-343:
        return 0.11
    if -342<difPromedio <-329:
        return 0.12
    if -328<difPromedio <-315:
        return 0.13
    if -314<difPromedio <-302:
        return 0.14
    if -301<difPromedio <-290:
        return 0.15
    if -289<difPromedio <-279:
        return 0.16
    if -278<difPromedio <-268:
        return 0.17
    if -267<difPromedio <-257:
        return 0.18
    if -256<difPromedio <-246:
        return 0.19
    if -245<difPromedio <-235:
       return 0.20
    if -234<difPromedio <-225:
        return 0.21
    if -224<difPromedio <-216:
        return 0.22
    if -215<difPromedio <-207:
        return 0.23
    if -206<difPromedio <-198:
        return 0.24
    if -197<difPromedio <-189:
       return 0.25
    if -189<difPromedio <-180:
        return 0.26
    if -179<difPromedio <-171:
        return 0.27
    if -170<difPromedio <-162:
        return 0.28
    if -161<difPromedio <-154:
          return 0.29
    if -153<difPromedio <-145:
        return 0.30
    if -144<difPromedio <-137:
        return 0.31
    if -136<difPromedio <-129:
        return 0.32
    if -128<difPromedio <-121:
        return 0.33
    if -120<difPromedio <-114:
        return 0.34
    if -113<difPromedio <-106:
        return 0.35
    if-105<difPromedio <- 99:
        return 0.36
    if-98<difPromedio <- 91:
        return 0.37
    if-90<difPromedio <- 84:
        return 0.38
    if-83<difPromedio <- 76:
        return 0.39
    if-75<difPromedio <- 69:
        return 0.40
    if-68<difPromedio <- 61:
        return 0.41
    if-60<difPromedio <- 54:
        return 0.42
    if-53<difPromedio <- 47:
        return 0.43
    if-46<difPromedio <- 40:
        return 0.44
    if-39<difPromedio <- 33:
        return 0.45
    if-32<difPromedio <- 25:
        return 0.46
    if-24<difPromedio <- 18:
        return 0.47
    if-17<difPromedio <- 11:
        return 0.48
    if-10<difPromedio <- 4:
        return 0.49
    
"""
Función para calcular el Ratting Nuevo
Nos imprime en la interface el ratting Nuevo
La diferencia entre el ratting nuevo y el anterior
El desempeño del jugador
"""

def calcularRatting():
    ra =  int(rattingActual.get())
    
    j1 = oponente1.get()
    j2 = oponente2.get()
    j3 = oponente3.get()
    j4 = oponente4.get()
    j5 = oponente5.get()
    j6 = oponente6.get()
    j7 = oponente7.get()
    j8 = oponente8.get()
    j9 = oponente9.get()
    j10 = oponente10.get()
    j11 = oponente11.get()
    j12 = oponente12.get()
    j13 = oponente13.get()
    j14 = oponente14.get()
    j15 = oponente15.get()
    j16 = oponente16.get()
    j17 = oponente17.get()
    j18 = oponente18.get()
    j19 = oponente19.get()
    j20 = oponente20.get()


    listaRattingJugadores = [j1,j2,j3,j4,j5,j6,j7,j8,j9,j10,j11,j12,j13,j14,j15,j16,j17,j18,j19,j20]
    juegos = int(numJuegos.get())
    
    suma = 0
    prom = 0
    print(promNiveles.get())
    if(promNiveles.get() ==''):
        for i in range(0,juegos):
            suma = suma + int(listaRattingJugadores[i])
        prom = suma/juegos
    else:
        prom = int(promNiveles.get())
        
    difPromedio = ra-prom
    puntosPorHacer = juegos*tablaElo(difPromedio)

    ratinNuevo = ra + int(constanteK.get())*(float(ganados.get())-puntosPorHacer)
    
    labelResultadoRN = Label(datosPrimarios,text=int(ratinNuevo), font=('Arial', 20))
    labelResultadoRN.grid(row=0, column=5)

    diferencia = ratinNuevo - ra

    labelResDif = Label(datosPrimarios, text=int(diferencia), font=('Arial',20))
    labelResDif.grid(row=1, column=5)

    desempenio = (suma+ 400*(int(ganados.get())-(juegos-int(ganados.get()))))/juegos

    labelResDesempenio = Label(datosPrimarios, text=int(desempenio), font=('Arial', 20 ))
    labelResDesempenio.grid(row=2, column=5)

"""
Función para limpiar los datos de la interface
"""

def limpiarDatos():
    rattingActual.delete(0,END)
    numJuegos.delete(0,END)
    ganados.delete(0,END)
    promNiveles.delete(0,END)
    constanteK.delete(0,END)
    oponente1.delete(0,END)
    oponente2.delete(0,END)
    oponente3.delete(0,END)
    oponente4.delete(0,END)
    oponente5.delete(0,END)
    oponente6.delete(0,END)
    oponente7.delete(0,END)
    oponente8.delete(0,END)
    oponente9.delete(0,END)
    oponente10.delete(0,END)
    oponente11.delete(0,END)
    oponente12.delete(0,END)
    oponente13.delete(0,END)
    oponente14.delete(0,END)
    oponente15.delete(0,END)
    oponente16.delete(0,END)
    oponente17.delete(0,END)
    oponente18.delete(0,END)
    oponente19.delete(0,END)
    oponente20.delete(0,END)


"""
Función para salir del programa
"""
def salir():
    ventana.destroy()


"""
Botones para las funciones
"""

buttonCalcular =  Button(datosPrimarios,text='Calcular',padx=50, command=calcularRatting)
buttonLimpiar = Button(datosPrimarios,text='Limpiar',padx=50, command=limpiarDatos)
buttonLSalir = Button(datosPrimarios,text='Salir',padx=50, command=salir)

buttonCalcular.grid(row=0, column=3, padx=80)
buttonLimpiar.grid(row=1, column=3)
buttonLSalir.grid(row=2, column=3)

labelRattingNuevo = Label(datosPrimarios  ,text='Ratting Nuevo:', font=('Arial',20))
labelRattingNuevo.grid(row=0, column=4)

labelDiferencia = Label(datosPrimarios, text='Diferencia:', font=('Arial',20))
labelDiferencia.grid(row=1, column=4)

labelDesempenio = Label(datosPrimarios, text="Desempeño:", font=('Arial',20)) 
labelDesempenio.grid(row=2, column=4)

"""
loop para que se mantenga la ventana
"""

ventana.mainloop()