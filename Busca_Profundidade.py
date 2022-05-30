grafo = {
    'a': ['b', 'd', 'e'],
    'b': ['a', 'c', 'e'],
    'c': ['b', 'e'],
    'd': ['a', 'e'],
    'e': ['a', 'b', 'c', 'd', 'f'],
    'f': ['e']
}

valor_profundidade_entrada = 0 #vertices entram da pilha
valor_profundidade_saida = 0 #vertices saem da pilha
profundidades_entrada_saida = {} #dicionario que gerencia o que entra e sai da pilha
principal = {} #vertice principal que busca os vertices
aresta = {} #arestas conecta no vertice principla
distancia = {} #distancia entre os vertices
proximo = {} #lista o vertice proximo da raiz
demarcadores = set() #demarca o vertice abaixo principal ou ele mesmo
articulacoes = set() #articula um vertice caso ele seja removido do grafo

def busca_em_profundidade(grafo, vertice): #funcão que recebe o grafo e vertice principal
    for vertice in grafo: #Para cada vertice no grafo
        proximo[vertice] = vertice #proximo recebe e o vertice e armazena em uma lista
    principal[vertice] = 0 #inicializa o vertice principal
    raiz = dfs(grafo, vertice, 1) #raiz recebe o grafo e o vertice e um contador
    if raiz <= 1: # se for menor que 1 na raiz
        articulacoes.remove(vertice) #remove o valor do vertice do grafo

def dfs(grafo, vertice, ponto): #função para a recursividade
    global valor_profundidade_entrada, valor_profundidade_saida #declara a entrada e saida com variaveis globais
    valor_profundidade_entrada += 1 # entrada recebe + 1 em um loop recursivo
    profundidades_entrada_saida[vertice] = [valor_profundidade_entrada, 0] # recebe a profundide do grafo
    distancia[vertice] = ponto # recebe o tamanho da distancia entre o vertices
 
    count_vertices = 0 #instancia os vertices

    for vizinho in grafo.get(vertice): #verifica quais são os vizinhos do vertice
        if not profundidades_entrada_saida.get(vizinho): #se não tiver o vertice na profundidade cai no else
            principal[vizinho] = vertice #principal recebe o vizinho
            count_vertices += 1 #conta quantidade de vertices
            dfs(grafo, vizinho, ponto + 1) # chama a função dfs()
            if distancia[proximo[vizinho]] < distancia[proximo[vertice]]: #verifica a distancia se é maior que o vertice 
                proximo[vertice] = proximo[vizinho] #passa pro proximo vertice
            elif vizinho in demarcadores: #verificar se o vizinho esta no demarcador
                articulacoes.add(vertice) #add o vertices na articulação
        else: 
            if not profundidades_entrada_saida[vizinho][1]: #verificação do vizinho 
                if principal[vertice] != vizinho: # verifica se o vertices principal esta diferente do vizinho
                    aresta[(vertice, vizinho)] = 'Vertices' #arestas que liga o vizinho 
                    print(aresta) #imprime a ligação do vertice principal

    valor_profundidade_saida += 1 #rebece um contador na saida da profundidade
    profundidades_entrada_saida[vertice][1] = valor_profundidade_saida # saida recebe os parametros de saida
    if proximo[vertice] in (vertice, principal[vertice]): #verifica se o vertice é ligado com o principal
        demarcadores.add(vertice) #add um vertice do demarcador
    return count_vertices #retorna a quantidade de vertices

busca_em_profundidade(grafo, 'e') #chama o grafo e o vertice