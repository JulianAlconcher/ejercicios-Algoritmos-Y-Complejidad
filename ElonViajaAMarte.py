import sys
import math

input = sys.stdin.readline

#-----------------------Functions-----------------------


# Takes user input and returns the input as an integer.
def inp() :
    return(int(input()))

# Converts space-separated user input into a list of integers.
# Return a list of integers parsed from the user input.
def inlt() :
    return(list(map(int,input().split())))


#---------------------------------------------------------
casosDePrueba = inp()

   
def esSolucion(S,W):
    if(len(S) == 0):
        return False
    return (sum(S) <= W) and (sum(S) >= math.ceil(W/2))

def esViable(S, x, W):
    return sum(S) + x <= W


resultados = []

for _ in range(casosDePrueba):
    n, W = inlt()
    paquetes = inlt()
    S = []
    indices_seleccionados = []  
    i = 1
    while i <= len(paquetes):
        x = paquetes[i-1]
        if esViable(S, x, W):
            S.append(x)
            indices_seleccionados.append(i)  
        i += 1
    
    if esSolucion(S, W):
        resultados.append((len(indices_seleccionados), indices_seleccionados))
    else:
        resultados.append("-1")

for resultado in resultados:
    if resultado == "-1":
        print(resultado)
    else:
        print(resultado[0])
        for indice in resultado[1]:
            print(indice, end=' ')
        print()


