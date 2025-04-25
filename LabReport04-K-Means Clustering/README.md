Problem Statement: Write a lab report on the implementation of a modified K-Means clustering algorithm using Python. In this task, you must generate a data file containing 100 Cartesian points P(x, y) and 10 initial cluster centers C(x, y). The algorithm should be rewritten to use the Manhattan distance method for calculating distances between points and clusters. Additionally, you are required to create a 2D visualization of the clustered data using a matrix, where each cell represents a coordinate on the plane and displays either a data point or a cluster center using distinct symbols. This visualization must be displayed using only the print() function.
Procedure:
Generate 100 unique random points on a 2D grid (e.g., 10x10).
Initialize 10 cluster centers randomly.
For each point:
 Compute the Manhattan distance to all cluster centers.
 Assign the point to the cluster with the smallest distance.
Update each cluster center as the mean position (average x and y) of its assigned points.
Repeat steps 3–4 until cluster centers no longer change.
Display the grid:
Each cell sh

Output :<img width="361" alt="image" src="https://github.com/user-attachments/assets/5377d6dd-38ee-4df9-9769-2c31387bf10d" />

Explain:<img width="228" alt="image" src="https://github.com/user-attachments/assets/68d1098b-8c22-474a-bafb-b4fa2099bb38" /><img width="381" alt="image" src="https://github.com/user-attachments/assets/6814ced6-5f36-4412-8490-aba81747dde2" /><img width="505" alt="image" src="https://github.com/user-attachments/assets/8c073f04-1720-4653-a45e-d9ea7f72bbc6" />
<img width="460" alt="image" src="https://github.com/user-attachments/assets/321d9390-ade6-4e6d-a243-71e77caf91fc" />



