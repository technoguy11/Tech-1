# Pract 7: DEAP (Distributed Evolutionary Algorithms in Python)
# Install first: pip install deap

import random
from deap import base, creator, tools, algorithms

def objective(individual):
    # Minimize x^2 + y^2
    x, y = individual
    return (x * x + y * y,)

def main():
    if not hasattr(creator, "FitnessMin"):
        creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
    if not hasattr(creator, "Individual"):
        creator.create("Individual", list, fitness=creator.FitnessMin)

    toolbox = base.Toolbox()
    toolbox.register("attr_float", random.uniform, -5.0, 5.0)
    toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_float, n=2)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)

    toolbox.register("evaluate", objective)
    toolbox.register("mate", tools.cxBlend, alpha=0.5)
    toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=1.0, indpb=0.5)
    toolbox.register("select", tools.selTournament, tournsize=3)

    population = toolbox.population(n=20)
    hof = tools.HallOfFame(1)

    algorithms.eaSimple(
        population,
        toolbox,
        cxpb=0.7,
        mutpb=0.3,
        ngen=30,
        halloffame=hof,
        verbose=True
    )

    best = hof[0]
    print("\nBest individual:", [round(v, 4) for v in best])
    print("Best fitness:", round(best.fitness.values[0], 6))

if __name__ == "__main__":
    main()
