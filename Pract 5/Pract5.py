# Pract 5: Genetic Algorithm Parameter Optimization

import random


# ---------------------------
# FITNESS FUNCTION
# ---------------------------
def fitness(x, y):
    """
    Higher fitness when (x, y) is close to (0.8, 0.2)
    """
    return 1 / (1 + (x - 0.8) ** 2 + (y - 0.2) ** 2)


# ---------------------------
# CREATE RANDOM INDIVIDUAL
# ---------------------------
def random_individual():
    """
    Chromosome structure:
    [population_size, crossover_rate, mutation_rate]
    """
    return [
        random.randint(10, 100),              # population size
        round(random.uniform(0.4, 0.95), 2), # crossover rate
        round(random.uniform(0.01, 0.3), 2)  # mutation rate
    ]


# ---------------------------
# MUTATION FUNCTION
# ---------------------------
def mutate(individual, prob=0.2):
    """
    Randomly modifies parameters
    """
    if random.random() < prob:
        individual[0] = max(10, min(100, individual[0] + random.randint(-10, 10)))

    if random.random() < prob:
        individual[1] = round(max(0.4, min(0.95, individual[1] + random.uniform(-0.1, 0.1))), 2)

    if random.random() < prob:
        individual[2] = round(max(0.01, min(0.3, individual[2] + random.uniform(-0.03, 0.03))), 2)

    return individual


# ---------------------------
# CROSSOVER FUNCTION
# ---------------------------
def crossover(p1, p2):
    """
    Combine two parents
    """
    idx = random.randint(1, 2)
    return p1[:idx] + p2[idx:], p2[:idx] + p1[idx:]


# ---------------------------
# EVALUATION FUNCTION
# ---------------------------
def evaluate(individual):
    pop_size, crossover_rate, mutation_rate = individual

    # Convert parameters into normalized values
    x = pop_size / 100.0
    y = crossover_rate * (1 - mutation_rate)

    return fitness(x, y)


# ---------------------------
# GENETIC ALGORITHM
# ---------------------------
def genetic_algorithm(generations=30, population_size=12):
    # Initialize population
    population = [random_individual() for _ in range(population_size)]

    best = None
    best_score = -1

    for gen in range(generations):
        # Evaluate population
        scored = [(evaluate(ind), ind) for ind in population]

        # Sort by fitness (descending)
        scored.sort(reverse=True, key=lambda x: x[0])

        # Update best solution
        if scored[0][0] > best_score:
            best_score = scored[0][0]
            best = scored[0][1]

        # Select top individuals (elitism)
        elites = [ind[:] for _, ind in scored[:4]]

        next_population = elites[:]

        # Generate new population
        while len(next_population) < population_size:
            p1, p2 = random.sample(elites, 2)

            if random.random() < 0.8:
                child1, child2 = crossover(p1[:], p2[:])
            else:
                child1, child2 = p1[:], p2[:]

            next_population.append(mutate(child1))

            if len(next_population) < population_size:
                next_population.append(mutate(child2))

        population = next_population[:population_size]

    return best_score, best


# ---------------------------
# MAIN
# ---------------------------
if __name__ == "__main__":
    score, best = genetic_algorithm()

    print("\nBest Fitness:", round(score, 4))
    print("Best Parameters [population_size, crossover_rate, mutation_rate]:", best)