# Nombre Martín Guerrero
'''
1). Lista concatenada
'''
from random import randint as rdi

print('Hola, este programa devolvera una lista concatenara de n largo ')
N = int(input('Ingrese n° de terminos de su lista: \n'))
# 2 Crear un ciclo while para cada pregunta t agregarlo a una lista, hacer un minicontador
L = []
while len(L) < N:
    L.append(input(f'Ingrese su elemento {len(L)+1}: \n'))
print(f'Lista = {L} \n')

# 3 Generar un n° aleatorio  y crear las variables a utilizar 

k = rdi(1,N) # K = n° aleatorio
L = L*k      # Creamos  la lista en factor de k de largo
s = 1        # Sera el minicontador para los terminos
print(f'N° aleatorio = {k}')

# 4 Usar el minicontador y el algoritmo de // y % para agregar a cada elemento un termino

for e in L:                                                 #Como el e parte del 0, le agregamos un 1, ademas cuando llega a un entero no debe cambiar aún, solo cuando sobre pasa el largo , asi nos aseguramos que todos los terminos esten cubiertos
    if (L.index(e)+1)//N == s and (L.index(e)+1)%N != 0:
        s += 1
    L[L.index(e)] += str(s)
print(L)