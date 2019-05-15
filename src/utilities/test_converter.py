from unittest import TestCase

import sympy

from src.utilities.converter import Converter


class TestConverter(TestCase):
    def test_to_string(self):
        number = 1234720998
        converter = Converter()
        number_as_string = converter.number_to_string(number)
        self.assertTrue(len(number_as_string) == converter.max_number_length)
        self.assertTrue(number_as_string.endswith(str(number)))

    def test_to_one_hot(self):
        number = 123456789
        converter = Converter()
        number_as_string = converter.number_to_string(number)
        number_as_one_hot = converter.string_to_one_hot(number_as_string)
        self.assertTrue(len(number_as_one_hot) == len(number_as_string))

    def test_one_hot_to_string(self):
        number = 123456789
        converter = Converter()
        number_as_string = converter.number_to_string(number)
        number_as_one_hot = converter.string_to_one_hot(number_as_string)
        number_as_string2 = converter.one_hot_to_string(number_as_one_hot)
        self.assertTrue(number_as_string == number_as_string2)

    def test_string_to_number(self):
        number = 123456789
        converter = Converter()
        number_as_string = converter.number_to_string(number)
        number2 = converter.string_to_number(number_as_string)
        self.assertTrue(number == number2)

    def test_is_number_prime_as_one_hot(self):
        converter = Converter()
        numbers = range(3, 100)
        for number in numbers:
            result = converter.is_number_prime_as_one_hot(number)
            if sympy.isprime(number):
                self.assertTrue(result[0] == 1)
            else:
                self.assertTrue(result[0] == 0)

    def test_max_value(self):
        converter = Converter()
        max_value = converter.max_value()
        print(f"Max value {max_value}")
