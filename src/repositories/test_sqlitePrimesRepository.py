import os
from unittest import TestCase

import sympy

from src.repositories.SqlitePrimesRepository import SqlitePrimesRepository, NotEnoughPrimesException, \
    IsLessThan3Exception, PrimeAlreadySavedException, NotAPrimeException


class TestSqlitePrimesRepository(TestCase):

    def test_init(self):
        repo = SqlitePrimesRepository()
        self.assertTrue(os.path.exists(repo.file))
        repo.close()

    def test_find_all(self):
        repo = SqlitePrimesRepository()
        primes = repo.find_all()
        self.assertTrue(len(primes) > 0)
        repo.close()

    def test_find(self):
        repo = SqlitePrimesRepository()
        prime = repo.find(3)
        self.assertTrue(prime == 3)
        prime = repo.find(4)
        self.assertIsNone(prime)
        repo.close()

    def test_save(self):
        repo = SqlitePrimesRepository()
        for number in range(0, 200000):
            try:
                repo.save(number)
                print('Adding number {0}'.format(number))
            except NotAPrimeException as e:
                print(e.message)
            except PrimeAlreadySavedException as e:
                print(e.message)
            except NotEnoughPrimesException as e:
                print(e.message)
            except IsLessThan3Exception as e:
                print(e.message)
        repo.close()

    def test_count(self):
        repo = SqlitePrimesRepository()
        count = repo.count()
        print(f"Found {count} primes.")
        self.assertTrue(count > 0)
        repo.close()

    def test_is_prime(self):
        repo = SqlitePrimesRepository()
        for number in range(0, 200):
            try:
                check_fast = repo.is_prime(number)
                check_slow = sympy.isprime(number)
                print(number, check_fast, check_slow)
                self.assertEqual(check_fast, check_slow)
            except NotEnoughPrimesException as e:
                print(e.message)
            except IsLessThan3Exception as e:
                print(e.message)
        repo.close()
