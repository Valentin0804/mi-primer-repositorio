from typing import Iterable

def multiplicar_basico(numeros: Iterable[float]) -> float:

    producto = 1
    if len(numeros) > 0:
        for numero in numeros:
            producto = producto * numero
        return producto
    else:
        return 0

assert multiplicar_basico([1, 2, 3, 4]) == 24
assert multiplicar_basico([2, 5]) == 10
assert multiplicar_basico([]) == 0
assert multiplicar_basico([1, 2, 3, 0, 4, 5]) == 0
assert multiplicar_basico(range(1, 20)) == 121_645_100_408_832_000

###############################################################################

from functools import reduce

def multiplicar_reduce(numeros: Iterable[float]) -> float:

    if len(numeros) > 0:
        return reduce(lambda x, y: x * y, numeros)
    else:
        return 0

if __name__ == "__main__":
    assert multiplicar_reduce([1, 2, 3, 4]) == 24
    assert multiplicar_reduce([2, 5]) == 10
    assert multiplicar_reduce([]) == 0
    assert multiplicar_reduce([1, 2, 3, 0, 4, 5]) == 0
    assert multiplicar_reduce(range(1, 20)) == 121_645_100_408_832_000