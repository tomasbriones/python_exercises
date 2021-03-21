#create a function that add a new board to play a game 
def crearTablero(alto,ancho):
    ready = False
    tablero = []
    for i in range(0,alto):
        for j in range(0,ancho):
            print("*")
            tablero.append("*")
    return ready

    crearTablero(5,6)