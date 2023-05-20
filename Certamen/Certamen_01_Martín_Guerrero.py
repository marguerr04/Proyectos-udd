# Nombre : Martín Guerrero
import numpy as np # link : https://numpy.org/doc/stable/reference/generated/numpy.array.html
import random as rd
'''
1) Preguntar características del juego y crear un tablero visualmente(matriz)
'''
partida = 'start'
while partida == 'start':
    Flores = -1
    Alto = int(input('Enter height(↕) of your board: \n'))
    Ancho = int(input('Enter the Width(↔) of your board: \n'))
    while Flores not in range(1,(Alto * Ancho)): # El n° flores debe estar entre 1 y el area del tablero -1
        Flores = int(input('Enter the n° of flowers in the range of the board \n'))
    tablero = []
    for i in range(Alto):
        fila = []
        for j in range(Ancho):
            fila.append('*')
            
        tablero.append(fila)

        #Array muestra una lista de lista como matriz
        matriz = np.array(tablero)
    '''   
    # 2) Generar coordenadas aleatorias, que estan dadas por en n° de flores + la posición de la abeja
    '''
    coordenadas = []
    while len(coordenadas) < (Flores + 1): # Generara coordenadas hasta que se cumpla la condición 2) 
        coordenada = [rd.randint(0,(Alto-1)), rd.randint(0, (Ancho-1))]   
        if coordenada not in coordenadas:    # Verífica no agregar coordenadas ya generadas 
            coordenadas.append(coordenada)
    '''
    3) Asignar una abeja 'R' y una flor 'F' a cada coordenada 
    '''
    R = coordenadas[0] 
    F = coordenadas[1:]
    '''
    4) Poder visualizar las flores y la abeja en el tablero
    '''
    matriz[R[0]][R[1]]= 'R'
    for f in F:
        matriz[f[0]][f[1]] = 'F'
    print(matriz)
    '''
    5) Hacer los movimientos de la abeja
    '''
    T = len(F) + ((Ancho*Alto)-len(F))//(100/50) # n° de intentos(Tries) -> n° flores + 50% del resto del tablero
    cT = 0 # contador de intentos
    while (cT < T) and (len(F) > 0):
        mov = input('Write w(up)/s(down)/a(left) or d(right), to make a move \n') 
        moves = {'s' : [(R[0])+1,R[1]], # diccionario (clase 12) que relaciona cada letra con una nueva posición 
        'w' : [(R[0])-1,R[1]],          # El movimiento esta como (x,y), si x+1 -> (1)abajo, si y+1 -> (1)derecha
        'a' : [R[0],(R[1])-1],
        'd' : [R[0],(R[1])+1]}
        for m in moves: # Verifica que el movimiento sea w,a,s,d y que las nuevas cordenadas (x,y) esten en el rango del tablero
            if (mov == m) and ((moves[m])[0] in range(0,Alto)) and ((moves[m])[1] in range(0,Ancho)): 
                    matriz[R[0]][R[1]] = '*'# La casilla original es reemplazada por '*'
                    R = moves[m]            # Ahora la abeja tendra 1 de las 4 posiciones de moves
                    cT += 1
                    matriz[R[0]][R[1]]= 'R' # Reusamos el codigo del paso 4)
                    print(matriz)
                    print(f'moves left: {T-cT}')
                    if R in F:          # Verificamos si la abeja esta en alguna coordenada de las flores,para eliminarla
                            F.remove(R) # Link : https://docs.python.org/3/tutorial/datastructures.html                
    '''
    6) Hacer que el juego se termine (Ganar o perder) y que se pueda reiniciar
    '''
    if len(F) == 0:
        print(f'¡Congratulations!, you had won the game with {T- cT} moves left!')
    elif cT == T:
        print(f'You had lose the game with {len(F)} flowers left')
    partida = input('write ''start'' or anything else to create a new game or exit the game ')
