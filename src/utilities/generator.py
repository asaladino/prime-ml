import random

from math import ceil

from src.repositories.SqlitePrimesRepository import SqlitePrimesRepository
from src.utilities.converter import Converter


class Generator:

    def __init__(self):
        self.repo = SqlitePrimesRepository()
        self.converter = Converter()

    def build_sample(self, sample_size, max_value):
        x = []
        y = []
        for i in range(ceil(sample_size / 2)):
            non_prime = self.random_non_prime(3, max_value)
            non_prime_string = self.converter.number_to_string(non_prime)
            x.append(self.converter.string_to_one_hot(non_prime_string))
            y.append([0])
            prime = self.random_prime(3, max_value)
            prime_string = self.converter.number_to_string(prime)
            x.append(self.converter.string_to_one_hot(prime_string))
            y.append([1])
        return x, y

    def random_non_prime(self, lower, upper):
        number = random.randint(lower, upper)
        is_prime = self.repo.find(number)
        if is_prime is None:
            return number
        else:
            return self.random_non_prime(lower, upper)

    def random_prime(self, lower, upper):
        number = random.randint(lower, upper)
        return int(self.repo.find_all_less(number).fetchone()[0])
