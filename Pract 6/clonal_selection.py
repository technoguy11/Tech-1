# Pract 6: Clonal Selection Algorithm (CSA) using Python
import random
import math

def fitness(candidate):
    # Sphere function minimization; higher affinity for lower objective value
    x, y = candidate
    value = x * x + y * y
    return 1 / (1 + value)

def random_candidate():
    return [random.uniform(-5, 5), random.uniform(-5, 5)]

def mutate(candidate, rate):
    x, y = candidate
    x += random.uniform(-rate, rate)
    y += random.uniform(-rate, rate)
    return [x, y]

def clone_and_select(population, clone_factor=4, mutation_rate=0.5, generations=20):
    best = None
    best_fit = -1

    for _ in range(generations):
        population.sort(key=fitness, reverse=True)

        if fitness(population[0]) > best_fit:
            best = population[0][:]
            best_fit = fitness(best)

        selected = population[: max(2, len(population) // 4)]
        clones = []

        for cand in selected:
            for _ in range(clone_factor):
                clones.append(mutate(cand[:], mutation_rate))

        combined = selected + clones
        combined.sort(key=fitness, reverse=True)
        population = combined[: len(population)]

    return best, best_fit

if __name__ == "__main__":
    initial_population = [random_candidate() for _ in range(12)]
    best, best_fit = clone_and_select(initial_population)

    print("Best candidate:", [round(v, 4) for v in best])
    print("Best affinity:", round(best_fit, 6))
