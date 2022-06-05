grafo = [ [2, 3],           # Vizinhos do vértice 0.
          [1],        # Vizinhos do vértice 1.
          [1, 4],        # Vizinhos do vértice 2.
          [-1],           # Vizinhos do vértice 3.
          [1, 5],            # Vizinhos do vértice 4.
          [5, 6],
          [7],
          [6]
        ]
grafo2 = [
         [1, 4],
         [0, 2, 3, 4],
         [1, 3, 4],
         [1, 2, 4],
         [0, 1, 2, 3]
]
class dfs: #Classe para a busca em profundidade
  def __init__(self, grafo):
    self.grafo = grafo #Inicialização do grafo
    self.tempo = 0 #Inicilização do tempo de processamento

  def explore(self, u): #Método de exploração
    self.tempo += 1 #Salvo o tempo do inicio do processo
    u['prenumb'] = self.tempo #Tempo antes do processamento
    u['visitado'] = True #Marcado como visitado
    verticeNumber = str(self.grafo.index(u)) #Pega o numero/nome do vértice
    for v in u[verticeNumber]: #Para cada um dos vizinhos do vértice
      verticeVizinho = self.grafo[v] #Pega o vértice com propriedades
      if not verticeVizinho['visitado']: #Se ainda não foi visitado
        verticeVizinho['pai'] = verticeNumber #Marca o pai do vértice vizinho
        self.explore(verticeVizinho) #Explora o vértice vizinho
    self.tempo += 1 #Salvo tempo pós processo
    u['postnumb'] = self.tempo #Tempo depois do processamento

  def busca(self): #Método de busca
    grafoComPropriedades = [] #Array com os vértices com propriedades
    verticeNumber=0 #Numero do vértice inicial
    for u in self.grafo: #Definição das propriedades de cada vértice
      vertice = {str(verticeNumber): u, 'visitado': False, 'pai': None, 'prenumb': 0, 'postnumb': 0} #Preenchimento do grafo alterado para uso no código
      verticeNumber+=1
      grafoComPropriedades.append(vertice) #Vértice salvo no array do grafo

    self.grafo = grafoComPropriedades #Atualiza propriedades do grafo
    for u in self.grafo: #Para cada vértice que ainda não foi visitado
      if not u['visitado']:
        self.explore(u) #É explorado


busca = dfs(grafo) #Instanciamento

busca.busca() #Realização da busca

for u in busca.grafo: #Exibindo o resultaod final
  print('-------')
  print(u)
  print('-------')
