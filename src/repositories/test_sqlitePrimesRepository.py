import os
from unittest import TestCase

from src.repositories.SqlitePrimesRepository import SqlitePrimesRepository


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
        repo.save(3)
        repo.save(5)
        repo.close()

    def test_count(self):
        repo = SqlitePrimesRepository()
        count = repo.count()
        print(f"Found {count} primes.")
        self.assertTrue(count > 0)
        repo.close()
