grafo = [ [(2, 3), (3, 2)],           # Vizinhos do vértice 0.
          [(1, 10)],        # Vizinhos do vértice 1.
          [(1, 12), (4, 4)],        # Vizinhos do vértice 2.
          [(1, 9)],           # Vizinhos do vértice 3.
          [(1, 8), (5, 2)],            # Vizinhos do vértice 4.
          [(5, 1), (6, 1)],
          [(7, 5)],
          [(6, 5)]
        ]

# a = 0
# b = 1
# c = 2
# d = 3
# e = 4
# x = 5
grafoAula = [
    [(2, 6), (5, 3)],
    [(5, 8), (3, 2)],
    [(0, 6), (5, 4), (3, 1), (4, 3)],
    [(1, 2), (2, 1), (4, 1)],
    [(2, 3), (5, 10), (3, 1)],
    [(0, 3), (2, 4), (4, 10), (1, 8)]
]

def remove_min(Q):
    i=0


def dijkstra(grafo, s):
    grafoComPropriedades = [] #Definição de grafo com o vértice com atributos: vizinhos, visitado, pai e distancia
    for u in grafo:
        vertice = {str(grafo.index(u)): u, 'visitado': False, 'pai': [], 'distancia': 9999999999999999} #Preenchimento do grafo alterado para uso no código
        grafoComPropriedades.append(vertice)
    
    ordem = []
    raiz = grafoComPropriedades[s]
    raiz['distancia'] = 0
    S = []
    Q = [raiz]
    while len(Q) != 0:
        u = Q.pop()
        ordem.append(u)
        S.append(u)
        uVertexName = str(grafoComPropriedades.index(u))
        for v in u[uVertexName]:
            vertexV = grafoComPropriedades[v[0]]
            if vertexV['distancia'] > u['distancia'] + v[1]:
                vertexV['distancia'] = u['distancia'] + v[1]
                vertexV['pai'] = uVertexName
                Q.append(vertexV)

    return grafoComPropriedades, S, ordem


grafoPropriedades, S, ordem = dijkstra(grafoAula, 5)

for vertice in grafoPropriedades:
    print(vertice)

print('--')
print(S)
print('--')
print(ordem)

for vertice in S:
    print('--')
    print('vertice: ' + str(grafoPropriedades.index(vertice)))
    print('distancia: ' + str(vertice['distancia']))
    print('pai: ' + str(vertice['pai']))
    print('--')