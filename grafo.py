grafo = [ [1],           # Vizinhos do vértice 0.
          [2, 3],        # Vizinhos do vértice 1.
          [1, 4],        # Vizinhos do vértice 2.
          [0],           # Vizinhos do vértice 3.
          [1]            # Vizinhos do vértice 4.
        ]

def bfs(grafo=[[]], s=0):
    grafoAlterado = [] #Definição de grafo com o vértice com atributos: vizinhos, visitado, pai e distancia
    for u in grafo:
        vertice = {'vizinhos': u, 'visitado': False, 'pai': [], 'distancia': 'infinite'} #Preenchimento do grafo alterado para uso no código
        grafoAlterado.append(vertice)
    
    raiz = grafoAlterado[s] #Pega a raiz, com o index de seu vértice como parametro de entrada
    raiz['visitado'] = True
    raiz['distancia'] = 0
    Q = [raiz]

    while len(Q) != 0: #Enquanto ter algo em Q
        u = Q.pop(0) #Pega o vértice raiz
        #print(u)
        for v in u['vizinhos']: #Para cada um de seus vizinhos
            grafoVizinho = grafoAlterado[v] #Pega a definição com atributo do vizinho
            if not grafoVizinho['visitado']: #Se ainda não foi visitado
                grafoVizinho['visitado'] = True #Marcado como visitado
                grafoVizinho['distancia'] = u['distancia'] + 1 #Marcado a distancia
                grafoVizinho['pai'].append(grafoAlterado.index(u)) #Definido o indéx do pai

                Q.append(grafoVizinho) #Próximo da fila para ser processado

    return grafoAlterado #Retorna o grafo com os vértices com a definição de vizinhos originais, pais e distancia
    
raiz = 0
busca = bfs(grafo, raiz)

for vertice in busca:
    print(vertice)
