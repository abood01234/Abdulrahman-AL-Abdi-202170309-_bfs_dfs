graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C']
}

def dfs(graph, start, goal):
    visited = []  # List to track visited nodes
    stack = [[start]]  # Use a stack for DFS

    while stack:
        path = stack.pop()  
        
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
                stack.append(new_path)  


solution = dfs(graph, 'A', 'F')
print('Solution is', solution)