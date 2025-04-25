import random
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.cluster = None

def manhattan_distance(p1, p2):
    return abs(p1.x - p2.x) + abs(p1.y - p2.y)

class KMeans:
    def __init__(self, total_points, total_clusters, grid_size=15):
        self.total_points = total_points
        self.total_clusters = total_clusters
        self.grid_size = grid_size

        all_positions = [(x, y) for x in range(grid_size) for y in range(grid_size)]
        random.shuffle(all_positions)
        if total_points > len(all_positions):
            raise ValueError("Grid too small for the number of points!")
        
        self.points = [Point(x, y) for x, y in all_positions[:total_points]]
        self.clusters = [Point(random.randint(0, grid_size - 1), random.randint(0, grid_size - 1)) for _ in range(total_clusters)]

        self.run_clustering()

    def run_clustering(self):
        while True:
            for p in self.points:
                distances = [manhattan_distance(p, center) for center in self.clusters]
                p.cluster = distances.index(min(distances))

            old_centers = [(c.x, c.y) for c in self.clusters]

            for i in range(self.total_clusters):
                cluster_points = [p for p in self.points if p.cluster == i]
                if cluster_points:
                    avg_x = sum(p.x for p in cluster_points) // len(cluster_points)
                    avg_y = sum(p.y for p in cluster_points) // len(cluster_points)
                    self.clusters[i].x = avg_x
                    self.clusters[i].y = avg_y

            new_centers = [(c.x, c.y) for c in self.clusters]
            if new_centers == old_centers:
                break
        self.visualize()

    def visualize(self):
        grid = [["." for _ in range(self.grid_size)] for _ in range(self.grid_size)]

        for p in self.points:
            grid[p.y][p.x] = str(p.cluster)

        for i, center in enumerate(self.clusters):
            grid[center.y][center.x] = chr(65 + i)

        print("\nCluster Visualization (using Manhattan Distance):\n")
        print("     " + "   ".join(f"{i:02}" for i in range(self.grid_size)))
        for row_idx, row in enumerate(grid):
            row_str = "    ".join(row)
            print(f"{row_idx:02}   {row_str}")
def main():
    KMeans(total_points=100, total_clusters=10, grid_size=10)
if __name__ == "__main__":
    main()
