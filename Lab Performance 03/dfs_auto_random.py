import random

class Node:
    def __init__(self, x, y, path):
        self.x = x  
        self.y = y  
        self.path = path  

class DFS:
    def __init__(self):
        self.directions = [(1, 0, "Down"), (-1, 0, "Up"), (0, 1, "Right"), (0, -1, "Left")]  
        self.N = random.randint(4, 7)  
        self.grid = []  
        self.source = None  
        self.goal = None  
        
    def generate_grid(self, obstacle_prob=0.5):
        self.grid = [[1 if random.random() > obstacle_prob else 0 for _ in range(self.N)] for _ in range(self.N)]

    def print_grid(self):
        for row in self.grid:
            print(" ".join(map(str, row)))

    def init(self):
        self.generate_grid()
        print(f"Generated {self.N}x{self.N} Grid:")
        self.print_grid()
        

        valid_positions = [(x, y) for x in range(self.N) for y in range(self.N) if self.grid[x][y] == 1]
        
        if len(valid_positions) < 2:
            print("Not enough valid positions to place source and goal.")
            return
        
        self.source = Node(*random.choice(valid_positions), [])
        self.goal = random.choice(valid_positions)
        
        print(f"Source: ({self.source.x}, {self.source.y})")
        print(f"Goal: ({self.goal[0]}, {self.goal[1]})")
        
        self.st_dfs()
        
    def st_dfs(self):
        stack = [self.source]
        visited = set()
        
        while stack:
            node = stack.pop()
            x, y, path = node.x, node.y, node.path
            
            if (x, y) == self.goal:
                print("Goal found in", len(path), "moves")
                for move in path:
                    print(f"Moving {move[2]} -> ({move[0]}, {move[1]})")
                return
            
            if (x, y) in visited:
                continue
            
            visited.add((x, y))
            
            for dx, dy, move in self.directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.N and 0 <= ny < self.N and self.grid[nx][ny] == 1 and (nx, ny) not in visited:
                    stack.append(Node(nx, ny, path + [(nx, ny, move)]))
        
        print("Goal cannot be reached")

if __name__ == "__main__":
    dfs = DFS()
    dfs.init()
