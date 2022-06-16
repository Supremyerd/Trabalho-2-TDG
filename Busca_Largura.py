g = {'a': ['b', 'd', 'e'], 'b': ['a', 'c', 'e'],'c': ['b', 'a'], 'd': ['a', 'f'], 'e': ['a', 'b', 'c', 'd', 'f'], 'f': ['e','a','c','e']} # Entrada do grafo

def bfs(g, V): # g de grafo e V os vertces
    Q = [] # Q Representa a fila da busca
    distancia = {} # Dicionario da distancia entre os vertices
    visitado = {} # Dicionario que ira verificar se o vertice ja foi visitado
    contador = 1 # Inicialização do contador
    
    Q.append(V) # Acrescenta o vertice na fila da lista Q
    distancia[V] = contador # Distancia recebe os vertices do grafo e o contador
    visitado[V] = 1 # Recebe o vertice e visitado é inicializado
    
    while len(Q): #Enquanto ter algum numero na fila em Q
        vertice = Q.pop(0) # Desenfilera o vertice 
        for proximo in g.get(vertice): #Loop pra cada um dos vertices proximos
            if not distancia.get(proximo): # Verifica se a distancia do proximo vertice ja foi executada
                Q.append(proximo) # Enfilera o vertice
                distancia[proximo] = contador # Marca distancia do proximo
                visitado[proximo] = visitado[vertice] # Inclui vetices visitados nos proximos
                contador += 1 # Acrestenta +1 contador no loop do while
            print('Grau de %s contem %s, distancia' %(str(vertice), str(proximo)) , distancia) # imprime o vertice e o apontamento e a distancia entre eles

    return distancia, visitado # retorna a distancia e o vertices visitados

distancia,visitado = bfs(g, 'a') # Puxa a função e o grafo e o vertice a ser mostrado
