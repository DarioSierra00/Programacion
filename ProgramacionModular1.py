#Ejercicio1
from random import randint

lista=[]

for i in range(10):
    lista.append(randint(0,1000))
    
def obtenerMayor(lista):
    mayor = lista[0]

    for i in range(len(lista)):
        if lista[i] > mayor:
            mayor = lista[i]

    return mayor

def obtenerMenor(lista):
    menor = lista[0]
    
    for i in range(len(lista)):
        if lista[i] < menor:
            menor = lista[i]
            
    return menor

def obtenerSuma(lista):
    suma = 0
    
    for lista in lista:
        suma+=lista
    
    return suma

def obtenerMedia(lista):
    suma = 0
    cont = 0
    
    for media in lista:
        suma+=media
        cont+=1
    media = suma/cont
        
    return media   

elemento_a_reemplazar = int(input("Que posición quieres sustituir: "))
elemento_sustituto = int(input("Por cual quieres sustituir: "))
while elemento_a_reemplazar < 0:
    elemento_a_reemplazar = int(input("Que posición quieres sustituir: "))
def sustituir_valor(lista, elemento_a_reemplazar, elemento_sustituto):
    
    for i in range(len(lista)):
        if elemento_a_reemplazar == elemento_sustituto[i]:
            lista[i]=elemento_sustituto
    return lista

print(sustituir_valor(lista))

print(lista)

print(f"El mayor es {obtenerMayor(lista)}")
print(f"El menor es {obtenerMenor(lista)}")
print(f"La suma es {obtenerSuma(lista)}")
print(f"La media es {obtenerMedia(lista)}")
print(f"La media es {sustituir_valor(lista)}")
print(lista)









"""
#Ejercicio2     if i<9:
            mensaje=mensaje+str(i)+","
Realiza un programa que lea 10 números, los imprima separados por coma y a
continuación los desplace una posición (y los muestre por pantalla desplazados), de
tal forma que el último pase a la primera posición, el primero a la segunda, el
segundo a la tercera, y así sucesivamente.
Opcional: Añade un parámetro (D/I) a la función para que el controle el sentido del
desplazamiento (a derechas/izquierdas) y otro que indique el número de posiciones
a desplazar (0: quedaría igual, 1: desplaza una posición, etc.).


lista=[0,1,2,3,4,5,6,7,8,9]

lista.insert(0, lista[-1])
lista .pop(-1)
print(lista)


lista=[1, 3, 5, 7]

def desplazar_posicion_derecha(lista):
    a_borrar, a_escribir = 0, lista[0]
    for i in range(len(lista)):
        a_borrar = lista[(i+1)%len(lista)]
        lista[(i+1)%len(lista)]=a_escribir
        a_escribir=a_borrar
        
    return lista
        
print(desplazar_posicion_derecha(lista))


mes[]

dia = int(input("Introduce el dia: "))
mes = int(input("Introduzca el mes: "))
año = int(input("Introduzca el año: "))

while dia<1 or dia>31:
    dia = int(input("Introduce el dia: "))
    
while mes<1 or mes>12:
    mes = int(input("Introduzca el mes: "))
    
"""
