#! /usr/bin/python3
from random import randint
import unittest
import sys
import os
try:
    p = os.getcwd()
    sys.path.insert(0, p)
    import invcnt
except ImportError:
    print("Nao foi possivel importar o arquivo invcnt.py")


class TestInvcnt(unittest.TestCase):

    # The following tests are the ones considered trivial/base tests
    def test_empty_case(self):
        lst = []
        self.assertEqual(invcnt.aux(lst), 0)

    def test_single_element(self):
        lst = [1]
        self.assertEqual(invcnt.aux(lst), 0)

    def test_ordered_list_size_2(self):
        lst = [1, 2]
        self.assertEqual(invcnt.aux(lst), 0)

    def test_unordered_list_size_2(self):
        lst = [2, 1]
        self.assertEqual(invcnt.aux(lst), 1)

    # The next set of tests are more complex
    # Two of them i've picked from the INVCNT Sphere online judge problem
    # Theres is also a function that generates a set of random values
    # based on the user input. Keep in mind that the result of an ordered
    # list of any length will always be 0
    def test_ordered_list_size_3(self):
        lst = [1, 2, 3]
        self.assertEqual(invcnt.aux(lst), 0)

    def test_unordered_list_size_3(self):
        lst = [3, 1, 2]
        self.assertEqual(invcnt.aux(lst), 2)

    def test_unordered_list_size_5(self):
        lst = [2, 3, 8, 6, 1]
        self.assertEqual(invcnt.aux(lst), 5)

    def test_unordered_list_size_20(self):
        lst = [3, 2, 1, 3, 4, 5, 6, 7, 8, 3, 4, 5, 6, 7, 8, 9, 1, 1, 2, 3]
        self.assertEqual(invcnt.aux(lst), 73)

    def test_unordered_list_size_25(self):
        lst = [3, 2, 1000, 300, 4, 5, 100000000, 7, 8, 3, 430, 321, 4, 5,
               212, 6, 0, 7, 8, 9, 100000000, 1, 23, 55, 32]
        self.assertEqual(invcnt.aux(lst), 129)

    def test_unordered_list_size_random(self):
        lst, result = self.generate_random_lst()
        self.assertEqual(invcnt.aux(lst), result)

    def generate_random_lst(self):
        lst = []
        size = input("\nEntre com um valor arbitrario para o tamanho da lista"
                     " de valores randomicos: ")
        for i in range(int(size)):
            lst.append(randint(0, 100000000))
        result = invcnt.aux(lst)
        print("Numero de inversoes:", result)
        return lst, result

if __name__ == '__main__':
    unittest.main()
