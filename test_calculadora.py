import unittest
from calculadora import sumar


class TestCalculadora(unittest.TestCase):

    def test_string_vacio_devuelve_cero(self):
        self.assertEqual(sumar(""), 0)
    def test_un_numero_devuelve_el_mismo_numero(self):
        self.assertEqual(sumar("1"), 1)
    def test_dos_numeros_devuelve_la_suma(self):
        self.assertEqual(sumar("1,2"), 3)
        self.assertEqual(sumar("4,2"), 6)
    def test_tres_numeros_devuelve_la_suma(self):
        self.assertEqual(sumar("1,2,3"), 6)


if __name__ == "__main__":
    unittest.main()