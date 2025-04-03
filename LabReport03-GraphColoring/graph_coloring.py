import os

filename = "input.txt"
if not os.path.exists(filename):
    with open(filename, "w") as f:
        f.write("4 5 3\n0 1\n0 2\n1 2\n1 3\n2 3\n")  # Sample input 

class GraphColoring:
    def __init__(self, N, M, K, edges):
        self.N = N  # Number of vertices
        self.M = M  # Number of edges
        self.K = K  # Number of colors
        self.graph = {i: [] for i in range(N)}  
        for u, v in edges:
            self.graph[u].append(v)
            self.graph[v].append(u)
        self.colors = [0] * N  # Color assignment for vertices

    def is_safe(self, node, c):
        """Check if color c can be assigned to node safely"""
        for neighbor in self.graph[node]:
            if self.colors[neighbor] == c:
                return False
        return True

    def backtrack(self, node):
        """Backtracking function to assign colors"""
        if node == self.N:
            return True
        for c in range(1, self.K + 1):
            if self.is_safe(node, c):
                self.colors[node] = c
                if self.backtrack(node + 1):
                    return True
                self.colors[node] = 0  # Backtrack
        return False

    def solve(self):
        """Solve the graph coloring problem"""
        if self.backtrack(0):
            print(f"Coloring Possible with {self.K} Colors")
            print("Color Assignment:", self.colors)
        else:
            print(f"Coloring Not Possible with {self.K} Colors")

# Function to parse input from file and run the test
def parse_and_run(filename):
    with open(filename, 'r') as file:
        N, M, K = map(int, file.readline().split())
        edges = [tuple(map(int, file.readline().split())) for _ in range(M)]
    
    solver = GraphColoring(N, M, K, edges)
    solver.solve()

# Example Usage
if __name__ == "__main__":
    parse_and_run("input.txt")