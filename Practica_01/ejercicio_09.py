def sumatoria_basico(n: int) -> int:

    sumatoria = 0
    for i in  range(1, n+1):
        sumatoria += i
    return sumatoria

assert sumatoria_basico(1) == 1
assert sumatoria_basico(100) == 5050


###############################################################################

def sumatoria_sum(n: int) -> int:

    return sum(range(1, n+1))

assert sumatoria_sum(1) == 1
assert sumatoria_sum(100) == 5050


###############################################################################

from functools import reduce

def sumatoria_reduce(n: int) -> int:

    # Paso 1: Definir la función que suma dos números
    def suma(x, y):
        return x + y
    # Paso 2: Utilizar reduce para sumar los números del rango
    return reduce(suma, range(1, n + 1))

if __name__ == "__main__":
    assert sumatoria_reduce(1) == 1
    assert sumatoria_reduce(100) == 5050

###############################################################################

def sumatoria_gauss(n: int) -> int:

    sumatoria = 0
    for i in range(1, n + 1):
        for l in range(n+1, 1):
            sumatoria += (i + l)
    return sumatoria

if __name__ == "__main__":
    assert sumatoria_gauss(1) == 1
    assert sumatoria_gauss(100) == 5050
