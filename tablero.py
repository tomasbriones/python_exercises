#create a function that add a new board to play a game 
def crearTablero(alto,ancho):
    tablero = []
    for i in range(0,alto):
        filas = []
        for j in range(0,ancho):
            filas.append("*")
        tablero.append(filas)
    return tablero

print(crearTablero(5,6))