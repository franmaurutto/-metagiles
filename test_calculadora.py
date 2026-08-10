import unittest
from calculadora import Sumar


class TestCalculadora(unittest.TestCase):

    def test_string_vacio_devuelve_cero(self):
        self.assertEqual(Sumar(""), 0)


if __name__ == "__main__":
    unittest.main()