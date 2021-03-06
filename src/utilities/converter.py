import sympy


class Converter:
    characters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    max_number_length = 7

    def char_len(self):
        return len(self.characters)

    def max_value(self):
        """
        Find the max value based on the max_number_length
        :return number:
        """
        max_value = 1
        for multi in range(self.max_number_length - 1):
            max_value *= 10
        return max_value

    @staticmethod
    def is_number_prime_as_one_hot(number):
        """
        Check if a number is prime and return a 1 hot array.
        :param number:
        :return: [1] is true and [0] is false.
        """
        return [1 if sympy.isprime(number) else 0]

    def number_to_string(self, number):
        """
        Convert a number to a padded string.
        :param number: to convert
        :return: the number as a padded string.
        """
        return str(number).zfill(self.max_number_length)

    def string_to_one_hot(self, number):
        """
        Convert a string to a 1 hot array
        :param number: to convert
        :return: the string as a one hot array.
        """
        new_array = []
        for char in number:
            index = self.characters.index(char)
            empty_list = [0] * len(self.characters)
            empty_list[index] = 1
            new_array.append(empty_list)
        return new_array

    def invert(self, one_hot):
        value = self.one_hot_to_string(one_hot)
        return self.string_to_number(value)

    def one_hot_to_string(self, one_hot):
        """
        Convert a one hot array to a string.
        :param one_hot: encoded number.
        :return: the array as a string.
        """
        new_string = ''
        for char in one_hot:
            new_string += self.characters[char.index(1)]
        return new_string

    @staticmethod
    def string_to_number(number):
        """
        Convert the padded string to a number.
        :param number: string that is padded.
        :return: a number.
        """
        return int(number.lstrip("0"))
