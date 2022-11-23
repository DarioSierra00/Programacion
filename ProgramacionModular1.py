"""

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



#Ejercicio2

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

dias=[0, 31,28,31,30,31,30,31,31,30,31,30,31]
meses=["0", "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
dia, mes, año = 1, 0 ,0

 
while dia > 0:
    dia = int(input("Introduce el dia: "))
    mes = int(input("Introduzca el mes: ")) 
    año = int(input("Introduzca el año: "))
    
    while mes<1 or mes>12:
        mes = int(input("Introduzca el mes: "))
        
    if (año%4 == 0) and (año%100 != 0) or (año%400 == 0):
        dias[2]=29
        
    while dia > dias[mes]:
        dia = int(input("Introduce el dia: "))
        
    print(f"Hoy es {dia} de {meses[mes]} de {año}")
    dia = int(input("Introduce el dia: "))

print("Terminó")


#Ejercicio4

lista = []


numero = 1

def obtenerMayor(lista):
    mayor = lista[0]

    for i in range(len(lista)):
        if lista[i] > mayor:
            mayor = lista[i]

    return mayor

def obtenerPar(lista):
    par = []
    for i in range(len(lista)):
        if lista[i]%2==0:
            par+=[lista[i]]
            
    return par

while numero > 0:
    lista+=[numero]
    numero = int(input("Introduce números: "))
    

print(lista)
print(f"El mayor es {obtenerMayor(lista)}")
print(f"Estos son los numeros pares {obtenerPar(lista)}")


#Ejercicio 5

lista = ["Di", "buen", "día", "a", "papa"]

def reverse(lista):
    revertido = []
    for i in lista:
        revertido=[i]+revertido
        
    return revertido
    
print(reverse(lista))


#Ejercicio 6

lista = [0,2,3,5,6]

def estaOrdenada(lista):
    resultado = True

    for i in range(1,len(lista)):
        if lista[i] < lista[i-1]:
            resultado = False
    return resultado

print(estaOrdenada(lista))
     

#Ejercicio 7

domino1 = [3,4]
domino2 = [3,5]

# def es_valida(domino1):
#     resultado = False
#     if domino1[1] in "0123456" and domino1[3] in "0123456":
#         resultado = True
#     if domino2[1] in "0123456" and domino2[3] in "0123456":
#         resultado = True
#     return resultado

def encajan(domino1,domino2):
    resultado = False
    for i in domino1:
        if i==domino2[0] or i==domino2[1]:
            resultado = True
        
    return resultado

# print(es_valida(domino1))
print(encajan(domino1, domino2))


#Ejercicio8

lista = []

vacia = []

enteros = int(input("Introduce numeros positivos: "))
lista.append(enteros)

while enteros>0:
    enteros = int(input("Introduce numeros positivos: "))
    if enteros>0:
        lista.append(enteros)

print(lista)

def es_primo(lista):
    for i in lista:
        if lista[i] > 2:
            if lista[i]%i!=0:
                vacia.append[i]
                
    return lista

print(es_primo(lista))


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

def factorial(lista):
    factorial = 0
    for i in lista:
        lista[i]+=factorial
        factorial*


print(f"La suma total es {(obtenerSuma(lista))}")
print(f"La media de todo es de {obtenerMedia(lista)}")

#Ejercicio 9

lista = []

entero = 8
numero = 1


while numero > 0: 
    numero = int(input("Introduce números: "))
    
    lista.append(numero)

def menores(lista):
    menor = []
    entero = 8
    for i in range(len(lista)):
        if lista[i] < entero:
            menor.append(lista)


def obtenerMayor(lista):
    mayor = []

    for i in range(len(lista)):  # Esto recorre la lista leyendola y si la posicion de i en la lista es mayor que la variable entero, la posicion de lista i, se añade a la lista mayor.
        if lista[i] > entero:
            mayor.append(lista[i])

    return mayor

def obtenerMultiplo(lista):
    multiplo = []
    for i in range(len(lista)):
        if lista[i]%entero==0:
            multiplo.append(lista[i])
            
    return multiplo
            


print(lista)
print(menores(lista))
print(obtenerMayor(lista))
print(obtenerMultiplo(lista))


#Ejercicio 10

def conversorBinarioDecimal(n):
    numero_decimal = 0
    posicion=len(numero)-1

    for i in numero:
        numero=int(i)
        numero_decimal+=numero*2**posicion
        posicion -= 1

    return numero_decimal

def conversorDecimalBinario(n):
    numeroBinario=0
    posicion=1
    n=int(n)
    while n!=0:
        numeroBinario=numeroBinario+n%2*posicion
        n//=2
        posicion*=10
    return numeroBinario

n=input("Introduce un número en binario o decimal acabado por D/B:").upper()

acceso=False
if n[len(n)-1:len(n)]=="B":
    while acceso==False:
        cambio=str(n[:-1])
        for i in range(len(cambio)):
            if cambio[i]=="0" or cambio[i]=="1":
                acceso=True
            else:
                acceso=False
               
        if acceso==False:
            n=input("Error.Introduce el formato correcto:")
           
    print(conversorBinarioDecimal(n))

elif n[len(n)-1:len(n)]=="D":
    n=int(n[:-1])
    while n<0:
        n=input("Error.El formato debe estar en positivivo.Inténtelo de nuevo:")
print(conversorDecimalBinario(n))


#Ejercicio 11
lista1 = [1,4,"curro",8]
lista2 = [2,"curro",8,8]
devolucion = []

def comunes(lista1,lista2):
    for i in range(len(lista1)):
        for j in range(len(lista2)):
            if lista1[i]==lista2[j]:
                if lista1[i] not in devolucion:
                    devolucion.append(lista1[i])
            
            
    return devolucion

print(comunes(lista1, lista2))


#Ejercicio 12

lista1 = [10,1,20,3]
lista2 = [1,2,3,4,5]

def unionListas(lista1,lista2):
    union = lista1 + lista2
    resultado = []
    for i in union:
        if i not in resultado:
            resultado.append(i)
    return resultado


print(unionListas(lista1, lista2))


#Ejercicio 13

lista = ["Dario","Sergio","Curro","David"]
letra = "D"

def devolverNombre(lista):
    curro = []
    for i in lista:
        if i[0]==letra:
            curro.append(i)

    return curro

print(devolverNombre(lista))

#Ejercicio 14

lista=["Hola","hey","curro", "heyheyhey"]

def obtener_Cadena_Mayor(lista):
    letra=0
    valor=""
    comparador=[]
    rep=0
   
    for i in lista:
        caracter=len(i)
        if caracter>letra:
            letra=caracter
            valor=i
           
    for j in lista:
        if len(valor)==len(j):
            comparador.append(j)
           
    for n in comparador:
        repetido=0
        for x in range(len(n)):
            for z in range(1,len(n)):
                if n[x]==n[z]:
                    repetido+=1
        if repetido>rep:
            rep=repetido
            palabra=n
    return palabra

print(obtener_Cadena_Mayor(lista))


# def calcular_letras_distintas(palabra):
#     letras_distintas = ""
#     for letra in palabra:
#         if letra not in letras_distintas:
#             letras_distintas+=letras
#
# def obtener_Cadena_Mayor(cad1, cad2):
#     mayor = ""
#     if len(cad1)>len(cad2):
#         mayor = cad1
#     elif len(cad1)<len(cad2):
#
#     else:
#
"""
