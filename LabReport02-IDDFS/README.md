Problem Statement: Given an N x M grid representing a maze, determine whether a valid path exists from the given start cell to the target cell. The movement is restricted to adjacent empty cells (0) in four directions: up, down, left, and right. Walls (1) cannot be traversed, and each cell may be visited only once per exploration path.
Algorithm Explanation IDDFS is a combination of Depth-First Search (DFS) and Depth-Limited Search (DLS). It progressively deepens the search depth until the target is found or the depth limit is exceeded.
Steps of IDDFS:
Start with depth = 0.
Perform a Depth-Limited Search (DLS) with the current depth.
If the target node is found, return the path.
If not, increment the depth and repeat until a maximum depth is reached.
If no path is found at the maximum depth, return "Path not found".

output:

4 4
0 0 1 0
1 0 1 0
0 0 0 0
1 1 0 1
Start: 0 0
Target: 2 3

Path found at depth 5 using IDDFS
Traversal Order: [(0,0), (1,0), (1,1), (0,1), (2,1), (2,2), (2,3)]
