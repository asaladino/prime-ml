import sqlite3
import os


class SqlitePrimesRepository:

    def __init__(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        self.file = os.path.realpath(os.path.join(dir_path, '..', '..', 'data', 'primes.sqlite'))
        self.db = sqlite3.connect(self.file)
        self.create_table()

    def create_table(self):
        cursor = self.db.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS primes(id INTEGER PRIMARY KEY, prime INTEGER UNIQUE)')
        self.db.commit()

    def count(self):
        cursor = self.db.cursor()
        cursor.execute('SELECT Count(*) FROM primes')
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
            return prime[0]
        return prime

    def save(self, number):
        try:
            cursor = self.db.cursor()
            cursor.execute('INSERT INTO primes(prime) VALUES(:prime)', {'prime': number})
            self.db.commit()
        except sqlite3.IntegrityError:
            pass

    def close(self):
        self.db.close()
