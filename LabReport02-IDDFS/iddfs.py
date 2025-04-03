class IDDFS:
    def __init__(self, grid, start, target):
        self.grid = grid
        self.N = len(grid)
        self.M = len(grid[0])
        self.start = start
        self.target = target
        self.directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Down, Up, Right, Left

    def dls(self, node, depth, path, visited):
        x, y = node
        if node == self.target:
            return True, path
        if depth == 0:
            return False, None

        visited.add(node)
        for dx, dy in self.directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.N and 0 <= ny < self.M and self.grid[nx][ny] == 0 and (nx, ny) not in visited:
                found, new_path = self.dls((nx, ny), depth - 1, path + [(nx, ny)], visited)
                if found:
                    return True, new_path
        visited.remove(node)
        return False, None

    def iddfs(self, max_depth):
        for depth in range(max_depth + 1):
            visited = set()
            found, path = self.dls(self.start, depth, [self.start], visited)
            if found:
                return f"Path found at depth {depth} using IDDFS", path
        return f"Path not found at max depth {max_depth} using IDDFS", None

# Function to take user input
def get_input():
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
    start_x, start_y = map(int, input().split()[1:])
    target_x, target_y = map(int, input().split()[1:])
    return grid, (start_x, start_y), (target_x, target_y)

if __name__ == "__main__":
    grid, start, target = get_input()
    solver = IDDFS(grid, start, target)
    result, path = solver.iddfs(len(grid) * len(grid[0]))
    print(result)
    if path:
        print("Traversal Order:", path)
