# Pract 10: Ant Colony Optimization for Traveling Salesman Problem

import random
import math


# -----------------------------
# DISTANCE MATRIX
# -----------------------------
distances = [
    [0, 2, 2, 5, 7],
    [2, 0, 4, 8, 2],
    [2, 4, 0, 1, 3],
    [5, 8, 1, 0, 2],
    [7, 2, 3, 2, 0]
]

NUM_CITIES = len(distances)

# Parameters
NUM_ANTS = 5
NUM_ITERATIONS = 50
ALPHA = 1       # Pheromone importance
BETA = 2        # Distance importance
EVAPORATION = 0.5
Q = 100

# Initialize pheromone matrix
pheromone = [[1 for _ in range(NUM_CITIES)] for _ in range(NUM_CITIES)]


# -----------------------------
# CALCULATE PATH DISTANCE
# -----------------------------
def path_distance(path):
    total = 0

    for i in range(len(path) - 1):
        total += distances[path[i]][path[i + 1]]

    # Return to starting city
    total += distances[path[-1]][path[0]]

    return total


# -----------------------------
# CHOOSE NEXT CITY
# -----------------------------
def choose_next_city(current, unvisited):
    probabilities = []

    denominator = 0

    for city in unvisited:
        pher = pheromone[current][city] ** ALPHA
        heuristic = (1 / distances[current][city]) ** BETA

        denominator += pher * heuristic

    for city in unvisited:
        pher = pheromone[current][city] ** ALPHA
        heuristic = (1 / distances[current][city]) ** BETA

        prob = (pher * heuristic) / denominator
        probabilities.append((city, prob))

    r = random.random()
    cumulative = 0

    for city, prob in probabilities:
        cumulative += prob
        if r <= cumulative:
            return city

    return probabilities[-1][0]


# -----------------------------
# BUILD TOUR
# -----------------------------
def build_tour():
    start = random.randint(0, NUM_CITIES - 1)

    path = [start]
    unvisited = set(range(NUM_CITIES))
    unvisited.remove(start)

    current = start

    while unvisited:
        next_city = choose_next_city(current, list(unvisited))
        path.append(next_city)

        unvisited.remove(next_city)
        current = next_city

    return path


# -----------------------------
# UPDATE PHEROMONE
# -----------------------------
def update_pheromone(all_paths):
    global pheromone

    # Evaporation
    for i in range(NUM_CITIES):
        for j in range(NUM_CITIES):
            pheromone[i][j] *= (1 - EVAPORATION)

    # Add pheromone
    for path, dist in all_paths:
        contribution = Q / dist

        for i in range(len(path) - 1):
            a = path[i]
            b = path[i + 1]

            pheromone[a][b] += contribution
            pheromone[b][a] += contribution


# -----------------------------
# MAIN ACO FUNCTION
# -----------------------------
def ant_colony_optimization():
    best_path = None
    best_distance = float("inf")

    for iteration in range(NUM_ITERATIONS):
        all_paths = []

        for ant in range(NUM_ANTS):
            path = build_tour()
            dist = path_distance(path)

            all_paths.append((path, dist))

            if dist < best_distance:
                best_distance = dist
                best_path = path

        update_pheromone(all_paths)

    return best_path, best_distance


# -----------------------------
# MAIN
# -----------------------------
if __name__ == "__main__":
    best_path, best_distance = ant_colony_optimization()

    print("\nBest Path:", best_path)
    print("Shortest Distance:", best_distance)