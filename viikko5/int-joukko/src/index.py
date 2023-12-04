import unittest
from int_joukko import IntJoukko


def main():
    joukko = IntJoukko(kapasiteetti=2)

    joukko.lisaa(1)
    print(joukko.to_int_list())
    joukko.poista(1)
    print(joukko.mahtavuus())
    joukko.lisaa(2)
    print(joukko.to_int_list())
    print(joukko.mahtavuus())
    joukko.lisaa(3)
    print(joukko)
    joukko.lisaa(2)
    joukko.lisaa(7)
    joukko.lisaa(99)

    print(joukko.to_int_list())


if __name__ == "__main__":
    main()
