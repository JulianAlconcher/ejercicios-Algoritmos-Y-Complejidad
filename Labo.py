def recorrido_dfs(grafo):
    pila = [(1, vertices[0])]
    caminos = []
    vistados = set()
    
    while pila:
        nodo_actual, gatos_consecutivos = pila.pop()
        if nodo_actual in vistados:
            continue
        vistados.add(nodo_actual)
 
        esRestaurant = True
        
        for nodo_siguiente in grafo[nodo_actual]:
            if nodo_siguiente not in vistados:
                esRestaurant = False
                if vertices[nodo_siguiente - 1] == 1:
                    nuevos_gatos_consecutivos = gatos_consecutivos + 1
                else:
                    nuevos_gatos_consecutivos = 0
                
                if nuevos_gatos_consecutivos <= m:
                    pila.append((nodo_siguiente, nuevos_gatos_consecutivos))
 
        if esRestaurant:
            if gatos_consecutivos <= m:
                caminos.append((nodo_actual, gatos_consecutivos))
 
    return caminos
 
if __name__ == "__main__":
    n, m = map(int, input().split())
    vertices = list(map(int, input().split()))
    grafo = {}
    
    for x in range(1, n + 1):
        grafo[x] = []
    
    for _ in range(n - 1):
        a, b = map(int, input().split())
        grafo[a].append(b)
        grafo[b].append(a)
        
    caminos = recorrido_dfs(grafo)
    cantidad = len(caminos)
    
    print(cantidad)