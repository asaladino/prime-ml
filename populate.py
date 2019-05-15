#!/usr/bin/python
import sys
import time

from src.repositories.SqlitePrimesRepository import SqlitePrimesRepository, NotAPrimeException, \
    PrimeAlreadySavedException, NotEnoughPrimesException, IsLessThan2Exception
from src.utilities.text_utility import text_out

repo = SqlitePrimesRepository()
upper_limit = 10000000
start_time = time.time()
print(f"Current number of primes found: {repo.count()}")
repo = SqlitePrimesRepository()
for number in range(0, upper_limit):
    try:
        text_out(f'Checking number {number}')
        repo.save(number)
        text_out(f'Adding number {number}')
    except NotAPrimeException as e:
        text_out(e.message)
    except PrimeAlreadySavedException as e:
        text_out(e.message)
    except NotEnoughPrimesException as e:
        text_out(e.message)
    except IsLessThan2Exception as e:
        text_out(e.message)
sys.stdout.write('\n')
print(f"Found {repo.count()} primes in {time.time() - start_time} seconds.")
sys.stdout.write('\n')
repo.close()
