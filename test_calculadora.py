import unittest
from calculadora import Sumar


class TestCalculadora(unittest.TestCase):

    def test_string_vacio_devuelve_cero(self):
        self.assertEqual(Sumar(""), 0)
    def test_un_numero_devuelve_el_mismo_numero(self):
        self.assertEqual(Sumar("1"), 1)


if __name__ == "__main__":
    unittest.main()