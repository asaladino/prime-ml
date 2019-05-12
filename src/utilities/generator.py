import random

import sympy

from src.repositories.SqlitePrimesRepository import SqlitePrimesRepository


class Generator:

    def __init__(self):
        self.sqlite_primes_repo = SqlitePrimesRepository()

    @staticmethod
    def find_all_primes_between(start, end):
        """
        Find all the primes in a specified range.
        :param start: number
        :param end: number
        :return: a list of primes in that range.
        """
        primes = []
        for num in range(start, end):
            if sympy.isprime(num):
                primes.append(num)
        return primes

    def random_none_prime_number(self, lower, upper):
        number = random.randint(lower, upper)
        is_prime = self.sqlite_primes_repo.find(number)
        if is_prime is None:
            return number
        else:
            self.random_none_prime_number(lower, upper)
