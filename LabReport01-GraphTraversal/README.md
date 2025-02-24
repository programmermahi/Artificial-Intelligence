Write a program that generates a random N×N grid (N between 4 and 7) with non-obstacle source and goal states. It performs DFS to find a path from source to goal and prints the grid, source, goal, DFS path, and topological order of node traversal.
<img width="613" alt="image" src="https://github.com/user-attachments/assets/2e7c6bcf-bae3-4b98-b07c-c7f71580bb2b" />
Methodology: 
The following steps outline the methodology used to implement and analyze the Depth-First Search (DFS) algorithm on a randomly generated 2D grid:

1. Grid Generation :
A random N×N grid is created, where N is chosen between 4 and 7.
Each cell in the grid is randomly assigned a value of 1 (valid cell) or 0 (obstacle).
The grid serves as the environment for the DFS traversal.
2. Source and Goal Selection :
Two distinct cells, representing the source and goal nodes, are randomly selected from the grid.
These nodes are ensured to be valid (non-obstacle) and distinct to guarantee a feasible starting point and destination.
3. DFS Implementation :
The DFS algorithm is implemented using an explicit stack to simulate recursion.
Starting from the source node, the algorithm explores neighboring cells in four possible directions: up, down, left, and right.
Each visited node is marked as "visited" by setting its value to 0 to prevent revisiting.
If the goal node is reached, the algorithm terminates, and the path is recorded.
4. Path Reconstruction :
The path from the source to the goal is reconstructed by storing the sequence of moves and coordinates during traversal.
If no path exists, the program indicates that the goal is unreachable.
5. Topological Order :
The order in which nodes are visited during the DFS traversal is recorded as the topological order.
This provides insight into the exploration pattern of the algorithm.
6. Output :
The program outputs:
The generated grid, showing obstacles and valid cells.
The coordinates of the source and goal nodes.
The step-by-step DFS path from the source to the goal (if found).
The topological order of node traversal.

