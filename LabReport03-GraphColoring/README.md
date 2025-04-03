problem statement: You are given an undirected graph with N vertices and M edges. Your task is to implement a Python program that uses Backtracking to determine whether the graph can be colored using K colors such that no two adjacent vertices share the same color. The input will be read from a file, where the first line contains three integers: N (number of vertices, numbered from 0 to N−1), M (number of edges), and K (number of available colors). Each of the following M lines contains two integers u and v, representing an undirected edge between vertex u and vertex v.
Textfile:
4 5 3
0 1
0 2
1 2
1 3
2 3

output:
<img width="327" alt="image" src="https://github.com/user-attachments/assets/4c51df0e-50e0-45e2-be90-44f7f7eb992f" />
Algorithem Expleation:Steps:
Initialization:

Create a graph using an adjacency list to represent the vertices and edges.

Initialize a color array to store the color of each vertex (starting with 0, meaning no color assigned).

Backtracking:

Start at the first vertex and try assigning a color (from 1 to K).

For each color, check if it can be assigned to the current vertex by ensuring that no adjacent vertex has the same color.

If a valid color is found, recursively assign colors to the next vertex.

If we reach the last vertex and successfully color it, the solution is found.

If no valid color can be assigned, backtrack and try a different color for the previous vertex.

Termination:

If all vertices are successfully colored, print the solution.

If it's not possible to color the graph with K colors, print that it's not possible
