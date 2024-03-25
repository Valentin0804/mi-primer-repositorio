def maximo_basico(a:float, b:float) -> float:
    if a > b:
        return a
    else:
        return b

assert maximo_basico(10, 5) == 10
assert maximo_basico(9, 18) == 18