import sqlite3
import os

import math


class SqlitePrimesRepository:

    def __init__(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        self.file = os.path.realpath(os.path.join(dir_path, '..', '..', 'data', 'primes.sqlite'))
        self.db = sqlite3.connect(self.file)
        self.create_table()

    def create_table(self):
        cursor = self.db.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS primes(id INTEGER PRIMARY KEY, prime TEXT UNIQUE)')
        self.db.commit()

    def is_prime(self, number):
        """
        Uses the saved primes to check if the number is prime.
        :param number: to check
        :return: True if it is prime.
        """
        # Check for min value.
        if number < 3:
            raise IsLessThan3Exception()
        num_str = str(number)
        last = int(num_str[len(num_str) - 1])
        square = math.sqrt(number)
        cursor = self.db.cursor()

        # Check for the initial primes.
        if number < 10 and (number == 3 or number == 5 or number == 7):
            return True

        # Check for even and fives.
        if last == 0 or last == 2 or last == 4 or last == 5 or last == 6 or last == 8:
            return False

        # Prime already exists
        if self.find(number) is None:
            return False

        # Check if there are enough primes in the database.
        cursor.execute('SELECT COUNT(*) FROM primes WHERE CAST(prime as INTEGER) > ?', (square,))
        count = cursor.fetchone()[0]
        if count == 0:
            return False

        cursor.execute('SELECT prime FROM primes WHERE CAST(prime as INTEGER) <= ?', (square,))
        for entry in cursor:
            if number % int(entry[0]) == 0:
                return False
        return True

    def count(self):
        cursor = self.db.cursor()
        cursor.execute('SELECT COUNT(*) FROM primes')
        return cursor.fetchone()[0]

    def find_all(self):
        cursor = self.db.cursor()
        cursor.execute('SELECT prime FROM primes')
        return cursor.fetchall()

    def find(self, number):
        cursor = self.db.cursor()
        cursor.execute('SELECT prime FROM primes WHERE prime=?', (number,))
        prime = cursor.fetchone()
        if prime is not None:
            return int(prime[0])
        return prime

    def find_all_less(self, number):
        cursor = self.db.cursor()
        cursor.execute('SELECT prime FROM primes WHERE CAST(prime as INTEGER) <= ?', (number,))
        return cursor.fetchall()

    def save(self, number):
        try:
            if self.is_prime(number):
                cursor = self.db.cursor()
                cursor.execute('INSERT INTO primes(prime) VALUES(:prime)', {'prime': number})
                self.db.commit()
            else:
                raise NotAPrimeException
        except sqlite3.IntegrityError:
            raise PrimeAlreadySavedException

    def close(self):
        self.db.close()


class NotAPrimeException(Exception):

    def __init__(self):
        self.message = 'That number is not prime.'
        super(NotAPrimeException, self).__init__(self.message)


class PrimeAlreadySavedException(Exception):

    def __init__(self):
        self.message = 'That prime is already saved.'
        super(PrimeAlreadySavedException, self).__init__(self.message)


class IsLessThan3Exception(Exception):

    def __init__(self):
        self.message = 'Only numbers greater than 2.'
        super(IsLessThan3Exception, self).__init__(self.message)


class NotEnoughPrimesException(Exception):

    def __init__(self):
        self.message = 'Not enough primes are in the database.'
        super(NotEnoughPrimesException, self).__init__(self.message)
