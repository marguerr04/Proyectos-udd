# Martín Guerrero
#1- El hervidor
print('Hervidor encendido, calentando su café \n .\n .. \n ...')
from random import randint
T = randint(18, 25)
while T < 94:
    T += 2
    if T > 94:
        break
    print(T)
print('Su  cafe ha alcanzado la temperatura ideal, retire su cafe')

#2-Remedios para su abuelita
print('Hola, este programa calculara cuando debe tomar las dosis de medicamentos')
A = input('Ingrese la fecha y hora del medicamento de cada 8 hrs  como en el sgte ejemplo: 01-01-2020-13:00 \n')
FechasA = A.split('-')
dA = int(FechasA[0]) # Día de A
mA = int(FechasA[1]) # Mes de A
yA = int(FechasA[2]) # Año de A
hA = int(FechasA[3].split(':')[0]) # Hora de A 
mmA = FechasA[3].split(':')[1] # Minutos como string
ho = 0
print("Medicamento", 'A' "(cada 8 horas):")
for dosis in range(42): # 14 dias con 3 dosis diarias = 42 dosis
    FechasA = [str(dA),str(mA),str(yA),str(hA)]
    print('-'.join(FechasA)+':'+mmA)
    ho = hA + 8 # la hora original(hA) + las 8 horas = horas de las dosis
    hA = ho%24
    dA = (dA + ho//24) # Que los dias se almacenen cada 24 horas
    if dA > 30: #Si los dias son mayor a 30, que el mes cambie
        dA = 1
        mA += 1
        if mA > 12: # si los meses son mayor a 12, que el año cambie
            mA = 1
            yA += 1 
B = input('Ingrese la fecha y hora del medicamento de cada 12 hrs  como en el sgte ejemplo: 01-01-2020-13:00 \n')
FechasB = B.split('-')
dB = int(FechasB[0]) # Día de B
mB = int(FechasB[1]) # Mes de B
yB = int(FechasB[2]) # Año de B
hB = int(FechasB[3].split(':')[0]) # Hora de B
mmB = FechasB[3].split(':')[1] # Minuto de B como string
print('Medicamento B cada 12 horas: ')
for dosis in range (28): # 14 dias con 2 dosis diarias = 28 dosis
    FechasB = [str(dB),str(mB),str[yB],str(hB)]
    print('-'.join(FechasB)+':'+mmB)
    ho = hB + 8
    hB = ho%24
    dB = (dB + ho//24)
    if dB > 30:
        dB = 1
        mB +=1
        if mB > 12:
            yB += 1

# 3- Series
print('Hola, este programa calculara una serie de numeros según un patrón')
x = int(input('Ingrese un numero entero\n'))
l = []
while x != 1:
    if x%2 == 0:
        x = x/2
    else:
        x = 3*x+1
    print(x)

# 4 - Mano de poker
import random as rd
tipos = ['Corazones', 'Diamantes', 'Picas', 'Tréboles']
valores = ['As', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
mazo = [] # Mazo general
mano = [] # Mazo del jugador (7 cartas)
trios = [] # Las cartas tríos
num_trios = 0 # numero de tríos
for valor in valores:
    for tipo in tipos:
        mazo.append(f'{valor} de {tipo}') 
rd.shuffle(mazo) #Revolver mazo de 52 cartas
for i in range (7):
    mano.append(mazo.pop()) # Quita y pone 7 cartas de la baraja original al mazo del jugador "mano" (parte 1)
# (parte 2)
for valor in valores: # Para cada carta de 1/4 de baraja
    contador = 0
    for carta in mano: # si el valor de la carta de la baraja coincide con algun valor del 1/4 de baraja, que se sume 1
        if carta.split()[0] == valor:
            contador += 1
    if contador >= 3: # Si hay 3 cartas con un mismo valor, entonces se suma 1 trio
        num_trios += 1
        for carta in mano:
            if carta.split()[0] == valor: # Si hay un trio, entonces recorrera la mano de nuevo y creara un mini mazo con los trios
                trios.append(carta)

print(f'El numero de tríos es de {num_trios}, los cuales son {trios} ')
print(f'Su mazo de 7 cartas fue de \n{mano}')

# 5 - Usuarios 

print('Bienvenido al portal web canvas.udd')
C1 = False
C2 = False
C3 = False
C4 = False
while (C1 and C2 and C3 and C4) == False: # Dejara ingresar al usuario cuando las 4 condiciones sean Verdaderas
    user = input('Ingrese su usuario \n')
    mail = input('ingrese su correo, este no debe coincidir con el nombre del usuario (antes del @) \n')
    clave = input('Ingrese una clave > 8 digitos, con almenos 1n° y ninguno de los sgtes caracteres: $, #, %, &, /  \n')
    numero = [0,1,2,3,4,5,6,7,8,9]
    CaractE = ['$','#','%','&','/']
    C1 = mail.split('@')[0] != user # Si es igual el nombre que el gmail, entonces C1 = falso
    C2 = True == (len(clave) >= 8) # Si el largo de la clave es menor a 8, entonces C2 = falso
    C3 = False
    n = 0
    C4 = True
    for caracter in clave: # Si la clave tiene un digito, C3 cambia de false a true
        if caracter.isdigit() == True:
            n += 1
    if n >= 1:
        C3 = True
    n2 = 0
    for caracter in CaractE: # Si la clava no tiene ningun caracter especial (n2 = 0), entonces n2 = true
        if clave.count(caracter) >= 1:
            n2 += 1
    if n2 != 0:
        C4 = False
print('Ha ingresado exitosamente al canvas.udd') #Cuando se cumplan las 4 condiciones