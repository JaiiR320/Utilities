visited = []

def DFS(graph, node):
  visited.append(node)
  print(node, end=" ")

  for neighbor in graph[node]:
    if neighbor not in visited:
      DFS(graph, neighbor)