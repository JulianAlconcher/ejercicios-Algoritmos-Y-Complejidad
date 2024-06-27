import sys
import math

input = sys.stdin.readline

casosDePrueba = int(input())

def esSolucion(suma_total,W):
    return (suma_total <= W) and (suma_total >= math.ceil(W/2))

def esViable(suma_total, x, W):
    return suma_total + x <= W

def estaEnRango(x, W):
    return (math.ceil(W/2) <= x) and (x <= W)

resultados = []

for _ in range(casosDePrueba):
    n, W = map(int, input().split())
    paquetes = list(map(int,input().split()))
    indices_seleccionados = []  
    suma_total = 0
    for i in range(n):
        x = paquetes[i]
        if estaEnRango(x, W):
            suma_total = x
            indices_seleccionados = [i+1] 
            break
        else:
            if esViable(suma_total, x, W):
                indices_seleccionados.append(i+1)  
                suma_total += x
    
    if esSolucion(suma_total, W):
        print(len(indices_seleccionados))
        print(*indices_seleccionados)
    else:
        print("-1")




