import random

pop_size = 100
mutation_rate = 0.1
max_gen = 1000 
def individual(k):
   return [random.randint(0, 9) for _ in range(k)]

def mul(individual):
   result = 1
   for num in individual:
       result *= num
   return result

def fitness(individual, T):
   return abs(T - mul(individual))

def mutate(individual):
   idx = random.randint(0, len(individual) - 1)
   individual[idx] = random.randint(0, 9)
   return individual

def crossover(parent1, parent2):
   k = len(parent1)
   split = random.randint(1, k - 1)
   return parent1[:split] + parent2[split:]

def gen_algo(T, k):
   population = [individual(k) for _ in range(pop_size)]

   for generation in range(max_gen):
       population.sort(key=lambda ind: fitness(ind, T))
      
       if mul(population[0]) == T:
           return population[0]
      
       next_gen = population[:10]

       while len(next_gen) < pop_size:
           p1 = random.choice(population[:50])
           p2 = random.choice(population[:50])
           child = crossover(p1, p2)
           if random.random() < mutation_rate:
               child = mutate(child)
           next_gen.append(child)

       population = next_gen

   print("No solution found.")
   return None

def main():
   T = int(input(" T: "))
   K = int(input(" K: "))
   result = gen_algo(T, K)
   if result:
       print("Result:", result)

if __name__ == "__main__":
   main()
