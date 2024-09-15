graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C']
}

def bfs(graph, start, goal):
    visited = []  # List to track visited nodes
    queue = [[start]]  

    while queue:
        path = queue.pop(0)  
        node = path[-1]  # Get the last node in the path
        
        if node in visited:
            continue
        
        visited.append(node)  # Mark the node as visited

        if node == goal:  # Check if we have reached the goal
            return path 
        
        adjacent_nodes = graph.get(node, [])
        for neighbor in adjacent_nodes:
            if neighbor not in path:  # Avoid cycles
                new_path = list(path) 
                new_path.append(neighbor)  
                queue.append(new_path) 


solution = bfs(graph, 'A', 'F')
print('Solution is', solution)