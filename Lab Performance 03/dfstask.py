import random

class Node:
    def __init__(self, x, y, path):
        self.x = x  # x−coordinate of the node
        self.y = y  # y−coordinate of the node
        self.path = path  # Path taken to reach this node

class DFS:
    def __init__(self):
        self.directions = [(1, 0, "Down"), (-1, 0, "Up"), (0, 1, "Right"), (0, -1, "Left")]  # Possible movement directions
        self.N = random.randint(4, 7)  # Generate random grid size between 4 and 7
        self.grid = []  # Grid representation
        self.source = None  # Source node
        self.goal = None  # Goal node
        
    def generate_grid(self, obstacle_prob=0.3):
        self.grid = [[1 if random.random() > obstacle_prob else 0 for _ in range(self.N)] for _ in range(self.N)]

    def print_grid(self):
        for row in self.grid:
            print(" ".join(map(str, row)))

    def init(self):
        self.generate_grid()
        print(f"Generated {self.N}x{self.N} Grid:")
        self.print_grid()
        
        sx, sy = map(int, input("Enter start coordinates (x y): ").split())
        gx, gy = map(int, input("Enter goal coordinates (x y): ").split())
        
        if self.grid[sx][sy] == 0 or self.grid[gx][gy] == 0:
            print("Invalid start or goal position (obstacle present)")
            return
        
        self.source = Node(sx, sy, [])
        self.goal = (gx, gy)
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
