import BFS
import DFS
import Graph

# graph = {
#   "a": ["b", "d"],
#   "b": ["c"],
#   "c": ["d", "e"],
#   "d": ["e"],
#   "e": ["a", "q"],
#   "q": []
# }

if __name__ == '__main__':
  g = Graph.Graph()
  g.addNode("a")
  g.draw()