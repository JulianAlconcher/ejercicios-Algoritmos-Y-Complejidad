import sys
import math
from collections import defaultdict, deque

if __name__ == "__main__":
    # n = cantidad de vertices
    # m = cantidad de gatos soportados consecutivos
    n, m = map(int, input().split())

    # vertices = lista de vertices (1 si tiene gato, 0 sino)
    vertices = [int(x) for x in input().split()]

    # arcs = lista de arcos
    arcos = []
    for _ in range(n-1):
        x, y = map(int, input().split())
        arcos.append((x, y))
    
    adj = [[] for _ in range(n + 1)]
    idx = 0
    for i in range(n - 1):
        u = int(vertices[idx])
        idx += 1
        v = int(vertices[idx])
        idx += 1
        
        adj[u].append(v)
        adj[v].append(u)
        
    vis = [False] * (n + 1)
    total = 0
    
