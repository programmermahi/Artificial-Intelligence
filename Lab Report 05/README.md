Problem Statement :Write a lab report in Python on solving the N-Queens problem using Genetic Algorithms.

⚙️ Procedure:

1.Chromosome Representation:
Each chromosome is a list of integers of length N, where the value at index i represents the row of the queen in column i.

2.Initialization:
Generate an initial population of chromosomes randomly.

3.Fitness Function:
Calculate the number of non-attacking queen pairs. Lower diagonal and horizontal collisions are penalized.

4.Selection:
Use probability-based selection (roulette wheel selection) to choose parents based on fitness.

5.Crossover:
Perform one-point crossover to combine two parents into a new child.

6.Mutation:
With a small probability (e.g., 3%), change a queen’s row position to maintain genetic diversity.

7.Termination:
Continue until a chromosome with maximum fitness is found (no conflicts).

8.Output:
Display the best solution and the chessboard configuration with queen placements.

<img width="442" alt="image" src="https://github.com/user-attachments/assets/5f290251-117c-4b57-869b-e5894be8f6cd" />



