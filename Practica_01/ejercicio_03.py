from typing import Union

def operacion_basica(a: float, b: float, multiplicar: bool) -> Union[float,str]:
    if multiplicar == True:
        Union = a*b
    else:
        if b != '0':
            Union = a / b
        else:
            Union = 'Operacion no valida'

    return  Union

assert operacion_basica(1, 1, True) == 1
assert operacion_basica(1, 1, False) == 1
assert operacion_basica(25, 5, True) == 125
assert operacion_basica(25, 5, False) == 5
assert operacion_basica(0, 5, True) == 0
assert operacion_basica(0, 5, False) == 0
assert operacion_basica(1, 0, True) == 0
assert operacion_basica(1, 0, False) == "Operación no válida"

###############################################################################

def operacion_multiple(a: float, b: float, multiplicar: bool) -> Union[float, str]:
        if multiplicar == True:
            return a * b
        else:
            if b != '0':
                return a / b
            else:
                return'Operacion no valida'

assert operacion_multiple(1, 1, True) == 1
assert operacion_multiple(1, 1, False) == 1
assert operacion_multiple(25, 5, True) == 125
assert operacion_multiple(25, 5, False) == 5
assert operacion_multiple(0, 5, True) == 0
assert operacion_multiple(0, 5, False) == 0
assert operacion_multiple(1, 0, True) == 0
assert operacion_multiple(1, 0, False) == "Operación no válida"