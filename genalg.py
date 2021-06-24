import random
from enum import Enum


class GeneticType(Enum):
    SINGLE_DECIMAL_INTEGER = 0
    CHARACTER = 1
    DECIMAL_INTEGER = 2


class GeneticAlg:
    def __init__(self, length: int, pop_size: int, genetic_material: []):
        self.population = []
        self.genetic_material = genetic_material
        self.pop_size = pop_size
        self.length = length

        # Create random start
        for pop in range(pop_size):
            dna = [random.choice(genetic_material) for _ in range(length)]
            self.population.append(dna)

    def run(self, generations: int, fitness_func, breeding=0.2, elitism=0.1, mutation=0.3):
        gen_id = 0
        max_generation = 1000
        last_best_fitness = -float('-inf')
        fitness_repeat = 0
        while gen_id < max_generation:
            self.population.sort(key=lambda d: fitness_func(d), reverse=True)

            if generations != -1 and gen_id >= generations:
                break
            elif fitness_repeat > 250:
                break
            elif last_best_fitness == self.population[0]:
                fitness_repeat += 1
            else:
                last_best_fitness = self.population[0]
                fitness_repeat = 0

            next_gen = []

            # Elitism
            elitists = int(len(self.population) * elitism)  # Number of top individuals surviving the generation
            next_gen += self.population[:elitists].copy()

            # Breeders
            b_n = int(len(self.population) * breeding)  # Number of individuals in the breed pool
            breeders = self.population[:b_n]
            while len(next_gen) < self.pop_size:
                mate1 = random.choice(breeders)
                mate2 = random.choice(breeders)  # Self fuck possible
                cuts = [random.randint(0, self.length), random.randint(0, self.length)]
                cut1 = min(cuts)
                cut2 = max(cuts)
                child = mate1[:cut1] + mate2[cut1:cut2] + mate1[cut2:]

                # Mutate child
                if random.random() < mutation:
                    child[random.randint(0, len(child)-1)] = random.choice(self.genetic_material)

                next_gen.append(child)

            next_gen.sort(key=lambda d: fitness_func(d), reverse=True)
            self.population = next_gen.copy()
            #print(self.population[0])
            gen_id += 1

        print(f'Quit after {gen_id} generations reaching {next_gen[0]} with a fitness {fitness_func(next_gen[0])}\n')
        return self.population[0]
