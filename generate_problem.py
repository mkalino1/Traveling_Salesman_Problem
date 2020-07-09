"""Skrypt pomocniczy do generowania danych do pliku data.txt. Wywolywany z jednym argumentem okreslajacym ilosc miast"""

import sys
from random import randint

MIN = 0
MAX = 200


def generate_cities(n, filename):
    with open(filename, "w") as f:
        for _ in range(n):
            f.write("{x} {y}\n".format(x=randint(MIN, MAX), y=randint(MIN, MAX)))


n = int(sys.argv[1])
generate_cities(n, 'data.txt')