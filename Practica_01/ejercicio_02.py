def maximo_encadenado(a: float, b: float, c: float) -> float:
    if a > b:
        if a > c:
            return a
        else:
            return c
    if b > c:
        return b
    else:
        return c


assert maximo_encadenado(1, 10, 5) == 10
assert maximo_encadenado(4, 9, 18) == 18
assert maximo_encadenado(24, 9, 18) == 24

def maximo_cuadruple(a: float, b: float, c: float, d: float) -> float:
    return max(a,b,c,d)

assert maximo_cuadruple(1, 10, 5, -5) == 10
assert maximo_cuadruple(4, 9, 18, 6) == 18
assert maximo_cuadruple(24, 9, 18, 20) == 24
assert maximo_cuadruple(24, 9, 18, 30) == 30

def maximo_arbitrario(*args) -> float:
    if not args:
        return None
    max_value = args[0]
    for arg in args[1:]:
        if arg > max_value:
            max_value = arg
    return max_value

assert maximo_arbitrario(10, 5) == 10
assert maximo_arbitrario(9, 18) == 18
assert maximo_arbitrario(1, 2, 3, 4, 5) == 5
assert maximo_arbitrario(-1, -2, -3, -4, -5) == -1
assert maximo_arbitrario(10) == 10
assert maximo_arbitrario() is None

def maximo_recursivo(*args) -> float:
    if not args:
        return None
    elif len(args) == 1:
        return args[0]
    else:
        max_resto = maximo_recursivo(*args[1:])
        return args[0] if args[0] > max_resto else max_resto