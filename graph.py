import networkx as nx
import matplotlib.pyplot as plt
import csv
import datetime

class Graph:
    def __init__(self):
       self.graph = nx.Graph()
       self.propNodes = None
       self.adjacentMatrix = []
       self.searchStartTime = 0
       self.searchEndTime = 0
    def loadAdjacentMatrix(self, graphFile):
        with open(graphFile) as csvFile:
            read = csv.reader(csvFile, delimiter=',', quotechar='|',)
            result = []
            for nodeNeighboor in read:
                resultItem = []
                for item in nodeNeighboor:
                    if item != '':
                        resultItem.append(int(item))
                result.append(resultItem)
            self.adjacentMatrix = result
        self.loadGraph()
    def loadGraph(self):
        edges = []
        i=0
        for vertex in self.adjacentMatrix:
            for nodeNeighboor in vertex:
                edge = (i, nodeNeighboor, )
                edges.append(edge)
            
            #print(vertex)
            i+=1
        print(edges)
        self.graph = nx.Graph(edges)

    def getAdjacentMatrix(self):
        return self.adjacentMatrix

    def showGraph(self, title ,graph):
        plt.title(title)
        nx.draw_shell(graph, nlist=[range(5, 10), range(5)], with_labels=True, font_weight='bold')
        plt.show()

class Dfs(Graph): #Classe para a busca em profundidade
  def __init__(self, grafo):
    self.loadAdjacentMatrix(grafo)
    self.resultGraph = nx.Graph()
    self.ordem = [] #Ordem do processamento
    self.tempo = 0
    self.startTime = None
    self.endTime = None

    grafoComPropriedades = [] #Array com os vértices com propriedades
    verticeNumber=0 #Numero do vértice inicial
    for u in self.adjacentMatrix: #Definição das propriedades de cada vértice
      vertice = {str(verticeNumber): u, 'visitado': False, 'pai': None, 'prenumb': 0, 'postnumb': 0} #Preenchimento do grafo alterado para uso no código
      verticeNumber+=1
      grafoComPropriedades.append(vertice) #Vértice salvo no array do grafo

    self.propNodes = grafoComPropriedades

  def explore(self, u): #Método de exploração
    self.tempo += 1 #Salvo o tempo do inicio do processo
    u['prenumb'] = self.tempo #Tempo antes do processamento
    u['visitado'] = True #Marcado como visitado
    verticeNumber = str(self.propNodes.index(u)) #Pega o numero/nome do vértice
    self.ordem.append(verticeNumber)
    for v in u[verticeNumber]: #Para cada um dos vizinhos do vértice
      verticeVizinho = self.propNodes[v] #Pega o vértice com propriedades
      if not verticeVizinho['visitado']: #Se ainda não foi visitado
        verticeVizinho['pai'] = verticeNumber #Marca o pai do vértice vizinho
        self.explore(verticeVizinho) #Explora o vértice vizinho
    self.tempo += 1 #Salvo tempo pós processo
    u['postnumb'] = self.tempo #Tempo depois do processamento

  def teste(self):
      print(self.propNodes)

  def createResultGraph(self):
      vertexs = list(range(0, len(self.adjacentMatrix)))
      self.resultGraph.add_nodes_from(vertexs)
      edges = []
      for item in self.propNodes:
          if not item['pai']:
              continue
          else:
              vertex = self.propNodes.index(item)
              edge = (int(item['pai']), vertex)
              edges.append(edge)
      self.resultGraph.add_edges_from(edges)

  def timeInSeconds(self):
      startTime = self.startTime.strftime("%M %S")
      startTime = [int(startTime[0:2]), int(startTime[3:5])]
      startTime = ((startTime[0] * 60) + startTime[1])

      endTime = self.endTime.strftime("%M %S")
      endTime = [int(endTime[0:2]), int(endTime[3:5])]
      endTime = (endTime[0] * 60) + endTime[1]

      return str(endTime - startTime) + " Segundos de processamento"
  def busca(self): #Método de busca
    self.startTime = datetime.datetime.now()
    for u in self.propNodes: #Para cada vértice que ainda não foi visitado
      if not u['visitado']:
        self.explore(u) #É explorado
    self.endTime = datetime.datetime.now()

class Bfs(Graph): #Classe para a busca em largura 
    def __init__(self, grafo):
        self.loadAdjacentMatrix(grafo)
        self.resultGraph = nx.Graph()
        self.ordem = [] #Ordem do processamento
        self.startTime = None
        self.endTime = None
        grafoComPropriedades = [] #Array com os vértices com propriedades
        verticeNumber=0 #Numero do vértice inicial
        for u in self.adjacentMatrix: #Definição das propriedades de cada vértice
            vertice = {str(verticeNumber): u, 'visitado': False, 'pai': None, 'distancia': 'infinite'} #Preenchimento do grafo alterado para uso no código
            verticeNumber+=1
            grafoComPropriedades.append(vertice) #Vértice salvo no array do grafo

        self.propNodes = grafoComPropriedades
    
    def timeInSeconds(self):
      startTime = self.startTime.strftime("%M %S")
      startTime = [int(startTime[0:2]), int(startTime[3:5])]
      startTime = ((startTime[0] * 60) + startTime[1])

      endTime = self.endTime.strftime("%M %S")
      endTime = [int(endTime[0:2]), int(endTime[3:5])]
      endTime = (endTime[0] * 60) + endTime[1]

      return str(endTime - startTime) + " Segundos de processamento"

    def createResultGraph(self):
      vertexs = list(range(0, len(self.adjacentMatrix)))
      self.resultGraph.add_nodes_from(vertexs)
      edges = []
      
      for item in self.propNodes:
          if item['pai'] == None:
              continue
          else:
              vertex = self.propNodes.index(item)
              edge = (int(item['pai']), vertex)
              edges.append(edge)

              
      self.resultGraph.add_edges_from(edges)

    def busca(self, raiz=0):
        self.startTime = datetime.datetime.now()
        raiz = self.propNodes[raiz] #Pega a raiz, com o index de seu vértice como parametro de entrada
        raiz['visitado'] = True
        raiz['distancia'] = 0
        Q = [raiz]

        while len(Q) != 0: #Enquanto ter algo em Q
            u = Q.pop(0) #Pega o vértice raiz
            grafoNome = self.propNodes.index(u)
            self.ordem.append(grafoNome)
            for v in u[str(grafoNome)]: #Para cada um de seus vizinhos
                grafoVizinho = self.propNodes[v] #Pega a definição com atributo do vizinho
                if not grafoVizinho['visitado']: #Se ainda não foi visitado
                    grafoVizinho['visitado'] = True #Marcado como visitado
                    grafoVizinho['distancia'] = u['distancia'] + 1 #Marcado a distancia
                    grafoVizinho['pai'] = self.propNodes.index(u) #Definido o indéx do pai

                    Q.append(grafoVizinho) #Próximo da fila para ser processado
        self.endTime = datetime.datetime.now()

while True:
    entrada = int(input('1-Para largura 2-Para profundidade: '))
    if entrada == 1:
        grafo = input('Escolha entre (Graph1.csv) ou (Graph2.csv): ')
        bfs = Bfs(grafo)
        raiz = int(input('Escolha a raiz (Numero de 0 até 24): '))
        bfs.busca(raiz)
        bfs.createResultGraph()
        while True:
            entrada = int(input('1-Para visualizar o grafo antes da busca, 2-Para visualizar grafo pós busca, 3-Para visualizar tempo de processamento, 4-Para visualizar a ordem: '))
            if entrada == 1:
                bfs.showGraph('Antes da busca em largura', bfs.graph)
            elif entrada == 2:
                bfs.showGraph('Depois da busca em largura', bfs.resultGraph)
            elif entrada == 3:
                print(bfs.timeInSeconds())
            elif entrada == 4:
                print(bfs.ordem)
            else: 
                break
    elif entrada == 2:
        grafo = input('Escolha entre (Graph1.csv) ou (Graph2.csv): ')
        dfs = Dfs(grafo)
        dfs.busca()
        dfs.createResultGraph()
        while True:
            entrada = int(input('1-Para visualizar o grafo antes da busca, 2-Para visualizar grafo pós busca, 3-Para visualizar tempo de processamento, 4-Para visualizar a ordem: '))
            if entrada == 1:
                dfs.showGraph('Antes da busca em profundidade', dfs.graph)
            elif entrada == 2:
                dfs.showGraph('Depois da busca em profundidade', dfs.resultGraph)
            elif entrada == 3:
                print(dfs.timeInSeconds())
            elif entrada == 4:
                print(dfs.ordem)
            else: 
                break
    else:
        break