from unittest import TestCase

from src.utilities.generator import Generator


class TestGenerator(TestCase):
    def test_find_all_primes_between(self):
        primes = Generator.find_all_primes_between(3, 1000000)
        print(f"Found {len(primes)} primes")

