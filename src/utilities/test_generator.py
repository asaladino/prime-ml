from unittest import TestCase

import sympy

from src.utilities.generator import Generator


class TestGenerator(TestCase):
    def test_find_all_primes_between(self):
        generator = Generator()
        for i in range(0, 20):
            random_not_prime = generator.random_non_prime(2, 1000)
            check_slow = sympy.isprime(random_not_prime)
            self.assertFalse(check_slow)

    def test_random_prime(self):
        generator = Generator()
        for i in range(0, 20):
            random_prime = generator.random_prime(2, 1000)
            check_slow = sympy.isprime(random_prime)
            self.assertTrue(check_slow)

    def test_build_sample(self):
        generator = Generator()
        x, y = generator.build_sample(10, 10000)
        print(x)
        print(y)
