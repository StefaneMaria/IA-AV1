import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def rastrigin(x: np.ndarray, __A=10):
    return __A * x.size + np.sum(x**2 - __A * np.cos(2 * np.pi * x))


def phi(x):
    return rastrigin(x) + 1


def initialize_population(N, p, nd):
    return np.random.randint(low=0, high=2, size=(N, p * nd))


def select(population, fitness) -> tuple:
    probabilities = fitness / np.sum(fitness)
    selected_indices = np.random.choice(
        len(population), 2, replace=True, p=probabilities
    )
    return population[selected_indices[0]], population[selected_indices[1]]


def crossover(parent1, parent2):
    crossover_point = np.random.choice(range(1, parent1.size), replace=False)
    child1 = np.concatenate([parent1[:crossover_point], parent2[crossover_point:]])
    child2 = np.concatenate([parent2[:crossover_point], parent1[crossover_point:]])
    return child1, child2


def mutate(genes, mutation_rate):
    for i in range(len(genes)):
        if np.random.rand() < mutation_rate:
            genes[i] = 1 - genes[i]
    return genes


def decode(gene):
    dec = 0
    for g in gene:
        dec += dec + g
    return dec


def genetic_algorithm(N, p, nd, max_generation, mutation_rate=0.01):
    population = initialize_population(N, p, nd)

    best_individual = None
    best_fitness = float("inf")

    for generation in range(max_generation):
        fitness = np.array([phi(individual) for individual in population])

        parent1, parent2 = select(population, fitness)
        child1, child2 = crossover(parent1, parent2)

        child1 = mutate(child1.copy(), mutation_rate)
        child2 = mutate(child2.copy(), mutation_rate)

        new_population = np.concatenate(
            (
                child1.reshape(1, -1),
                child2.reshape(1, -1),
                population[fitness.argsort()[N - 2 :]],
            )
        )

        fitness_min = fitness.min()
        if fitness_min < best_fitness:
            best_fitness = fitness_min
            best_individual = population[fitness.argmin()]

        population = new_population

    return best_individual, best_fitness


fitness = []
for g in range(100):
    _, best_fitness = genetic_algorithm(100, 20, 10, 100)
    fitness.append(best_fitness)

dt = pd.DataFrame(
    {
        "Minimum fitness": [np.min(fitness)],
        "Maximum fitness": [np.max(fitness)],
        "Average fitness": [np.mean(fitness)],
        "Standard deviation": [np.std(fitness)],
    }
)

print(dt)
