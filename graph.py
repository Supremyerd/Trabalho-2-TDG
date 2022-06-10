# Importação das bibliotecas
import networkx as nx
import matplotlib.pyplot as plt
import csv
import datetime


class Graph:
    def __init__(self):  # função principal que recebe as variaveis
        self.graph = nx.Graph()  # Grafo importado do networkx
        self.propNodes = None  # Variavel para verificação se o vetice foi visitado
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
                        # armazena o numero de itens no resultado
                        resultItem.append(int(item))
                # o numero de itens passa para o resultado
                result.append(resultItem)
            self.adjacentMatrix = result  # matriz de adjacencia ira receber o itens no resultado
        self.loadGraph()  # carrega o grafo

    def loadGraph(self):
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
        print(edges)  # imprime as bordas
        # Grafo importado do networkx como parametro no edges
        self.graph = nx.Graph(edges)

    def getAdjacentMatrix(self):  # função que recebe a matriz adjacente
        return self.adjacentMatrix  # retorna a matriz de adjacencia

    def showGraph(self, title, graph):  # Metodo de amostra do grafo
        plt.title(title)  # instacia que representa o titulo
        nx.draw_shell(graph,
                      nlist=[range(5, 50), range(30)],
                      with_labels=True,
                      font_weight='bold')  # desenha o grafo
        plt.show()  # monstra atraves do matplotlib


class Dfs(Graph):  # Classe para a busca em profundidade
    def __init__(self, grafo):
        self.loadAdjacentMatrix(grafo)  # puxa o csv contido na Load
        self.resultGraph = nx.Graph()  # Grafo importado do networkx passado pro resultado
        self.ordem = []  # Ordem do processamento
        self.tempo = 0  # inicialização da variavel tempo
        self.startTime = None  # Atributo com o proposito de começar a contar o tempo de busca
        self.endTime = None  # Atributo com o proposito de finalizar o tempo de busca

        grafoComPropriedades = []  # Array com os vértices com propriedades
        verticeNumber = 0  # Numero do vértice inicial
        for u in self.adjacentMatrix:  # Definição das propriedades de cada vértice
            vertice = {
                str(verticeNumber): u,
                'visitado': False,
                'pai': None,
                'prenumb': 0,
                'postnumb': 0
            }  # Preenchimento do grafo alterado para uso no código
            verticeNumber += 1  # contador
            grafoComPropriedades.append(
                vertice)  # Vértice salvo no array do grafo

        self.propNodes = grafoComPropriedades

    def explore(self, u):  # Método de exploração
        self.tempo += 1  # Salvo o tempo do inicio do processo
        u['prenumb'] = self.tempo  # Tempo antes do processamento
        u['visitado'] = True  # Marcado como visitado
        verticeNumber = str(
            self.propNodes.index(u))  # Pega o numero/nome do vértice
        self.ordem.append(verticeNumber)
        for v in u[verticeNumber]:  # Para cada um dos vizinhos do vértice
            verticeVizinho = self.propNodes[
                v]  # Pega o vértice com propriedades
            if not verticeVizinho['visitado']:  # Se ainda não foi visitado
                verticeVizinho[
                    'pai'] = verticeNumber  # Marca o pai do vértice vizinho
                self.explore(verticeVizinho)  # Explora o vértice vizinho
        self.tempo += 1  # Salvo tempo pós processo
        u['postnumb'] = self.tempo  # Tempo depois do processamento

    def teste(self):  # Metodo Teste
        print(self.propNodes)  # Imprime o vertices visitados

    def createResultGraph(self):
        # vertices passado lista de 0 até o tamanho pertencente a matriz de adjacencia
        vertexs = list(range(0, len(self.adjacentMatrix)))
        # Passado os vertices ao resultado
        self.resultGraph.add_nodes_from(vertexs)
        edges = []  # Declaração de edges como lista
        for item in self.propNodes:  # Verica qual dos vertices esta no grafo
            if not item['pai']:  # Se tem ligação com o pai
                continue
            else:  # se não
                # Define o index pros visitados
                vertex = self.propNodes.index(item)
                edge = (int(item['pai']), vertex)  # Define o index pro pai
                edges.append(edge)  # acrecenta na variavel edge
        # parametro edges passado pro resultado
        self.resultGraph.add_edges_from(edges)

    def timeInSeconds(self):
        # Definição de minutos e segundos
        startTime = self.startTime.strftime("%M %S")
        # Pega minuto e segundo que iniciou o processo
        startTime = [int(startTime[0:2]), int(startTime[3:5])]
        # Converção de minutos para segundos
        startTime = ((startTime[0] * 60) + startTime[1])

        # Definição de minutos e segundos
        endTime = self.endTime.strftime("%M %S")
        # Pega minuto e segundo que iniciou o processo
        endTime = [int(endTime[0:2]), int(endTime[3:5])]
        # Converção de minutos para segundos
        endTime = (endTime[0] * 60) + endTime[1]

        # imprime o tempo total
        return str(endTime - startTime) + " Segundos de processamento"

    def busca(self):  # Método de busca
        self.startTime = datetime.datetime.now()  # define o começo da busca
        for u in self.propNodes:  # Para cada vértice que ainda não foi visitado
            if not u['visitado']:  # verifica se ja foi visitado
                self.explore(u)  # É explorado
        self.endTime = datetime.datetime.now()  # define o final da busca


class Bfs(Graph):  # Classe para a busca em largura
    def __init__(self, grafo):
        self.loadAdjacentMatrix(grafo)  # Carrega o grafo
        self.resultGraph = nx.Graph()  # Resultado do grafo
        self.ordem = []  # Ordem do processamento
        self.startTime = None  # Atributo com o proposito de começar a contar o tempo de busca
        self.endTime = None  # Atributo com o proposito de finalizar o tempo de busca
        grafoComPropriedades = []  # Array com os vértices com propriedades
        verticeNumber = 0  # Numero do vértice inicial
        for u in self.adjacentMatrix:  # Definição das propriedades de cada vértice
            vertice = {
                str(verticeNumber): u,
                'visitado': False,
                'pai': None,
                'distancia': 'infinite'
            }  # Preenchimento do grafo alterado para uso no código
            verticeNumber += 1  # contador
            grafoComPropriedades.append(
                vertice)  # Vértice salvo no array do grafo

        # PropNodes recebe o proximo vertice na fila
        self.propNodes = grafoComPropriedades

    def timeInSeconds(self):  # Metodo de contagem de tempo
        # Definição de minutos e segundos
        startTime = self.startTime.strftime("%M %S")
        # Pega minuto e segundo que iniciou o processo
        startTime = [int(startTime[0:2]), int(startTime[3:5])]
        # Converção de minutos para segundos
        startTime = ((startTime[0] * 60) + startTime[1])

        # Definição de minutos e segundos
        endTime = self.endTime.strftime("%M %S")
        # Pega minuto e segundo que iniciou o processo
        endTime = [int(endTime[0:2]), int(endTime[3:5])]
        # Converção de minutos para segundos
        endTime = (endTime[0] * 60) + endTime[1]

        # imprime o tempo total
        return str(endTime - startTime) + " Segundos de processamento"

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
                edge = (int(item['pai']), vertex)  # Definido o indéx do pai
                edges.append(edge)  # edges recebe o proximo da fila

        # parametro edges passado pro resultado
        self.resultGraph.add_edges_from(edges)

    def busca(self, raiz=0):  # Método de busca
        self.startTime = datetime.datetime.now()  # define o tempo inicial da busca
        raiz = self.propNodes[
            raiz]  # Pega a raiz, com o index de seu vértice como parametro de entrada
        # inicializa a raiz que contem vertice que foi vizitado
        raiz['visitado'] = True
        raiz['distancia'] = 0  # inicializa a distancia da raiz
        Q = [raiz]  # Q recebe o numero contido na raiz

        while len(Q) != 0:  # Enquanto ter algo em Q
            u = Q.pop(0)  # Pega o vértice raiz
            # GrafoNome armazena com index de seu vértice como parametro de entrada
            grafoNome = self.propNodes.index(u)
            self.ordem.append(grafoNome)  # encaminha para a fila
            for v in u[str(grafoNome)]:  # Para cada um de seus vizinhos
                grafoVizinho = self.propNodes[
                    v]  # Pega a definição com atributo do vizinho
                if not grafoVizinho['visitado']:  # Se ainda não foi visitado
                    grafoVizinho['visitado'] = True  # Marcado como visitado
                    grafoVizinho[
                        'distancia'] = u['distancia'] + 1  # Marcado a distancia
                    grafoVizinho['pai'] = self.propNodes.index(
                        u)  # Definido o indéx do pai

                    Q.append(
                        grafoVizinho)  # Próximo da fila para ser processado
        self.endTime = datetime.datetime.now()  # define o tempo final da busca


while True:  # Menu
    # Usuario escolhe qual metodo ira usar
    entrada = int(input('1-Para largura 2-Para profundidade: '))
    if entrada == 1:  # Entrada para busca de largura
        # Usuario escolhe o grafo
        grafo = input('Escolha entre (Graph1.csv) ou (Graph2.csv): ')
        bfs = Bfs(grafo)  # bfs variavel que recebe bfs com o grafo
        # Usuario escolhe qual será o vertices raiz
        raiz = int(input('Escolha a raiz (Numero de 0 até '+str(len(bfs.adjacentMatrix)-1)+'): '))
        # Chamada da função de busca que recebe como parametro a raiz
        bfs.busca(raiz)
        bfs.createResultGraph()  # chamada do metodo createResultGraph()
        while True:  # Menu secundario que recebe 4 entradas
            entrada = int(
                input(
                    '1-Para visualizar o grafo antes da busca, 2-Para visualizar grafo pós busca, 3-Para visualizar tempo de processamento, 4-Para visualizar a ordem: '
                ))  # Usuario escolhe qual metodo ira chamar
            if entrada == 1:  # se for digitado '1' mostrará a vizualização antes da busca de largura
                # mostra o grafo antes da busca de largura
                bfs.showGraph('Antes da busca em largura', bfs.graph)
            elif entrada == 2:  # se for digitado '2' mostrará a vizualização depois da busca de largura
                # mostra o grafo depois da busca de largura
                bfs.showGraph('Depois da busca em largura', bfs.resultGraph)
            elif entrada == 3:  # se for digitado '3' mostrará o tempo de processamento em segundos
                # mostra o tempo de processamento em segundos
                print(bfs.timeInSeconds())
            elif entrada == 4:  # se for digitado '4' mostrará a ordem do vertices
                print(bfs.ordem)  # mostra a ordem do vertices
            else:
                break  # Fim do menu
    elif entrada == 2:  # Entrada para busca de profundidade
        # Usuario escolhe o grafo
        grafo = input('Escolha entre (Graph1.csv) ou (Graph2.csv): ')
        dfs = Dfs(grafo)  # dfs Recebe o valor informado pelo usuario
        dfs.busca()  # Chamada do metodo de busca
        dfs.createResultGraph()  # chamada do metodo createResultGraph()
        while True:  # Menu secundario que recebe 4 entradas
            entrada = int(
                input(
                    '1-Para visualizar o grafo antes da busca, 2-Para visualizar grafo pós busca, 3-Para visualizar tempo de processamento, 4-Para visualizar a ordem: '
                ))  # Usuario escolhe qual metodo ira chamar
            if entrada == 1:  # se for digitado '1' mostrará a vizualização antes da busca de profundidade
                # mostra o grafo antes da busca de profundidade
                dfs.showGraph('Antes da busca em profundidade', dfs.graph)
            elif entrada == 2:  # se for digitado '2' mostrará a vizualização pós da busca de profundidade
                dfs.showGraph('Depois da busca em profundidade',
                              dfs.resultGraph)  # mostra o grafo antes da busca de profundidade
            elif entrada == 3:  # se for digitado '3' mostrará o tempo de processamento em segundos
                # mostra o tempo de processamento em segundos
                print(dfs.timeInSeconds())
            elif entrada == 4:  # se for digitado '4' mostrará a mostra a ordem do vertices
                print(dfs.ordem)  # mostra a ordem do vertices
            else:
                break  # Fim do menu
    else:
        break  # Fim do menu
