# Classe representnte ao grafo
class Graph:
 
    def __init__(self, vertices):
        self.V = vertices # Numeros vertices
        self.graph = []
 
    # função para adicionar uma aresta ao gráfico
    def addEdge(self, a, b, c):
        self.graph.append([a, b, c])
         
    # função usada para imprimir a solução
    def printArr(self, dist):
        print("Distância do vértice da fonte")
        for i in range(self.V):
            print("{0}\t\t{1}".format(i, dist[i]))
     
    # A função principal que encontra as distâncias mais curtas de src a todos os outros vértices usando o algoritmo de Bellman-Ford. A função também detecta ciclo de peso negativo
    def BellmanFord(self, src):
 
        # Inicializa distâncias de src para todos os outros vértices
        dist = [float("Inf")] * self.V
        dist[src] = 0
       # Todas as arestas |V| - 1 vezes. Um simples mais curto caminho de src para qualquer outro vértice pode ter no máximo |V| - 1 arestas
        for _ in range(self.V - 1):
            #Atualiza o valor dist e o índice pai dos vértices adjacentes de o vértice escolhido. Considera apenas os vértices que ainda estão em fila
            for a, b, c in self.graph:
                if dist[a] != float("Inf") and dist[a] + c < dist[b]:
                        dist[b] = dist[a] + c           
        # Verifica se há ciclos de peso negativo. O passo acima e garante distâncias mais curtas se o gráfico não contiver ciclo de peso negativo. Se conseguirmos um caminho mais curto, então é um ciclo. 
        for a, b, c in self.graph:
                if dist[a] != float("Inf") and dist[a] + c < dist[b]:
                        print("O grafo contém ciclo de peso negativo")
                        return                        
        # imprime todas as distancias
        self.printArr(dist)

# Grafo representante
g = Graph(5)
g.addEdge(0, 1, 5)
g.addEdge(0, 3, 7)
g.addEdge(1, 3, 6)
g.addEdge(1, 4, -4)
g.addEdge(2, 1, -2)
g.addEdge(3, 2, -3)
g.addEdge(3, 4, 3)
g.addEdge(4, 2, 7)
 
# imprime a solução
g.BellmanFord(0)
