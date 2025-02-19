import random

def generate_grid(N):
    grid = [[random.choice([0, 1]) for _ in range(N)] for _ in range(N)]
    return grid

def print_grid(grid):
    print("Generated Grid:")
    for row in grid:
        print(" ".join(map(str, row)))

def dfs(grid, x, y, goal_x, goal_y, visited, path):
    if x < 0 or x >= len(grid) or y < 0 or y >= len(grid) or visited[x][y] or grid[x][y] == 0:
        return False
    
    visited[x][y] = True
    path.append((x, y))
    
    if x == goal_x and y == goal_y:
        return True
    
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for dx, dy in directions:
        if dfs(grid, x + dx, y + dy, goal_x, goal_y, visited, path):
            return True
    
    path.pop()
    return False

def find_path(grid, source_x, source_y, goal_x, goal_y):
    N = len(grid)
    visited = [[False] * N for _ in range(N)]
    path = []
    
    if dfs(grid, source_x, source_y, goal_x, goal_y, visited, path):
        print("Path found:")
        for step in path:
            print(step)
    else:
        print("No path found")

def main():
    N = int(input("Enter grid size N: "))
    grid = generate_grid(N)
    print_grid(grid)
    
    source_x, source_y = map(int, input("Enter source x y: ").split())
    goal_x, goal_y = map(int, input("Enter goal x y: ").split())
    
    find_path(grid, source_x, source_y, goal_x, goal_y)

if __name__ == "__main__":
    main()
