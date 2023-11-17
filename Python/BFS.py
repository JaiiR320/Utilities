def BFS(graph, node):
  visited = []
  queue = []

  visited.append(node)
  queue.append(node)

  while queue:
    s = queue.pop(0)
    print(s, end=" ")
    for i in graph[s]:
      if i not in visited:
        queue.append(i)
        visited.append(i)
        
  return visited