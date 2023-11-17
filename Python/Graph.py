class Graph:
  def __init__(self, n, edges):
    self.graph = [None] * n
    for i in range(n):
      self.graph[i] = []
    for (src, dest, weight) in edges:
      self.graph[src].append((dest, weight))
  
  def getNeighbors(self, src):
    return self.graph[src]

  def printGraph(self):
    for src in range(len(self.graph)):
      for (dest, weight) in self.graph[src]:
        print(f'({src} -> {dest}, {weight})', end=' ')
      print()

edges = [
  (0, 1, 0), (0, 2, 0),
  (1, 2, 0),
  (2, 3, 0), (2, 4, 0),
  (3, 4, 0),
  (4, 0, 0)
]
g = Graph(5, edges)
g.printGraph()
print(g.getNeighbors(2))
