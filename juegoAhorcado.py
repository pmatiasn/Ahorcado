# Funciones para definir la palabra completa el usuario
def generoPalabraCompleta (palabraJuego):
    palabraCompleta= []
    for i in palabraJuego:
        palabraCompleta.append (i)
    return palabraCompleta

#Funcion para generar la palabra incompleta
def generoPalabraIncompleta (palabraJuegoCompleta):
    palabraIncompleta= []  
    for i in palabraJuegoCompleta:
        palabraIncompleta.append ("_")
    palabraIncompleta [0]= palabraJuegoCompleta [0]
    palabraIncompleta [len (palabraIncompleta)-1]= palabraJuegoCompleta [len (palabraJuegoCompleta)-1]  
    return palabraIncompleta

#Limpia la terminal para jugar (buscado en internet)
def limpiar ():
    import os
    def clear():
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
    clear()

# Funcion para saber si la letra esta
def estaLetra (palabra, letra):
    if (letra in palabra):
        return True
    else:
        return False

# Funcion para reemplazar la letra
def reemplazarLetra (palabraCompleta, palabraIncompleta,letra):
    for i in range (0, len (palabraCompleta)):
        if palabraCompleta [i] == letra:
            palabraIncompleta [i] = letra

# Ver si la palabra incompleta se lleno
def verPalabra (palabraIncompleta):
    if ("_" in palabraIncompleta):
        return False
    else:
        return True

# Estado de inicio
print ("¡JUEGO DEL AHORCADO!")
palabraUsuario= input ("Ingrese la palabra con la que jugara: ")

palabraCompleta = generoPalabraCompleta (palabraUsuario)
palabraIncompleta = generoPalabraIncompleta (palabraCompleta)
vidas = 6
fallos = []

#Limpia la terminal para jugar (buscado en internet)
limpiar ()

# Juego
while vidas > 0:
    limpiar ()
    print (palabraIncompleta)
    print (fallos)
    letraIngresada= input ("Ingrese una letra: ")
    # Resultado del ingrso
    resultado= estaLetra (palabraCompleta, letraIngresada)
    if resultado == True:
        # Reemplazo la letra en la palabra incompleta
        reemplazarLetra (palabraCompleta, palabraIncompleta, letraIngresada)
    else:
        # Agrego la letra a las fallas
        fallos.append (letraIngresada)
        vidas= vidas - 1
    # Da la victoria o la derrota
    if verPalabra (palabraIncompleta):
        print ("¡Gano el juego! la palabra era: ", palabraIncompleta)
        break
    elif vidas == 0:
        print ("¡FIN DEL JUEGO! No tienes vidas, la palabra era: ", palabraCompleta)
        