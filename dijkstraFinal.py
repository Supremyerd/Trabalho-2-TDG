# Importação das bibliotecas
import networkx as nx
import matplotlib.pyplot as plt
import csv
import datetime
import timeit


class Graph:
    def __init__(self, hasWeight=False):  # função principal que recebe as variaveis
        self.graph = nx.Graph()  # Grafo importado do networkx
        self.propNodes = None  # Variavel para verificação se o vetice foi visitado
        self.hasWeight = hasWeight
        # Entradas da matriz varia de acordo com as propriedades do grafo
        self.adjacentMatrix = []
        # Atributo com o proposito de começar a contar o tempo de busca
        self.searchStartTime = 0
        self.searchEndTime = 0  # Atributo com o proposito de finalizar o tempo de busca

    def loadAdjacentMatrix(self, graphFile):  # função que carregar o arquivo csv
        with open(graphFile) as csvFile:  # Reconhece o arquivo como csv
            read = csv.reader(  # read variavel para ler os delimitar com , e separação de colunas
                csvFile,  # arquivo CSV
                delimiter=',',  # Delimitador com ,
                quotechar='|',  # separação de colunas
            )
            result = []
            for nodeNeighboor in read:  # leitura se ele é vizinho
                resultItem = []  # Declaração de resultItem como lista
                for item in nodeNeighboor:  # verificação se há vizinho
                    if item != '':  # se item for diferente de nulo
                        if self.hasWeight:  # Alteração para salvar propriedade de peso na aresta
                            edge = item.split('x')
                            print(edge)
                            v = edge[0]
                            w = edge[1]
                            neighboor = (int(v), int(w),)
                            resultItem.append(neighboor)
                        else:
                            print(item)
                            # armazena o numero de itens no resultado
                            resultItem.append(int(item))
                # o numero de itens passa para o resultado
                result.append(resultItem)
            self.adjacentMatrix = result  # matriz de adjacencia ira receber o itens no resultado
            # print(self.adjacentMatrix)
        self.loadGraph()  # carrega o grafo

    def loadGraph(self):
        if self.hasWeight:
          #Salvar o grafo networkx usando o peso das arestas
            edges = []
            i = 0
            for vertex in self.adjacentMatrix:
                for nodeNeighboor in vertex:
                    v = nodeNeighboor[0]
                    w = nodeNeighboor[1]
                    edge = (i, v, {'weight': w})
                    edges.append(edge)
                i += 1
            self.graph = nx.Graph(edges)

        else:
            edges = []  # Declaração de edges como lista
            i = 0
            for vertex in self.adjacentMatrix:  # verificação se o vertice esta na matriz de adjacencia
                for nodeNeighboor in vertex:  # verifica se o vertice é vizinho
                    edge = (
                        i,
                        nodeNeighboor,
                    )  # egde recebe o (i,vertico vizinho)
                    edges.append(edge)  # edges recebe edge

                # print(vertex)
                i += 1
            self.graph = nx.Graph(edges)
            # Grafo importado do networkx como parametro no edges

    def getAdjacentMatrix(self):  # função que retorna a matriz adjacente
        return self.adjacentMatrix  # retorna a matriz de adjacencia

    def showGraph(self, title, graph):  # Metodo de amostra do grafo
        if self.hasWeight:
            plt.title(title)
            pos = nx.spring_layout(graph)
            nx.draw_networkx(graph, pos, with_labels=True)
            labels = nx.get_edge_attributes(graph, 'weight')
            nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
            plt.show()
        else:
            plt.title(title)  # instacia que representa o titulo
            pos = nx.spring_layout(graph)
            nx.draw_networkx(graph, pos, with_labels=True)
            plt.show()  # monstra atraves do matplotlib


class Dijkstra(Graph):
    def __init__(self, grafo, hasWeight):
        super().__init__(hasWeight=hasWeight)
        self.loadAdjacentMatrix(grafo)  # Carrega o grafo
        self.resultGraph = nx.Graph()  # Resultado do grafo
        self.ordem = []  # Ordem do processamento
        self.startTime = None  # Atributo com o proposito de começar a contar o tempo de busca
        self.endTime = None  # Atributo com o proposito de finalizar o tempo de busca
        self.S = [] #Atributo de lista de prioridades minimas
        grafoComPropriedades = []  # Array com os vértices com propriedades
        verticeNumber = 0  # Numero do vértice inicial
        for u in self.adjacentMatrix:  # Definição das propriedades de cada vértice
            vertice = {
                str(verticeNumber): u,
                'visitado': False,
                'pai': None,
                'distancia': 9999999999999999
            }  # Preenchimento do grafo alterado para uso no código
            verticeNumber += 1  # contador
            grafoComPropriedades.append(
                vertice)  # Vértice salvo no array do grafo

        # PropNodes recebe o proximo vertice na fila
        self.propNodes = grafoComPropriedades

    def showTime(self):  # Metodo de contagem de tempo

        return str(self.endTime - self.startTime) + " Segundos de processamento"

    def createResultGraph(self):  # Metodo pro resultado
        # contagem de vetices no grafo
        vertexs = list(range(0, len(self.adjacentMatrix)))
        # Resultado que armazena os vertices
        self.resultGraph.add_nodes_from(vertexs)
        edges = []  # Declaração de edges como lista

        for item in self.propNodes:  # Verica qual dos vertices esta no grafo
            if item['pai'] == None:  # Se tem ligação com o pai
                continue
            else:  # se não
                # Definido o indéx dos visitados
                vertex = self.propNodes.index(item)
                edge = (int(item['pai']), vertex,{'weight': item['distancia']})  # Definido o indéx do pai
                edges.append(edge)  # edges recebe o proximo da fila

        # parametro edges passado pro resultado
        self.resultGraph.add_edges_from(edges)

    def busca(self, raiz=0):  # Método de busca
        self.startTime = timeit.default_timer()  # define o tempo inicial da busca
        # Pega a raiz, com o index de seu vértice como parametro de entrada
        raiz = self.propNodes[raiz]
        # inicializa a raiz que contem vertice que foi vizitado
        raiz['visitado'] = True
        raiz['distancia'] = 0  # inicializa a distancia da raiz
        Q = [raiz]  # Q recebe o numero contido na raiz
        
        while len(Q) != 0:
            u = Q.pop()  # Pega o ultimo da lista de busca
            existe = False
            for s in self.S:
                if s == u:
                    existe = True  # Verifica se o vértice ja foi salvo

            if not existe:  # Se não ter sido salvo
                self.S.append(u)  # Salva na lista de prioridades minimas
            # Extrai o numero do vértice
            uVertexName = str(self.propNodes.index(u))
            for v in u[uVertexName]:  # para cada um dos vizinhos
                # propriedade do vértice vizinho
                vertexV = self.propNodes[v[0]]
                # Se a distancia for maior que a distancia do pai + peso
                if vertexV['distancia'] > u['distancia'] + v[1]:
                    vertexV['distancia'] = u['distancia'] + \
                        v[1]  # definição da distancia
                    vertexV['pai'] = uVertexName  # Definição do pai
                    Q.append(vertexV)  # Salvando na lista de busca
            self.endTime = timeit.default_timer()  # define o tempo final da busca


while True: #Menu para escolher grafo
    grafoNome = input('Entre com nome do grafo: ')
    grafo = Dijkstra(grafoNome + '.csv', True) #Carrega grafo pelo nome
    grafo.busca() #Realiza a busca com algoritmo de dijkstra
    grafo.showGraph('Antes da busca ' + grafoNome, grafo.graph) #Exibe o grafo antes da busca
    grafo.createResultGraph() #Cria o grafo depois da busca
    grafo.showGraph('Depois da busca '+ grafoNome, grafo.resultGraph) #Exibe o grafo pós busca
    print(grafo.showTime()) #Exibe o tempo de busca