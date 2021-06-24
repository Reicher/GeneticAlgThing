import string
import unittest

from genalg import GeneticAlg, GeneticType

CHARACTER_GOAL = 'RobinReicher'
NUMBER_GOAL = [4, 0, 0]


class GeneticCase(unittest.TestCase):

    @staticmethod
    def fitness_numbers(dna):
        score = 0
        for c in range(len(NUMBER_GOAL)):
            score -= abs(NUMBER_GOAL[c] - dna[c])
        return score

    @staticmethod
    def fitness_characters(dna):
        score = 0
        for c in range(len(CHARACTER_GOAL)):
            score -= abs(ord(CHARACTER_GOAL[c]) - ord(dna[c]))
        return score

    @staticmethod
    def fitness_eq_solution(dna):
        x = dna[0]
        y = dna[1]
        z = dna[2]
        return -abs((x * (y - z)) - 10)

    def test_simple_integer(self):
        print(f'Simple_integer')
        genome_length = len(NUMBER_GOAL)
        pop_size = 10
        test = GeneticAlg(genome_length, pop_size, range(10))
        assert len(test.population) == pop_size
        for pop in test.population:
            assert len(pop) == genome_length

        end_pop = test.run(-1, self.fitness_numbers)
        #assert self.fitness_numbers(end_pop) == 0

    def test_simple_character(self):
        print(f'Character')
        genome_length = len(CHARACTER_GOAL)
        pop_size = 10
        test = GeneticAlg(genome_length, pop_size, string.ascii_letters)
        assert len(test.population) == pop_size
        for pop in test.population:
            assert len(pop) == genome_length

        end_pop = test.run(-1, self.fitness_characters)
        #assert self.fitness_characters(end_pop) == 0

    def test_maximize(self):
        print(f'Maximize')
        pop_size = 100
        test = GeneticAlg(3, pop_size, range(10))
        assert len(test.population) == pop_size
        for pop in test.population:
            assert len(pop) == 3

        end_pop = test.run(30, self.fitness_eq_solution)

if __name__ == '__main__':
    unittest.main()
